"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://falconswap.typeform.com
Prompt: Provide an example of how to use the Typeform API to retrieve survey responses and export them to a Google Sheet.
Generated: DETERMINISTIC_623f850af665b149
Batch ID: 20250612_151912
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms/{form_id}/responses": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://spreadsheets.google.com/feeds": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/drive": {
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
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

# Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms/{form_id}/responses"
GOOGLE_SHEET_NAME = "Typeform Responses"
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDENTIALS_FILE = 'path/to/your/credentials.json'  # Path to Google API credentials

def get_typeform_responses(form_id, api_key):
    """
    Retrieve survey responses from Typeform using the API.

    :param form_id: ID of the Typeform form
    :param api_key: API key for Typeform
    :return: List of responses
    """
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(TYPEFORM_API_URL.format(form_id=form_id), headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('items', [])
    except requests.RequestException as e:
        print(f"Error retrieving responses: {e}")
        return []

def export_to_google_sheet(responses, sheet_name):
    """
    Export survey responses to a Google Sheet.

    :param responses: List of responses from Typeform
    :param sheet_name: Name of the Google Sheet to export to
    """
    try:
        # Setup Google Sheets API client
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
        client = gspread.authorize(creds)
        sheet = client.open(sheet_name).sheet1  # Open the first sheet

        # Prepare headers based on the first response keys
        if responses:
            headers = responses[0]['answers']  # Assuming the first response contains all the columns
            headers = [answer['field']['id'] for answer in headers]  # Extract field IDs for headers

            # Clear existing data
            sheet.clear()

            # Update headers
            sheet.append_row(headers)

            # Append each response as a new row
            for response in responses:
                row = [answer['text'] if 'text' in answer else '' for answer in response['answers']]
                sheet.append_row(row)
    except Exception as e:
        print(f"Error exporting to Google Sheet: {e}")

def main():
    FORM_ID = 'your_typeform_form_id'  # Replace with your Typeform form ID
    TYPEFORM_API_KEY = 'your_typeform_api_key'  # Replace with your Typeform API key

    # Retrieve responses from Typeform
    responses = get_typeform_responses(FORM_ID, TYPEFORM_API_KEY)

    # Export responses to Google Sheet
    export_to_google_sheet(responses, GOOGLE_SHEET_NAME)

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `'path/to/your/credentials.json'`, `'your_typeform_form_id'`, and `'your_typeform_api_key'` with your actual credentials and IDs.
2. Make sure the Google Sheets API is enabled for your project and that your service account has access to the target spreadsheet.
