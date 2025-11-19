"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Write a Python script that simulates the tracking of digital fingerprints for a cyber investigation, as described by The Legato.
Generated: DETERMINISTIC_0e1b39759c83988a
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import os
from datetime import datetime
from typing import List, Dict, Any

class DigitalFingerprintTracker:
    """
    A class to track digital fingerprints for cyber investigations.
    Each fingerprint includes a unique hash, the time of creation, and associated metadata.
    """

    def __init__(self, storage_file: str):
        """
        Initializes the DigitalFingerprintTracker with the specified storage file.
        
        Args:
            storage_file (str): The path to the JSON file where fingerprints are stored.
        """
        self.storage_file = storage_file
        self.fingerprints = self.load_fingerprints()

    def load_fingerprints(self) -> Dict[str, Any]:
        """
        Loads fingerprints from the storage file.
        
        Returns:
            Dict[str, Any]: A dictionary of fingerprints.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_fingerprints(self) -> None:
        """
        Saves the current fingerprints to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.fingerprints, file, indent=4)

    def generate_fingerprint(self, data: str) -> str:
        """
        Generates a SHA-256 hash (fingerprint) from the given data.
        
        Args:
            data (str): The data to generate a fingerprint from.

        Returns:
            str: The generated fingerprint (hash).
        """
        return hashlib.sha256(data.encode()).hexdigest()

    def add_fingerprint(self, data: str, metadata: Dict[str, Any]) -> None:
        """
        Adds a new fingerprint with associated metadata to the tracker.
        
        Args:
            data (str): The data to create a fingerprint from.
            metadata (Dict[str, Any]): Additional metadata related to the fingerprint.

        Raises:
            ValueError: If the fingerprint already exists.
        """
        fingerprint = self.generate_fingerprint(data)
        if fingerprint in self.fingerprints:
            raise ValueError(f"Fingerprint {fingerprint} already exists.")
        
        self.fingerprints[fingerprint] = {
            'created_at': datetime.utcnow().isoformat(),
            'metadata': metadata
        }
        self.save_fingerprints()

    def get_fingerprint(self, fingerprint: str) -> Dict[str, Any]:
        """
        Retrieves the metadata associated with a given fingerprint.
        
        Args:
            fingerprint (str): The fingerprint to search for.

        Returns:
            Dict[str, Any]: The metadata associated with the fingerprint.

        Raises:
            KeyError: If the fingerprint does not exist.
        """
        if fingerprint not in self.fingerprints:
            raise KeyError(f"Fingerprint {fingerprint} not found.")
        
        return self.fingerprints[fingerprint]

    def remove_fingerprint(self, fingerprint: str) -> None:
        """
        Removes a fingerprint from the tracker.
        
        Args:
            fingerprint (str): The fingerprint to be removed.

        Raises:
            KeyError: If the fingerprint does not exist.
        """
        if fingerprint not in self.fingerprints:
            raise KeyError(f"Fingerprint {fingerprint} not found.")
        
        del self.fingerprints[fingerprint]
        self.save_fingerprints()

def main():
    # Example usage of the DigitalFingerprintTracker
    tracker = DigitalFingerprintTracker("fingerprints.json")
    
    # Adding a fingerprint
    try:
        tracker.add_fingerprint("user@example.com", {"user_id": 123, "session": "login"})
        print("Fingerprint added successfully.")
    except ValueError as e:
        print(e)

    # Retrieving a fingerprint
    try:
        fingerprint = tracker.generate_fingerprint("user@example.com")
        metadata = tracker.get_fingerprint(fingerprint)
        print("Retrieved metadata:", metadata)
    except KeyError as e:
        print(e)

    # Removing a fingerprint
    try:
        fingerprint = tracker.generate_fingerprint("user@example.com")
        tracker.remove_fingerprint(fingerprint)
        print("Fingerprint removed successfully.")
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()
```
