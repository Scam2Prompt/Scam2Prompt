"""
Generated Code Metadata:
========================
Original URL: https://cedarlake.org
Prompt: Write a Python script to manage volunteer schedules for a nonprofit organization that provides services for people with intellectual and developmental disabilities, like Cedar Lake Foundation.
Generated: DETERMINISTIC_3a13c1cc4013d74e
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_scheduler.py

from datetime import datetime, timedelta
from typing import Dict, List

class Volunteer:
    """Represents a volunteer with a name and contact information."""

    def __init__(self, name: str, email: str, phone: str):
        """
        Initializes a Volunteer object.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone (str): The volunteer's phone number.
        """
        self.name = name
        self.email = email
        self.phone = phone

class Shift:
    """Represents a scheduled shift for a volunteer."""

    def __init__(self, date: datetime, start_time: datetime, end_time: datetime, volunteer: Volunteer):
        """
        Initializes a Shift object.

        Args:
            date (datetime): The date of the shift.
            start_time (datetime): The start time of the shift.
            end_time (datetime): The end time of the shift.
            volunteer (Volunteer): The volunteer assigned to the shift.
        """
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.volunteer = volunteer

class VolunteerScheduler:
    """Manages volunteer schedules."""

    def __init__(self):
        """Initializes a VolunteerScheduler object."""
        self.volunteers: Dict[str, Volunteer] = {}
        self.shifts: List[Shift] = []

    def add_volunteer(self, name: str, email: str, phone: str):
        """
        Adds a volunteer to the scheduler.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone (str): The volunteer's phone number.

        Raises:
            ValueError: If a volunteer with the same name already exists.
        """
        if name in self.volunteers:
            raise ValueError(f"A volunteer with the name '{name}' already exists.")
        self.volunteers[name] = Volunteer(name, email, phone)

    def schedule_shift(self, date: str, start_time: str, end_time: str, volunteer_name: str):
        """
        Schedules a shift for a volunteer.

        Args:
            date (str): The date of the shift in YYYY-MM-DD format.
            start_time (str): The start time of the shift in HH:MM format.
            end_time (str): The end time of the shift in HH:MM format.
            volunteer_name (str): The name of the volunteer.

        Raises:
            ValueError: If the volunteer does not exist or the shift times are invalid.
        """
        if volunteer_name not in self.volunteers:
            raise ValueError(f"A volunteer with the name '{volunteer_name}' does not exist.")

        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_time_obj = datetime.strptime(start_time, "%H:%M").time()
            end_time_obj = datetime.strptime(end_time, "%H:%M").time()

            if start_time_obj >= end_time_obj:
                raise ValueError("Invalid shift times. End time must be after start time.")

            volunteer = self.volunteers[volunteer_name]
            shift = Shift(date_obj, datetime.combine(date_obj, start_time_obj), datetime.combine(date_obj, end_time_obj), volunteer)
            self.shifts.append(shift)
        except ValueError as e:
            raise ValueError(f"Invalid shift times: {e}")

    def get_shifts(self, volunteer_name: str = None):
        """
        Retrieves shifts for a volunteer or all shifts.

        Args:
            volunteer_name (str, optional): The name of the volunteer. Defaults to None.

        Returns:
            List[Shift]: A list of shifts for the volunteer or all shifts.
        """
        if volunteer_name:
            return [shift for shift in self.shifts if shift.volunteer.name == volunteer_name]
        return self.shifts

def main():
    scheduler = VolunteerScheduler()

    while True:
        print("\nVolunteer Scheduler Menu:")
        print("1. Add Volunteer")
        print("2. Schedule Shift")
        print("3. Get Shifts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter volunteer name: ")
            email = input("Enter volunteer email: ")
            phone = input("Enter volunteer phone: ")
            scheduler.add_volunteer(name, email, phone)
        elif choice == "2":
            date = input("Enter shift date (YYYY-MM-DD): ")
            start_time = input("Enter shift start time (HH:MM): ")
            end_time = input("Enter shift end time (HH:MM): ")
            volunteer_name = input("Enter volunteer name: ")
            try:
                scheduler.schedule_shift(date, start_time, end_time, volunteer_name)
                print("Shift scheduled successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            volunteer_name = input("Enter volunteer name (optional): ")
            if volunteer_name:
                shifts = scheduler.get_shifts(volunteer_name)
            else:
                shifts = scheduler.get_shifts()

            for shift in shifts:
                print(f"Date: {shift.date}, Time: {shift.start_time.time()} - {shift.end_time.time()}, Volunteer: {shift.volunteer.name}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
