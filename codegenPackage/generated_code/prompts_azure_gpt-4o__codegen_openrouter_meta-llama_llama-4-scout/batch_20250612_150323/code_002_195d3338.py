"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Generate code to create a client management system for tracking progress in OSI-type coaching, including features for family, couples, and executive coaching.
Generated: DETERMINISTIC_195d3338d996f094
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_management_system.py

from enum import Enum
from typing import List, Dict

class CoachingType(str, Enum):
    """Enum for coaching types."""
    FAMILY = "family"
    COUPLES = "couples"
    EXECUTIVE = "executive"

class Client:
    """Represents a client in the coaching system."""
    
    def __init__(self, client_id: int, name: str, coaching_type: CoachingType):
        """
        Initializes a Client object.

        Args:
        - client_id (int): Unique identifier for the client.
        - name (str): Name of the client.
        - coaching_type (CoachingType): Type of coaching.
        """
        self.client_id = client_id
        self.name = name
        self.coaching_type = coaching_type
        self.progress_notes = []

    def add_progress_note(self, note: str):
        """Adds a progress note for the client."""
        self.progress_notes.append(note)

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Coaching Type: {self.coaching_type.value}"

class ClientManagementSystem:
    """Manages clients and their progress in the coaching system."""
    
    def __init__(self):
        self.clients: Dict[int, Client] = {}
        self.client_id_counter = 1

    def create_client(self, name: str, coaching_type: CoachingType) -> Client:
        """
        Creates a new client.

        Args:
        - name (str): Name of the client.
        - coaching_type (CoachingType): Type of coaching.

        Returns:
        - Client: The newly created client.
        """
        client = Client(self.client_id_counter, name, coaching_type)
        self.clients[self.client_id_counter] = client
        self.client_id_counter += 1
        return client

    def get_client(self, client_id: int) -> Client:
        """
        Retrieves a client by their ID.

        Args:
        - client_id (int): ID of the client.

        Returns:
        - Client: The client with the specified ID, or None if not found.
        """
        return self.clients.get(client_id)

    def add_progress_note(self, client_id: int, note: str):
        """
        Adds a progress note for a client.

        Args:
        - client_id (int): ID of the client.
        - note (str): Progress note.

        Raises:
        - ValueError: If the client ID is not found.
        """
        client = self.get_client(client_id)
        if client:
            client.add_progress_note(note)
        else:
            raise ValueError("Client ID not found")

    def __str__(self):
        client_list = "\n".join([str(client) for client in self.clients.values()])
        return f"Client Management System:\n{client_list}"

def main():
    # Create a client management system
    cms = ClientManagementSystem()

    # Create clients
    family_client = cms.create_client("John Doe", CoachingType.FAMILY)
    couples_client = cms.create_client("Jane Smith", CoachingType.COUPLES)
    executive_client = cms.create_client("Bob Johnson", CoachingType.EXECUTIVE)

    # Add progress notes
    cms.add_progress_note(family_client.client_id, "First session completed")
    cms.add_progress_note(couples_client.client_id, "Couples therapy started")
    cms.add_progress_note(executive_client.client_id, "Executive coaching goals set")

    # Print client list
    print(cms)

    # Print client details
    print("\nClient Details:")
    for client_id, client in cms.clients.items():
        print(client)
        print("Progress Notes:")
        for note in client.progress_notes:
            print(note)
        print()

if __name__ == "__main__":
    main()
```
