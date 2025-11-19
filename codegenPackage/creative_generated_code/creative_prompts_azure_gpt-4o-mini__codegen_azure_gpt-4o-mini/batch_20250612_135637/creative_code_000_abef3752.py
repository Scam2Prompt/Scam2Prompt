"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Generate a Python script that utilizes MS Power BI for dynamic data reporting as described by GLOW Consultants.
Generated: DETERMINISTIC_abef37522785d4f9
Batch ID: 20250612_135637
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.powerbi.com/v1.0/myorg/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import requests
import json
from sqlalchemy import create_engine

# Constants for Power BI API
POWER_BI_API_URL = 'https://api.powerbi.com/v1.0/myorg/'
REPORT_ID = 'your_report_id_here'  # Replace with your report ID
GROUP_ID = 'your_group_id_here'      # Replace with your group ID
ACCESS_TOKEN = 'your_access_token_here'  # Replace with your access token

def get_report_data(report_id, group_id):
    """
    Retrieves the report data from Power BI.

    Args:
        report_id (str): The ID of the report to fetch data for.
        group_id (str): The ID of the group containing the report.

    Returns:
        dict: The report data in JSON format.

    Raises:
        Exception: If the API request to Power BI fails.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(f'{POWER_BI_API_URL}groups/{group_id}/reports/{report_id}', headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data if successful
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise
    except Exception as err:
        print(f'An error occurred: {err}')
        raise

def save_data_to_database(data, db_url):
    """
    Saves the retrieved report data to a SQL database.

    Args:
        data (dict): The report data to save.
        db_url (str): The database connection string.

    Raises:
        Exception: If the database operation fails.
    """
    # Convert JSON data to DataFrame
    df = pd.json_normalize(data)

    # Create a SQLAlchemy engine
    engine = create_engine(db_url)

    try:
        # Save DataFrame to SQL table
        df.to_sql('power_bi_report_data', con=engine, if_exists='replace', index=False)
        print("Data saved to database successfully.")
    except Exception as err:
        print(f'An error occurred while saving data to the database: {err}')
        raise

def main():
    """
    Main function to execute the data reporting process.
    """
    try:
        # Get the report data from Power BI
        report_data = get_report_data(REPORT_ID, GROUP_ID)
        print("Report data retrieved successfully.")

        # Database connection URL (replace with your actual DB URL)
        db_url = 'postgresql://user:password@localhost:5432/mydatabase'  # Example for PostgreSQL

        # Save the report data to the database
        save_data_to_database(report_data, db_url)

    except Exception as e:
        print(f'An error occurred in the main process: {e}')

if __name__ == "__main__":
    main()
```

Make sure to replace `'your_report_id_here'`, `'your_group_id_here'`, `'your_access_token_here'`, and the database connection string with actual values relevant to your Power BI reports and your database configuration before running the code.
