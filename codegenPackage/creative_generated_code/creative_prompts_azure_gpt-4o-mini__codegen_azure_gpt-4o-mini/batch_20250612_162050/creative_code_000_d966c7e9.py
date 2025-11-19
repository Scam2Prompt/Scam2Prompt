"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: How can I implement a verification system for automotive parts like the authenticity system used by یاتاقان گلدن?
Generated: DETERMINISTIC_d966c7e9f0c7daa8
Batch ID: 20250612_162050
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

class PartVerificationSystem:
    def __init__(self, storage_file='parts_database.json'):
        """
        Initializes the verification system with a database file.
        """
        self.storage_file = storage_file
        self.parts_db = self.load_parts_database()

    def load_parts_database(self):
        """
        Loads the parts database from a JSON file.
        If the file does not exist, it creates an empty database.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_parts_database(self):
        """
        Saves the current parts database to a JSON file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.parts_db, file, indent=4)

    def add_part(self, part_id, part_info):
        """
        Adds a new part to the verification system.

        :param part_id: Unique identifier for the part
        :param part_info: Dictionary containing information about the part
        """
        if part_id in self.parts_db:
            raise ValueError("Part ID already exists in the database.")
        
        # Create a hash of the part information for integrity
        part_hash = self.generate_hash(part_info)
        self.parts_db[part_id] = {
            'info': part_info,
            'hash': part_hash
        }
        self.save_parts_database()

    def generate_hash(self, part_info):
        """
        Generates a SHA-256 hash for the given part information.

        :param part_info: Dictionary containing information about the part
        :return: SHA-256 hash string
        """
        part_info_string = json.dumps(part_info, sort_keys=True).encode('utf-8')
        return hashlib.sha256(part_info_string).hexdigest()

    def verify_part(self, part_id):
        """
        Verifies the authenticity of a part using its ID.

        :param part_id: Unique identifier for the part
        :return: Boolean indicating whether the part is authentic or not
        """
        if part_id not in self.parts_db:
            raise ValueError("Part ID not found in the database.")
        
        stored_info = self.parts_db[part_id]['info']
        stored_hash = self.parts_db[part_id]['hash']
        current_hash = self.generate_hash(stored_info)
        
        return stored_hash == current_hash

# Example usage:
if __name__ == "__main__":
    try:
        verification_system = PartVerificationSystem()

        # Adding a part for testing
        part_id = "12345"
        part_info = {
            "name": "Engine Bearing",
            "manufacturer": "Golden Bearing Co.",
            "model": "GB123",
            "date_of_manufacture": "2023-01-15"
        }
        verification_system.add_part(part_id, part_info)

        # Verifying the part
        is_authentic = verification_system.verify_part(part_id)
        print(f"Part ID {part_id} authenticity: {is_authentic}")

        # Attempting to verify a non-existent part
        verification_system.verify_part("67890")

    except Exception as e:
        print(f"An error occurred: {e}")
```
