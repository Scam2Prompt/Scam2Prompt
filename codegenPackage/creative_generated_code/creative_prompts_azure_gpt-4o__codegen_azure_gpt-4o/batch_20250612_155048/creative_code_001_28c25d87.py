"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Generate a script using the Google Sheets API to create a catalog of CM-Canada's product lines, including Fontes, Accouplements, Valves, and PEX systems, with columns for product names, descriptions, and prices.
Generated: DETERMINISTIC_28c25d870ad5d8e9
Batch ID: 20250612_155048
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/spreadsheets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://developers.google.com/sheets/api/quickstart/python": {
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
"""
Script to create a product catalog in a Google Sheet using the Google Sheets API.

This script assumes you have set up the Google Sheets API and have valid credentials.
Refer to the official Google Sheets API documentation for setup instructions:
https://developers.google.com/sheets/api/quickstart/python
"""

import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Define the Google Sheets API scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Path to your Google service account credentials
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-credentials.json'

# Authenticate to Google Sheets API using the service account credentials
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)

# Define the spreadsheet details
SPREADSHEET_TITLE = "CM-Canada Product Catalog"
PRODUCT_LINES = [
    ["Fontes", "High-quality cast iron products", "$200-$500"],
    ["Accouplements", "Durable couplings for various applications", "$50-$150"],
    ["Valves", "Reliable valves for industrial use", "$100-$300"],
    ["PEX Systems", "Efficient piping systems for residential projects", "$50-$250"]
]

def create_spreadsheet():
    """Create a new Google Sheet and return its spreadsheet ID."""
    try:
        # Request to create a new spreadsheet
        spreadsheet_body = {
            'properties': {'title': SPREADSHEET_TITLE}
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet_body).execute()
        print(f"Spreadsheet created successfully: {spreadsheet['spreadsheetUrl']}")
        return spreadsheet['spreadsheetId']
    except Exception as e:
        print(f"Error creating spreadsheet: {e}")
        raise

def populate_spreadsheet(spreadsheet_id):
    """Populate the Google Sheet with product catalog data."""
    try:
        # Define the data to write to the spreadsheet
        values = [
            ["Product Line", "Description", "Price Range"],  # Header row
        ] + PRODUCT_LINES

        body = {
            'values': values
        }

        # Write the data to the sheet
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="A1",  # Start at the top-left corner
            valueInputOption="RAW",
            body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
    except Exception as e:
        print(f"Error populating spreadsheet: {e}")
        raise

def main():
    """Main function to create and populate the Google Sheet."""
    try:
        spreadsheet_id = create_spreadsheet()
        populate_spreadsheet(spreadsheet_id)
    except Exception as e:
        print(f"Error in main execution: {e}")
        raise

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `'path/to/your/service-account-credentials.json'` with the path to your Google service account credentials file.
- Ensure that the service account has access to create and modify Google Sheets in your Google Workspace.
- Install the required dependencies (`google-api-python-client` and `google-auth`) via pip:
  ```bash
  pip install google-api-python-client google-auth
  ```
- This script adheres to best practices, including error handling and clear documentation.
