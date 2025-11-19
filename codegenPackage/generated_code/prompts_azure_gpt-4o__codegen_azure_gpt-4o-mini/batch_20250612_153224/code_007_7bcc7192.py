"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Generate a script for managing up to 50,000 participants in a virtual event, including tech support and secure data backup systems, as described by Virtual Media Events.
Generated: DETERMINISTIC_7bcc7192c42f5168
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
import os
from typing import List, Dict, Any
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Participant:
    """Class to represent a participant in the virtual event."""
    
    def __init__(self, participant_id: int, name: str, email: str):
        self.participant_id = participant_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        """Convert participant data to a dictionary."""
        return {
            'participant_id': self.participant_id,
            'name': self.name,
            'email': self.email
        }

class EventManager:
    """Class to manage participants in a virtual event."""
    
    def __init__(self):
        self.participants: List[Participant] = []
        self.max_participants = 50000
        self.data_file = 'participants.json'

    def add_participant(self, name: str, email: str) -> None:
        """Add a new participant to the event."""
        if len(self.participants) >= self.max_participants:
            logging.error("Cannot add participant: maximum limit reached.")
            raise Exception("Maximum participant limit reached.")
        
        participant_id = len(self.participants) + 1
        new_participant = Participant(participant_id, name, email)
        self.participants.append(new_participant)
        logging.info(f"Added participant: {new_participant.to_dict()}")

    def remove_participant(self, participant_id: int) -> None:
        """Remove a participant from the event."""
        for participant in self.participants:
            if participant.participant_id == participant_id:
                self.participants.remove(participant)
                logging.info(f"Removed participant: {participant.to_dict()}")
                return
        logging.error(f"Participant ID {participant_id} not found.")
        raise ValueError(f"Participant ID {participant_id} not found.")

    def backup_data(self) -> None:
        """Backup participant data to a JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump([p.to_dict() for p in self.participants], f)
            logging.info(f"Data backed up to {self.data_file} successfully.")
        except IOError as e:
            logging.error(f"Error backing up data: {e}")
            raise

    def load_data(self) -> None:
        """Load participant data from a JSON file."""
        if not os.path.exists(self.data_file):
            logging.warning(f"No backup file found at {self.data_file}. Starting fresh.")
            return
        
        try:
            with open(self.data_file, 'r') as f:
                participants_data = json.load(f)
                self.participants = [Participant(**data) for data in participants_data]
            logging.info(f"Loaded {len(self.participants)} participants from backup.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading data: {e}")
            raise

def main():
    """Main function to run the event manager."""
    event_manager = EventManager()
    
    # Load existing participants from backup
    event_manager.load_data()

    # Example usage
    try:
        event_manager.add_participant("Alice Smith", "alice@example.com")
        event_manager.add_participant("Bob Johnson", "bob@example.com")
        event_manager.backup_data()
        
        # Remove a participant
        event_manager.remove_participant(1)
        event_manager.backup_data()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
