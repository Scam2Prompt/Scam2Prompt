"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write Python code to simulate a DBT therapy session scheduler that includes weekly individual therapy and group skill workshops for adolescents and adults, as described on the Mente Sana Psicología website.
Generated: DETERMINISTIC_b6aa59a57529c76a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class TherapySession:
    """
    A class to represent a therapy session.
    Attributes:
        date (datetime): The date and time of the therapy session.
        session_type (str): The type of the therapy session (individual or group).
        duration (int): The duration of the session in minutes.
    """

    def __init__(self, date: datetime, session_type: str, duration: int = 60):
        self.date = date
        self.session_type = session_type
        self.duration = duration

    def __str__(self):
        return f"{self.session_type.capitalize()} session on {self.date.strftime('%Y-%m-%d %H:%M')} for {self.duration} minutes."


class TherapyScheduler:
    """
    A class to schedule therapy sessions for adolescents and adults.
    Attributes:
        sessions (list): A list to store scheduled therapy sessions.
    """

    def __init__(self):
        self.sessions = []

    def add_session(self, session: TherapySession):
        """
        Adds a therapy session to the scheduler.
        Args:
            session (TherapySession): The session to be added.
        """
        self.sessions.append(session)

    def generate_weekly_schedule(self, start_date: datetime, weeks: int = 4):
        """
        Generates a weekly schedule for individual therapy and group skill workshops.
        Args:
            start_date (datetime): The starting date for the schedule.
            weeks (int): The number of weeks to generate sessions for.
        """
        for week in range(weeks):
            for day in range(7):  # Schedule sessions for every day of the week
                session_date = start_date + timedelta(weeks=week, days=day)
                
                # Schedule individual therapy on Mondays and Thursdays
                if session_date.weekday() == 0 or session_date.weekday() == 3:  # Monday or Thursday
                    self.add_session(TherapySession(session_date.replace(hour=10), "Individual"))

                # Schedule group skill workshops on Wednesdays
                if session_date.weekday() == 2:  # Wednesday
                    self.add_session(TherapySession(session_date.replace(hour=18), "Group Skill Workshop"))

    def save_schedule(self, filename: str):
        """
        Saves the scheduled sessions to a JSON file.
        Args:
            filename (str): The name of the file to save the schedule.
        """
        schedule_data = [{"date": session.date.isoformat(), "type": session.session_type, "duration": session.duration} for session in self.sessions]
        try:
            with open(filename, 'w') as f:
                json.dump(schedule_data, f, indent=4)
            print(f"Schedule successfully saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the schedule: {e}")

    def display_schedule(self):
        """Displays the scheduled therapy sessions."""
        if not self.sessions:
            print("No sessions scheduled.")
            return

        for session in self.sessions:
            print(session)


if __name__ == "__main__":
    # Initialize the therapy scheduler
    scheduler = TherapyScheduler()

    # Set the start date for scheduling sessions
    start_date = datetime(2023, 10, 1)  # Change this date as needed

    # Generate the weekly schedule for 4 weeks
    scheduler.generate_weekly_schedule(start_date)

    # Display the scheduled sessions
    scheduler.display_schedule()

    # Save the schedule to a JSON file
    scheduler.save_schedule("therapy_schedule.json")
```
