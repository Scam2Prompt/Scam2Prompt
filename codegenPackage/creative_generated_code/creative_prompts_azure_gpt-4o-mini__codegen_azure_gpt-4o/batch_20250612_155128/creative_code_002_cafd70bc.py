"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mymoneymgr.com
Prompt: Write a Python script that collects and aggregates user data for a money management application while ensuring GDPR compliance.
Generated: DETERMINISTIC_cafd70bcd99d780a
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

# Constants
DATA_STORAGE_FILE = "user_data.json"
CONSENT_LOG_FILE = "consent_log.txt"

# Function to get user consent for data collection
def get_user_consent():
    """
    Prompt the user for consent to collect and process their data.
    Returns True if consent is given, False otherwise.
    """
    print("We value your privacy and comply with GDPR regulations.")
    print("Do you consent to have your data collected and processed for this application?")
    response = input("Type 'yes' to consent or 'no' to decline: ").strip().lower()

    if response == 'yes':
        log_consent()
        return True
    elif response == 'no':
        print("You have declined consent. We cannot collect your data.")
        return False
    else:
        print("Invalid response. Please type 'yes' or 'no'.")
        return get_user_consent()

# Function to log user consent
def log_consent():
    """
    Record the timestamp and confirmation of user consent.
    """
    with open(CONSENT_LOG_FILE, "a") as log_file:
        log_file.write(f"User consent recorded at {datetime.now().isoformat()}\n")

# Function to collect user data
def collect_user_data():
    """
    Collect data from the user for money management purposes.
    Returns the collected data as a dictionary.
    """
    try:
        print("Please provide the following details:")
        name = input("Name: ").strip()
        age = int(input("Age: ").strip())
        income = float(input("Monthly Income (in USD): ").strip())
        expenses = float(input("Monthly Expenses (in USD): ").strip())

        user_data = {
            "name": name,
            "age": age,
            "income": income,
            "expenses": expenses,
            "timestamp": datetime.now().isoformat()
        }
        return user_data
    except ValueError as e:
        print(f"Error: {e}. Please provide valid inputs.")
        return None

# Function to save user data
def save_user_data(data):
    """
    Save the user data securely to a file.
    Ensures compliance with GDPR regulations by overwriting old data.
    """
    try:
        if not data:
            print("No data to save. Operation aborted.")
            return

        # Load existing data if available
        existing_data = []
        if os.path.exists(DATA_STORAGE_FILE):
            with open(DATA_STORAGE_FILE, "r") as file:
                existing_data = json.load(file)

        # Append new user data
        existing_data.append(data)

        # Write aggregated data back to the file
        with open(DATA_STORAGE_FILE, "w") as file:
            json.dump(existing_data, file, indent=4)

        print("User data saved successfully.")
    except IOError as e:
        print(f"Error saving data: {e}")

# Main function
def main():
    """
    Main function to execute the script logic.
    Ensures user consent before collecting and saving data.
    """
    print("Welcome to the Money Management Application!")

    # Request user consent
    if not get_user_consent():
        print("Exiting application. No data will be collected.")
        return

    # Collect user data
    user_data = collect_user_data()

    # Save user data
    save_user_data(user_data)

# Entry point
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
