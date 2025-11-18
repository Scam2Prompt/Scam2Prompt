"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Write Python code to create a custom "Action Tracker" Google Sheet template for monitoring daily progress, inspired by the tools offered in the Action Accelerator Academy. Include features for tracking completed tasks, setting intentions, and reflecting on progress.
Generated: DETERMINISTIC_dfc3071f1bb018d5
Batch ID: 20250612_152240
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/drive": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

# Define the scope for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Path to the service account credentials JSON file
SERVICE_ACCOUNT_FILE = 'path/to/your-service-account-file.json'

# Authenticate and initialize the client
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(credentials)

# Function to create a custom "Action Tracker" Google Sheet template
def create_action_tracker(sheet_name):
    try:
        # Create a new Google Sheet
        spreadsheet = gc.create(sheet_name)
        
        # Share the sheet (Optional: Replace with your email or remove this line if not needed)
        spreadsheet.share("your-email@example.com", perm_type='user', role='writer')
        
        # Open the sheet
        worksheet = spreadsheet.sheet1
        
        # Set the title and headers for the sheet
        worksheet.update_title("Action Tracker")
        headers = [
            "Date",
            "Intention for the Day",
            "Tasks Completed",
            "Reflections",
            "Mood/Overall Feeling"
        ]
        worksheet.insert_row(headers, index=1)
        
        # Add example data for demonstration (Optional)
        example_data = [
            ["2023-10-01", "Stay focused on priorities", "Finished project report", "Felt productive", "Good"],
            ["2023-10-02", "Practice mindfulness", "Completed workout", "Calm and centered", "Great"]
        ]
        worksheet.insert_rows(example_data, row=2)
        
        print(f"Action Tracker created successfully: {spreadsheet.url}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to create the Google Sheet
create_action_tracker("My Action Tracker")
```

**Note:** 
1. Replace `path/to/your-service-account-file.json` with the actual path to your Google Cloud Service Account JSON file. 
2. Replace `your-email@example.com` with your email address or the email address you'd like to share the sheet with.
3. Ensure the `gspread` library is installed (`pip install gspread google-auth`).
