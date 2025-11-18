"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Write a program to manage ICT training sessions in diverse fields, referencing MIEC's IT training offerings. Include scheduling and participant tracking features.
Generated: DETERMINISTIC_1142e87b534a06e3
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TrainingSession:
    """
    A class to represent a training session.

    Attributes:
        title (str): Title of the training session.
        field (str): Area of ICT the training session covers.
        date (datetime.date): Date of the training session.
        start_time (datetime.time): Start time of the training session.
        end_time (datetime.time): End time of the training session.
        participants (list): List of participants registered for the session.
    """

    def __init__(self, title, field, date, start_time, end_time):
        self.title = title
        self.field = field
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.participants = []

    def add_participant(self, participant):
        """
        Adds a participant to the training session.

        Args:
            participant (str): Name of the participant.

        Raises:
            ValueError: If the participant is already registered.
        """
        if participant in self.participants:
            raise ValueError(f"{participant} is already registered for this session.")
        self.participants.append(participant)

    def remove_participant(self, participant):
        """
        Removes a participant from the training session.

        Args:
            participant (str): Name of the participant.

        Raises:
            ValueError: If the participant is not found.
        """
        if participant not in self.participants:
            raise ValueError(f"{participant} is not registered for this session.")
        self.participants.remove(participant)

    def get_participant_list(self):
        """
        Returns the list of participants registered for the session.

        Returns:
            list: List of participant names.
        """
        return self.participants

    def __str__(self):
        return f"{self.title} ({self.field}) on {self.date} from {self.start_time} to {self.end_time}"


class TrainingManager:
    """
    A class to manage multiple training sessions.

    Attributes:
        sessions (list): List of training sessions.
    """

    def __init__(self):
        self.sessions = []

    def schedule_session(self, title, field, date, start_time, end_time):
        """
        Schedules a new training session.

        Args:
            title (str): Title of the session.
            field (str): Area of ICT the training session covers.
            date (datetime.date): Date of the training session.
            start_time (datetime.time): Start time of the training session.
            end_time (datetime.time): End time of the training session.
        """
        session = TrainingSession(title, field, date, start_time, end_time)
        self.sessions.append(session)
        print(f"Session '{title}' scheduled successfully.")

    def get_sessions(self):
        """
        Returns the list of scheduled training sessions.

        Returns:
            list: List of scheduled sessions.
        """
        return self.sessions

    def find_session_by_title(self, title):
        """
        Finds a session by its title.

        Args:
            title (str): Title of the session to find.

        Returns:
            TrainingSession: The matching session.

        Raises:
            ValueError: If the session is not found.
        """
        for session in self.sessions:
            if session.title == title:
                return session
        raise ValueError(f"No session found with title '{title}'.")


# Example usage
if __name__ == "__main__":
    manager = TrainingManager()
    
    # Scheduling sessions
    try:
        manager.schedule_session("Python Basics", "Programming", datetime.date(2023, 12, 1), 
                                 datetime.time(9, 0), datetime.time(12, 0))
        manager.schedule_session("Data Science with Python", "Data Science", datetime.date(2023, 12, 3), 
                                 datetime.time(10, 0), datetime.time(16, 0))

        # Adding participants
        session = manager.find_session_by_title("Python Basics")
        session.add_participant("Alice Johnson")
        session.add_participant("Bob Smith")

        print(f"Participants for '{session.title}': {session.get_participant_list()}")

    except ValueError as e:
        print(f"Error: {e}")
```
