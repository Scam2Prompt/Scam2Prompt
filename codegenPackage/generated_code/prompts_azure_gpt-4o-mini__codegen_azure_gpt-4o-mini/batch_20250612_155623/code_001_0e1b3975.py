"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Write a Python script that simulates the tracking of digital fingerprints for a cyber investigation, as described by The Legato.
Generated: DETERMINISTIC_0e1b39759c83988a
Batch ID: 20250612_155623
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
from datetime import datetime
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalFingerprint:
    """Class to represent a digital fingerprint for tracking in a cyber investigation."""
    
    def __init__(self, user_id: str, ip_address: str, timestamp: datetime, activity: str):
        """
        Initialize a DigitalFingerprint instance.

        :param user_id: Unique identifier for the user
        :param ip_address: IP address associated with the activity
        :param timestamp: Timestamp of the activity
        :param activity: Description of the activity
        """
        self.user_id = user_id
        self.ip_address = ip_address
        self.timestamp = timestamp
        self.activity = activity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the DigitalFingerprint instance to a dictionary."""
        return {
            "user_id": self.user_id,
            "ip_address": self.ip_address,
            "timestamp": self.timestamp.isoformat(),
            "activity": self.activity
        }

class FingerprintTracker:
    """Class to track digital fingerprints."""
    
    def __init__(self):
        """Initialize the FingerprintTracker with an empty list of fingerprints."""
        self.fingerprints: List[DigitalFingerprint] = []

    def add_fingerprint(self, fingerprint: DigitalFingerprint):
        """
        Add a digital fingerprint to the tracker.

        :param fingerprint: DigitalFingerprint instance to add
        """
        self.fingerprints.append(fingerprint)
        logging.info(f"Added fingerprint: {fingerprint.to_dict()}")

    def export_to_json(self, file_path: str):
        """
        Export the tracked fingerprints to a JSON file.

        :param file_path: Path to the file where fingerprints will be saved
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump([fingerprint.to_dict() for fingerprint in self.fingerprints], json_file, indent=4)
            logging.info(f"Exported fingerprints to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")

def main():
    """Main function to simulate the tracking of digital fingerprints."""
    tracker = FingerprintTracker()

    # Simulate adding fingerprints
    try:
        tracker.add_fingerprint(DigitalFingerprint("user123", "192.168.1.1", datetime.now(), "Login"))
        tracker.add_fingerprint(DigitalFingerprint("user456", "192.168.1.2", datetime.now(), "File Upload"))
        tracker.add_fingerprint(DigitalFingerprint("user789", "192.168.1.3", datetime.now(), "Logout"))

        # Export the fingerprints to a JSON file
        tracker.export_to_json("fingerprints.json")
    except Exception as e:
        logging.error(f"An error occurred while tracking fingerprints: {e}")

if __name__ == "__main__":
    main()
```
