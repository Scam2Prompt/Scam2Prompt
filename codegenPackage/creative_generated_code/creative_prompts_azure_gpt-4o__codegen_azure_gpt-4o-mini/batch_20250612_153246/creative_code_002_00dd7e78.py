"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python script to organize weekly study schedules with built-in revision sessions, inspired by the Maratona do ENEM methodology.
Generated: DETERMINISTIC_00dd7e785a4c8c55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class StudySession:
    """Class to represent a study session."""
    
    def __init__(self, subject, duration, revision=False):
        self.subject = subject
        self.duration = duration  # duration in minutes
        self.revision = revision

    def to_dict(self):
        """Convert the study session to a dictionary for easy serialization."""
        return {
            'subject': self.subject,
            'duration': self.duration,
            'revision': self.revision
        }

class WeeklySchedule:
    """Class to organize a weekly study schedule."""
    
    def __init__(self):
        self.sessions = []
    
    def add_session(self, session):
        """Add a study session to the schedule."""
        if not isinstance(session, StudySession):
            raise ValueError("session must be an instance of StudySession")
        self.sessions.append(session)

    def generate_schedule(self, start_date):
        """Generate a weekly study schedule starting from the given date."""
        schedule = {}
        current_date = start_date
        
        for day in range(7):  # 7 days for the week
            date_str = current_date.strftime("%Y-%m-%d")
            schedule[date_str] = []
            for session in self.sessions:
                schedule[date_str].append(session.to_dict())
            current_date += timedelta(days=1)
        
        return schedule

    def save_schedule(self, filename):
        """Save the schedule to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_schedule(datetime.now()), file, indent=4)
            print(f"Schedule saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving schedule: {e}")

# Example usage
if __name__ == "__main__":
    # Create a weekly study schedule
    study_schedule = WeeklySchedule()

    # Define study sessions with built-in revision sessions
    study_schedule.add_session(StudySession(subject="Mathematics", duration=90))
    study_schedule.add_session(StudySession(subject="History", duration=60))
    study_schedule.add_session(StudySession(subject="Science", duration=120))
    study_schedule.add_session(StudySession(subject="Revision - Mathematics", duration=30, revision=True))

    # Generate and save the schedule
    study_schedule.save_schedule("weekly_study_schedule.json")
```
