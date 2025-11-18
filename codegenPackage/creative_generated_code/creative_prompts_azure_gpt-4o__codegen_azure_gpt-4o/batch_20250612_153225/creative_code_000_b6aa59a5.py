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
import datetime
from typing import List, Dict

class TherapySession:
    """
    Class to represent a therapy session.
    """
    def __init__(self, session_name: str, session_type: str, day_of_week: str, time: datetime.time, target_group: str):
        """
        Initialize a therapy session.

        :param session_name: Name of the session
        :param session_type: Type of the session (individual or group)
        :param day_of_week: Day of the week the session occurs
        :param time: Time the session occurs
        :param target_group: Target group for the session (adolescents or adults)
        """
        self.session_name = session_name
        self.session_type = session_type
        self.day_of_week = day_of_week
        self.time = time
        self.target_group = target_group

    def __str__(self):
        """
        String representation of the therapy session.
        """
        return f"{self.session_name} ({self.session_type}) - {self.target_group} on {self.day_of_week} at {self.time.strftime('%H:%M')}"

class TherapyScheduler:
    """
    Class to manage therapy sessions scheduling.
    """
    def __init__(self):
        """
        Initialize the therapy scheduler.
        """
        self.sessions: List[TherapySession] = []

    def add_session(self, session_name: str, session_type: str, day_of_week: str, time: str, target_group: str):
        """
        Add a new therapy session.

        :param session_name: Name of the session
        :param session_type: Type of the session (individual or group)
        :param day_of_week: Day of the week the session occurs
        :param time: Time the session occurs (in HH:MM format)
        :param target_group: Target group for the session (adolescents or adults)
        """
        try:
            # Convert time string to datetime.time
            session_time = datetime.datetime.strptime(time, '%H:%M').time()
            session = TherapySession(session_name, session_type, day_of_week, session_time, target_group)
            self.sessions.append(session)
        except ValueError as e:
            print(f"Error adding session: {e}. Please ensure the time format is HH:MM.")

    def get_sessions(self) -> List[Dict]:
        """
        Retrieve all scheduled sessions.

        :return: List of dictionaries representing the scheduled sessions
        """
        return [
            {
                "session_name": session.session_name,
                "session_type": session.session_type,
                "day_of_week": session.day_of_week,
                "time": session.time.strftime('%H:%M'),
                "target_group": session.target_group
            }
            for session in self.sessions
        ]

    def print_schedule(self):
        """
        Print the schedule of all therapy sessions.
        """
        if not self.sessions:
            print("No sessions scheduled.")
            return

        print("Scheduled Therapy Sessions:")
        for session in self.sessions:
            print(f"  - {session}")

# Example Usage:
if __name__ == "__main__":
    scheduler = TherapyScheduler()

    # Adding weekly individual therapy sessions
    scheduler.add_session("Individual Therapy", "Individual", "Monday", "10:00", "Adolescents")
    scheduler.add_session("Individual Therapy", "Individual", "Tuesday", "11:00", "Adults")

    # Adding weekly group skill workshops
    scheduler.add_session("Group Skills Workshop", "Group", "Wednesday", "14:00", "Adolescents")
    scheduler.add_session("Group Skills Workshop", "Group", "Thursday", "15:00", "Adults")

    # Print the schedule
    scheduler.print_schedule()
```
