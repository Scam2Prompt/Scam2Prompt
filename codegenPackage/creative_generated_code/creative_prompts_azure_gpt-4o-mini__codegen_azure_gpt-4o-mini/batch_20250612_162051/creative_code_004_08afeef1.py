"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write a code example that showcases how to manage a digital platform for music rehearsal sessions at the Ferme Bermond, as described by the association.
Generated: DETERMINISTIC_08afeef1bfd4dbcd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# music_rehearsal_manager.py

from datetime import datetime, timedelta
from typing import List, Optional

class RehearsalSession:
    """Class representing a music rehearsal session."""
    
    def __init__(self, date: datetime, duration: int, room: str):
        """
        Initializes a rehearsal session.
        
        Args:
            date (datetime): The date and time of the rehearsal.
            duration (int): Duration in minutes.
            room (str): The room where the rehearsal takes place.
        """
        self.date = date
        self.duration = duration
        self.room = room

    def __repr__(self):
        return f"RehearsalSession(date={self.date}, duration={self.duration}, room='{self.room}')"

class RehearsalManager:
    """Manager class for handling rehearsal sessions."""
    
    def __init__(self):
        """Initializes the rehearsal manager with an empty session list."""
        self.sessions: List[RehearsalSession] = []

    def schedule_session(self, date: datetime, duration: int, room: str) -> None:
        """
        Schedules a new rehearsal session.
        
        Args:
            date (datetime): The date and time of the rehearsal.
            duration (int): Duration in minutes.
            room (str): The room where the rehearsal takes place.
        
        Raises:
            ValueError: If the session conflicts with an existing session.
        """
        if self.is_conflicting(date, duration, room):
            raise ValueError("The session conflicts with an existing rehearsal session.")

        self.sessions.append(RehearsalSession(date, duration, room))
        print(f"Scheduled session: {self.sessions[-1]}")

    def is_conflicting(self, date: datetime, duration: int, room: str) -> bool:
        """
        Checks if the new session conflicts with existing sessions.
        
        Args:
            date (datetime): The date and time of the rehearsal.
            duration (int): Duration in minutes.
            room (str): The room where the rehearsal takes place.
        
        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        end_time = date + timedelta(minutes=duration)
        for session in self.sessions:
            if session.room == room:
                if (session.date < end_time) and (date < (session.date + timedelta(minutes=session.duration))):
                    return True
        return False

    def list_sessions(self) -> List[RehearsalSession]:
        """Returns a list of all scheduled rehearsal sessions."""
        return self.sessions

# Example usage
if __name__ == "__main__":
    manager = RehearsalManager()
    
    # Schedule a session
    try:
        manager.schedule_session(datetime(2023, 10, 15, 14, 0), 60, "Room A")
        manager.schedule_session(datetime(2023, 10, 15, 15, 0), 30, "Room A")  # Conflict
    except ValueError as e:
        print(f"Error: {e}")

    # List all sessions
    print("All scheduled sessions:")
    for session in manager.list_sessions():
        print(session)
```
