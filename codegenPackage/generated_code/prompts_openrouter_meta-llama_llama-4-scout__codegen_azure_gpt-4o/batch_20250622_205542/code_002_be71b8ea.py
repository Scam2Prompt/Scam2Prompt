"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: "Design a training program for women leaders in effective advocacy and entrepreneurship, specifically in the context of briquettes production in Kenya."
Generated: DETERMINISTIC_be71b8ea6083d5be
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program: Women Leaders Training Program for Advocacy and Entrepreneurship
Context: Briquettes Production in Kenya
Description: This program manages training sessions, tracks participants, and provides resources for women leaders.
Language: Python
"""

import datetime

# Define a class for participants
class Participant:
    def __init__(self, name, age, location, contact):
        """
        Initialize a participant with basic details.
        :param name: Full name of the participant
        :param age: Age of the participant
        :param location: Location of the participant
        :param contact: Contact information (email or phone)
        """
        self.name = name
        self.age = age
        self.location = location
        self.contact = contact

    def __str__(self):
        """
        String representation of a participant.
        """
        return f"Name: {self.name}, Age: {self.age}, Location: {self.location}, Contact: {self.contact}"


# Define a class for training sessions
class TrainingSession:
    def __init__(self, topic, date, location, trainer):
        """
        Initialize a training session with details.
        :param topic: Topic of the training session
        :param date: Date of the training session
        :param location: Location of the training session
        :param trainer: Trainer conducting the session
        """
        self.topic = topic
        self.date = date
        self.location = location
        self.trainer = trainer
        self.participants = []

    def add_participant(self, participant):
        """
        Add a participant to the training session.
        :param participant: Instance of Participant class
        """
        if isinstance(participant, Participant):
            self.participants.append(participant)
        else:
            raise ValueError("Invalid participant. Must be an instance of Participant class.")

    def list_participants(self):
        """
        List all participants in the training session.
        """
        return [str(p) for p in self.participants]

    def __str__(self):
        """
        String representation of a training session.
        """
        return f"Topic: {self.topic}, Date: {self.date}, Location: {self.location}, Trainer: {self.trainer}"


# Define a class for the training program
class TrainingProgram:
    def __init__(self, name, description):
        """
        Initialize the training program.
        :param name: Name of the training program
        :param description: Description of the training program
        """
        self.name = name
        self.description = description
        self.sessions = []

    def add_session(self, session):
        """
        Add a training session to the program.
        :param session: Instance of TrainingSession class
        """
        if isinstance(session, TrainingSession):
            self.sessions.append(session)
        else:
            raise ValueError("Invalid session. Must be an instance of TrainingSession class.")

    def list_sessions(self):
        """
        List all sessions in the training program.
        """
        return [str(s) for s in self.sessions]

    def __str__(self):
        """
        String representation of the training program.
        """
        return f"Program Name: {self.name}, Description: {self.description}"


# Main function to demonstrate the program functionality
def main():
    try:
        # Create a training program
        program = TrainingProgram(
            name="Women Leaders Advocacy and Entrepreneurship Training",
            description="Empowering women leaders in Kenya to excel in briquettes production."
        )

        # Create training sessions
        session1 = TrainingSession(
            topic="Effective Advocacy Strategies",
            date=datetime.date(2023, 11, 15),
            location="Nairobi, Kenya",
            trainer="Dr. Jane Doe"
        )

        session2 = TrainingSession(
            topic="Entrepreneurship in Briquettes Production",
            date=datetime.date(2023, 11, 16),
            location="Mombasa, Kenya",
            trainer="Mr. John Smith"
        )

        # Add sessions to the program
        program.add_session(session1)
        program.add_session(session2)

        # Create participants
        participant1 = Participant(name="Alice Wanjiku", age=35, location="Nairobi", contact="alice@example.com")
        participant2 = Participant(name="Beatrice Kamau", age=40, location="Mombasa", contact="beatrice@example.com")

        # Add participants to sessions
        session1.add_participant(participant1)
        session2.add_participant(participant2)

        # Display program details
        print(program)
        print("\nTraining Sessions:")
        for session in program.list_sessions():
            print(session)

        print("\nParticipants in Session 1:")
        for participant in session1.list_participants():
            print(participant)

        print("\nParticipants in Session 2:")
        for participant in session2.list_participants():
            print(participant)

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
