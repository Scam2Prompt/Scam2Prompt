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
import hashlib
import os
import json
from datetime import datetime

class DigitalFingerprintTracker:
    """
    A class to simulate the tracking of digital fingerprints for a cyber investigation.
    """

    def __init__(self, storage_file="fingerprints.json"):
        """
        Initializes the tracker with a storage file for fingerprints.

        :param storage_file: Path to the file where fingerprints will be stored.
        """
        self.storage_file = storage_file
        self.fingerprints = {}
        self._load_fingerprints()

    def _load_fingerprints(self):
        """
        Loads existing fingerprints from the storage file.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as file:
                    self.fingerprints = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading fingerprints: {e}")
                self.fingerprints = {}

    def _save_fingerprints(self):
        """
        Saves the current fingerprints to the storage file.
        """
        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.fingerprints, file, indent=4)
        except IOError as e:
            print(f"Error saving fingerprints: {e}")

    def generate_fingerprint(self, data):
        """
        Generates a digital fingerprint (SHA-256 hash) for the given data.

        :param data: The data to hash (string).
        :return: The generated fingerprint (hexadecimal string).
        """
        if not isinstance(data, str):
            raise ValueError("Data must be a string.")
        return hashlib.sha256(data.encode()).hexdigest()

    def add_fingerprint(self, identifier, data):
        """
        Adds a new fingerprint to the tracker.

        :param identifier: A unique identifier for the fingerprint (e.g., file name, user ID).
        :param data: The data to generate the fingerprint from.
        """
        fingerprint = self.generate_fingerprint(data)
        timestamp = datetime.now().isoformat()
        self.fingerprints[identifier] = {
            "fingerprint": fingerprint,
            "timestamp": timestamp
        }
        self._save_fingerprints()

    def verify_fingerprint(self, identifier, data):
        """
        Verifies if the fingerprint for the given identifier matches the provided data.

        :param identifier: The unique identifier for the fingerprint.
        :param data: The data to verify against the stored fingerprint.
        :return: True if the fingerprint matches, False otherwise.
        """
        if identifier not in self.fingerprints:
            raise KeyError(f"No fingerprint found for identifier: {identifier}")
        stored_fingerprint = self.fingerprints[identifier]["fingerprint"]
        generated_fingerprint = self.generate_fingerprint(data)
        return stored_fingerprint == generated_fingerprint

    def list_fingerprints(self):
        """
        Lists all stored fingerprints.

        :return: A dictionary of fingerprints with their identifiers and timestamps.
        """
        return self.fingerprints


# Example usage
if __name__ == "__main__":
    tracker = DigitalFingerprintTracker()

    # Add fingerprints
    tracker.add_fingerprint("file1.txt", "This is the content of file1.")
    tracker.add_fingerprint("file2.txt", "This is the content of file2.")

    # Verify fingerprints
    try:
        is_valid = tracker.verify_fingerprint("file1.txt", "This is the content of file1.")
        print(f"Verification for 'file1.txt': {is_valid}")
    except KeyError as e:
        print(e)

    # List all fingerprints
    print("Stored fingerprints:")
    print(json.dumps(tracker.list_fingerprints(), indent=4))
```
