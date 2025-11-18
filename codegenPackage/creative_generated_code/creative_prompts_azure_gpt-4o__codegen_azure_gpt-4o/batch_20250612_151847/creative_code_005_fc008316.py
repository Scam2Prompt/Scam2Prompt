"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktx.typeform.com
Prompt: Provide an example of how to use Typeform's NPS form builder to collect Net Promoter Score data and integrate it with Google Sheets for reporting.
Generated: DETERMINISTIC_fc0083164d30aba6
Batch ID: 20250612_151847
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

# Constants for Typeform API
TYPEFORM_API_TOKEN = "your_typeform_api_token"
TYPEFORM_FORM_ID = "your_typeform_form_id"

# Google Sheets setup
GOOGLE_SHEETS_CREDENTIALS_FILE = "path_to_your_google_service_account_credentials.json"
GOOGLE_SHEET_NAME = "NPS_Data"

# Function to fetch NPS data from Typeform
def fetch_nps_data():
    """
    Fetch NPS response data from Typeform API.
    Returns:
        list of dict: List of responses containing email and score.
    """
    url = f"https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Typeform: {e}")
        return []

    # Parse responses to extract email and score
    results = []
    for item in data.get('items', []):
        answers = {answer['field']['id']: answer['text'] for answer in item.get('answers', [])}
        email = answers.get("your_email_field_id")  # Replace with your actual field ID
        score = answers.get("your_score_field_id")  # Replace with your actual field ID
        if email and score:
            results.append({"email": email, "score": score})
    return results

# Function to save data to Google Sheets
def save_to_google_sheets(data):
    """
    Save NPS data to Google Sheets.
    Args:
        data (list of dict): List of responses containing email and score.
    """
    try:
        # Setup Google Sheets authentication
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS_FILE, scope)
        client = gspread.authorize(creds)

        # Open the workbook and sheet
        sheet = client.open(GOOGLE_SHEET_NAME).sheet1

        # Add header row if not present
        if len(sheet.get_all_records()) == 0:
            sheet.append_row(["Email", "Score"])

        # Append data row-by-row
        for entry in data:
            sheet.append_row([entry["email"], entry["score"]])
    except Exception as e:
        print(f"Error saving data to Google Sheets: {e}")

# Main function to orchestrate the process
def main():
    """
    Main function to fetch NPS data from Typeform and save to Google Sheets.
    """
    print("Fetching NPS data from Typeform...")
    nps_data = fetch_nps_data()
    if not nps_data:
        print("No data found or an error occurred.")
        return

    print("Saving data to Google Sheets...")
    save_to_google_sheets(nps_data)
    print("Data successfully saved!")

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note:** Replace placeholders (`your_typeform_api_token`, `your_typeform_form_id`, `your_email_field_id`, `your_score_field_id`, and `path_to_your_google_service_account_credentials.json`) with appropriate values specific to your Typeform form and Google Sheets setup. Ensure your Google Service Account has write permissions to the target Google Sheet.
