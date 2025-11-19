"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Develop a code snippet that organizes training sessions for young leaders, utilizing the concepts introduced in the UngLeder Norway program.
Generated: DETERMINISTIC_6720d48003178f99
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_session_organizer.py

from datetime import datetime, timedelta
from typing import List, Dict

class TrainingSession:
    def __init__(self, title: str, date: datetime, duration: timedelta, location: str, attendees: List[str]):
        """
        Initialize a TrainingSession object.

        Args:
        title (str): The title of the training session.
        date (datetime): The date and time of the training session.
        duration (timedelta): The duration of the training session.
        location (str): The location of the training session.
        attendees (List[str]): A list of attendees for the training session.
        """
        self.title = title
        self.date = date
        self.duration = duration
        self.location = location
        self.attendees = attendees

    def __str__(self):
        return f"{self.title} on {self.date} at {self.location}"


class UngLederNorwayProgram:
    def __init__(self):
        """
        Initialize an UngLederNorwayProgram object.
        """
        self.training_sessions = []

    def add_training_session(self, session: TrainingSession):
        """
        Add a training session to the program.

        Args:
        session (TrainingSession): The training session to add.
        """
        self.training_sessions.append(session)

    def remove_training_session(self, session_title: str):
        """
        Remove a training session from the program.

        Args:
        session_title (str): The title of the training session to remove.

        Raises:
        ValueError: If no training session with the given title exists.
        """
        for session in self.training_sessions:
            if session.title == session_title:
                self.training_sessions.remove(session)
                return
        raise ValueError("No training session with the given title exists")

    def get_training_sessions(self) -> List[TrainingSession]:
        """
        Get a list of all training sessions in the program.

        Returns:
        List[TrainingSession]: A list of all training sessions.
        """
        return self.training_sessions


class TrainingSessionOrganizer:
    def __init__(self, program: UngLederNorwayProgram):
        """
        Initialize a TrainingSessionOrganizer object.

        Args:
        program (UngLederNorwayProgram): The UngLeder Norway program.
        """
        self.program = program

    def organize_sessions(self, sessions: List[Dict]):
        """
        Organize training sessions based on the provided data.

        Args:
        sessions (List[Dict]): A list of dictionaries containing session data.

        Raises:
        ValueError: If invalid session data is provided.
        """
        for session_data in sessions:
            try:
                title = session_data["title"]
                date = datetime.strptime(session_data["date"], "%Y-%m-%d %H:%M")
                duration = timedelta(hours=int(session_data["duration_hours"]), minutes=int(session_data["duration_minutes"]))
                location = session_data["location"]
                attendees = session_data["attendees"]

                session = TrainingSession(title, date, duration, location, attendees)
                self.program.add_training_session(session)
            except KeyError as e:
                raise ValueError("Invalid session data") from e

    def print_session_details(self):
        """
        Print details of all training sessions in the program.
        """
        for session in self.program.get_training_sessions():
            print(f"Title: {session.title}")
            print(f"Date: {session.date}")
            print(f"Duration: {session.duration}")
            print(f"Location: {session.location}")
            print(f"Attendees: {', '.join(session.attendees)}")
            print("------------------------")


def main():
    program = UngLederNorwayProgram()
    organizer = TrainingSessionOrganizer(program)

    sessions = [
        {
            "title": "Leadership Fundamentals",
            "date": "2024-09-20 09:00",
            "duration_hours": 2,
            "duration_minutes": 30,
            "location": "Oslo",
            "attendees": ["John Doe", "Jane Smith"]
        },
        {
            "title": "Communication Skills",
            "date": "2024-09-22 10:00",
            "duration_hours": 1,
            "duration_minutes": 45,
            "location": "Bergen",
            "attendees": ["Jane Smith", "Bob Johnson"]
        }
    ]

    organizer.organize_sessions(sessions)
    organizer.print_session_details()


if __name__ == "__main__":
    main()
```
