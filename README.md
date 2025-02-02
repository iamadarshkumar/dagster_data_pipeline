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
   <img width="780" alt="image" src="https://github.com/user-attachments/assets/822294c0-9b40-49e4-8057-c094432ddc34" />

7. Materialize all processes to create SQLite tables in `databases/dagster_data.db`


## Unit testing

Tests are in the `data_pipeline_tests` directory and you can run tests using `pytest`:

```bash
pytest
```

## Limitations

<b>Limited Scalability with SQLite:</b> 
<br>The project uses SQLite3 which is a lightweight, serverless, and file-based database, and is great for small-scale applications, local development, or testing. However, it's not optimized for handling large amounts of concurrent users or high traffic. Additionally, partitioning is not supported in SQLite3 hence there was a partition simulation by creating an hourly column in `bank_transactions_data` table.

<b>Data Processing Performance:</b>
<br>The data processing is done using pandas in memory, which might be fine for small datasets but could lead to performance issues as the dataset grows. The system may run out of memory for large datasets.

## Future Scope
<b>Scalability:</b>
<br>For production use or when dealing with larger datasets, we might need to transition to a more scalable relational database like PostgreSQL or MySQL.

<b>Performance</b>
<br>Distributed data processing frameworks like Apache Spark can be introduced to handle large-scale data processing.

