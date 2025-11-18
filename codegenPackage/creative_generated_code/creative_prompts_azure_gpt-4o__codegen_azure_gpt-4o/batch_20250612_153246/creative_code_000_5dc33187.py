"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Write Python code to automate scheduling of housekeeping services using the contact details and service categories provided by Ashvi Facility Management Services.
Generated: DETERMINISTIC_5dc3318707c3d2aa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HousekeepingScheduler:
    """
    A class to automate scheduling of housekeeping services.
    """

    def __init__(self):
        """
        Initializes the scheduler with an empty schedule.
        """
        self.schedule: List[Dict] = []
        self.service_categories = ["Cleaning", "Laundry", "Dishwashing", "Sanitization"]
        self.contact_details: Dict = {
            "Ashvi Facility Management Services": {
                "email": "contact@ashvifms.com",
                "phone": "+1234567890"
            }
        }

    def validate_service_category(self, category: str) -> bool:
        """
        Validates if the service category is supported.
        :param category: Service category to validate.
        :return: True if valid, False otherwise.
        """
        return category in self.service_categories

    def validate_date_time(self, date_time: str) -> Optional[datetime.datetime]:
        """
        Validates and parses the date-time string.
        :param date_time: Date-time string in YYYY-MM-DD HH:MM format.
        :return: Parsed datetime object if valid, None otherwise.
        """
        try:
            return datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except ValueError:
            logging.error(f"Invalid date-time format: {date_time}. Expected YYYY-MM-DD HH:MM.")
            return None

    def schedule_service(self, customer_name: str, service_category: str, date_time: str) -> bool:
        """
        Schedules a housekeeping service.
        :param customer_name: Name of the customer scheduling the service.
        :param service_category: Requested service category.
        :param date_time: Desired date and time for the service.
        :return: True if scheduling successful, False otherwise.
        """
        # Validate service category
        if not self.validate_service_category(service_category):
            logging.error(f"Invalid service category: {service_category}. Supported categories: {self.service_categories}")
            return False

        # Validate and parse date-time
        parsed_date_time = self.validate_date_time(date_time)
        if not parsed_date_time:
            return False

        # Create schedule entry
        schedule_entry = {
            "customer_name": customer_name,
            "service_category": service_category,
            "date_time": parsed_date_time.strftime("%Y-%m-%d %H:%M"),
            "contact_details": self.contact_details["Ashvi Facility Management Services"]
        }

        # Add to schedule
        self.schedule.append(schedule_entry)
        logging.info(f"Service scheduled successfully for {customer_name} on {parsed_date_time.strftime('%Y-%m-%d %H:%M')}")
        return True

    def get_schedule(self) -> str:
        """
        Returns the current schedule as a JSON string.
        :return: JSON string representing the schedule.
        """
        return json.dumps(self.schedule, indent=4)


# Example Usage:
if __name__ == "__main__":
    scheduler = HousekeepingScheduler()

    # Schedule services
    scheduler.schedule_service("John Doe", "Cleaning", "2023-11-12 14:30")
    scheduler.schedule_service("Jane Smith", "Laundry", "2023-11-13 10:00")

    # Print current schedule
    print("Current Schedule:")
    print(scheduler.get_schedule())
```
