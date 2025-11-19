"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Generate code to create a flexible scheduling system for Agile training sessions, reflecting CrestAgile's emphasis on accommodating busy lifestyles.
Generated: DETERMINISTIC_558d1e3535529434
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class Day(Enum):
    """Enum for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class SessionStatus(Enum):
    """Enum for session status"""
    SCHEDULED = 1
    CANCELED = 2
    COMPLETED = 3

class AgileTrainingSession:
    """Class representing an Agile training session"""
    def __init__(self, id, name, start_time, end_time, day):
        """
        Initialize an Agile training session

        Args:
            id (int): Unique session ID
            name (str): Session name
            start_time (datetime): Session start time
            end_time (datetime): Session end time
            day (Day): Day of the week
        """
        self.id = id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.day = day
        self.status = SessionStatus.SCHEDULED

    def __str__(self):
        return f"Session {self.id}: {self.name} on {self.day.name} from {self.start_time} to {self.end_time}"

class SchedulingSystem:
    """Class representing the scheduling system"""
    def __init__(self):
        self.sessions = {}

    def add_session(self, session):
        """
        Add a session to the scheduling system

        Args:
            session (AgileTrainingSession): Session to add
        """
        self.sessions[session.id] = session

    def remove_session(self, session_id):
        """
        Remove a session from the scheduling system

        Args:
            session_id (int): ID of the session to remove

        Raises:
            ValueError: If the session ID does not exist
        """
        if session_id not in self.sessions:
            raise ValueError("Session ID does not exist")
        del self.sessions[session_id]

    def update_session(self, session_id, new_session):
        """
        Update a session in the scheduling system

        Args:
            session_id (int): ID of the session to update
            new_session (AgileTrainingSession): New session details

        Raises:
            ValueError: If the session ID does not exist
        """
        if session_id not in self.sessions:
            raise ValueError("Session ID does not exist")
        self.sessions[session_id] = new_session

    def cancel_session(self, session_id):
        """
        Cancel a session in the scheduling system

        Args:
            session_id (int): ID of the session to cancel

        Raises:
            ValueError: If the session ID does not exist
        """
        if session_id not in self.sessions:
            raise ValueError("Session ID does not exist")
        self.sessions[session_id].status = SessionStatus.CANCELED

    def print_schedule(self):
        """Print the current schedule"""
        for session in self.sessions.values():
            print(session)

def main():
    # Create a scheduling system
    scheduling_system = SchedulingSystem()

    # Create some sessions
    session1 = AgileTrainingSession(1, "Agile Fundamentals", datetime(2024, 9, 17, 9), datetime(2024, 9, 17, 17), Day.MONDAY)
    session2 = AgileTrainingSession(2, "Agile Advanced", datetime(2024, 9, 18, 9), datetime(2024, 9, 18, 17), Day.TUESDAY)

    # Add sessions to the scheduling system
    scheduling_system.add_session(session1)
    scheduling_system.add_session(session2)

    # Print the initial schedule
    print("Initial Schedule:")
    scheduling_system.print_schedule()

    # Cancel a session
    scheduling_system.cancel_session(1)

    # Print the updated schedule
    print("\nUpdated Schedule:")
    scheduling_system.print_schedule()

if __name__ == "__main__":
    main()
```
