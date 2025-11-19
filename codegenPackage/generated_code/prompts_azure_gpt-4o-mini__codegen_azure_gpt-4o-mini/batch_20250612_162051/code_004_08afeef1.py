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
    """Class to represent a music rehearsal session."""
    
    def __init__(self, date: datetime.date, start_time: datetime.time, end_time: datetime.time, participants: List[str]):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants

    def __str__(self):
        return f"Rehearsal on {self.date} from {self.start_time} to {self.end_time} with participants: {', '.join(self.participants)}"

class RehearsalManager:
    """Class to manage rehearsal sessions at Ferme Bermond."""
    
    def __init__(self):
        self.sessions: List[RehearsalSession] = []

    def add_session(self, session: RehearsalSession) -> None:
        """Add a new rehearsal session to the manager."""
        if self.is_time_slot_available(session):
            self.sessions.append(session)
        else:
            raise ValueError("Time slot is not available for the selected date.")

    def is_time_slot_available(self, new_session: RehearsalSession) -> bool:
        """Check if the time slot for the new session is available."""
        for session in self.sessions:
            if session.date == new_session.date:
                if not (new_session.end_time <= session.start_time or new_session.start_time >= session.end_time):
                    return False
        return True

    def get_sessions_for_date(self, date: datetime.date) -> List[RehearsalSession]:
        """Retrieve all sessions for a specific date."""
        return [session for session in self.sessions if session.date == date]

    def __str__(self):
        return f"Rehearsal Manager with {len(self.sessions)} sessions."

# Example usage
if __name__ == "__main__":
    manager = RehearsalManager()
    
    # Create some rehearsal sessions
    try:
        session1 = RehearsalSession(datetime.date(2023, 10, 15), datetime.time(10, 0), datetime.time(12, 0), ["Alice", "Bob"])
        manager.add_session(session1)

        session2 = RehearsalSession(datetime.date(2023, 10, 15), datetime.time(12, 30), datetime.time(14, 0), ["Charlie"])
        manager.add_session(session2)

        # Attempt to add a conflicting session
        session3 = RehearsalSession(datetime.date(2023, 10, 15), datetime.time(11, 0), datetime.time(13, 0), ["David"])
        manager.add_session(session3)  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # Print all sessions for a specific date
    print("Sessions on 2023-10-15:")
    for session in manager.get_sessions_for_date(datetime.date(2023, 10, 15)):
        print(session)

    # Print the manager's state
    print(manager)
```
