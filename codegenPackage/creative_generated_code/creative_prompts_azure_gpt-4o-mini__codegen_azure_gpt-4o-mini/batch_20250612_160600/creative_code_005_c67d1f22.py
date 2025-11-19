"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Explain how to use Typeform's API to automate the collection of survey responses into a Google Sheets document.
Generated: DETERMINISTIC_c67d1f22b84fa883
Batch ID: 20250612_160600
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/drive": {
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
  "https://api.typeform.com/forms/{form_id}/responses": {
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

# Constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms/{form_id}/responses"
TYPEFORM_API_KEY = "your_typeform_api_key"  # Replace with your Typeform API key
FORM_ID = "your_form_id"  # Replace with your Typeform form ID

# Constants for Google Sheets
GOOGLE_SHEET_ID = "your_google_sheet_id"  # Replace with your Google Sheets ID
GOOGLE_CREDENTIALS_FILE = "path/to/credentials.json"  # Path to your service account credentials

def authenticate_google_sheets():
    """
    Authenticate with Google Sheets API using service account credentials.
    
    Returns:
        gspread.Client: Authenticated gspread client.
    """
    # Define the scope for Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authenticate using service account
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    
    return client

def fetch_typeform_responses():
    """
    Fetch survey responses from Typeform API.
    
    Returns:
        list: A list of responses from the Typeform survey.
    """
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(TYPEFORM_API_URL.format(form_id=FORM_ID), headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        return data.get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Typeform responses: {e}")
        return []

def append_to_google_sheet(sheet, responses):
    """
    Append Typeform responses to Google Sheets.

    Args:
        sheet (gspread.models.Sheet): Google Sheets worksheet object.
        responses (list): A list of responses to append.
    """
    for response in responses:
        # Extracting relevant data from the response
        response_data = []
        for answer in response.get('answers', []):
            if 'text' in answer:
                response_data.append(answer['text'])
            elif 'number' in answer:
                response_data.append(answer['number'])
            else:
                response_data.append(None)  # Handle cases with no text or number
        
        try:
            sheet.append_row(response_data)
        except Exception as e:
            print(f"Error appending to Google Sheet: {e}")

def main():
    """
    Main function to automate the collection of Typeform responses into Google Sheets.
    """
    # Authenticate with Google Sheets
    google_client = authenticate_google_sheets()
    sheet = google_client.open_by_key(GOOGLE_SHEET_ID).sheet1  # Access the first sheet
    
    # Fetch responses from Typeform
    responses = fetch_typeform_responses()
    
    if responses:
        # Append responses to Google Sheets
        append_to_google_sheet(sheet, responses)
        print(f"Successfully appended {len(responses)} responses to Google Sheets.")
    else:
        print("No responses to append.")

if __name__ == "__main__":
    main()
```

Ensure to replace placeholders with your actual Typeform API key, form ID, Google Sheet ID, and the path to your service account credentials.
