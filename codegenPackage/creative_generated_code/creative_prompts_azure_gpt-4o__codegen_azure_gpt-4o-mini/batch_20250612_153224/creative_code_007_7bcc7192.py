"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Generate a script for managing up to 50,000 participants in a virtual event, including tech support and secure data backup systems, as described by Virtual Media Events.
Generated: DETERMINISTIC_7bcc7192c42f5168
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import logging
from typing import List, Dict, Any
from datetime import datetime
from shutil import copyfile

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EventManager:
    """Class for managing participants in a virtual event."""

    def __init__(self, event_name: str):
        """Initialize the EventManager with an event name."""
        self.event_name = event_name
        self.participants = {}
        self.max_participants = 50000
        self.backup_file = f"{self.event_name}_backup.json"

    def add_participant(self, participant_id: str, participant_info: Dict[str, Any]) -> None:
        """Add a participant to the event."""
        try:
            if len(self.participants) >= self.max_participants:
                raise ValueError("Maximum number of participants reached.")
            if participant_id in self.participants:
                raise ValueError("Participant with this ID already exists.")
            self.participants[participant_id] = participant_info
            logging.info(f"Participant {participant_id} added successfully.")
        except Exception as e:
            logging.error(f"Error adding participant: {e}")

    def remove_participant(self, participant_id: str) -> None:
        """Remove a participant from the event."""
        try:
            if participant_id not in self.participants:
                raise ValueError("Participant not found.")
            del self.participants[participant_id]
            logging.info(f"Participant {participant_id} removed successfully.")
        except Exception as e:
            logging.error(f"Error removing participant: {e}")

    def list_participants(self) -> List[Dict[str, Any]]:
        """Return a list of all participants."""
        return list(self.participants.values())

    def backup_data(self) -> None:
        """Backup participant data to a JSON file."""
        try:
            with open(self.backup_file, 'w') as backup:
                json.dump(self.participants, backup)
            logging.info("Data backed up successfully.")
        except IOError as e:
            logging.error(f"Error backing up data: {e}")

    def restore_data(self) -> None:
        """Restore participant data from a JSON file."""
        try:
            if not os.path.exists(self.backup_file):
                raise FileNotFoundError("Backup file does not exist.")
            with open(self.backup_file, 'r') as backup:
                self.participants = json.load(backup)
            logging.info("Data restored successfully.")
        except Exception as e:
            logging.error(f"Error restoring data: {e}")

# Example usage
if __name__ == "__main__":
    event_manager = EventManager("Virtual Media Conference")
    
    # Adding participants
    event_manager.add_participant("001", {"name": "Alice", "email": "alice@example.com"})
    event_manager.add_participant("002", {"name": "Bob", "email": "bob@example.com"})
    
    # Listing participants
    participants_list = event_manager.list_participants()
    print("Current Participants:", participants_list)

    # Backing up data
    event_manager.backup_data()
    
    # Removing a participant
    event_manager.remove_participant("001")
    
    # Restoring data
    event_manager.restore_data()
```
