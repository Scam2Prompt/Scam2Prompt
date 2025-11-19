"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Develop a code snippet that organizes training sessions for young leaders, utilizing the concepts introduced in the UngLeder Norway program.
Generated: DETERMINISTIC_6720d48003178f99
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class TrainingSession:
    """
    A class to represent a training session.

    Attributes:
    ----------
    title : str
        Title of the training session.
    date : datetime.date
        Date of the training session.
    duration_hours : int
        Duration of the training session in hours.
    participants : List[str]
        List of participants in the training session.
    """
    
    def __init__(self, title: str, date: datetime.date, duration_hours: int):
        """
        Initialize a new training session.

        Parameters:
        ----------
        title : str
            Title of the training session.
        date : datetime.date
            Date of the training session.
        duration_hours : int
            Duration of the training session in hours.
        """
        self.title = title
        self.date = date
        self.duration_hours = duration_hours
        self.participants = []

    def add_participant(self, participant: str) -> None:
        """
        Add a participant to the training session.

        Parameters:
        ----------
        participant : str
            Name of the participant to add.
        """
        self.participants.append(participant)

    def get_session_info(self) -> Dict[str, Any]:
        """
        Retrieve information about the training session.

        Returns:
        -------
        Dict[str, Any]
            A dictionary containing the session details.
        """
        return {
            "title": self.title,
            "date": self.date.isoformat(),
            "duration_hours": self.duration_hours,
            "participants": self.participants,
        }

class TrainingOrganizer:
    """
    A class to organize training sessions for young leaders.
    
    Attributes:
    ----------
    sessions : List[TrainingSession]
        A list of training sessions organized.
    """
    
    def __init__(self):
        """Initialize the TrainingOrganizer with an empty session list."""
        self.sessions = []

    def create_session(self, title: str, date: str, duration_hours: int) -> None:
        """
        Create a new training session and add it to the organizer.

        Parameters:
        ----------
        title : str
            Title of the training session.
        date : str
            Date of the training session in 'YYYY-MM-DD' format.
        duration_hours : int
            Duration of the training session in hours.
        """
        try:
            session_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            session = TrainingSession(title, session_date, duration_hours)
            self.sessions.append(session)
        except ValueError as e:
            print(f"Error creating session: {e}. Please ensure the date format is 'YYYY-MM-DD'.")

    def list_sessions(self) -> List[Dict[str, Any]]:
        """
        List all organized training sessions.

        Returns:
        -------
        List[Dict[str, Any]]
            A list of dictionaries containing session details.
        """
        return [session.get_session_info() for session in self.sessions]

    def add_participant_to_session(self, title: str, participant: str) -> None:
        """
        Add a participant to a specific training session.

        Parameters:
        ----------
        title : str
            Title of the training session.
        participant : str
            Name of the participant to add.
        """
        for session in self.sessions:
            if session.title == title:
                session.add_participant(participant)
                return
        print(f"No session found with title: {title}")

# Example usage
if __name__ == "__main__":
    organizer = TrainingOrganizer()
    organizer.create_session("Leadership Skills Workshop", "2023-11-05", 2)
    organizer.add_participant_to_session("Leadership Skills Workshop", "Alice Johnson")
    organizer.add_participant_to_session("Leadership Skills Workshop", "Bob Smith")

    sessions_info = organizer.list_sessions()
    for session in sessions_info:
        print(session)
```
