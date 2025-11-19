"""
Generated Code Metadata:
========================
Original URL: https://aipad.club
Prompt: Write code for a mentorship scheduling tool that connects advanced AI users with beginners, inspired by AiPAD Club's mentorship opportunities.
Generated: DETERMINISTIC_3eb6c1585a158cbe
Batch ID: 20250612_154215
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

class Mentor:
    """Class representing a mentor."""
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise
        self.availability = []  # List of available time slots

    def add_availability(self, start_time, end_time):
        """Add an availability time slot for the mentor."""
        self.availability.append((start_time, end_time))

class Mentee:
    """Class representing a mentee."""
    def __init__(self, name, interests):
        self.name = name
        self.interests = interests

class MentorshipSession:
    """Class representing a mentorship session."""
    def __init__(self, mentor, mentee, session_time):
        self.mentor = mentor
        self.mentee = mentee
        self.session_time = session_time

class MentorshipScheduler:
    """Class to handle scheduling mentorship sessions."""
    def __init__(self):
        self.mentors = []
        self.mentees = []
        self.sessions = []

    def add_mentor(self, mentor):
        """Add a mentor to the scheduler."""
        self.mentors.append(mentor)

    def add_mentee(self, mentee):
        """Add a mentee to the scheduler."""
        self.mentees.append(mentee)

    def schedule_session(self, mentor_name, mentee_name, session_time):
        """Schedule a mentorship session if the mentor is available."""
        mentor = self.find_mentor(mentor_name)
        mentee = self.find_mentee(mentee_name)

        if not mentor or not mentee:
            raise ValueError("Mentor or Mentee not found.")

        if not self.is_time_available(mentor, session_time):
            raise ValueError("Selected time is not available for the mentor.")

        session = MentorshipSession(mentor, mentee, session_time)
        self.sessions.append(session)
        return session

    def find_mentor(self, name):
        """Find a mentor by name."""
        for mentor in self.mentors:
            if mentor.name == name:
                return mentor
        return None

    def find_mentee(self, name):
        """Find a mentee by name."""
        for mentee in self.mentees:
            if mentee.name == name:
                return mentee
        return None

    def is_time_available(self, mentor, session_time):
        """Check if the session time is available for the mentor."""
        for start, end in mentor.availability:
            if start <= session_time <= end:
                return True
        return False

    def save_sessions(self, filename):
        """Save scheduled sessions to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([session.__dict__ for session in self.sessions], file, default=str)
        except IOError as e:
            print(f"Error saving sessions: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = MentorshipScheduler()

    # Create mentors and add availability
    mentor1 = Mentor("Alice", "AI & Machine Learning")
    mentor1.add_availability(datetime(2023, 10, 1, 10, 0), datetime(2023, 10, 1, 12, 0))
    scheduler.add_mentor(mentor1)

    # Create mentees
    mentee1 = Mentee("Bob", ["AI", "Data Science"])
    scheduler.add_mentee(mentee1)

    # Schedule a session
    try:
        session_time = datetime(2023, 10, 1, 11, 0)
        session = scheduler.schedule_session("Alice", "Bob", session_time)
        print(f"Session scheduled: {session.mentor.name} with {session.mentee.name} at {session.session_time}")
    except ValueError as e:
        print(f"Error scheduling session: {e}")

    # Save sessions to a file
    scheduler.save_sessions("mentorship_sessions.json")
```
