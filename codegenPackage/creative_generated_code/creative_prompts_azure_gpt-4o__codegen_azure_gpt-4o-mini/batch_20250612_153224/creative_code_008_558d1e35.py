"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Generate code to create a flexible scheduling system for Agile training sessions, reflecting CrestAgile's emphasis on accommodating busy lifestyles.
Generated: DETERMINISTIC_558d1e3535529434
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
import os


class Session:
    """
    Class representing a training session.
    
    Attributes:
        title (str): The title of the session.
        start_time (datetime): The start time of the session.
        duration (timedelta): The duration of the session.
    """
    
    def __init__(self, title: str, start_time: datetime, duration: timedelta):
        self.title = title
        self.start_time = start_time
        self.duration = duration

    def __str__(self):
        end_time = self.start_time + self.duration
        return f"{self.title}: {self.start_time.strftime('%Y-%m-%d %H:%M')} - {end_time.strftime('%H:%M')}"

    def to_dict(self):
        """Convert the Session object to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'start_time': self.start_time.isoformat(),
            'duration': str(self.duration)
        }


class Schedule:
    """
    Class representing a schedule for Agile training sessions.
    
    Attributes:
        sessions (list): A list of scheduled training sessions.
    """
    
    def __init__(self):
        self.sessions = []

    def add_session(self, session: Session):
        """Add a new session to the schedule."""
        if any(s.start_time < session.start_time + session.duration and session.start_time < s.start_time + s.duration for s in self.sessions):
            raise ValueError("Session times overlap with an existing session.")
        self.sessions.append(session)

    def remove_session(self, session_title: str):
        """Remove a session by its title."""
        self.sessions = [s for s in self.sessions if s.title != session_title]

    def get_schedule(self):
        """Return the scheduled sessions."""
        return self.sessions

    def save_schedule(self, filename: str):
        """Save the schedule to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([s.to_dict() for s in self.sessions], f, indent=4)
        except IOError as e:
            print(f"Error saving schedule: {e}")

    def load_schedule(self, filename: str):
        """Load the schedule from a JSON file."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    sessions_data = json.load(f)
                    self.sessions = [Session(data['title'], datetime.fromisoformat(data['start_time']), 
                                             timedelta(hours=int(data['duration'].split(':')[0]), 
                                                       minutes=int(data['duration'].split(':')[1]))) 
                                     for data in sessions_data]
            else:
                print("Schedule file does not exist.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule: {e}")


# Example usage
if __name__ == "__main__":
    schedule = Schedule()

    try:
        # Adding sessions
        session1 = Session("Agile Fundamentals", datetime(2023, 10, 30, 10, 0), timedelta(hours=2))
        schedule.add_session(session1)

        session2 = Session("Scrum Deep Dive", datetime(2023, 10, 30, 13, 0), timedelta(hours=3))
        schedule.add_session(session2)

        # Displaying the schedule
        for session in schedule.get_schedule():
            print(session)

        # Saving the schedule
        schedule.save_schedule("agile_schedule.json")

        # Loading the schedule
        new_schedule = Schedule()
        new_schedule.load_schedule("agile_schedule.json")
        print("\nLoaded Schedule:")
        for session in new_schedule.get_schedule():
            print(session)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
