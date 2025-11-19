"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Write a program to manage ICT training sessions in diverse fields, referencing MIEC's IT training offerings. Include scheduling and participant tracking features.
Generated: DETERMINISTIC_1142e87b534a06e3
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ICT Training Session Management System

This program manages ICT training sessions across diverse fields, inspired by MIEC's IT training offerings.
It includes features for scheduling sessions and tracking participants.

Key Features:
- Session scheduling with date, time, and field
- Participant registration and tracking
- Session capacity management
- Reporting capabilities
"""

import datetime
import json
import os
from typing import Dict, List, Optional, Tuple


class TrainingSession:
    """Represents a single training session with scheduling and participant information."""

    def __init__(
        self,
        session_id: str,
        title: str,
        field: str,
        date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
        max_participants: int,
        instructor: str,
        location: str,
    ):
        """Initialize a training session."""
        self.session_id = session_id
        self.title = title
        self.field = field
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.max_participants = max_participants
        self.instructor = instructor
        self.location = location
        self.participants: List[Dict[str, str]] = []

    def add_participant(self, participant_id: str, name: str, email: str) -> bool:
        """Add a participant to the session if capacity allows."""
        if len(self.participants) >= self.max_participants:
            return False

        self.participants.append(
            {"participant_id": participant_id, "name": name, "email": email}
        )
        return True

    def remove_participant(self, participant_id: str) -> bool:
        """Remove a participant from the session."""
        for i, participant in enumerate(self.participants):
            if participant["participant_id"] == participant_id:
                self.participants.pop(i)
                return True
        return False

    def get_participant_count(self) -> int:
        """Return the current number of participants."""
        return len(self.participants)

    def to_dict(self) -> Dict:
        """Convert session data to dictionary for serialization."""
        return {
            "session_id": self.session_id,
            "title": self.title,
            "field": self.field,
            "date": self.date.isoformat(),
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "max_participants": self.max_participants,
            "instructor": self.instructor,
            "location": self.location,
            "participants": self.participants,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "TrainingSession":
        """Create a TrainingSession from dictionary data."""
        session = cls(
            session_id=data["session_id"],
            title=data["title"],
            field=data["field"],
            date=datetime.date.fromisoformat(data["date"]),
            start_time=datetime.time.fromisoformat(data["start_time"]),
            end_time=datetime.time.fromisoformat(data["end_time"]),
            max_participants=data["max_participants"],
            instructor=data["instructor"],
            location=data["location"],
        )
        session.participants = data["participants"]
        return session


class TrainingManager:
    """Manages all training sessions and provides operations for the system."""

    def __init__(self, data_file: str = "training_data.json"):
        """Initialize the training manager with data storage file."""
        self.data_file = data_file
        self.sessions: Dict[str, TrainingSession] = {}
        self.load_data()

    def add_session(self, session: TrainingSession) -> bool:
        """Add a new training session."""
        if session.session_id in self.sessions:
            return False
        self.sessions[session.session_id] = session
        self.save_data()
        return True

    def remove_session(self, session_id: str) -> bool:
        """Remove a training session."""
        if session_id not in self.sessions:
            return False
        del self.sessions[session_id]
        self.save_data()
        return True

    def get_session(self, session_id: str) -> Optional[TrainingSession]:
        """Retrieve a session by ID."""
        return self.sessions.get(session_id)

    def get_sessions_by_field(self, field: str) -> List[TrainingSession]:
        """Retrieve all sessions in a specific field."""
        return [
            session for session in self.sessions.values() if session.field.lower() == field.lower()
        ]

    def get_upcoming_sessions(self, days: int = 30) -> List[TrainingSession]:
        """Retrieve sessions scheduled within the next specified days."""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days)
        return [
            session
            for session in self.sessions.values()
            if today <= session.date <= end_date
        ]

    def register_participant(
        self, session_id: str, participant_id: str, name: str, email: str
    ) -> Tuple[bool, str]:
        """Register a participant for a session."""
        session = self.get_session(session_id)
        if not session:
            return False, "Session not found"

        if session.add_participant(participant_id, name, email):
            self.save_data()
            return True, "Registration successful"
        return False, "Session is full"

    def cancel_registration(self, session_id: str, participant_id: str) -> bool:
        """Cancel a participant's registration."""
        session = self.get_session(session_id)
        if not session:
            return False

        if session.remove_participant(participant_id):
            self.save_data()
            return True
        return False

    def load_data(self) -> None:
        """Load session data from file."""
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.sessions = {
                    session_id: TrainingSession.from_dict(session_data)
                    for session_id, session_data in data.items()
                }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")

    def save_data(self) -> None:
        """Save session data to file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(
                    {session_id: session.to_dict() for session_id, session in self.sessions.items()},
                    f,
                    indent=2,
                )
        except IOError as e:
            print(f"Error saving data: {e}")


class TrainingSystemUI:
    """Provides a command-line interface for the training management system."""

    def __init__(self):
        """Initialize the UI with a training manager instance."""
        self.manager = TrainingManager()

    def display_menu(self) -> None:
        """Display the main menu."""
        print("\nICT Training Management System")
        print("1. Schedule a new training session")
        print("2. View all sessions")
        print("3. View sessions by field")
        print("4. View upcoming sessions")
        print("5. Register a participant")
        print("6. Cancel a registration")
        print("7. Remove a session")
        print("8. Exit")

    def run(self) -> None:
        """Run the main program loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")

            try:
                if choice == "1":
                    self.schedule_session()
                elif choice == "2":
                    self.view_all_sessions()
                elif choice == "3":
                    self.view_sessions_by_field()
                elif choice == "4":
                    self.view_upcoming_sessions()
                elif choice == "5":
                    self.register_participant()
                elif choice == "6":
                    self.cancel_registration()
                elif choice == "7":
                    self.remove_session()
                elif choice == "8":
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def schedule_session(self) -> None:
        """Handle scheduling a new training session."""
        print("\nSchedule a New Training Session")
        session_id = input("Enter session ID: ")
        title = input("Enter session title: ")
        field = input("Enter field (e.g., Programming, Networking, Cybersecurity): ")
        
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.date.fromisoformat(date_str)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        start_time_str = input("Enter start time (HH:MM): ")
        end_time_str = input("Enter end time (HH:MM): ")
        try:
            start_time = datetime.time.fromisoformat(start_time_str)
            end_time = datetime.time.fromisoformat(end_time_str)
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
            return
