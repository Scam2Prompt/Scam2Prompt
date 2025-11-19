"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Design a system for automating the maintenance and servicing of home security and alarm systems in a property management company.
Generated: DETERMINISTIC_1f8db90d35c744de
Batch ID: 20250622_210443
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
SERVICE_INTERVAL_DAYS = 180  # Number of days between maintenance checks
ALARM_SYSTEMS_FILE = "alarm_systems.json"  # File to store alarm system data

# Define custom exceptions
class AlarmSystemError(Exception):
    """Custom exception for alarm system errors."""
    pass

# Define data model for alarm systems
class AlarmSystem:
    def __init__(self, system_id: str, location: str, last_service_date: str):
        """
        Initialize an AlarmSystem instance.

        :param system_id: Unique identifier for the alarm system
        :param location: Location of the alarm system
        :param last_service_date: Last service date in YYYY-MM-DD format
        """
        self.system_id = system_id
        self.location = location
        self.last_service_date = datetime.datetime.strptime(last_service_date, "%Y-%m-%d")

    def needs_service(self) -> bool:
        """
        Check if the alarm system needs servicing.

        :return: True if the system needs servicing, False otherwise
        """
        next_service_date = self.last_service_date + datetime.timedelta(days=SERVICE_INTERVAL_DAYS)
        return datetime.datetime.now() >= next_service_date

    def update_service_date(self):
        """
        Update the last service date to the current date.
        """
        self.last_service_date = datetime.datetime.now()

# Utility functions
def load_alarm_systems(file_path: str) -> List[AlarmSystem]:
    """
    Load alarm systems from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of AlarmSystem objects
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return [AlarmSystem(**system) for system in data]
    except FileNotFoundError:
        logging.warning("Alarm systems file not found. Starting with an empty list.")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON file: {e}")
        raise AlarmSystemError("Failed to load alarm systems data.")

def save_alarm_systems(file_path: str, systems: List[AlarmSystem]):
    """
    Save alarm systems to a JSON file.

    :param file_path: Path to the JSON file
    :param systems: List of AlarmSystem objects
    """
    try:
        with open(file_path, "w") as file:
            json.dump([{
                "system_id": system.system_id,
                "location": system.location,
                "last_service_date": system.last_service_date.strftime("%Y-%m-%d")
            } for system in systems], file, indent=4)
    except Exception as e:
        logging.error(f"Error saving alarm systems data: {e}")
        raise AlarmSystemError("Failed to save alarm systems data.")

def perform_maintenance(systems: List[AlarmSystem]) -> List[Dict[str, str]]:
    """
    Perform maintenance on alarm systems that need servicing.

    :param systems: List of AlarmSystem objects
    :return: List of maintenance records
    """
    maintenance_records = []
    for system in systems:
        if system.needs_service():
            logging.info(f"Performing maintenance on system {system.system_id} at {system.location}.")
            system.update_service_date()
            maintenance_records.append({
                "system_id": system.system_id,
                "location": system.location,
                "service_date": system.last_service_date.strftime("%Y-%m-%d")
            })
    return maintenance_records

# Main function
def main():
    """
    Main function to automate maintenance and servicing of alarm systems.
    """
    try:
        # Load alarm systems
        alarm_systems = load_alarm_systems(ALARM_SYSTEMS_FILE)

        # Perform maintenance
        maintenance_records = perform_maintenance(alarm_systems)

        # Save updated alarm systems
        save_alarm_systems(ALARM_SYSTEMS_FILE, alarm_systems)

        # Log maintenance records
        if maintenance_records:
            logging.info("Maintenance completed for the following systems:")
            for record in maintenance_records:
                logging.info(record)
        else:
            logging.info("No systems required maintenance at this time.")
    except AlarmSystemError as e:
        logging.error(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
