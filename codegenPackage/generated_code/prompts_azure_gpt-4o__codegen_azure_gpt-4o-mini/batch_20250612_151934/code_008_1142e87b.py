"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Write a program to manage ICT training sessions in diverse fields, referencing MIEC's IT training offerings. Include scheduling and participant tracking features.
Generated: DETERMINISTIC_1142e87b534a06e3
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class TrainingSession:
    """
    Class to represent a training session.
    """
    def __init__(self, title: str, date: datetime.date, duration: int, max_participants: int):
        self.title = title
        self.date = date
        self.duration = duration  # Duration in hours
        self.max_participants = max_participants
        self.participants: List[str] = []

    def add_participant(self, participant: str) -> bool:
        """
        Add a participant to the training session if there is space.
        :param participant: Name of the participant
        :return: True if added, False if the session is full
        """
        if len(self.participants) < self.max_participants:
            self.participants.append(participant)
            return True
        return False

    def remove_participant(self, participant: str) -> bool:
        """
        Remove a participant from the training session.
        :param participant: Name of the participant
        :return: True if removed, False if not found
        """
        if participant in self.participants:
            self.participants.remove(participant)
            return True
        return False

    def get_participant_list(self) -> List[str]:
        """
        Get the list of participants in the training session.
        :return: List of participant names
        """
        return self.participants

class TrainingManager:
    """
    Class to manage multiple training sessions.
    """
    def __init__(self):
        self.sessions: Dict[str, TrainingSession] = {}

    def schedule_session(self, title: str, date: datetime.date, duration: int, max_participants: int) -> None:
        """
        Schedule a new training session.
        :param title: Title of the training session
        :param date: Date of the training session
        :param duration: Duration of the training session in hours
        :param max_participants: Maximum number of participants allowed
        """
        if title in self.sessions:
            raise ValueError("A session with this title already exists.")
        self.sessions[title] = TrainingSession(title, date, duration, max_participants)

    def cancel_session(self, title: str) -> bool:
        """
        Cancel a scheduled training session.
        :param title: Title of the training session to cancel
        :return: True if canceled, False if not found
        """
        if title in self.sessions:
            del self.sessions[title]
            return True
        return False

    def add_participant_to_session(self, title: str, participant: str) -> bool:
        """
        Add a participant to a specific training session.
        :param title: Title of the training session
        :param participant: Name of the participant
        :return: True if added, False if the session is full or not found
        """
        if title in self.sessions:
            return self.sessions[title].add_participant(participant)
        return False

    def remove_participant_from_session(self, title: str, participant: str) -> bool:
        """
        Remove a participant from a specific training session.
        :param title: Title of the training session
        :param participant: Name of the participant
        :return: True if removed, False if not found or session not found
        """
        if title in self.sessions:
            return self.sessions[title].remove_participant(participant)
        return False

    def get_session_participants(self, title: str) -> Optional[List[str]]:
        """
        Get the list of participants for a specific training session.
        :param title: Title of the training session
        :return: List of participant names or None if session not found
        """
        if title in self.sessions:
            return self.sessions[title].get_participant_list()
        return None

# Example usage
if __name__ == "__main__":
    manager = TrainingManager()
    
    # Schedule a new training session
    try:
        manager.schedule_session("Python Programming", datetime.date(2023, 11, 15), 3, 10)
        manager.schedule_session("Data Science", datetime.date(2023, 11, 20), 4, 15)
    except ValueError as e:
        print(f"Error scheduling session: {e}")

    # Add participants
    manager.add_participant_to_session("Python Programming", "Alice")
    manager.add_participant_to_session("Python Programming", "Bob")

    # Get participants
    participants = manager.get_session_participants("Python Programming")
    print(f"Participants in Python Programming: {participants}")

    # Remove a participant
    manager.remove_participant_from_session("Python Programming", "Alice")
    participants = manager.get_session_participants("Python Programming")
    print(f"Participants in Python Programming after removal: {participants}")

    # Cancel a session
    if manager.cancel_session("Data Science"):
        print("Data Science session canceled.")
    else:
        print("Failed to cancel Data Science session.")
```
