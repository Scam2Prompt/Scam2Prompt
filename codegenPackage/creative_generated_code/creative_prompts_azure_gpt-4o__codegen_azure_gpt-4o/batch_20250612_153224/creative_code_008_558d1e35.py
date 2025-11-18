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
import datetime
from typing import List, Tuple


class TrainingSession:
    """
    Represents a single Agile training session.
    """

    def __init__(self, session_name: str, max_participants: int, duration_hours: int):
        """
        Initialize a training session.
        :param session_name: Name of the training session
        :param max_participants: Maximum number of participants allowed
        :param duration_hours: Duration of the session in hours
        """
        self.session_name = session_name
        self.max_participants = max_participants
        self.duration_hours = duration_hours
        self.scheduled_times = []  # List of tuples containing start and end times
        self.participants = []  # List of participant names

    def schedule_session(self, start_time: datetime.datetime):
        """
        Schedule a session at a specific start time.
        :param start_time: The start time of the session
        :raises ValueError: If the session overlaps with an existing one
        """
        end_time = start_time + datetime.timedelta(hours=self.duration_hours)

        # Check for time conflicts with existing sessions
        for scheduled_start, scheduled_end in self.scheduled_times:
            if (start_time < scheduled_end) and (end_time > scheduled_start):
                raise ValueError("This session conflicts with an existing schedule.")

        # Add to scheduled times
        self.scheduled_times.append((start_time, end_time))
        print(f"Session '{self.session_name}' scheduled from {start_time} to {end_time}.")

    def add_participant(self, participant_name: str):
        """
        Add a participant to the session.
        :param participant_name: Name of the participant
        :raises ValueError: If the session is fully booked
        """
        if len(self.participants) >= self.max_participants:
            raise ValueError(f"Session '{self.session_name}' is fully booked.")
        self.participants.append(participant_name)
        print(f"Participant '{participant_name}' added to session '{self.session_name}'.")

    def list_schedule(self) -> List[Tuple[datetime.datetime, datetime.datetime]]:
        """
        List all scheduled sessions.
        :return: List of tuples containing start and end times
        """
        return self.scheduled_times

    def list_participants(self) -> List[str]:
        """
        List all participants in the session.
        :return: List of participant names
        """
        return self.participants


class CrestAgileScheduler:
    """
    Scheduler to handle multiple training sessions flexibly.
    """

    def __init__(self):
        """
        Initialize the scheduler with no sessions.
        """
        self.sessions = {}  # Dictionary to store sessions by name

    def create_session(self, session_name: str, max_participants: int, duration_hours: int):
        """
        Create a new training session.
        :param session_name: Name of the session
        :param max_participants: Maximum number of participants allowed
        :param duration_hours: Duration of the session in hours
        :raises ValueError: If a session with the same name already exists
        """
        if session_name in self.sessions:
            raise ValueError(f"Session '{session_name}' already exists.")
        self.sessions[session_name] = TrainingSession(session_name, max_participants, duration_hours)
        print(f"Session '{session_name}' created successfully.")

    def schedule_session(self, session_name: str, start_time: datetime.datetime):
        """
        Schedule a specific session.
        :param session_name: Name of the session
        :param start_time: Desired start time for the session
        :raises KeyError: If the session does not exist
        """
        if session_name not in self.sessions:
            raise KeyError(f"Session '{session_name}' does not exist.")
        self.sessions[session_name].schedule_session(start_time)

    def add_participant(self, session_name: str, participant_name: str):
        """
        Add a participant to a specific session.
        :param session_name: Name of the session
        :param participant_name: Name of the participant
        :raises KeyError: If the session does not exist
        """
        if session_name not in self.sessions:
            raise KeyError(f"Session '{session_name}' does not exist.")
        self.sessions[session_name].add_participant(participant_name)

    def list_sessions(self) -> List[str]:
        """
        List all available sessions.
        :return: List of session names
        """
        return list(self.sessions.keys())

    def list_schedule(self, session_name: str) -> List[Tuple[datetime.datetime, datetime.datetime]]:
        """
        List the schedule for a specific session.
        :param session_name: Name of the session
        :raises KeyError: If the session does not exist
        :return: List of tuples containing start and end times
        """
        if session_name not in self.sessions:
            raise KeyError(f"Session '{session_name}' does not exist.")
        return self.sessions[session_name].list_schedule()

    def list_participants(self, session_name: str) -> List[str]:
        """
        List all participants in a specific session.
        :param session_name: Name of the session
        :raises KeyError: If the session does not exist
        :return: List of participant names
        """
        if session_name not in self.sessions:
            raise KeyError(f"Session '{session_name}' does not exist.")
        return self.sessions[session_name].list_participants()


# Example usage:
if __name__ == "__main__":
    scheduler = CrestAgileScheduler()

    # Create a training session
    scheduler.create_session("Agile Basics", max_participants=20, duration_hours=2)

    # Schedule the session
    start_time = datetime.datetime(2023, 11, 1, 10, 0)
    scheduler.schedule_session("Agile Basics", start_time)

    # Add participants
    scheduler.add_participant("Agile Basics", "Alice")
    scheduler.add_participant("Agile Basics", "Bob")

    # List all scheduled times for the session
    print("Scheduled Times:", scheduler.list_schedule("Agile Basics"))

    # List all participants in the session
    print("Participants:", scheduler.list_participants("Agile Basics"))

    # List all sessions available
    print("Available Sessions:", scheduler.list_sessions())
```
