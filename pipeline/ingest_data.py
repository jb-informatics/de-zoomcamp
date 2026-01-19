#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
import pyarrow.parquet as pq
import requests
from io import BytesIO
from sqlalchemy import create_engine
from tqdm.auto import tqdm

@click.command()
@click.option('--pg_user', default='root', help='PostgreSQL user')
@click.option('--pg_password', default='root', help='PostgreSQL password')
@click.option('--pg_host', default='localhost', help='PostgreSQL host')
@click.option('--pg_port', default='5432', help='PostgreSQL port')
@click.option('--pg_db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--taxi_color', default='green', help='Taxi color')
@click.option('--year', default=2025, help='Year for data ingestion')
@click.option('--month', default=11, help='Month for data ingestion')
@click.option('--target_table', default=None, help='Target table in PostgreSQL')
@click.option('--chunksize', default=100000, help='Size of data chunks for ingestion')
def run(pg_user, pg_password, pg_host, pg_port, pg_db, year, month, taxi_color, target_table, chunksize):

    prefix = "https://d37ci6vzurychx.cloudfront.net/trip-data"
    url = f"{prefix}/{taxi_color}_tripdata_{year}-{month:02d}.parquet"

    engine = create_engine(f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}")

    if target_table is None:
        target_table = f"{taxi_color}_taxi_data_{year}"

    # df_iter = pd.read_parquet(url,
    #                  iterator=True,
    #                  chunksize=chunksize,
    # )

    r = requests.get(url)
    df_iter = pq.ParquetFile(BytesIO(r.content)).iter_batches(batch_size=chunksize)

    first=True

    for df_chunk in tqdm(df_iter):

        df_chunk = df_chunk.to_pandas()

        if first:
            df_chunk.to_sql(
                name=target_table,
                con=engine,
                if_exists="replace"
            )
            first=False
        else:
            df_chunk.to_sql(name=target_table, con=engine, if_exists="append")


    # Taxi Zone Lookup Data
    df = pd.read_csv("https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv")
    df.to_sql(name="taxi_zone_lookup", con=engine, if_exists="replace")

if __name__ == '__main__':
    run()