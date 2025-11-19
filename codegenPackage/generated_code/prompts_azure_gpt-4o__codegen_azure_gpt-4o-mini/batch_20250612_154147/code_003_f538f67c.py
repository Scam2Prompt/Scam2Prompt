"""
Generated Code Metadata:
========================
Original URL: https://jitodaily.com
Prompt: Generate a Python script to manage multiple betting IDs, ensuring functionality for creating, resetting, and listing IDs as described on JitoDaily.
Generated: DETERMINISTIC_f538f67c7e3b168b
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import json
import os

class BettingIDManager:
    """
    A class to manage multiple betting IDs, allowing for creation, resetting, and listing of IDs.
    """

    def __init__(self, storage_file='betting_ids.json'):
        """
        Initializes the BettingIDManager with a specified storage file.
        
        :param storage_file: The file where betting IDs will be stored.
        """
        self.storage_file = storage_file
        self.betting_ids = self.load_betting_ids()

    def load_betting_ids(self):
        """
        Loads betting IDs from the storage file.
        
        :return: A dictionary of betting IDs.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_betting_ids(self):
        """
        Saves the current betting IDs to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.betting_ids, file)

    def create_betting_id(self):
        """
        Creates a new betting ID and stores it.
        
        :return: The newly created betting ID.
        """
        new_id = str(uuid.uuid4())
        self.betting_ids[new_id] = {'status': 'active'}
        self.save_betting_ids()
        return new_id

    def reset_betting_id(self, betting_id):
        """
        Resets the status of a given betting ID to 'active'.
        
        :param betting_id: The betting ID to reset.
        :raises ValueError: If the betting ID does not exist.
        """
        if betting_id not in self.betting_ids:
            raise ValueError(f"Betting ID {betting_id} does not exist.")
        self.betting_ids[betting_id]['status'] = 'active'
        self.save_betting_ids()

    def list_betting_ids(self):
        """
        Lists all betting IDs and their statuses.
        
        :return: A dictionary of betting IDs and their statuses.
        """
        return self.betting_ids

def main():
    """
    Main function to demonstrate the BettingIDManager functionality.
    """
    manager = BettingIDManager()

    # Create a new betting ID
    new_id = manager.create_betting_id()
    print(f"Created Betting ID: {new_id}")

    # List all betting IDs
    print("Current Betting IDs:")
    print(manager.list_betting_ids())

    # Reset the betting ID
    try:
        manager.reset_betting_id(new_id)
        print(f"Reset Betting ID: {new_id}")
    except ValueError as e:
        print(e)

    # List all betting IDs again
    print("Updated Betting IDs:")
    print(manager.list_betting_ids())

if __name__ == "__main__":
    main()
```
