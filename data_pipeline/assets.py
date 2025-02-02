import pandas as pd
from data_pipeline.resources import SQLiteResource
from dagster import asset, Output

# Asset 1: Load Data from Dataset:
# Bank Transactions: (https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)
@asset
def bank_transactions():
    
    # Read Bank Transactions Data
    df = pd.read_csv("input_datasets/bank_transactions_data.csv")

    # Convert TransactionDate to timestamp
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

    # Simulate partitioning by adding a 'TransactionHour' column
    df["TransactionHour"] = df["TransactionDate"].dt.strftime("%Y-%m-%d %H:00:00")

    # Get SQLite connection if exists
    conn = SQLiteResource('databases/dagster_data.db').get_connection()
    
    # Save the data to bank_transactions table
    df.to_sql("bank_transactions", conn, if_exists="replace", index=False)
    
    # Close the connection
    conn.close()

    return Output(df)

# Asset 2: Load Another Dataset: 
# US Zip Codes: ( https://simplemaps.com/data/us-zips )
@asset
def us_zips():

    # Read US Zips file
    df = pd.read_csv("input_datasets/us_zips.csv")

    # Cast population to int
    df['population'] = df['population'].fillna(0).astype('int')

    # Get SQLite connection if exists
    conn = SQLiteResource('databases/dagster_data.db').get_connection()

    # Save the data to us_zips table
    df.to_sql("us_zips", conn, if_exists="replace", index=False)

    # Close the connection
    conn.close()

    return Output(df)

# Asset 3: Join bank_transactions and us_zips to get city info
@asset(deps=[bank_transactions, us_zips])
def transactions_city_info():

    # SQL query on SQLite
    query = """
    SELECT t1.*, t2.*
    FROM bank_transactions t1
    LEFT JOIN us_zips t2 ON t1.Location = t2.city
    """

    # Get SQLite connection if exists
    conn = SQLiteResource('databases/dagster_data.db').get_connection()
    df = pd.read_sql(query, conn)

    # Save the joined table as transactions_city_info
    df.to_sql("transactions_city_info", conn, if_exists="replace", index=False)

    # Close the connection
    conn.close()

    return Output(df)
