"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Develop a library recommendation for creating a worship service schedule and management system inspired by the ministries offered at Word of Life Northwest.
Generated: DETERMINISTIC_9f64a01eaa132d27
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict

class Service:
    def __init__(self, name: str, start_time: datetime, end_time: datetime):
        """
        Initialize a Service.

        Args:
        - name (str): The name of the service.
        - start_time (datetime): The start time of the service.
        - end_time (datetime): The end time of the service.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name}: {self.start_time} - {self.end_time}"


class Ministry:
    def __init__(self, name: str):
        """
        Initialize a Ministry.

        Args:
        - name (str): The name of the ministry.
        """
        self.name = name
        self.services: List[Service] = []

    def add_service(self, service: Service):
        """
        Add a service to the ministry.

        Args:
        - service (Service): The service to add.
        """
        self.services.append(service)

    def __str__(self):
        ministry_info = f"Ministry: {self.name}\n"
        services_info = "\n".join([str(service) for service in self.services])
        return ministry_info + services_info


class WorshipServiceSchedule:
    def __init__(self):
        """
        Initialize a Worship Service Schedule.
        """
        self.ministries: Dict[str, Ministry] = {}

    def add_ministry(self, ministry: Ministry):
        """
        Add a ministry to the schedule.

        Args:
        - ministry (Ministry): The ministry to add.
        """
        self.ministries[ministry.name] = ministry

    def get_ministry(self, name: str) -> Ministry:
        """
        Get a ministry by name.

        Args:
        - name (str): The name of the ministry.

        Returns:
        - Ministry: The ministry with the given name, or None if not found.
        """
        return self.ministries.get(name)

    def __str__(self):
        schedule_info = "Worship Service Schedule:\n"
        ministries_info = "\n\n".join([str(ministry) for ministry in self.ministries.values()])
        return schedule_info + ministries_info


def main():
    try:
        # Create a worship service schedule
        schedule = WorshipServiceSchedule()

        # Create ministries
        sunday_service = Ministry("Sunday Service")
        prayer_meeting = Ministry("Prayer Meeting")

        # Create services
        sunday_service_am = Service("Sunday Service AM", datetime(2024, 9, 16, 9, 0), datetime(2024, 9, 16, 10, 30))
        sunday_service_pm = Service("Sunday Service PM", datetime(2024, 9, 16, 11, 0), datetime(2024, 9, 16, 12, 30))
        prayer_meeting_service = Service("Prayer Meeting", datetime(2024, 9, 17, 19, 0), datetime(2024, 9, 17, 20, 30))

        # Add services to ministries
        sunday_service.add_service(sunday_service_am)
        sunday_service.add_service(sunday_service_pm)
        prayer_meeting.add_service(prayer_meeting_service)

        # Add ministries to schedule
        schedule.add_ministry(sunday_service)
        schedule.add_ministry(prayer_meeting)

        # Print schedule
        print(schedule)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
