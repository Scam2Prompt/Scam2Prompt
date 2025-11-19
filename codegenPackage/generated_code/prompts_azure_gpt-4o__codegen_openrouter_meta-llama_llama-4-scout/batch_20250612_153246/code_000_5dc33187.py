"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write Python code to automate scheduling of housekeeping services using the contact details and service categories provided by Ashvi Facility Management Services.
Generated: DETERMINISTIC_5dc3318707c3d2aa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HousekeepingService:
    def __init__(self, contact_details: Dict, service_categories: List):
        """
        Initialize the HousekeepingService class.

        Args:
        - contact_details (Dict): A dictionary containing contact information.
        - service_categories (List): A list of service categories.
        """
        self.contact_details = contact_details
        self.service_categories = service_categories
        self.schedule = {}

    def add_service(self, service_name: str, service_date: str, service_time: str):
        """
        Add a service to the schedule.

        Args:
        - service_name (str): The name of the service.
        - service_date (str): The date of the service in YYYY-MM-DD format.
        - service_time (str): The time of the service in HH:MM format.

        Returns:
        - bool: True if the service was added successfully, False otherwise.
        """
        try:
            # Validate date and time
            datetime.datetime.strptime(service_date, '%Y-%m-%d')
            datetime.datetime.strptime(service_time, '%H:%M')

            # Create a service ID
            service_id = f"{service_name}_{service_date}_{service_time}"

            # Add service to schedule
            self.schedule[service_id] = {
                'service_name': service_name,
                'service_date': service_date,
                'service_time': service_time,
                'contact_details': self.contact_details,
                'service_categories': self.service_categories
            }

            logging.info(f"Service '{service_name}' added to schedule for {service_date} at {service_time}")
            return True

        except ValueError:
            logging.error("Invalid date or time format")
            return False

    def view_schedule(self):
        """
        View the current schedule.

        Returns:
        - Dict: The current schedule.
        """
        return self.schedule

    def save_schedule(self, filename: str):
        """
        Save the schedule to a JSON file.

        Args:
        - filename (str): The name of the file to save the schedule to.

        Returns:
        - bool: True if the schedule was saved successfully, False otherwise.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            logging.info(f"Schedule saved to {filename}")
            return True

        except Exception as e:
            logging.error(f"Failed to save schedule: {str(e)}")
            return False

def main():
    # Example usage
    contact_details = {
        'name': 'Ashvi Facility Management Services',
        'phone': '1234567890',
        'email': 'ashvi@example.com'
    }

    service_categories = ['Housekeeping', 'Laundry', 'Pest Control']

    housekeeping_service = HousekeepingService(contact_details, service_categories)

    housekeeping_service.add_service('Housekeeping', '2024-09-17', '10:00')
    housekeeping_service.add_service('Laundry', '2024-09-18', '14:00')

    schedule = housekeeping_service.view_schedule()
    print(json.dumps(schedule, indent=4))

    housekeeping_service.save_schedule('schedule.json')

if __name__ == "__main__":
    main()
```
