"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: Generate a script using the Google Sheets API to create a catalog of CM-Canada's product lines, including Fontes, Accouplements, Valves, and PEX systems, with columns for product names, descriptions, and prices.
Generated: DETERMINISTIC_28c25d870ad5d8e9
Batch ID: 20250612_155048
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/spreadsheets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Define the scope for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# Path to the service account key file
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'

# Authenticate and create a client to interact with Google Sheets
def authenticate_google_sheets():
    try:
        credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        print(f"Error during authentication: {e}")
        raise

# Create a new Google Sheet for the product catalog
def create_product_catalog(client):
    try:
        # Create a new spreadsheet
        spreadsheet = client.create('CM-Canada Product Catalog')
        # Share the spreadsheet with a specific email (optional)
        # spreadsheet.share('your-email@example.com', perm_type='user', role='writer')
        return spreadsheet
    except Exception as e:
        print(f"Error creating spreadsheet: {e}")
        raise

# Populate the spreadsheet with product data
def populate_catalog(sheet):
    # Define the headers and product data
    headers = ['Product Name', 'Description', 'Price']
    products = [
        ['Fontes', 'High-quality fontes for various applications', 100.00],
        ['Accouplements', 'Durable accouplements for secure connections', 75.00],
        ['Valves', 'Reliable valves for fluid control', 50.00],
        ['PEX Systems', 'Flexible PEX systems for plumbing solutions', 120.00]
    ]

    try:
        # Select the first worksheet
        worksheet = sheet.get_worksheet(0)
        # Update the worksheet with headers and product data
        worksheet.append_row(headers)
        for product in products:
            worksheet.append_row(product)
        print("Product catalog populated successfully.")
    except Exception as e:
        print(f"Error populating catalog: {e}")
        raise

# Main function to execute the script
def main():
    client = authenticate_google_sheets()
    sheet = create_product_catalog(client)
    populate_catalog(sheet)

if __name__ == '__main__':
    main()
```

**Note:** 
- Replace `'path/to/your/service_account.json'` with the actual path to your Google service account JSON key file.
- Optionally, you can uncomment the line to share the spreadsheet with a specific email address.
