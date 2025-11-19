"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Generate a code snippet for a training management system that tracks the training progress of security personnel, inspired by Mando Security's Training Academy offerings.
Generated: DETERMINISTIC_70f3442ab71f8c64
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_management_system.py

class TrainingSession:
    """
    Represents a training session for security personnel.
    """
    def __init__(self, title, duration, date):
        self.title = title  # Title of the training session
        self.duration = duration  # Duration in hours
        self.date = date  # Date of the training session
        self.participants = []  # List to hold participants

    def add_participant(self, participant):
        """
        Adds a participant to the training session.
        
        :param participant: A dictionary containing participant details
        """
        if not isinstance(participant, dict):
            raise ValueError("Participant must be a dictionary.")
        self.participants.append(participant)

    def get_participant_list(self):
        """
        Returns the list of participants in the training session.
        
        :return: List of participants
        """
        return self.participants


class Personnel:
    """
    Represents a security personnel member.
    """
    def __init__(self, name, id_number):
        self.name = name  # Name of the personnel
        self.id_number = id_number  # Unique ID for the personnel
        self.training_records = []  # List to hold training records

    def enroll_in_training(self, training_session):
        """
        Enrolls the personnel in a training session.
        
        :param training_session: An instance of TrainingSession
        """
        if not isinstance(training_session, TrainingSession):
            raise ValueError("Invalid training session.")
        training_session.add_participant({'name': self.name, 'id_number': self.id_number})
        self.training_records.append(training_session)

    def get_training_progress(self):
        """
        Returns the training progress of the personnel.
        
        :return: List of training sessions attended
        """
        return [session.title for session in self.training_records]


def main():
    """
    Main function to demonstrate the training management system.
    """
    try:
        # Create training sessions
        session1 = TrainingSession("Basic Security Training", 8, "2023-11-01")
        session2 = TrainingSession("Advanced Surveillance Techniques", 6, "2023-11-15")

        # Create personnel
        personnel1 = Personnel("John Doe", "ID001")
        personnel2 = Personnel("Jane Smith", "ID002")

        # Enroll personnel in training sessions
        personnel1.enroll_in_training(session1)
        personnel1.enroll_in_training(session2)
        personnel2.enroll_in_training(session1)

        # Display training progress
        print(f"{personnel1.name}'s Training Progress: {personnel1.get_training_progress()}")
        print(f"{personnel2.name}'s Training Progress: {personnel2.get_training_progress()}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
