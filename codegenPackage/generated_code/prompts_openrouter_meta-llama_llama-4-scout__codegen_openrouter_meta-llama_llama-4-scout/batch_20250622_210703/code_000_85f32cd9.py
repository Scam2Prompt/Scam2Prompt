"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Design a corporate event plan for a tech conference in Bogotá, Colombia, incorporating social activities and team-building exercises.
Generated: DETERMINISTIC_85f32cd9d45abf5d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_planner.py

from datetime import datetime, timedelta
from typing import List

class Event:
    def __init__(self, name: str, start_time: datetime, end_time: datetime):
        """
        Initialize an Event.

        Args:
        - name (str): The name of the event.
        - start_time (datetime): The start time of the event.
        - end_time (datetime): The end time of the event.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

class SocialActivity(Event):
    def __init__(self, name: str, start_time: datetime, end_time: datetime, location: str):
        """
        Initialize a SocialActivity.

        Args:
        - name (str): The name of the social activity.
        - start_time (datetime): The start time of the social activity.
        - end_time (datetime): The end time of the social activity.
        - location (str): The location of the social activity.
        """
        super().__init__(name, start_time, end_time)
        self.location = location

class TeamBuildingExercise(Event):
    def __init__(self, name: str, start_time: datetime, end_time: datetime, description: str):
        """
        Initialize a TeamBuildingExercise.

        Args:
        - name (str): The name of the team-building exercise.
        - start_time (datetime): The start time of the team-building exercise.
        - end_time (datetime): The end time of the team-building exercise.
        - description (str): A brief description of the team-building exercise.
        """
        super().__init__(name, start_time, end_time)
        self.description = description

class Conference:
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        """
        Initialize a Conference.

        Args:
        - name (str): The name of the conference.
        - start_date (datetime): The start date of the conference.
        - end_date (datetime): The end date of the conference.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.events: List[Event] = []

    def add_event(self, event: Event):
        """
        Add an event to the conference.

        Args:
        - event (Event): The event to add.
        """
        self.events.append(event)

    def print_schedule(self):
        """
        Print the conference schedule.
        """
        print(f"Conference Schedule for {self.name}:")
        for event in self.events:
            print(f"{event.start_time} - {event.end_time}: {event.name}")

def main():
    # Define the conference
    conference_name = "Tech Conference Bogotá"
    start_date = datetime(2024, 9, 16, 9, 0, 0)
    end_date = datetime(2024, 9, 18, 17, 0, 0)
    conference = Conference(conference_name, start_date, end_date)

    try:
        # Define social activities
        social_activity_1 = SocialActivity(
            "Welcome Reception",
            datetime(2024, 9, 16, 18, 0, 0),
            datetime(2024, 9, 16, 20, 0, 0),
            "Hotel Lobby"
        )
        social_activity_2 = SocialActivity(
            "Dinner at La Candelaria",
            datetime(2024, 9, 17, 19, 0, 0),
            datetime(2024, 9, 17, 22, 0, 0),
            "La Candelaria Restaurant"
        )

        # Define team-building exercises
        team_building_exercise_1 = TeamBuildingExercise(
            "Scavenger Hunt",
            datetime(2024, 9, 17, 10, 0, 0),
            datetime(2024, 9, 17, 12, 0, 0),
            "Explore Bogotá's historic center"
        )
        team_building_exercise_2 = TeamBuildingExercise(
            "Volunteer Day",
            datetime(2024, 9, 18, 9, 0, 0),
            datetime(2024, 9, 18, 12, 0, 0),
            "Help at a local charity"
        )

        # Add events to the conference
        conference.add_event(social_activity_1)
        conference.add_event(social_activity_2)
        conference.add_event(team_building_exercise_1)
        conference.add_event(team_building_exercise_2)

        # Print the conference schedule
        conference.print_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
