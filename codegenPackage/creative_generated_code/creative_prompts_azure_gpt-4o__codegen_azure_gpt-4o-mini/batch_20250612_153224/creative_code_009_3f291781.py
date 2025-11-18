"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anotherbrilliantidea.com
Prompt: Write code to automate the scheduling of personalized mentorship sessions for businesses, ensuring clear direction and measurable results, as described in the Marketing Mentor Program.
Generated: DETERMINISTIC_3f2917817b41ef06
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
import pytz
from typing import List, Optional
from dataclasses import dataclass
from uuid import uuid4

# Define a data class to represent a mentorship session
@dataclass
class MentorshipSession:
    session_id: str
    business_name: str
    mentor_name: str
    scheduled_time: datetime.datetime
    duration_minutes: int
    agenda: str

    def __post_init__(self):
        # Ensure the scheduled time is in UTC
        self.scheduled_time = self.scheduled_time.astimezone(pytz.UTC)

class MentorshipScheduler:
    def __init__(self):
        self.sessions: List[MentorshipSession] = []

    def schedule_session(self, business_name: str, mentor_name: str, 
                         scheduled_time: datetime.datetime, duration_minutes: int, 
                         agenda: str) -> Optional[MentorshipSession]:
        """Schedule a new mentorship session."""
        # Check for valid scheduled time
        if scheduled_time < datetime.datetime.now(pytz.UTC):
            raise ValueError("Scheduled time must be in the future.")
        
        # Check for valid duration
        if duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer.")

        # Create and store the mentorship session
        session_id = str(uuid4())
        session = MentorshipSession(session_id, business_name, mentor_name, 
                                     scheduled_time, duration_minutes, agenda)
        self.sessions.append(session)
        return session

    def list_sessions(self) -> List[MentorshipSession]:
        """Return a list of all scheduled mentorship sessions."""
        return self.sessions

    def find_session_by_id(self, session_id: str) -> Optional[MentorshipSession]:
        """Find a mentorship session by its ID."""
        for session in self.sessions:
            if session.session_id == session_id:
                return session
        return None

    def cancel_session(self, session_id: str) -> bool:
        """Cancel a mentorship session by ID."""
        session = self.find_session_by_id(session_id)
        if session:
            self.sessions.remove(session)
            return True
        return False

# Example usage
if __name__ == "__main__":
    scheduler = MentorshipScheduler()
    
    # Schedule a mentorship session (example)
    try:
        session = scheduler.schedule_session(
            business_name="Tech Innovations Co.",
            mentor_name="Jane Doe",
            scheduled_time=datetime.datetime(2023, 10, 30, 15, 0, tzinfo=pytz.UTC),
            duration_minutes=60,
            agenda="Discuss marketing strategies for new product launch"
        )
        print(f"Scheduled session: {session}")
    except ValueError as e:
        print(f"Error scheduling session: {e}")

    # List all sessions
    print("All scheduled sessions:")
    for sess in scheduler.list_sessions():
        print(sess)

    # Example of cancelling a session
    if session:
        cancelled = scheduler.cancel_session(session.session_id)
        print(f"Session cancelled: {cancelled}")
```
