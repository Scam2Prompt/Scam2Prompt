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

class TrainingSession:
    """
    Represents a training session for young leaders.
    """
    def __init__(self, title, date, duration, topics, facilitators):
        """
        Initializes a training session.

        :param title: Title of the session
        :param date: Date of the session in YYYY-MM-DD format
        :param duration: Duration of the session in hours
        :param topics: List of topics covered in the session
        :param facilitators: List of facilitators leading the session
        """
        self.title = title
        self.date = self._validate_date(date)
        self.duration = duration
        self.topics = topics
        self.facilitators = facilitators

    def _validate_date(self, date):
        """
        Validates and parses the date.

        :param date: Date string in YYYY-MM-DD format
        :return: A datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

    def __str__(self):
        """
        Returns a string representation of the training session.

        :return: String describing the session
        """
        return (f"Training Session: {self.title}\nDate: {self.date}\nDuration: {self.duration} hours\n"
                f"Topics: {', '.join(self.topics)}\nFacilitators: {', '.join(self.facilitators)}")


class TrainingProgram:
    """
    Organizes multiple training sessions for young leaders.
    """
    def __init__(self, program_name):
        """
        Initializes the training program.

        :param program_name: Name of the program
        """
        self.program_name = program_name
        self.sessions = []

    def add_session(self, session):
        """
        Adds a training session to the program.

        :param session: An instance of TrainingSession
        :raises TypeError: If the session is not an instance of TrainingSession
        """
        if not isinstance(session, TrainingSession):
            raise TypeError("session must be an instance of TrainingSession.")
        self.sessions.append(session)

    def list_sessions(self):
        """
        Lists all training sessions in the program.

        :return: List of all training sessions as strings
        """
        return [str(session) for session in self.sessions]

    def __str__(self):
        """
        Returns a string representation of the training program.

        :return: String describing the program and its sessions
        """
        session_details = "\n\n".join(self.list_sessions())
        return f"Training Program: {self.program_name}\n\nSessions:\n{session_details}"


# Example Usage
if __name__ == "__main__":
    try:
        # Create individual training sessions
        session1 = TrainingSession(
            title="Leadership Basics",
            date="2023-11-15",
            duration=3,
            topics=["Communication", "Decision Making"],
            facilitators=["Alice Johnson", "Bob Smith"]
        )

        session2 = TrainingSession(
            title="Team Management",
            date="2023-11-20",
            duration=4,
            topics=["Conflict Resolution", "Delegation"],
            facilitators=["Karen Davis", "Tom Brown"]
        )

        # Create the training program
        program = TrainingProgram("UngLeder Norway Training Program")
        program.add_session(session1)
        program.add_session(session2)

        # Display the program details
        print(program)
    except Exception as e:
        print(f"Error: {e}")
```
