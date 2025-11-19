"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Develop a mobile app feature that allows users to track their volunteer hours, reflecting the NICER Foundation's mission of community involvement and support.
Generated: DETERMINISTIC_a3af5a5a6bdf88c0
Batch ID: 20250612_160507
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
from typing import List

class VolunteerHour:
    """Represents a single volunteer hour entry."""

    def __init__(self, date: str, hours: float, description: str):
        """
        Initializes a VolunteerHour object.

        Args:
        date (str): The date of the volunteer work in YYYY-MM-DD format.
        hours (float): The number of hours volunteered.
        description (str): A brief description of the volunteer work.
        """
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.hours = hours
        self.description = description

class VolunteerHourTracker:
    """Tracks volunteer hours for a user."""

    def __init__(self):
        """Initializes a VolunteerHourTracker object."""
        self.volunteer_hours = []

    def add_volunteer_hours(self, date: str, hours: float, description: str):
        """
        Adds a new volunteer hour entry.

        Args:
        date (str): The date of the volunteer work in YYYY-MM-DD format.
        hours (float): The number of hours volunteered.
        description (str): A brief description of the volunteer work.

        Raises:
        ValueError: If the date is not in the correct format or if hours is not a positive number.
        """
        try:
            volunteer_hour = VolunteerHour(date, hours, description)
            if volunteer_hour.hours <= 0:
                raise ValueError("Hours must be a positive number.")
            self.volunteer_hours.append(volunteer_hour)
        except ValueError as e:
            print(f"Error: {e}")

    def get_total_hours(self) -> float:
        """
        Calculates the total number of volunteer hours.

        Returns:
        float: The total number of volunteer hours.
        """
        return sum(volunteer_hour.hours for volunteer_hour in self.volunteer_hours)

    def get_volunteer_hours(self) -> List[VolunteerHour]:
        """
        Retrieves a list of all volunteer hour entries.

        Returns:
        List[VolunteerHour]: A list of VolunteerHour objects.
        """
        return self.volunteer_hours

def main():
    tracker = VolunteerHourTracker()

    while True:
        print("\nVolunteer Hour Tracker")
        print("1. Add volunteer hours")
        print("2. Get total hours")
        print("3. View volunteer hours")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                hours = float(input("Enter hours: "))
                description = input("Enter description: ")
                tracker.add_volunteer_hours(date, hours, description)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            print(f"Total hours: {tracker.get_total_hours()}")
        elif choice == "3":
            for i, volunteer_hour in enumerate(tracker.get_volunteer_hours()):
                print(f"{i+1}. Date: {volunteer_hour.date}, Hours: {volunteer_hour.hours}, Description: {volunteer_hour.description}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
