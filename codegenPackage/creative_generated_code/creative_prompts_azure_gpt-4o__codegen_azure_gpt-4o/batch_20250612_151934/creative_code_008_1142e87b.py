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
    Class to represent a training session.
    """
    def __init__(self, title, field, date, max_participants):
        self.title = title
        self.field = field
        self.date = date
        self.max_participants = max_participants
        self.participants = []  # List to store participant names

    def add_participant(self, participant_name):
        """
        Add a participant to the training session.
        """
        if len(self.participants) >= self.max_participants:
            raise ValueError("Session is full. Cannot add more participants.")
        if participant_name in self.participants:
            raise ValueError("Participant is already registered.")
        self.participants.append(participant_name)

    def remove_participant(self, participant_name):
        """
        Remove a participant from the training session.
        """
        if participant_name not in self.participants:
            raise ValueError("Participant not found.")
        self.participants.remove(participant_name)

    def get_participant_list(self):
        """
        Get the list of participants for the session.
        """
        return self.participants

    def __str__(self):
        """
        String representation of the training session.
        """
        return f"Title: {self.title}, Field: {self.field}, Date: {self.date}, " \
               f"Max Participants: {self.max_participants}, Current Participants: {len(self.participants)}"

class TrainingManager:
    """
    Class to manage multiple training sessions.
    """
    def __init__(self):
        self.sessions = []  # List to store training sessions

    def create_session(self, title, field, date, max_participants):
        """
        Create a new training session.
        """
        try:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            new_session = TrainingSession(title, field, date_obj, max_participants)
            self.sessions.append(new_session)
            return new_session
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. {e}")

    def list_sessions(self):
        """
        List all training sessions.
        """
        return self.sessions

    def find_session_by_title(self, title):
        """
        Find a session by its title.
        """
        for session in self.sessions:
            if session.title == title:
                return session
        raise ValueError(f"No session found with title '{title}'.")

    def delete_session(self, title):
        """
        Delete a session by its title.
        """
        session = self.find_session_by_title(title)
        self.sessions.remove(session)

# Example Usage
if __name__ == "__main__":
    try:
        manager = TrainingManager()

        # Create training sessions
        session1 = manager.create_session("Python Basics", "Programming", "2023-11-01", 20)
        session2 = manager.create_session("Data Analysis with Python", "Data Science", "2023-11-15", 15)

        # Add participants
        session1.add_participant("Alice")
        session1.add_participant("Bob")

        session2.add_participant("Charlie")

        # List sessions
        for session in manager.list_sessions():
            print(session)

        # Find a session
        found_session = manager.find_session_by_title("Python Basics")
        print(f"Found Session: {found_session}")

        # Remove a participant
        found_session.remove_participant("Alice")

        # Delete a session
        manager.delete_session("Data Analysis with Python")

        # List sessions after deletion
        for session in manager.list_sessions():
            print(session)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
