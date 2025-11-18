"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Write Python code to create a custom "Action Tracker" Google Sheet template for monitoring daily progress, inspired by the tools offered in the Action Accelerator Academy. Include features for tracking completed tasks, setting intentions, and reflecting on progress.
Generated: DETERMINISTIC_dfc3071f1bb018d5
Batch ID: 20250612_152240
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
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Define the scope and credentials for Google Sheets API
SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Authenticate and create a client to interact with Google Sheets
def authenticate_gsheet():
    try:
        credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        print(f"Error authenticating with Google Sheets API: {e}")
        raise

# Create a new Google Sheet for the Action Tracker
def create_action_tracker_sheet(client):
    try:
        sheet_title = f"Action Tracker - {datetime.now().strftime('%Y-%m-%d')}"
        sheet = client.create(sheet_title)
        return sheet
    except Exception as e:
        print(f"Error creating Google Sheet: {e}")
        raise

# Set up the sheet with headers and formatting
def setup_sheet(sheet):
    try:
        worksheet = sheet.get_worksheet(0)  # Get the first worksheet
        headers = ["Date", "Task", "Intention", "Completed", "Reflection"]
        worksheet.append_row(headers)  # Add the headers
        
        # Set column widths
        worksheet.format("A:A", {"width": 120})  # Date
        worksheet.format("B:B", {"width": 300})  # Task
        worksheet.format("C:C", {"width": 200})  # Intention
        worksheet.format("D:D", {"width": 100})  # Completed
        worksheet.format("E:E", {"width": 300})  # Reflection

        print("Sheet setup completed with headers and formatting.")
    except Exception as e:
        print(f"Error setting up the sheet: {e}")
        raise

# Main function to execute the Action Tracker creation
def main():
    client = authenticate_gsheet()  # Authenticate with Google Sheets
    action_tracker_sheet = create_action_tracker_sheet(client)  # Create the sheet
    setup_sheet(action_tracker_sheet)  # Set up the sheet

# Entry point of the script
if __name__ == "__main__":
    main()
```
Make sure to replace `'path/to/your/service-account-file.json'` with the actual path to your Google Cloud service account JSON file. This code will create a new Google Sheet titled "Action Tracker - YYYY-MM-DD" with appropriate headers and formatting for tracking daily progress.
