"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: Write a Python script to handle service maintenance notifications for a web application, similar to the message on the Giorgiobarbagelata website.
Generated: DETERMINISTIC_c12a72330e4d5bf0
Batch ID: 20250612_135538
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
MAINTENANCE_FILE = "maintenance_schedule.json"  # File to store maintenance schedule
NOTIFICATION_FILE = "notifications.json"       # File to store notifications
DEFAULT_NOTIFICATION = "The service is currently under maintenance. Please check back later."

# Function to load JSON data from a file
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning(f"{file_path} not found. Returning empty data.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {file_path}. Returning empty data.")
        return {}

# Function to save JSON data to a file
def save_json(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving JSON to {file_path}: {e}")

# Function to check if the service is under maintenance
def is_under_maintenance():
    maintenance_data = load_json(MAINTENANCE_FILE)
    current_time = datetime.datetime.now()

    for maintenance in maintenance_data.get("schedule", []):
        try:
            start_time = datetime.datetime.strptime(maintenance["start"], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.datetime.strptime(maintenance["end"], "%Y-%m-%d %H:%M:%S")
            if start_time <= current_time <= end_time:
                return True, maintenance.get("message", DEFAULT_NOTIFICATION)
        except KeyError as e:
            logging.error(f"Missing key in maintenance schedule: {e}")
        except ValueError as e:
            logging.error(f"Error parsing datetime in maintenance schedule: {e}")

    return False, ""

# Function to handle notifications
def handle_notifications():
    under_maintenance, message = is_under_maintenance()

    if under_maintenance:
        logging.info("Service is under maintenance.")
        notification_data = {"status": "maintenance", "message": message}
    else:
        logging.info("Service is operational.")
        notification_data = {"status": "operational", "message": "The service is running normally."}

    save_json(NOTIFICATION_FILE, notification_data)
    return notification_data

# Main function
def main():
    try:
        notification = handle_notifications()
        print(json.dumps(notification, indent=4))
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```

### Notes:
- The script assumes the existence of a `maintenance_schedule.json` file with a structure like:
  ```json
  {
      "schedule": [
          {
              "start": "2023-10-01 10:00:00",
              "end": "2023-10-01 12:00:00",
              "message": "Scheduled maintenance is ongoing. Please check back later."
          }
      ]
  }
  ```
- The script creates or updates a `notifications.json` file with the current service status.
- Proper error handling is included for file operations and datetime parsing.
