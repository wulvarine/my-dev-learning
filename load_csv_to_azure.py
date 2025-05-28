import pandas as pd
import logging
import sys

logging.basicConfig(level=logging.INFO)

file_path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"❌ Error: {file_path} not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print(f"❌ Error: {file_path} is empty.")
    exit(1)

if df.empty:
    print("❌ Error: DataFrame is empty after loading.")
    exit(1)

expected_columns = {'id', 'name', 'email'}
if not expected_columns.issubset(df.columns):
    print(f"❌ Missing columns: {expected_columns - set(df.columns)}")
    exit(1)

logging.info(df.head())
