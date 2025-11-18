"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define constants for the Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'  # Replace with your spreadsheet ID
RANGE_NAME = 'Sheet1!A1:C1'  # Adjust according to your sheet's layout

# Function to create a Google Sheet if it doesn't exist
def create_spreadsheet(service):
    """Create a new spreadsheet for the product catalog"""
    spreadsheet_body = {
        'properties': {
            'title': 'CM-Canada Product Catalog'
        },
        'sheets': [{'properties': {'title': 'Sheet1'}}]
    }
    
    try:
        spreadsheet = service.spreadsheets().create(body=spreadsheet_body).execute()
        print(f"Spreadsheet created: {spreadsheet['spreadsheetUrl']}")
        return spreadsheet['spreadsheetId']
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Function to update the sheet with product data
def update_sheet(service, spreadsheet_id, values):
    """Update the Google Sheet with product data"""
    body = {
        'values': values
    }
    
    try:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=RANGE_NAME,
            valueInputOption='RAW',
            body=body
        ).execute()
        print("Sheet updated successfully.")
    except HttpError as error:
        print(f"An error occurred while updating the sheet: {error}")

def main():
    """Main function to create and update the product catalog in Google Sheets"""
    # Authenticate and create the Google Sheets API service
    creds, _ = google.auth.default(scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Create a new spreadsheet if it doesn't exist
    spreadsheet_id = SPREADSHEET_ID or create_spreadsheet(service)

    if spreadsheet_id:
        # Define product catalog data
        product_lines = [
            ["Product Name", "Description", "Price"],
            ["Fontes", "High-quality fontes for various applications.", "100"],
            ["Accouplements", "Durable couplings for industrial use.", "150"],
            ["Valves", "Reliable valves for fluid control.", "200"],
            ["PEX Systems", "Efficient PEX systems for plumbing.", "250"]
        ]

        # Update the sheet with the product data
        update_sheet(service, spreadsheet_id, product_lines)

if __name__ == '__main__':
    main()
```

**Note:** 
- Replace `YOUR_SPREADSHEET_ID` with the actual ID of your Google Sheets document.
- Ensure you have the necessary credentials set up for Google Sheets API access in your environment.
