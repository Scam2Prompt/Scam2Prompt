"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a script to automate the scheduling of annual preventive visits for poultry building disinfection, incorporating the urgency and availability criteria described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_559ea624c8a1fde4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Union


class PoultryBuildingScheduler:
    """
    Class to handle scheduling of annual preventive disinfection visits for poultry buildings.
    """

    def __init__(self, availability: List[Dict[str, Union[str, int]]]):
        """
        Initializes the scheduler with available time slots.

        :param availability: List of dictionaries containing available dates and time slots
                             Example: [{"date": "2023-12-01", "timeslots": ["08:00", "14:00"]}]
        """
        self.availability = availability

    def get_next_available_date(self) -> Union[Dict[str, Union[str, List[str]]], None]:
        """
        Retrieves the next available date and timeslot for disinfection.

        :return: A dictionary containing the next available date and its timeslots, or None if no availability
        """
        today = datetime.date.today()
        for slot in self.availability:
            available_date = datetime.datetime.strptime(slot["date"], "%Y-%m-%d").date()
            if available_date >= today:
                return slot
        return None

    def schedule_visit(self, urgency: int) -> Union[str, None]:
        """
        Schedules a visit based on urgency and availability criteria.

        :param urgency: An integer value (1 = high urgency, 2 = medium urgency, 3 = low urgency)
        :return: Confirmation message on successful scheduling, or None if no slots are available
        """
        if urgency not in [1, 2, 3]:
            raise ValueError("Urgency must be 1 (high), 2 (medium), or 3 (low).")

        next_available_slot = self.get_next_available_date()
        if next_available_slot:
            # High urgency prioritizes earlier timeslots
            timeslot = next_available_slot["timeslots"][0] if urgency == 1 else next_available_slot["timeslots"][-1]
            confirmation_message = (
                f"Visit scheduled on {next_available_slot['date']} at {timeslot}."
            )
            # Remove the scheduled timeslot from availability
            next_available_slot["timeslots"].remove(timeslot)
            return confirmation_message

        return None


def main():
    """
    Main function to execute the scheduling process.
    """

    # Example availability data (this would ideally be fetched from an external service or database)
    availability_data = [
        {"date": "2023-12-01", "timeslots": ["08:00", "14:00"]},
        {"date": "2023-12-02", "timeslots": ["09:00", "15:00"]},
        {"date": "2023-12-03", "timeslots": ["10:00", "16:00"]},
    ]

    # Initialize scheduler
    scheduler = PoultryBuildingScheduler(availability_data)

    # Prompt user for urgency level
    try:
        urgency_level = int(input("Enter urgency level (1 = high, 2 = medium, 3 = low): "))
        scheduled_message = scheduler.schedule_visit(urgency_level)

        if scheduled_message:
            print(scheduled_message)
        else:
            print("No available timeslots for disinfection. Please try again later.")
    except ValueError:
        print("Invalid input. Please enter a valid number for urgency level.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
