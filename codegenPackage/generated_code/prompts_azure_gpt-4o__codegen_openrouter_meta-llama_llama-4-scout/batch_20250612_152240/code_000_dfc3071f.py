"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write Python code to create a custom "Action Tracker" Google Sheet template for monitoring daily progress, inspired by the tools offered in the Action Accelerator Academy. Include features for tracking completed tasks, setting intentions, and reflecting on progress.
Generated: DETERMINISTIC_dfc3071f1bb018d5
Batch ID: 20250612_152240
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
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

# Generated Code:
# ===============

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# Set up authentication with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Create a client instance
client = gspread.authorize(credentials)

# Define the template for the Action Tracker sheet
def create_action_tracker_template(sheet_name):
    """
    Creates a custom Action Tracker Google Sheet template.

    Args:
        sheet_name (str): The name of the sheet to create.

    Returns:
        The created sheet object.
    """
    try:
        # Create a new spreadsheet
        spreadsheet = client.create(sheet_name)

        # Get the first sheet
        sheet = client.open(sheet_name).sheet1

        # Set up the header row
        sheet.update_acell('A1', 'Date')
        sheet.update_acell('B1', 'Intention')
        sheet.update_acell('C1', 'Completed Tasks')
        sheet.update_acell('D1', 'Reflection')

        # Set up the formatting for the header row
        sheet.format('A1:D1', {'textFormat': {'bold': True}})

        # Freeze the header row
        sheet.format('A1:D1', {'horizontalAlignment': 'center'})

        # Return the created sheet
        return sheet

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define a function to update the Action Tracker sheet
def update_action_tracker(sheet, date, intention, completed_tasks, reflection):
    """
    Updates the Action Tracker sheet with new data.

    Args:
        sheet: The sheet object to update.
        date (str): The date of the entry.
        intention (str): The intention for the day.
        completed_tasks (str): The completed tasks for the day.
        reflection (str): The reflection for the day.
    """
    try:
        # Get the next available row
        row = sheet.row_count + 1

        # Update the cells
        sheet.update_acell(f'A{row}', date)
        sheet.update_acell(f'B{row}', intention)
        sheet.update_acell(f'C{row}', completed_tasks)
        sheet.update_acell(f'D{row}', reflection)

    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to get today's date
def get_today():
    """
    Returns today's date in the format YYYY-MM-DD.
    """
    return datetime.now().strftime('%Y-%m-%d')

# Define a function to get yesterday's date
def get_yesterday():
    """
    Returns yesterday's date in the format YYYY-MM-DD.
    """
    return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

# Example usage
if __name__ == "__main__":
    sheet_name = 'Action Tracker'
    sheet = create_action_tracker_template(sheet_name)

    if sheet:
        today = get_today()
        intention = 'Example intention'
        completed_tasks = 'Task 1, Task 2'
        reflection = 'Example reflection'

        update_action_tracker(sheet, today, intention, completed_tasks, reflection)

        yesterday = get_yesterday()
        update_action_tracker(sheet, yesterday, 'Yesterday\'s intention', 'Task 3', 'Yesterday\'s reflection')
```
