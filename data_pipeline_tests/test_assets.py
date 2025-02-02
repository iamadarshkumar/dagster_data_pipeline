from data_pipeline.assets import bank_transactions, us_zips, transactions_city_info
import pandas as pd
import pytest

def test_bank_transactions():
    df = bank_transactions().value
    assert not df.empty

    # Check if 'TransactionDate' is a valid timestamp
    try:
        # Attempt to convert the 'TransactionDate' column to datetime
        df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='raise')
    except Exception as e:
        # If there is an error during conversion, the test fails
        pytest.fail(f"Error: {e} - 'TransactionDate' is not a valid timestamp.")
    
    # Also, check if the column is indeed a datetime type
    assert pd.api.types.is_datetime64_any_dtype(df['TransactionDate']), "'TransactionDate' is not of datetime type"

def test_us_zips():
    df = us_zips().value
    assert not df.empty

def test_transactions_city_info():
    df = transactions_city_info().value
    assert not df.empty