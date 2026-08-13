import duckdb
import pandas as pd

# Set pandas display options for clean terminal output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'left')


def run_logistics_analysis():
  # Connect to in-memory DuckDB
  con = duckdb.connect(database=':memory:')

  # Register the CSV file as a virtual table named 'saudi_logistics_data'
  con.execute(
      "CREATE VIEW saudi_logistics_data AS SELECT * FROM"
      " 'saudi_logistics_data.csv'"
  )

  # Read the SQL queries file
  with open('warehouse_analysis.sql', 'r') as file:
    sql_script = file.read()

  # Split SQL queries by semicolon
  queries = [q.strip() for q in sql_script.split(';') if q.strip()]

  headers = [
      '📊 1. Regional On-Time In-Full (OTIF) Performance by Hub',
      '🚚 2. Courier Speed & Cost Efficiency Ranking',
      '🚨 3. Top Bottleneck Routes & Delay Impact Analysis',
  ]

  print('=' * 80)
  print('🇸🇦 SAUDI LOGISTICS & SUPPLY CHAIN ANALYTICS REPORT')
  print('=' * 80 + '\n')

  for i, query in enumerate(queries):
    if i < len(headers):
      print(f'{headers[i]}')
      print('-' * 80)

    # Execute query and fetch as Pandas DataFrame
    df_result = con.execute(query).df()
    print(df_result.to_string(index=False))
    print('\n' + '=' * 80 + '\n')


if __name__ == '__main__':
  run_logistics_analysis()