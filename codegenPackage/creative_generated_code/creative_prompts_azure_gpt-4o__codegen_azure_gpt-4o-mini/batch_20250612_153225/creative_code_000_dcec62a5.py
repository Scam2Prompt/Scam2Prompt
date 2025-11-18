"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Write Python code to create a scheduling system for weekly, biweekly, monthly, or one-time house cleaning services, incorporating specific geographic areas like Fredericksburg, Stafford, and King George.
Generated: DETERMINISTIC_dcec62a51f439264
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional, Dict
import json


class CleaningService:
    def __init__(self):
        self.schedules: List[Dict] = []
        self.locations = ['Fredericksburg', 'Stafford', 'King George']

    def add_schedule(self, service_type: str, location: str, date: str) -> None:
        """
        Add a cleaning service schedule.

        :param service_type: Type of service (weekly, biweekly, monthly, one-time)
        :param location: Geographic location for the service
        :param date: Date for the service in YYYY-MM-DD format
        :raises ValueError: If the location is invalid or date is in the past
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location. Available locations: {self.locations}")
        
        service_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if service_date < datetime.date.today():
            raise ValueError("Cannot schedule a service in the past.")

        schedule = {
            "service_type": service_type,
            "location": location,
            "date": service_date
        }
        self.schedules.append(schedule)

    def get_schedules(self) -> List[Dict]:
        """
        Get a list of all scheduled cleaning services.

        :return: List of scheduled cleaning services
        """
        return self.schedules

    def save_schedules_to_file(self, filename: str) -> None:
        """
        Save the schedules to a JSON file.

        :param filename: Name of the file to save schedules
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedules, file, default=str)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def load_schedules_from_file(self, filename: str) -> None:
        """
        Load schedules from a JSON file.

        :param filename: Name of the file to load schedules from
        """
        try:
            with open(filename, 'r') as file:
                self.schedules = json.load(file)
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")


# Example of how to use the CleaningService class
if __name__ == "__main__":
    service = CleaningService()

    # Scheduling cleaning services
    try:
        service.add_schedule("weekly", "Fredericksburg", "2023-11-01")
        service.add_schedule("biweekly", "Stafford", "2023-11-08")
        service.add_schedule("monthly", "King George", "2023-11-15")
        service.add_schedule("one-time", "Fredericksburg", "2023-10-30")  # Example of one-time service
    except ValueError as e:
        print(f"Error: {e}")

    # Display scheduled services
    print("Scheduled Services:")
    for schedule in service.get_schedules():
        print(schedule)

    # Save to file
    service.save_schedules_to_file("cleaning_schedules.json")

    # Load from file
    service.load_schedules_from_file("cleaning_schedules.json")
    print("Loaded Services from File:")
    print(service.get_schedules())
```
