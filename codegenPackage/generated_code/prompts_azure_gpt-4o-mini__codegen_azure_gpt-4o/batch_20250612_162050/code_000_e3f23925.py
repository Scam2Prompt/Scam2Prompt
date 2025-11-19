"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write a Python script that implements a basic structure for a Dialectical Behavior Therapy (DBT) program, including modules for individual therapy and group skills training.
Generated: DETERMINISTIC_e3f2392521fb05d9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Dialectical Behavior Therapy (DBT) Program Script
This script provides a basic structure for a DBT program, including modules for individual therapy
and group skills training. It is designed to be extensible and production-ready.
"""

import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("dbt_program.log"), logging.StreamHandler()]
)

class DBTProgram:
    """
    Main class for managing the DBT program.
    Includes individual therapy and group skills training modules.
    """
    def __init__(self):
        self.individual_sessions = []
        self.group_sessions = []
        logging.info("DBT Program initialized.")

    def add_individual_session(self, therapist, client, date, focus_area):
        """
        Add an individual therapy session to the program.
        :param therapist: Name of the therapist
        :param client: Name of the client
        :param date: Date of the session (YYYY-MM-DD)
        :param focus_area: Focus area of the session (e.g., emotion regulation)
        """
        try:
            session = IndividualTherapySession(therapist, client, date, focus_area)
            self.individual_sessions.append(session)
            logging.info(f"Added individual session: {session}")
        except ValueError as e:
            logging.error(f"Error adding individual session: {e}")

    def add_group_session(self, facilitator, topic, date, participants):
        """
        Add a group skills training session to the program.
        :param facilitator: Name of the facilitator
        :param topic: Topic of the session (e.g., mindfulness)
        :param date: Date of the session (YYYY-MM-DD)
        :param participants: List of participant names
        """
        try:
            session = GroupSkillsTrainingSession(facilitator, topic, date, participants)
            self.group_sessions.append(session)
            logging.info(f"Added group session: {session}")
        except ValueError as e:
            logging.error(f"Error adding group session: {e}")

    def list_sessions(self):
        """
        List all sessions in the DBT program.
        """
        logging.info("Listing all sessions...")
        print("\nIndividual Therapy Sessions:")
        for session in self.individual_sessions:
            print(session)
        print("\nGroup Skills Training Sessions:")
        for session in self.group_sessions:
            print(session)


class IndividualTherapySession:
    """
    Represents an individual therapy session.
    """
    def __init__(self, therapist, client, date, focus_area):
        self.therapist = therapist
        self.client = client
        self.date = self.validate_date(date)
        self.focus_area = focus_area

    def validate_date(self, date):
        """
        Validate the date format (YYYY-MM-DD).
        :param date: Date string
        :return: Validated date string
        :raises ValueError: If the date format is invalid
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def __str__(self):
        return f"Therapist: {self.therapist}, Client: {self.client}, Date: {self.date}, Focus Area: {self.focus_area}"


class GroupSkillsTrainingSession:
    """
    Represents a group skills training session.
    """
    def __init__(self, facilitator, topic, date, participants):
        self.facilitator = facilitator
        self.topic = topic
        self.date = self.validate_date(date)
        self.participants = self.validate_participants(participants)

    def validate_date(self, date):
        """
        Validate the date format (YYYY-MM-DD).
        :param date: Date string
        :return: Validated date string
        :raises ValueError: If the date format is invalid
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def validate_participants(self, participants):
        """
        Validate the participants list.
        :param participants: List of participant names
        :return: Validated participants list
        :raises ValueError: If the participants list is empty
        """
        if not participants or not isinstance(participants, list):
            raise ValueError("Participants must be a non-empty list.")
        return participants

    def __str__(self):
        return f"Facilitator: {self.facilitator}, Topic: {self.topic}, Date: {self.date}, Participants: {', '.join(self.participants)}"


# Example usage
if __name__ == "__main__":
    dbt_program = DBTProgram()

    # Add individual therapy sessions
    dbt_program.add_individual_session("Dr. Smith", "Alice", "2023-10-01", "Emotion Regulation")
    dbt_program.add_individual_session("Dr. Brown", "Bob", "2023-10-02", "Distress Tolerance")

    # Add group skills training sessions
    dbt_program.add_group_session("Ms. Johnson", "Mindfulness", "2023-10-03", ["Alice", "Bob", "Charlie"])
    dbt_program.add_group_session("Mr. Lee", "Interpersonal Effectiveness", "2023-10-04", ["Alice", "Charlie"])

    # List all sessions
    dbt_program.list_sessions()
```
