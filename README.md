# Dagster Data Pipeline

This is a [Dagster](https://dagster.io/) project: ```Dagster Data Pipeline```.
It uses a local SQLite3 database for storing and retrieving tables.

## Datasets used

<b>1. Bank Transaction Dataset for Fraud Detection</b> : (https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)
<p>This dataset provides a detailed look into transactional behavior and financial activity patterns, ideal for exploring fraud detection and anomaly identification.</p>

<b>2. US Zip Codes Database:</b> (https://simplemaps.com/data/us-zips)
<p>
Up-to-date database of US Zip Codes</p>


## Here's what this data pipeline does:
1. Read and transform `bank_transactions_data`
2. Read and transform `us_zips` data
3. Join the two datasets to get transaction logs along with states and populations for corresponding cities.

## Getting started

1. Clone the repository

2. Inside the cloned folder, create a python virtual environment

```bash
cd dagster_data_pipeline
python -m venv virtual_env
source virtual_env/bin/activate
```

3. Install pip modules:
```bash
pip install dagster dagit dagster-webserver pandas pytest
```

4. Then, start the Dagster UI web server:

```bash
dagster dev
```

5. Open http://localhost:3000 with your browser to see the project.
6. Materialize all processes to create SQLite tables in databases/data.db


## Unit testing

Tests are in the `data_pipeline_tests` directory and you can run tests using `pytest`:

```bash
pytest data_pipeline_tests
```
