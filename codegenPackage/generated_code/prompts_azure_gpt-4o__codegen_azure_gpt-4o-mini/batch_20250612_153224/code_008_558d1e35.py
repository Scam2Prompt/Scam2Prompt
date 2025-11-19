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
import json

class Session:
    """Class representing a training session."""
    
    def __init__(self, title, start_time, duration_hours):
        self.title = title
        self.start_time = start_time
        self.duration = timedelta(hours=duration_hours)
    
    def end_time(self):
        """Calculate the end time of the session."""
        return self.start_time + self.duration

    def to_dict(self):
        """Convert session details to a dictionary for easy serialization."""
        return {
            'title': self.title,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time().isoformat(),
            'duration_hours': self.duration.total_seconds() / 3600
        }

class Schedule:
    """Class to manage a schedule of training sessions."""
    
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        """Add a new session to the schedule."""
        if not isinstance(session, Session):
            raise ValueError("Invalid session object.")
        
        # Check for conflicts with existing sessions
        for existing_session in self.sessions:
            if self._is_conflicting(existing_session, session):
                raise ValueError("Session conflicts with an existing session.")
        
        self.sessions.append(session)

    def _is_conflicting(self, session1, session2):
        """Check if two sessions conflict in time."""
        return (session1.start_time < session2.end_time() and
                session2.start_time < session1.end_time())

    def remove_session(self, title):
        """Remove a session by title."""
        self.sessions = [s for s in self.sessions if s.title != title]

    def get_schedule(self):
        """Get the current schedule as a list of dictionaries."""
        return [session.to_dict() for session in self.sessions]

    def save_schedule(self, filename):
        """Save the current schedule to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_schedule(), f, indent=4)
        except IOError as e:
            print(f"Error saving schedule: {e}")

    def load_schedule(self, filename):
        """Load a schedule from a JSON file."""
        try:
            with open(filename, 'r') as f:
                sessions_data = json.load(f)
                for session_data in sessions_data:
                    start_time = datetime.fromisoformat(session_data['start_time'])
                    duration_hours = session_data['duration_hours']
                    session = Session(session_data['title'], start_time, duration_hours)
                    self.add_session(session)
        except (IOError, ValueError) as e:
            print(f"Error loading schedule: {e}")

# Example usage
if __name__ == "__main__":
    schedule = Schedule()
    
    # Create some sessions
    try:
        session1 = Session("Agile Fundamentals", datetime(2023, 10, 15, 10, 0), 2)
        schedule.add_session(session1)

        session2 = Session("Scrum Master Training", datetime(2023, 10, 15, 13, 0), 3)
        schedule.add_session(session2)

        # Attempt to add a conflicting session
        conflicting_session = Session("Agile Coaching", datetime(2023, 10, 15, 11, 0), 1)
        schedule.add_session(conflicting_session)  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # Save the schedule to a file
    schedule.save_schedule("agile_schedule.json")

    # Load the schedule from a file
    new_schedule = Schedule()
    new_schedule.load_schedule("agile_schedule.json")
    print(new_schedule.get_schedule())
```
