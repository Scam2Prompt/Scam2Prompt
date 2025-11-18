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
from typing import List, Dict, Optional

class PoultryDisinfectionScheduler:
    """
    A class to automate the scheduling of annual preventive visits for poultry building disinfection.
    """

    def __init__(self):
        # Initialize an empty list to store scheduled visits
        self.scheduled_visits: List[Dict[str, Optional[datetime.date]]] = []

    def schedule_visit(self, date: datetime.date, urgency: str, available_dates: List[datetime.date]) -> None:
        """
        Schedule a disinfection visit based on urgency and availability.

        :param date: The preferred date for the disinfection visit.
        :param urgency: The urgency level for the visit (e.g., 'high', 'medium', 'low').
        :param available_dates: A list of dates that are available for scheduling.
        """
        # Check if the preferred date is available
        if date not in available_dates:
            raise ValueError(f"Preferred date {date} is not available for scheduling.")

        # Schedule the visit based on urgency
        visit = {
            'date': date,
            'urgency': urgency,
            'scheduled_on': datetime.date.today()
        }

        self.scheduled_visits.append(visit)

    def get_scheduled_visits(self) -> List[Dict[str, Optional[datetime.date]]]:
        """
        Retrieve the list of scheduled visits.

        :return: List of scheduled visits.
        """
        return self.scheduled_visits

    def display_scheduled_visits(self) -> None:
        """
        Display all scheduled visits in a readable format.
        """
        if not self.scheduled_visits:
            print("No scheduled visits yet.")
            return
        
        print("Scheduled Disinfection Visits:")
        for visit in self.scheduled_visits:
            print(f"Date: {visit['date']}, Urgency: {visit['urgency']}, "
                  f"Scheduled On: {visit['scheduled_on']}")

def main():
    """
    Main function to demonstrate the disinfection visit scheduling.
    """
    # Create an instance of the scheduler
    scheduler = PoultryDisinfectionScheduler()

    # Define available dates for scheduling
    available_dates = [
        datetime.date(2024, 1, 15),
        datetime.date(2024, 2, 10),
        datetime.date(2024, 3, 21)
    ]

    try:
        # Schedule a visit with high urgency
        scheduler.schedule_visit(datetime.date(2024, 1, 15), 'high', available_dates)

        # Schedule a visit with medium urgency
        scheduler.schedule_visit(datetime.date(2024, 2, 10), 'medium', available_dates)

        # Attempt to schedule a visit on a non-available date (error handling demonstration)
        scheduler.schedule_visit(datetime.date(2024, 4, 1), 'low', available_dates)

    except ValueError as e:
        print(f"Error scheduling visit: {e}")

    # Display the scheduled visits
    scheduler.display_scheduled_visits()

if __name__ == "__main__":
    main()
```
