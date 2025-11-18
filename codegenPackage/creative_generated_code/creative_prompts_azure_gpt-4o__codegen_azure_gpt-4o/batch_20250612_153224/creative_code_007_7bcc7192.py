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
import threading
import logging
from datetime import datetime
import hashlib

# Constants
MAX_PARTICIPANTS = 50000
DATA_BACKUP_FILE = "participant_data_backup.json"
EVENT_LOG_FILE = "event_logs.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(EVENT_LOG_FILE),
        logging.StreamHandler(),
    ],
)

# Participant management system
class VirtualEventManager:
    def __init__(self):
        self.participants = {}
        self.lock = threading.Lock()  # Ensures thread safety for participant data

    def add_participant(self, participant_id, name, email):
        """
        Adds a participant to the system.
        :param participant_id: Unique identifier for the participant
        :param name: Participant's full name
        :param email: Participant's email
        """
        self.lock.acquire()
        try:
            if len(self.participants) >= MAX_PARTICIPANTS:
                raise ValueError("Maximum participant capacity reached.")
            if participant_id in self.participants:
                raise ValueError(f"Participant with ID {participant_id} already exists.")

            self.participants[participant_id] = {
                "name": name,
                "email": email,
                "registration_time": datetime.utcnow().isoformat(),
            }
            logging.info(f"Participant {participant_id} added successfully.")
        except Exception as e:
            logging.error(f"Failed to add participant: {e}")
        finally:
            self.lock.release()

    def remove_participant(self, participant_id):
        """
        Removes a participant from the system.
        :param participant_id: Unique identifier for the participant
        """
        self.lock.acquire()
        try:
            if participant_id not in self.participants:
                raise ValueError(f"Participant with ID {participant_id} does not exist.")

            del self.participants[participant_id]
            logging.info(f"Participant {participant_id} removed successfully.")
        except Exception as e:
            logging.error(f"Failed to remove participant: {e}")
        finally:
            self.lock.release()

    def list_participants(self):
        """
        Lists all participants in the system.
        :return: A dictionary of all participants
        """
        self.lock.acquire()
        try:
            return self.participants.copy()
        finally:
            self.lock.release()

    def backup_data(self):
        """
        Backs up participant data to a secure file.
        """
        self.lock.acquire()
        try:
            with open(DATA_BACKUP_FILE, "w") as backup_file:
                json.dump(self.participants, backup_file, indent=4)
            logging.info("Participant data backed up successfully.")
        except Exception as e:
            logging.error(f"Failed to back up data: {e}")
        finally:
            self.lock.release()

    def restore_data(self):
        """
        Restores participant data from a backup file.
        """
        self.lock.acquire()
        try:
            if not os.path.exists(DATA_BACKUP_FILE):
                raise FileNotFoundError("Backup file does not exist.")

            with open(DATA_BACKUP_FILE, "r") as backup_file:
                self.participants = json.load(backup_file)
            logging.info("Participant data restored successfully.")
        except Exception as e:
            logging.error(f"Failed to restore data: {e}")
        finally:
            self.lock.release()


# Tech support system
def encrypt_data(data):
    """
    Encrypts data using SHA256 (for demonstration purposes).
    :param data: The data to encrypt
    :return: Encrypted data
    """
    return hashlib.sha256(data.encode()).hexdigest()


def provide_tech_support(issue_description):
    """
    Simulates providing tech support for a participant.
    :param issue_description: Description of the issue
    """
    try:
        logging.info(f"Tech support initiated for issue: {issue_description}")
        # Simulate issue resolution
        logging.info("Issue resolved.")
    except Exception as e:
        logging.error(f"Tech support failed: {e}")


# Main script execution
if __name__ == "__main__":
    event_manager = VirtualEventManager()

    # Example usage
    event_manager.add_participant("12345", "Alice Johnson", "alice@example.com")
    event_manager.add_participant("67890", "Bob Smith", "bob@example.com")

    event_manager.backup_data()
    all_participants = event_manager.list_participants()
    logging.info(f"Current Participants: {all_participants}")

    provide_tech_support("Cannot access event link.")
    event_manager.restore_data()
    logging.info(f"Data after restoration: {event_manager.list_participants()}")
```
