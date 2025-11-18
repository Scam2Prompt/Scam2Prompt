"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Generate code to schedule and register field visits for agronomic activities, including timeline tracking and reporting, as outlined in Azagros' platform.
Generated: DETERMINISTIC_c415ecf7dfd06a8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class FieldVisit:
    """
    Class representing a field visit for agronomic activities.
    """

    def __init__(self, visit_id, farmer_name, activity, visit_date, duration, notes):
        """
        Initialize a FieldVisit instance.

        :param visit_id: Unique identifier for the visit
        :param farmer_name: Name of the farmer
        :param activity: Type of agronomic activity
        :param visit_date: Scheduled date for the visit
        :param duration: Duration of the visit in hours
        :param notes: Additional notes regarding the visit
        """
        self.visit_id = visit_id
        self.farmer_name = farmer_name
        self.activity = activity
        self.visit_date = visit_date
        self.duration = duration
        self.notes = notes

    def to_dict(self):
        """
        Convert the FieldVisit instance into a dictionary.

        :return: Dictionary representation of the FieldVisit
        """
        return {
            "visit_id": self.visit_id,
            "farmer_name": self.farmer_name,
            "activity": self.activity,
            "visit_date": self.visit_date.isoformat(),
            "duration": self.duration,
            "notes": self.notes
        }

class FieldVisitScheduler:
    """
    Class responsible for scheduling and managing field visits.
    """

    def __init__(self):
        """
        Initializes an empty list to hold scheduled field visits.
        """
        self.visits = []

    def schedule_visit(self, visit):
        """
        Schedule a new field visit.

        :param visit: FieldVisit object to be scheduled
        :raises ValueError: If the visit date is in the past
        """
        if visit.visit_date < datetime.now():
            raise ValueError("Cannot schedule a visit in the past.")

        self.visits.append(visit)

    def get_scheduled_visits(self):
        """
        Retrieve all scheduled visits.

        :return: List of scheduled FieldVisit objects
        """
        return self.visits

    def generate_report(self):
        """
        Generate a report of scheduled visits.

        :return: JSON formatted string of scheduled visits
        """
        report_data = [visit.to_dict() for visit in self.visits]
        return json.dumps(report_data, indent=2)

def main():
    """
    Main function to demonstrate scheduling field visits.
    """
    scheduler = FieldVisitScheduler()

    # Schedule example visits
    try:
        visit1 = FieldVisit(
            visit_id=1,
            farmer_name="John Doe",
            activity="Soil Testing",
            visit_date=datetime.now() + timedelta(days=5),  # Scheduled in the future
            duration=2,
            notes="Collect samples from the north field."
        )
        scheduler.schedule_visit(visit1)

        visit2 = FieldVisit(
            visit_id=2,
            farmer_name="Jane Smith",
            activity="Fertilizer Application",
            visit_date=datetime.now() + timedelta(days=10),  # Scheduled in the future
            duration=3,
            notes="Apply nitrogen fertilizer."
        )
        scheduler.schedule_visit(visit2)

        # Attempt to schedule a visit in the past
        visit3 = FieldVisit(
            visit_id=3,
            farmer_name="Old Farmer",
            activity="Weed Control",
            visit_date=datetime.now() - timedelta(days=1),  # Scheduled in the past
            duration=1,
            notes="Check for invasive species."
        )
        scheduler.schedule_visit(visit3)  # This will raise an error

    except ValueError as e:
        print(f"Error scheduling visit: {e}")

    # Print all scheduled visits
    print("Scheduled Visits:")
    print(scheduler.generate_report())

if __name__ == "__main__":
    main()
```
