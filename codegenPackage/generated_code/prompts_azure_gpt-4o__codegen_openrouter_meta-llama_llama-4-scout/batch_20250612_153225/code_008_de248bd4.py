"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Create a program to schedule health education activities and multi-diagnostic camps for rural areas, as described under MIMSR's outreach initiatives.
Generated: DETERMINISTIC_de248bd498679ed9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# health_education_scheduler.py

from datetime import datetime, timedelta
from typing import List, Dict

class HealthEducationActivity:
    def __init__(self, id: int, name: str, date: str, time: str, location: str):
        """
        Initialize a Health Education Activity.

        Args:
        id (int): Unique identifier for the activity.
        name (str): Name of the activity.
        date (str): Date of the activity in YYYY-MM-DD format.
        time (str): Time of the activity in HH:MM format.
        location (str): Location of the activity.
        """
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()
        self.location = location

class MultiDiagnosticCamp:
    def __init__(self, id: int, name: str, date: str, start_time: str, end_time: str, location: str):
        """
        Initialize a Multi-Diagnostic Camp.

        Args:
        id (int): Unique identifier for the camp.
        name (str): Name of the camp.
        date (str): Date of the camp in YYYY-MM-DD format.
        start_time (str): Start time of the camp in HH:MM format.
        end_time (str): End time of the camp in HH:MM format.
        location (str): Location of the camp.
        """
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()
        self.location = location

class HealthEducationScheduler:
    def __init__(self):
        self.activities: List[HealthEducationActivity] = []
        self.camps: List[MultiDiagnosticCamp] = []

    def add_health_education_activity(self, activity: HealthEducationActivity):
        """
        Add a health education activity to the scheduler.

        Args:
        activity (HealthEducationActivity): The activity to add.
        """
        self.activities.append(activity)

    def add_multi_diagnostic_camp(self, camp: MultiDiagnosticCamp):
        """
        Add a multi-diagnostic camp to the scheduler.

        Args:
        camp (MultiDiagnosticCamp): The camp to add.
        """
        self.camps.append(camp)

    def get_all_activities(self) -> List[Dict]:
        """
        Get all health education activities and multi-diagnostic camps.

        Returns:
        List[Dict]: A list of dictionaries containing activity information.
        """
        activities_info = []
        for activity in self.activities:
            activities_info.append({
                "id": activity.id,
                "name": activity.name,
                "date": activity.date,
                "time": activity.time,
                "location": activity.location,
                "type": "Health Education Activity"
            })
        for camp in self.camps:
            activities_info.append({
                "id": camp.id,
                "name": camp.name,
                "date": camp.date,
                "start_time": camp.start_time,
                "end_time": camp.end_time,
                "location": camp.location,
                "type": "Multi-Diagnostic Camp"
            })
        return activities_info

def main():
    try:
        scheduler = HealthEducationScheduler()

        # Create health education activities
        activity1 = HealthEducationActivity(1, "Activity 1", "2024-09-20", "10:00", "Rural Area 1")
        activity2 = HealthEducationActivity(2, "Activity 2", "2024-09-22", "14:00", "Rural Area 2")

        # Create multi-diagnostic camps
        camp1 = MultiDiagnosticCamp(1, "Camp 1", "2024-09-25", "09:00", "17:00", "Rural Area 3")
        camp2 = MultiDiagnosticCamp(2, "Camp 2", "2024-09-28", "10:00", "18:00", "Rural Area 4")

        # Add activities and camps to the scheduler
        scheduler.add_health_education_activity(activity1)
        scheduler.add_health_education_activity(activity2)
        scheduler.add_multi_diagnostic_camp(camp1)
        scheduler.add_multi_diagnostic_camp(camp2)

        # Get and print all activities
        activities = scheduler.get_all_activities()
        for activity in activities:
            print(f"ID: {activity['id']}")
            print(f"Name: {activity['name']}")
            print(f"Date: {activity['date']}")
            if activity['type'] == "Health Education Activity":
                print(f"Time: {activity['time']}")
            else:
                print(f"Start Time: {activity['start_time']}")
                print(f"End Time: {activity['end_time']}")
            print(f"Location: {activity['location']}")
            print(f"Type: {activity['type']}\n")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
