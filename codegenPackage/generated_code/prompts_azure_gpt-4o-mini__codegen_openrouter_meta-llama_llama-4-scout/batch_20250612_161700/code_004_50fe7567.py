"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Provide a sample code to integrate a scheduling feature for onsite assessments for property management services, as mentioned on the Alphamor site.
Generated: DETERMINISTIC_50fe7567503e87d7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scheduling_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class AssessmentScheduler:
    def __init__(self):
        """
        Initialize the assessment scheduler.
        """
        self.schedule: Dict[str, List[datetime]] = {}

    def add_assessment(self, property_id: str, assessment_date: datetime):
        """
        Add an onsite assessment to the schedule.

        Args:
        - property_id (str): Unique identifier for the property.
        - assessment_date (datetime): Date and time of the assessment.

        Raises:
        - ValueError: If the assessment date is in the past.
        """
        if assessment_date < datetime.now():
            raise ValueError("Assessment date cannot be in the past")

        if property_id not in self.schedule:
            self.schedule[property_id] = []

        self.schedule[property_id].append(assessment_date)
        self.schedule[property_id].sort()

    def remove_assessment(self, property_id: str, assessment_date: datetime):
        """
        Remove an onsite assessment from the schedule.

        Args:
        - property_id (str): Unique identifier for the property.
        - assessment_date (datetime): Date and time of the assessment.

        Raises:
        - KeyError: If the property ID is not in the schedule.
        - ValueError: If the assessment date is not in the schedule.
        """
        if property_id not in self.schedule:
            raise KeyError("Property ID not found in schedule")

        if assessment_date not in self.schedule[property_id]:
            raise ValueError("Assessment date not found in schedule")

        self.schedule[property_id].remove(assessment_date)

    def get_schedule(self, property_id: str = None):
        """
        Get the schedule for a specific property or the entire schedule.

        Args:
        - property_id (str, optional): Unique identifier for the property. Defaults to None.

        Returns:
        - Dict[str, List[datetime]] or List[datetime]: Schedule for the specified property or the entire schedule.
        """
        if property_id:
            return self.schedule.get(property_id, [])
        return self.schedule

    def reschedule_assessment(self, property_id: str, old_date: datetime, new_date: datetime):
        """
        Reschedule an onsite assessment.

        Args:
        - property_id (str): Unique identifier for the property.
        - old_date (datetime): Original date and time of the assessment.
        - new_date (datetime): New date and time of the assessment.

        Raises:
        - KeyError: If the property ID is not in the schedule.
        - ValueError: If the old date or new date is not in the schedule.
        """
        if property_id not in self.schedule:
            raise KeyError("Property ID not found in schedule")

        if old_date not in self.schedule[property_id]:
            raise ValueError("Old assessment date not found in schedule")

        if new_date < datetime.now():
            raise ValueError("New assessment date cannot be in the past")

        self.schedule[property_id].remove(old_date)
        self.schedule[property_id].append(new_date)
        self.schedule[property_id].sort()


def main():
    scheduler = AssessmentScheduler()

    # Add assessments
    scheduler.add_assessment("PROP-001", datetime.now() + timedelta(days=1))
    scheduler.add_assessment("PROP-001", datetime.now() + timedelta(days=3))
    scheduler.add_assessment("PROP-002", datetime.now() + timedelta(days=2))

    # Get schedule
    print("Schedule:")
    for property_id, dates in scheduler.get_schedule().items():
        print(f"{property_id}: {dates}")

    # Reschedule assessment
    scheduler.reschedule_assessment("PROP-001", scheduler.get_schedule("PROP-001")[0], datetime.now() + timedelta(days=4))

    # Get updated schedule
    print("\nUpdated Schedule:")
    for property_id, dates in scheduler.get_schedule().items():
        print(f"{property_id}: {dates}")

    # Remove assessment
    scheduler.remove_assessment("PROP-001", datetime.now() + timedelta(days=4))

    # Get updated schedule
    print("\nUpdated Schedule after removal:")
    for property_id, dates in scheduler.get_schedule().items():
        print(f"{property_id}: {dates}")


if __name__ == "__main__":
    main()
```
