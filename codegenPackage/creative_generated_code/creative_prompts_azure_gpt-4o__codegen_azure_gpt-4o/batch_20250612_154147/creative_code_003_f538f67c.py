"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jitodaily.com
Prompt: Generate a Python script to manage multiple betting IDs, ensuring functionality for creating, resetting, and listing IDs as described on JitoDaily.
Generated: DETERMINISTIC_f538f67c7e3b168b
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Betting ID Manager Script

This script provides functionality to manage multiple betting IDs.
It includes options for creating, resetting, and listing IDs.
"""

import uuid  # For generating unique IDs
import json  # For persistent storage
import os    # For file operations

# File to store betting IDs
DATA_FILE = "betting_ids.json"


class BettingIDManager:
    def __init__(self, data_file=DATA_FILE):
        """
        Initialize the BettingIDManager instance.
        :param data_file: Path to the file where betting IDs are stored.
        """
        self.data_file = data_file
        self.betting_ids = self._load_data()

    def _load_data(self):
        """
        Load betting IDs from the data file.
        :return: List of betting IDs.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                # Handle corrupt file or IO issues
                print("Error loading data file. Starting with an empty list.")
                return []
        return []

    def _save_data(self):
        """
        Save betting IDs to the data file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.betting_ids, file, indent=4)
        except IOError:
            print("Error saving data to file.")

    def create_id(self):
        """
        Create a new unique betting ID.
        :return: The newly created betting ID.
        """
        new_id = str(uuid.uuid4())
        self.betting_ids.append(new_id)
        self._save_data()
        return new_id

    def reset_ids(self):
        """
        Reset all betting IDs (clear the list).
        """
        self.betting_ids = []
        self._save_data()

    def list_ids(self):
        """
        List all existing betting IDs.
        :return: List of betting IDs.
        """
        return self.betting_ids


def main():
    """
    Main function to interact with the BettingIDManager.
    Provides a command-line interface for managing betting IDs.
    """
    manager = BettingIDManager()

    while True:
        print("\nBetting ID Manager")
        print("------------------")
        print("1. Create a new Betting ID")
        print("2. Reset all Betting IDs")
        print("3. List all Betting IDs")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            new_id = manager.create_id()
            print(f"New Betting ID created: {new_id}")
        elif choice == 2:
            manager.reset_ids()
            print("All Betting IDs have been reset.")
        elif choice == 3:
            ids = manager.list_ids()
            if ids:
                print("Existing Betting IDs:")
                for betting_id in ids:
                    print(betting_id)
            else:
                print("No Betting IDs found.")
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
```
