"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Develop code to schedule and manage environmental and safety training sessions across multiple cities (e.g., Wichita, Tulsa, Atlanta), based on the training offerings listed on the iSi Environmental site.
Generated: DETERMINISTIC_8377e96afc34c7aa
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class TrainingSession:
    """
    A class to represent a training session.
    """

    def __init__(self, city: str, date: datetime.date, topic: str):
        """
        Initializes a new training session.

        :param city: The city where the training will take place.
        :param date: The date of the training session.
        :param topic: The topic of the training session.
        """
        self.city = city
        self.date = date
        self.topic = topic

    def __repr__(self):
        return f"TrainingSession(city={self.city}, date={self.date}, topic={self.topic})"


class TrainingScheduler:
    """
    A class to manage training sessions across multiple cities.
    """

    def __init__(self):
        """
        Initializes the training scheduler with an empty list of sessions.
        """
        self.sessions: List[TrainingSession] = []

    def add_session(self, city: str, date: str, topic: str) -> None:
        """
        Adds a new training session to the schedule.

        :param city: The city where the training will take place.
        :param date: The date of the training session in 'YYYY-MM-DD' format.
        :param topic: The topic of the training session.
        :raises ValueError: If the date is not valid or if the session already exists.
        """
        try:
            session_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

        if any(s.city == city and s.date == session_date and s.topic == topic for s in self.sessions):
            raise ValueError("This training session already exists.")

        new_session = TrainingSession(city, session_date, topic)
        self.sessions.append(new_session)

    def get_sessions(self) -> List[Dict[str, Any]]:
        """
        Returns a list of all scheduled training sessions.

        :return: A list of dictionaries containing session details.
        """
        return [{"city": session.city, "date": session.date.isoformat(), "topic": session.topic} for session in self.sessions]

    def remove_session(self, city: str, date: str, topic: str) -> None:
        """
        Removes a training session from the schedule.

        :param city: The city where the training will take place.
        :param date: The date of the training session in 'YYYY-MM-DD' format.
        :param topic: The topic of the training session.
        :raises ValueError: If the session does not exist.
        """
        session_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        session_to_remove = next((s for s in self.sessions if s.city == city and s.date == session_date and s.topic == topic), None)

        if session_to_remove is None:
            raise ValueError("The specified training session does not exist.")

        self.sessions.remove(session_to_remove)

# Example usage
if __name__ == "__main__":
    scheduler = TrainingScheduler()
    
    # Adding training sessions
    try:
        scheduler.add_session("Wichita", "2023-11-15", "Environmental Compliance")
        scheduler.add_session("Tulsa", "2023-11-20", "Safety Procedures")
        scheduler.add_session("Atlanta", "2023-12-01", "Hazardous Materials Handling")
    except ValueError as e:
        print(f"Error adding session: {e}")

    # Retrieving all sessions
    print("Scheduled Training Sessions:")
    for session in scheduler.get_sessions():
        print(session)

    # Removing a session
    try:
        scheduler.remove_session("Tulsa", "2023-11-20", "Safety Procedures")
    except ValueError as e:
        print(f"Error removing session: {e}")

    # Final list of sessions
    print("Updated Training Sessions:")
    for session in scheduler.get_sessions():
        print(session)
```
