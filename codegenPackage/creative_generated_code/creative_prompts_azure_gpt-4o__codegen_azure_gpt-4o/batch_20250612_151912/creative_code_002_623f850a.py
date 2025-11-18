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
  "https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses": {
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

# Google Sheets setup
# Replace 'path/to/credentials.json' with the path to your Google Service Account JSON credentials file.
# Replace 'Google Sheet Name' with the name of your Google Sheet.
GOOGLE_SHEET_NAME = 'Google Sheet Name'
GOOGLE_CREDENTIALS_FILE = 'path/to/credentials.json'

# Typeform API setup
TYPEFORM_API_KEY = 'your_typeform_api_key'
TYPEFORM_FORM_ID = 'your_form_id'
TYPEFORM_API_URL = f'https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses'

def fetch_typeform_responses(api_key, form_id):
    """
    Fetch survey responses from Typeform API.
    :param api_key: Typeform API key.
    :param form_id: Typeform form ID.
    :return: List of survey responses.
    """
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    try:
        response = requests.get(TYPEFORM_API_URL, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data.get('items', [])  # Return the survey responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching responses from Typeform API: {e}")
        return []

def update_google_sheet(sheet_name, credentials_file, survey_responses):
    """
    Update a Google Sheet with survey responses.
    :param sheet_name: Name of the Google Sheet.
    :param credentials_file: Path to Google Service Account credentials file.
    :param survey_responses: List of survey responses from Typeform.
    """
    # Define the scope for Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    try:
        # Authenticate with Google Sheets
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(credentials)
        
        # Open the Google Sheet
        sheet = client.open(sheet_name).sheet1
        
        # Clear existing content in the sheet
        sheet.clear()
        
        # Prepare headers and data for Google Sheet
        headers = ['Response ID', 'Submitted At', 'Answers']
        data = [headers]  # Initialize with headers
        
        for response in survey_responses:
            response_id = response.get('response_id')
            submitted_at = response.get('submitted_at')
            answers = response.get('answers', [])

            # Extract answers in a readable format
            formatted_answers = ', '.join([f"{a.get('field', {}).get('ref')}: {a.get('text', '')}" for a in answers])
            data.append([response_id, submitted_at, formatted_answers])
        
        # Update the Google Sheet with data
        sheet.update(data)
        print("Google Sheet updated successfully.")
    except Exception as e:
        print(f"Error updating Google Sheet: {e}")

def main():
    """
    Main function to fetch Typeform survey responses and export them to a Google Sheet.
    """
    survey_responses = fetch_typeform_responses(TYPEFORM_API_KEY, TYPEFORM_FORM_ID)
    if survey_responses:
        update_google_sheet(GOOGLE_SHEET_NAME, GOOGLE_CREDENTIALS_FILE, survey_responses)
    else:
        print("No responses found or error occurred.")

if __name__ == '__main__':
    main()
```

### Instructions:
1. Replace `'your_typeform_api_key'` and `'your_form_id'` with your Typeform API key and form ID.
2. Replace `'path/to/credentials.json'` and `'Google Sheet Name'` with appropriate values for your Google Sheet setup.
3. Install the required packages using `pip install requests gspread oauth2client`.
4. Run the script (`python script_name.py`) after setting up the necessary configurations.
