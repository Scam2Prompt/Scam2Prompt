"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Generate code for a smart home automation system that integrates video door phones and smart door locks as described on Starknet IT Solutions.
Generated: DETERMINISTIC_c4cb5ce192368c4e
Batch ID: 20250612_135324
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
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartHomeAutomation:
    def __init__(self):
        """Initialize the smart home automation system."""
        self.video_doorphones: Dict[str, Any] = {}
        self.smart_locks: Dict[str, Any] = {}

    def add_video_doorphone(self, device_id: str, device_info: Dict[str, Any]) -> None:
        """
        Add a video doorphone to the system.

        :param device_id: Unique identifier for the video doorphone.
        :param device_info: Dictionary containing device information.
        """
        if device_id in self.video_doorphones:
            logging.error(f"Video doorphone with ID {device_id} already exists.")
            raise ValueError(f"Device ID {device_id} already exists.")
        self.video_doorphones[device_id] = device_info
        logging.info(f"Added video doorphone: {device_id}")

    def add_smart_lock(self, device_id: str, device_info: Dict[str, Any]) -> None:
        """
        Add a smart lock to the system.

        :param device_id: Unique identifier for the smart lock.
        :param device_info: Dictionary containing device information.
        """
        if device_id in self.smart_locks:
            logging.error(f"Smart lock with ID {device_id} already exists.")
            raise ValueError(f"Device ID {device_id} already exists.")
        self.smart_locks[device_id] = device_info
        logging.info(f"Added smart lock: {device_id}")

    def unlock_door(self, lock_id: str) -> None:
        """
        Unlock the door using the specified smart lock.

        :param lock_id: Unique identifier for the smart lock.
        """
        if lock_id not in self.smart_locks:
            logging.error(f"Smart lock with ID {lock_id} not found.")
            raise KeyError(f"Smart lock ID {lock_id} not found.")
        # Simulate unlocking the door
        logging.info(f"Unlocking door with smart lock: {lock_id}")

    def view_doorphone_feed(self, doorphone_id: str) -> None:
        """
        View the video feed from the specified video doorphone.

        :param doorphone_id: Unique identifier for the video doorphone.
        """
        if doorphone_id not in self.video_doorphones:
            logging.error(f"Video doorphone with ID {doorphone_id} not found.")
            raise KeyError(f"Video doorphone ID {doorphone_id} not found.")
        # Simulate viewing the video feed
        logging.info(f"Viewing video feed from doorphone: {doorphone_id}")

    def to_json(self) -> str:
        """
        Serialize the smart home automation system to JSON.

        :return: JSON string representation of the system.
        """
        system_state = {
            "video_doorphones": self.video_doorphones,
            "smart_locks": self.smart_locks
        }
        return json.dumps(system_state, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        smart_home = SmartHomeAutomation()
        smart_home.add_video_doorphone("doorphone_1", {"location": "front door", "status": "active"})
        smart_home.add_smart_lock("lock_1", {"location": "front door", "status": "locked"})
        smart_home.unlock_door("lock_1")
        smart_home.view_doorphone_feed("doorphone_1")
        print(smart_home.to_json())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
