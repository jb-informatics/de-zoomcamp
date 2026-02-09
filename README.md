# de-zoomcamp

### Module 01 - Docker & Terraform
This module focuses on using Docker to containerize services such as PostgreSQL and pgAdmin. The [NYC taxi trip dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) is loaded into PostgreSQL for hands-on data ingestion practice. The module also introduces Terraform as an infrastructure-as-code (IaC) tool and uses Google Cloud Platform (GCP) as the cloud service provider.

### Module 02 - Workflow Orchestration with Kestra
This module demonstrates how to use Kestra as a workflow orchestration tool to design, schedule, and manage end-to-end data pipelines. Pipelines are developed and tested locally using PostgreSQL, typically in a Dockerized setup, to validate task logic and dependencies before deployment. The workflows are then deployed to production on GCP, integrating cloud infrastructure and services to run scalable and reliable data pipelines.

### Module 03 - Data Warehouse with BigQuery
This module introduces data warehousing concepts using Google BigQuery as the main analytical database. It covers table design, querying, and performance optimization techniques like partitioning and clustering, plus using external tables. The module also includes hands-on SQL practice and homework, with a brief introduction to BigQuery ML for running machine learning directly in the warehouse.

### Homework
[Homework 1](01-docker-terraform/homework-01.ipynb)

[Homework 2](02-workflow-orchestration/homework-02.ipynb)

[Homework 3](03-data-warehouse/README.md)