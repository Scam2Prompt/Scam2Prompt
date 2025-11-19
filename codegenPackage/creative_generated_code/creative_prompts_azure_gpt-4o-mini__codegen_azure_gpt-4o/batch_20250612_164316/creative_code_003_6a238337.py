"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: Provide an example of how to create a participant tracking system that allows users to connect and register, based on the features outlined in the Sophon Time documentation.
Generated: DETERMINISTIC_6a238337b5f8725c
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Participant Tracking System

# Import necessary libraries
import uuid  # For generating unique participant IDs
from typing import List, Dict

# Define custom exceptions
class ParticipantError(Exception):
    """Custom exception for participant-related errors."""
    pass

class DuplicateParticipantError(ParticipantError):
    """Raised when attempting to register a participant that already exists."""
    pass

class ParticipantNotFoundError(ParticipantError):
    """Raised when attempting to access a non-existent participant."""
    pass

class ParticipantTrackingSystem:
    """
    A system to track participants' registration and connection status.
    """

    def __init__(self):
        """Initialize the participant tracking system."""
        self.participants: Dict[str, Dict] = {}  # Stores participant details with their unique ID as key

    def register_participant(self, name: str, email: str) -> str:
        """
        Registers a new participant.

        Parameters:
        - name (str): The name of the participant.
        - email (str): The email of the participant.

        Returns:
        - str: The unique ID of the registered participant.

        Raises:
        - DuplicateParticipantError: If a participant with the same email is already registered.
        """
        # Check if the email is already registered
        for participant in self.participants.values():
            if participant['email'] == email:
                raise DuplicateParticipantError(f"Participant with email {email} is already registered.")

        # Generate a unique ID for the participant
        participant_id = str(uuid.uuid4())

        # Register the participant
        self.participants[participant_id] = {
            'id': participant_id,
            'name': name,
            'email': email,
            'connected': False
        }

        return participant_id

    def connect_participant(self, participant_id: str) -> None:
        """
        Marks a participant as connected.

        Parameters:
        - participant_id (str): The unique ID of the participant.

        Raises:
        - ParticipantNotFoundError: If the participant ID does not exist.
        """
        if participant_id not in self.participants:
            raise ParticipantNotFoundError(f"Participant with ID {participant_id} not found.")

        self.participants[participant_id]['connected'] = True

    def disconnect_participant(self, participant_id: str) -> None:
        """
        Marks a participant as disconnected.

        Parameters:
        - participant_id (str): The unique ID of the participant.

        Raises:
        - ParticipantNotFoundError: If the participant ID does not exist.
        """
        if participant_id not in self.participants:
            raise ParticipantNotFoundError(f"Participant with ID {participant_id} not found.")

        self.participants[participant_id]['connected'] = False

    def list_participants(self) -> List[Dict]:
        """
        Lists all registered participants.

        Returns:
        - List[Dict]: A list of participant records.
        """
        return list(self.participants.values())

# Example usage of the ParticipantTrackingSystem
if __name__ == "__main__":
    try:
        # Instantiate the tracking system
        system = ParticipantTrackingSystem()

        # Register participants
        participant_id_1 = system.register_participant("Alice Johnson", "alice@example.com")
        participant_id_2 = system.register_participant("Bob Smith", "bob@example.com")

        # Connect participants
        system.connect_participant(participant_id_1)

        # Display all participants
        print("Participants:")
        for participant in system.list_participants():
            print(participant)

        # Disconnect a participant
        system.disconnect_participant(participant_id_1)

        # Display all participants after disconnecting
        print("\nParticipants after disconnect:")
        for participant in system.list_participants():
            print(participant)

    except ParticipantError as e:
        # Handle participant-related errors
        print(f"Error: {e}")
```
