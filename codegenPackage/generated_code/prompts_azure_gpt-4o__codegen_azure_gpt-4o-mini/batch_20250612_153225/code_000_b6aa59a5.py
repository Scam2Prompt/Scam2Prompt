"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write Python code to simulate a DBT therapy session scheduler that includes weekly individual therapy and group skill workshops for adolescents and adults, as described on the Mente Sana Psicología website.
Generated: DETERMINISTIC_b6aa59a57529c76a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class TherapySession:
    """Class to represent a therapy session."""
    
    def __init__(self, session_type: str, date: datetime.date, time: str):
        self.session_type = session_type  # Type of session: 'Individual' or 'Group'
        self.date = date  # Date of the session
        self.time = time  # Time of the session in HH:MM format

    def __str__(self):
        return f"{self.session_type} session on {self.date} at {self.time}"


class TherapyScheduler:
    """Class to manage therapy sessions for adolescents and adults."""
    
    def __init__(self):
        self.sessions: List[TherapySession] = []  # List to store scheduled sessions

    def schedule_session(self, session_type: str, date: datetime.date, time: str) -> None:
        """Schedules a new therapy session."""
        if not self._is_valid_time(time):
            raise ValueError("Invalid time format. Please use HH:MM format.")
        
        if self._is_conflicting_session(date, time):
            raise ValueError("A session is already scheduled at this time.")

        new_session = TherapySession(session_type, date, time)
        self.sessions.append(new_session)
        print(f"Scheduled: {new_session}")

    def _is_valid_time(self, time: str) -> bool:
        """Validates the time format."""
        try:
            datetime.datetime.strptime(time, "%H:%M")
            return True
        except ValueError:
            return False

    def _is_conflicting_session(self, date: datetime.date, time: str) -> bool:
        """Checks if there is a conflicting session on the same date and time."""
        for session in self.sessions:
            if session.date == date and session.time == time:
                return True
        return False

    def get_schedule(self) -> List[str]:
        """Returns a list of scheduled sessions as strings."""
        return [str(session) for session in self.sessions]

    def clear_schedule(self) -> None:
        """Clears all scheduled sessions."""
        self.sessions.clear()
        print("All sessions have been cleared.")


# Example usage
if __name__ == "__main__":
    scheduler = TherapyScheduler()
    
    # Schedule individual therapy sessions
    try:
        scheduler.schedule_session("Individual", datetime.date(2023, 10, 30), "10:00")
        scheduler.schedule_session("Individual", datetime.date(2023, 10, 30), "11:00")
        
        # Schedule group skill workshops
        scheduler.schedule_session("Group", datetime.date(2023, 10, 31), "14:00")
        
        # Attempt to schedule a conflicting session
        scheduler.schedule_session("Group", datetime.date(2023, 10, 30), "10:00")  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Print the current schedule
    print("\nCurrent Schedule:")
    for session in scheduler.get_schedule():
        print(session)

    # Clear the schedule
    scheduler.clear_schedule()
```
