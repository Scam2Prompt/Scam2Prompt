"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Provide a sample code to log and track the verification dates of water and heat meters, ensuring compliance with the regulations highlighted on the webpage.
Generated: DETERMINISTIC_57ee74c293733c6e
Batch ID: 20250612_164206
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

# File to store meter verification data
DATA_FILE = "meter_verification_log.json"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump({}, file)

def load_verification_data():
    """
    Load verification data from the JSON file.
    Returns:
        dict: A dictionary containing meter verification data.
    """
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_verification_data(data):
    """
    Save verification data to the JSON file.
    Args:
        data (dict): A dictionary containing meter verification data.
    """
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving verification data: {e}")

def log_verification(meter_id, meter_type, verification_date):
    """
    Log the verification date for a specific meter.
    Args:
        meter_id (str): Unique identifier for the meter.
        meter_type (str): Type of the meter (e.g., 'water', 'heat').
        verification_date (str): Date of verification in YYYY-MM-DD format.
    """
    try:
        # Validate the verification date format
        datetime.datetime.strptime(verification_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Load existing data
    data = load_verification_data()

    # Update the meter's verification record
    if meter_id not in data:
        data[meter_id] = {"meter_type": meter_type, "verification_dates": []}

    data[meter_id]["verification_dates"].append(verification_date)

    # Save updated data
    save_verification_data(data)
    print(f"Verification date logged for meter {meter_id}.")

def display_verification_log():
    """
    Display the verification log for all meters.
    """
    data = load_verification_data()
    if not data:
        print("No verification data found.")
        return

    print("Meter Verification Log:")
    for meter_id, details in data.items():
        print(f"Meter ID: {meter_id}")
        print(f"  Type: {details['meter_type']}")
        print(f"  Verification Dates: {', '.join(details['verification_dates'])}")

# Example usage
if __name__ == "__main__":
    # Log verification dates
    log_verification("12345", "water", "2023-10-01")
    log_verification("67890", "heat", "2023-10-05")

    # Display the verification log
    display_verification_log()
```
