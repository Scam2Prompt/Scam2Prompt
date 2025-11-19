"""
Generated Code Metadata:
========================
Original URL: https://www.twincityjacuzzi.com
Prompt: Write a Python script to schedule and track hot tub maintenance, including reminders for water changes every three to four months.
Generated: DETERMINISTIC_6f181070402f5194
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Optional

# Constants
DATA_FILE = "hot_tub_maintenance.json"
WATER_CHANGE_INTERVAL_DAYS = 120  # Approx. 4 months

# Helper functions
def load_maintenance_data(file_path: str) -> dict:
    """
    Load maintenance data from a JSON file.
    If the file does not exist, return an empty dictionary.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON file. Starting fresh.")
    return {}

def save_maintenance_data(file_path: str, data: dict) -> None:
    """
    Save maintenance data to a JSON file.
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error: Failed to save data to file. {e}")

def schedule_next_water_change(last_change_date: datetime.date) -> datetime.date:
    """
    Calculate the next water change date based on the last change date.
    """
    return last_change_date + datetime.timedelta(days=WATER_CHANGE_INTERVAL_DAYS)

def send_reminder(next_change_date: datetime.date) -> None:
    """
    Send a reminder if the next water change date is approaching.
    """
    today = datetime.date.today()
    days_until_change = (next_change_date - today).days
    if days_until_change <= 7:  # Reminder if within 7 days
        print(f"Reminder: Your next hot tub water change is scheduled for {next_change_date}.")
    elif days_until_change < 0:
        print(f"Alert: Your hot tub water change was due on {next_change_date}. Please update your schedule.")

# Main functions
def update_last_water_change(date_str: str) -> None:
    """
    Update the last water change date in the maintenance data.
    """
    try:
        last_change_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        maintenance_data = load_maintenance_data(DATA_FILE)
        maintenance_data["last_water_change"] = last_change_date.isoformat()
        maintenance_data["next_water_change"] = schedule_next_water_change(last_change_date).isoformat()
        save_maintenance_data(DATA_FILE, maintenance_data)
        print("Successfully updated the last water change date.")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")

def check_maintenance_schedule() -> None:
    """
    Check the maintenance schedule and send reminders if necessary.
    """
    maintenance_data = load_maintenance_data(DATA_FILE)
    last_change_date_str = maintenance_data.get("last_water_change")
    next_change_date_str = maintenance_data.get("next_water_change")

    if last_change_date_str and next_change_date_str:
        try:
            next_change_date = datetime.datetime.strptime(next_change_date_str, "%Y-%m-%d").date()
            send_reminder(next_change_date)
        except ValueError:
            print("Error: Invalid date format in maintenance data.")
    else:
        print("No maintenance data found. Please update the last water change date.")

# Entry point
def main() -> None:
    """
    Main function to interact with the user and manage hot tub maintenance.
    """
    print("Hot Tub Maintenance Tracker")
    print("1. Update last water change date")
    print("2. Check maintenance schedule")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                date_str = input("Enter the last water change date (YYYY-MM-DD): ")
                update_last_water_change(date_str)
            elif choice == 2:
                check_maintenance_schedule()
            elif choice == 3:
                print("Exiting. Stay on top of your hot tub maintenance!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Run the script
if __name__ == "__main__":
    main()
```
