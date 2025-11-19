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
"""
Worship Service Schedule and Management System Library
Inspired by the ministries offered at Word of Life Northwest.

This library provides functionality to create, manage, and retrieve worship service schedules,
including ministries, volunteers, and service details.

Author: Expert Programmer
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional


class WorshipServiceSchedule:
    """
    A class to manage worship service schedules and related data.
    """

    def __init__(self):
        """
        Initializes the WorshipServiceSchedule instance with empty schedules and ministries.
        """
        self.schedules: List[Dict] = []  # List to store service schedules
        self.ministries: Dict[str, List[str]] = {}  # Dictionary to store ministries and volunteers

    def add_ministry(self, ministry_name: str, volunteers: Optional[List[str]] = None) -> None:
        """
        Adds a new ministry with optional volunteers.

        :param ministry_name: Name of the ministry.
        :param volunteers: List of volunteers for the ministry (default is an empty list).
        """
        if ministry_name in self.ministries:
            raise ValueError(f"Ministry '{ministry_name}' already exists.")
        self.ministries[ministry_name] = volunteers or []

    def add_volunteer_to_ministry(self, ministry_name: str, volunteer_name: str) -> None:
        """
        Adds a volunteer to an existing ministry.

        :param ministry_name: Name of the ministry.
        :param volunteer_name: Name of the volunteer.
        """
        if ministry_name not in self.ministries:
            raise ValueError(f"Ministry '{ministry_name}' does not exist.")
        if volunteer_name in self.ministries[ministry_name]:
            raise ValueError(f"Volunteer '{volunteer_name}' is already part of ministry '{ministry_name}'.")
        self.ministries[ministry_name].append(volunteer_name)

    def create_schedule(self, service_date: str, service_time: str, ministries_involved: List[str]) -> None:
        """
        Creates a new worship service schedule.

        :param service_date: Date of the service (format: YYYY-MM-DD).
        :param service_time: Time of the service (format: HH:MM).
        :param ministries_involved: List of ministries involved in the service.
        """
        try:
            # Validate date and time format
            service_datetime = datetime.strptime(f"{service_date} {service_time}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time.")

        # Validate ministries
        for ministry in ministries_involved:
            if ministry not in self.ministries:
                raise ValueError(f"Ministry '{ministry}' does not exist.")

        # Add schedule
        schedule = {
            "service_datetime": service_datetime,
            "ministries_involved": ministries_involved,
        }
        self.schedules.append(schedule)

    def get_upcoming_services(self) -> List[Dict]:
        """
        Retrieves a list of upcoming services.

        :return: List of dictionaries containing upcoming service details.
        """
        now = datetime.now()
        return [schedule for schedule in self.schedules if schedule["service_datetime"] > now]

    def get_ministry_volunteers(self, ministry_name: str) -> List[str]:
        """
        Retrieves the list of volunteers for a specific ministry.

        :param ministry_name: Name of the ministry.
        :return: List of volunteers for the ministry.
        """
        if ministry_name not in self.ministries:
            raise ValueError(f"Ministry '{ministry_name}' does not exist.")
        return self.ministries[ministry_name]

    def remove_schedule(self, service_date: str, service_time: str) -> None:
        """
        Removes a worship service schedule.

        :param service_date: Date of the service (format: YYYY-MM-DD).
        :param service_time: Time of the service (format: HH:MM).
        """
        try:
            service_datetime = datetime.strptime(f"{service_date} {service_time}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time.")

        for schedule in self.schedules:
            if schedule["service_datetime"] == service_datetime:
                self.schedules.remove(schedule)
                return

        raise ValueError("No matching schedule found to remove.")

    def list_all_schedules(self) -> List[Dict]:
        """
        Lists all worship service schedules.

        :return: List of dictionaries containing all service schedules.
        """
        return self.schedules


# Example usage (commented out for production-ready code):
# schedule_manager = WorshipServiceSchedule()
# schedule_manager.add_ministry("Music Ministry", ["Alice", "Bob"])
# schedule_manager.add_ministry("Usher Ministry", ["Charlie", "David"])
# schedule_manager.create_schedule("2023-10-15", "10:00", ["Music Ministry", "Usher Ministry"])
# print(schedule_manager.get_upcoming_services())
# print(schedule_manager.get_ministry_volunteers("Music Ministry"))
```
