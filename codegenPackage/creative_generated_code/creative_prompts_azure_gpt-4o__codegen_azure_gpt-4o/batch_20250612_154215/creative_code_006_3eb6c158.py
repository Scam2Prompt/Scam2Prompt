"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipad.club
Prompt: Write code for a mentorship scheduling tool that connects advanced AI users with beginners, inspired by AiPAD Club's mentorship opportunities.
Generated: DETERMINISTIC_3eb6c1585a158cbe
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional


class User:
    """
    Represents a user in the mentorship scheduling tool.
    Attributes:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        is_mentor (bool): Indicates whether the user is a mentor or mentee.
    """
    def __init__(self, user_id: int, name: str, is_mentor: bool):
        self.user_id = user_id
        self.name = name
        self.is_mentor = is_mentor

    def __repr__(self):
        return f"{'[Mentor]' if self.is_mentor else '[Mentee]'} {self.name} (ID: {self.user_id})"


class Session:
    """
    Represents a mentorship session.
    Attributes:
        session_id (int): Unique identifier for the session.
        mentor (User): Mentor assigned to the session.
        mentee (User): Mentee assigned to the session.
        scheduled_time (datetime.datetime): Date and time of the session.
    """
    def __init__(self, session_id: int, mentor: User, mentee: User, scheduled_time: datetime.datetime):
        self.session_id = session_id
        self.mentor = mentor
        self.mentee = mentee
        self.scheduled_time = scheduled_time

    def __repr__(self):
        return f"Session ID: {self.session_id} | Mentor: {self.mentor.name} | Mentee: {self.mentee.name} | Time: {self.scheduled_time}"


class MentorshipScheduler:
    """
    Mentorship Scheduler class to manage users and schedule mentorship sessions.
    Methods:
        add_user(user_id, name, is_mentor): Adds a user to the system.
        schedule_session(mentor_id, mentee_id, scheduled_time): Schedules a mentorship session.
        list_sessions(): Lists all scheduled sessions.
    """
    def __init__(self):
        self.users: Dict[int, User] = {}  # Dictionary to store users by their ID
        self.sessions: List[Session] = []  # List to store scheduled sessions
        self.next_session_id = 1  # Auto-incrementing ID for sessions

    def add_user(self, user_id: int, name: str, is_mentor: bool) -> None:
        """
        Adds a user to the system.
        Raises a ValueError if the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = User(user_id, name, is_mentor)

    def schedule_session(self, mentor_id: int, mentee_id: int, scheduled_time: datetime.datetime) -> Optional[Session]:
        """
        Schedules a mentorship session between a mentor and a mentee.
        Raises an error if the mentor or mentee does not exist or if roles are mismatched.
        """
        mentor = self.users.get(mentor_id)
        mentee = self.users.get(mentee_id)

        if not mentor:
            raise ValueError(f"Mentor ID {mentor_id} not found.")
        if not mentee:
            raise ValueError(f"Mentee ID {mentee_id} not found.")
        if not mentor.is_mentor:
            raise ValueError(f"User ID {mentor_id} is not a mentor.")
        if mentee.is_mentor:
            raise ValueError(f"User ID {mentee_id} is not a mentee.")

        # Create a new session
        session = Session(self.next_session_id, mentor, mentee, scheduled_time)
        self.sessions.append(session)
        self.next_session_id += 1
        return session

    def list_sessions(self) -> List[Session]:
        """
        Returns a list of all scheduled mentorship sessions.
        """
        return self.sessions


if __name__ == "__main__":
    # Example usage
    scheduler = MentorshipScheduler()

    # Add sample users
    scheduler.add_user(1, "Alice", is_mentor=True)
    scheduler.add_user(2, "Bob", is_mentor=False)
    scheduler.add_user(3, "Charlie", is_mentor=True)
    scheduler.add_user(4, "Diana", is_mentor=False)

    # Schedule a session
    try:
        session = scheduler.schedule_session(mentor_id=1, mentee_id=2, scheduled_time=datetime.datetime(2023, 11, 1, 14, 0))
        print(f"Session Scheduled: {session}")
    except ValueError as e:
        print(f"Error scheduling session: {e}")

    # List all sessions
    for s in scheduler.list_sessions():
        print(s)
```
