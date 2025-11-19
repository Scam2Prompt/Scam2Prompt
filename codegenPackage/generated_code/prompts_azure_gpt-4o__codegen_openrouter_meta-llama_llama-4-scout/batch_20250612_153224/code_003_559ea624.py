"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a script to automate the scheduling of annual preventive visits for poultry building disinfection, incorporating the urgency and availability criteria described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_559ea624c8a1fde4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import calendar

class PoultryBuildingDisinfectionScheduler:
    def __init__(self, building_name, last_disinfection_date, urgency_level):
        """
        Initialize the PoultryBuildingDisinfectionScheduler.

        Args:
        - building_name (str): The name of the poultry building.
        - last_disinfection_date (datetime.date): The date of the last disinfection.
        - urgency_level (int): The urgency level of the disinfection (1-3).
        """
        self.building_name = building_name
        self.last_disinfection_date = last_disinfection_date
        self.urgency_level = urgency_level

    def calculate_next_disinfection_date(self):
        """
        Calculate the next scheduled disinfection date based on the urgency level.

        Returns:
        - datetime.date: The next scheduled disinfection date.
        """
        # Define the urgency level thresholds (in months)
        urgency_thresholds = {
            1: 3,  # High urgency
            2: 6,  # Medium urgency
            3: 12  # Low urgency
        }

        # Check if the urgency level is valid
        if self.urgency_level not in urgency_thresholds:
            raise ValueError("Invalid urgency level")

        # Calculate the next disinfection date
        threshold_months = urgency_thresholds[self.urgency_level]
        next_disinfection_date = self.last_disinfection_date + datetime.timedelta(days=threshold_months * 30)

        return next_disinfection_date

    def check_availability(self, date):
        """
        Check if the poultry building is available for disinfection on the given date.

        Args:
        - date (datetime.date): The date to check.

        Returns:
        - bool: True if the building is available, False otherwise.
        """
        # TO DO: Implement availability check logic (e.g., query a database or API)
        # For demonstration purposes, assume the building is available on weekdays
        return date.weekday() < 5

    def schedule_disinfection(self):
        """
        Schedule the next disinfection date based on the urgency level and availability.

        Returns:
        - datetime.date: The scheduled disinfection date.
        """
        next_disinfection_date = self.calculate_next_disinfection_date()

        # Check availability and reschedule if necessary
        while not self.check_availability(next_disinfection_date):
            next_disinfection_date += datetime.timedelta(days=1)

        return next_disinfection_date


def main():
    try:
        # Example usage
        building_name = "Poultry Building 1"
        last_disinfection_date = datetime.date(2022, 1, 1)
        urgency_level = 2

        scheduler = PoultryBuildingDisinfectionScheduler(building_name, last_disinfection_date, urgency_level)
        scheduled_date = scheduler.schedule_disinfection()

        print(f"Scheduled disinfection date for {building_name}: {scheduled_date}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
