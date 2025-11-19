"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Write a code example that showcases how to manage a digital platform for music rehearsal sessions at the Ferme Bermond, as described by the association.
Generated: DETERMINISTIC_08afeef1bfd4dbcd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional


class RehearsalSession:
    """
    Represents a music rehearsal session.
    """
    def __init__(self, session_id: int, date: datetime.date, start_time: datetime.time, end_time: datetime.time, band_name: str):
        self.session_id = session_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.band_name = band_name

    def __str__(self):
        return f"Session {self.session_id}: {self.band_name} on {self.date} from {self.start_time} to {self.end_time}"


class RehearsalManager:
    """
    Manages rehearsal sessions for the Ferme Bermond platform.
    """
    def __init__(self):
        self.sessions: List[RehearsalSession] = []
        self.next_session_id = 1

    def add_session(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, band_name: str) -> RehearsalSession:
        """
        Adds a new rehearsal session.
        """
        # Validate that the end time is after the start time
        if end_time <= start_time:
            raise ValueError("End time must be after start time.")

        # Check for scheduling conflicts
        for session in self.sessions:
            if session.date == date and not (end_time <= session.start_time or start_time >= session.end_time):
                raise ValueError(f"Scheduling conflict with session {session.session_id}.")

        # Create and store the new session
        session = RehearsalSession(self.next_session_id, date, start_time, end_time, band_name)
        self.sessions.append(session)
        self.next_session_id += 1
        return session

    def list_sessions(self, date: Optional[datetime.date] = None) -> List[RehearsalSession]:
        """
        Lists all sessions, optionally filtered by a specific date.
        """
        if date:
            return [session for session in self.sessions if session.date == date]
        return self.sessions

    def cancel_session(self, session_id: int) -> bool:
        """
        Cancels a session by its ID.
        """
        for session in self.sessions:
            if session.session_id == session_id:
                self.sessions.remove(session)
                return True
        return False


# Example usage
if __name__ == "__main__":
    manager = RehearsalManager()

    try:
        # Add some sessions
        session1 = manager.add_session(
            date=datetime.date(2023, 11, 1),
            start_time=datetime.time(14, 0),
            end_time=datetime.time(16, 0),
            band_name="The Jazz Cats"
        )
        print(f"Added: {session1}")

        session2 = manager.add_session(
            date=datetime.date(2023, 11, 1),
            start_time=datetime.time(16, 30),
            end_time=datetime.time(18, 30),
            band_name="Rock Revolution"
        )
        print(f"Added: {session2}")

        # List all sessions
        print("\nAll Sessions:")
        for session in manager.list_sessions():
            print(session)

        # Cancel a session
        if manager.cancel_session(session1.session_id):
            print(f"\nSession {session1.session_id} canceled successfully.")

        # List sessions after cancellation
        print("\nSessions After Cancellation:")
        for session in manager.list_sessions():
            print(session)

    except ValueError as e:
        print(f"Error: {e}")
```
