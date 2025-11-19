"""
Generated Code Metadata:
========================
Original URL: https://anotherbrilliantidea.com
Prompt: Write code to automate the scheduling of personalized mentorship sessions for businesses, ensuring clear direction and measurable results, as described in the Marketing Mentor Program.
Generated: DETERMINISTIC_3f2917817b41ef06
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import List, Dict, Optional

class MentorshipSession:
    """Class to represent a mentorship session."""
    
    def __init__(self, mentor: str, mentee: str, date: datetime.date, time: str, duration: int):
        self.mentor = mentor
        self.mentee = mentee
        self.date = date
        self.time = time
        self.duration = duration  # Duration in minutes

    def __str__(self):
        return f"{self.mentee} with {self.mentor} on {self.date} at {self.time} for {self.duration} minutes."


class MentorshipScheduler:
    """Class to manage scheduling of mentorship sessions."""
    
    def __init__(self):
        self.sessions: List[MentorshipSession] = []

    def schedule_session(self, mentor: str, mentee: str, date: datetime.date, time: str, duration: int) -> None:
        """Schedule a new mentorship session."""
        if self.is_time_slot_available(date, time, duration):
            session = MentorshipSession(mentor, mentee, date, time, duration)
            self.sessions.append(session)
            print(f"Scheduled: {session}")
        else:
            raise ValueError("The selected time slot is not available.")

    def is_time_slot_available(self, date: datetime.date, time: str, duration: int) -> bool:
        """Check if the time slot is available for scheduling."""
        end_time = self.calculate_end_time(time, duration)
        for session in self.sessions:
            if session.date == date and self.is_time_conflict(session.time, end_time, time):
                return False
        return True

    @staticmethod
    def calculate_end_time(start_time: str, duration: int) -> str:
        """Calculate the end time of a session given a start time and duration."""
        start_dt = datetime.datetime.strptime(start_time, "%H:%M")
        end_dt = start_dt + datetime.timedelta(minutes=duration)
        return end_dt.strftime("%H:%M")

    @staticmethod
    def is_time_conflict(existing_time: str, end_time: str, new_start_time: str) -> bool:
        """Check if there is a time conflict between existing and new sessions."""
        existing_start = datetime.datetime.strptime(existing_time, "%H:%M")
        new_start = datetime.datetime.strptime(new_start_time, "%H:%M")
        existing_end = existing_start + datetime.timedelta(minutes=30)  # Assuming default session duration is 30 mins
        return (new_start < existing_end) and (existing_start < datetime.datetime.strptime(end_time, "%H:%M"))

    def save_sessions_to_file(self, filename: str) -> None:
        """Save scheduled sessions to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([session.__dict__ for session in self.sessions], file, default=str)
            print(f"Sessions saved to {filename}.")
        except IOError as e:
            print(f"Error saving sessions to file: {e}")

    def load_sessions_from_file(self, filename: str) -> None:
        """Load scheduled sessions from a JSON file."""
        try:
            with open(filename, 'r') as file:
                sessions_data = json.load(file)
                self.sessions = [MentorshipSession(**session) for session in sessions_data]
            print(f"Sessions loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading sessions from file: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = MentorshipScheduler()
    
    # Load existing sessions if any
    scheduler.load_sessions_from_file("mentorship_sessions.json")
    
    # Schedule new sessions
    try:
        scheduler.schedule_session("Alice", "Bob", datetime.date(2023, 10, 15), "10:00", 30)
        scheduler.schedule_session("Alice", "Charlie", datetime.date(2023, 10, 15), "10:30", 30)  # This will raise an error
    except ValueError as e:
        print(e)

    # Save sessions to file
    scheduler.save_sessions_to_file("mentorship_sessions.json")
```
