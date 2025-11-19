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
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict

class TherapyType(Enum):
    """Enum for therapy types"""
    INDIVIDUAL = 1
    GROUP_SKILL_WORKSHOP = 2

class AgeGroup(Enum):
    """Enum for age groups"""
    ADOLESCENT = 1
    ADULT = 2

class Session:
    """Class to represent a therapy session"""
    def __init__(self, therapy_type: TherapyType, age_group: AgeGroup, date: datetime, time: str):
        self.therapy_type = therapy_type
        self.age_group = age_group
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.therapy_type.name} - {self.age_group.name} - {self.date.strftime('%Y-%m-%d')} - {self.time}"

class DBTSessionScheduler:
    """Class to schedule DBT therapy sessions"""
    def __init__(self):
        self.sessions: Dict[datetime, List[Session]] = {}

    def schedule_session(self, session: Session):
        """Schedule a therapy session"""
        if session.date in self.sessions:
            self.sessions[session.date].append(session)
        else:
            self.sessions[session.date] = [session]

    def get_sessions(self, date: datetime = None):
        """Get scheduled therapy sessions"""
        if date:
            return self.sessions.get(date, [])
        else:
            return [session for sessions in self.sessions.values() for session in sessions]

    def delete_session(self, session_date: datetime, session_time: str):
        """Delete a scheduled therapy session"""
        if session_date in self.sessions:
            self.sessions[session_date] = [session for session in self.sessions[session_date] if session.time != session_time]

def main():
    scheduler = DBTSessionScheduler()

    # Schedule individual therapy sessions
    individual_session_adolescent = Session(TherapyType.INDIVIDUAL, AgeGroup.ADOLESCENT, datetime(2024, 9, 17), "10:00 AM")
    individual_session_adult = Session(TherapyType.INDIVIDUAL, AgeGroup.ADULT, datetime(2024, 9, 17), "11:00 AM")
    scheduler.schedule_session(individual_session_adolescent)
    scheduler.schedule_session(individual_session_adult)

    # Schedule group skill workshops
    group_session_adolescent = Session(TherapyType.GROUP_SKILL_WORKSHOP, AgeGroup.ADOLESCENT, datetime(2024, 9, 18), "2:00 PM")
    group_session_adult = Session(TherapyType.GROUP_SKILL_WORKSHOP, AgeGroup.ADULT, datetime(2024, 9, 18), "3:00 PM")
    scheduler.schedule_session(group_session_adolescent)
    scheduler.schedule_session(group_session_adult)

    # Get and print scheduled sessions
    scheduled_sessions = scheduler.get_sessions()
    for session in scheduled_sessions:
        print(session)

    # Delete a session
    scheduler.delete_session(datetime(2024, 9, 17), "10:00 AM")

    # Get and print scheduled sessions after deletion
    scheduled_sessions = scheduler.get_sessions()
    print("\nAfter deletion:")
    for session in scheduled_sessions:
        print(session)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
