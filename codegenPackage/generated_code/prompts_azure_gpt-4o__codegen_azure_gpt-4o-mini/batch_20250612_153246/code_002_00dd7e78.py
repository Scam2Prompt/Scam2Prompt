"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python script to organize weekly study schedules with built-in revision sessions, inspired by the Maratona do ENEM methodology.
Generated: DETERMINISTIC_00dd7e785a4c8c55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class StudySession:
    """Class to represent a study session."""
    
    def __init__(self, subject, duration, revision=False):
        """
        Initialize a study session.

        Args:
            subject (str): The subject to study.
            duration (int): Duration of the study session in minutes.
            revision (bool): Indicates if the session is a revision session.
        """
        self.subject = subject
        self.duration = duration
        self.revision = revision

    def __repr__(self):
        return f"{'Revision' if self.revision else 'Study'}: {self.subject} for {self.duration} mins"


class WeeklySchedule:
    """Class to manage a weekly study schedule."""
    
    def __init__(self):
        """Initialize the weekly schedule with an empty list of sessions."""
        self.sessions = []

    def add_session(self, session):
        """
        Add a study session to the schedule.

        Args:
            session (StudySession): The study session to add.
        """
        if not isinstance(session, StudySession):
            raise ValueError("session must be an instance of StudySession")
        self.sessions.append(session)

    def generate_schedule(self):
        """Generate a weekly schedule with built-in revision sessions."""
        schedule = {}
        start_date = datetime.now()
        
        for i in range(7):  # Create a schedule for 7 days
            day = start_date + timedelta(days=i)
            schedule[day.strftime("%Y-%m-%d")] = []

            # Add study sessions
            for session in self.sessions:
                schedule[day.strftime("%Y-%m-%d")].append(session)

            # Add revision sessions (every 3rd day)
            if i % 3 == 0:
                revision_session = StudySession("Revision", 30, revision=True)
                schedule[day.strftime("%Y-%m-%d")].append(revision_session)

        return schedule

    def save_schedule(self, filename):
        """
        Save the schedule to a JSON file.

        Args:
            filename (str): The name of the file to save the schedule.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_schedule(), file, default=str, indent=4)
            print(f"Schedule saved to {filename}")
        except IOError as e:
            print(f"Error saving schedule: {e}")


def main():
    """Main function to create and save a study schedule."""
    # Create a weekly study schedule
    weekly_schedule = WeeklySchedule()

    # Add study sessions (example subjects and durations)
    subjects = [
        ("Mathematics", 60),
        ("History", 45),
        ("Biology", 50),
        ("Chemistry", 40),
        ("Literature", 30)
    ]

    for subject, duration in subjects:
        session = StudySession(subject, duration)
        weekly_schedule.add_session(session)

    # Save the schedule to a file
    weekly_schedule.save_schedule("weekly_study_schedule.json")


if __name__ == "__main__":
    main()
```
