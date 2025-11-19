"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Write a Python script to manage a study schedule for ENEM preparation, incorporating the Maratona do ENEM's review and simulation strategy."
Generated: DETERMINISTIC_547ef7fdf462ff9f
Batch ID: 20250622_210703
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
    
    def __init__(self, subject, duration, date):
        self.subject = subject
        self.duration = duration  # in minutes
        self.date = date  # datetime object

    def __str__(self):
        return f"{self.subject} for {self.duration} minutes on {self.date.strftime('%Y-%m-%d %H:%M')}"

class StudySchedule:
    """Class to manage the study schedule."""
    
    def __init__(self):
        self.sessions = []

    def add_session(self, subject, duration, date):
        """Add a new study session to the schedule."""
        try:
            session = StudySession(subject, duration, date)
            self.sessions.append(session)
            print(f"Added session: {session}")
        except Exception as e:
            print(f"Error adding session: {e}")

    def remove_session(self, session_index):
        """Remove a study session from the schedule by index."""
        try:
            removed_session = self.sessions.pop(session_index)
            print(f"Removed session: {removed_session}")
        except IndexError:
            print("Error: Session index out of range.")
        except Exception as e:
            print(f"Error removing session: {e}")

    def view_schedule(self):
        """Display the current study schedule."""
        if not self.sessions:
            print("No study sessions scheduled.")
            return
        print("Current Study Schedule:")
        for index, session in enumerate(self.sessions):
            print(f"{index}: {session}")

    def save_schedule(self, filename):
        """Save the study schedule to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([session.__dict__ for session in self.sessions], file, default=str)
            print(f"Schedule saved to {filename}")
        except Exception as e:
            print(f"Error saving schedule: {e}")

    def load_schedule(self, filename):
        """Load the study schedule from a JSON file."""
        try:
            with open(filename, 'r') as file:
                sessions_data = json.load(file)
                self.sessions = [StudySession(**data) for data in sessions_data]
            print(f"Schedule loaded from {filename}")
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: File is not a valid JSON.")
        except Exception as e:
            print(f"Error loading schedule: {e}")

def main():
    """Main function to run the study schedule manager."""
    schedule = StudySchedule()

    # Example usage
    schedule.add_session("Mathematics", 120, datetime.now() + timedelta(days=1))
    schedule.add_session("Physics", 90, datetime.now() + timedelta(days=2))
    schedule.view_schedule()

    # Save and load schedule
    schedule.save_schedule("study_schedule.json")
    schedule.load_schedule("study_schedule.json")

if __name__ == "__main__":
    main()
```
