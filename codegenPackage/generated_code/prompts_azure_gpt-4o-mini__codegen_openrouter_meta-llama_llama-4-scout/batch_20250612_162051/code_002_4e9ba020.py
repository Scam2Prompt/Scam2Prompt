"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Generate a Python script that tracks emotional states over time, helping users identify patterns similar to the "Calendário das Emoções" mentioned on the site.
Generated: DETERMINISTIC_4e9ba020227dbfa6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class EmotionalStateTracker:
    def __init__(self, data_file='emotional_states.json'):
        """
        Initialize the emotional state tracker.

        Args:
            data_file (str): The file to store the emotional state data.
        """
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """
        Load existing emotional state data from the file.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        """
        Save the emotional state data to the file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_emotional_state(self, date, state, note=None):
        """
        Add a new emotional state entry.

        Args:
            date (str): The date in YYYY-MM-DD format.
            state (str): The emotional state.
            note (str, optional): An optional note. Defaults to None.
        """
        if date in self.data:
            print("Entry for this date already exists. Please update instead.")
            return

        self.data[date] = {'state': state, 'note': note}
        self.save_data()

    def update_emotional_state(self, date, state=None, note=None):
        """
        Update an existing emotional state entry.

        Args:
            date (str): The date in YYYY-MM-DD format.
            state (str, optional): The new emotional state. Defaults to None.
            note (str, optional): The new note. Defaults to None.
        """
        if date not in self.data:
            print("Entry for this date does not exist. Please add instead.")
            return

        if state:
            self.data[date]['state'] = state
        if note:
            self.data[date]['note'] = note
        self.save_data()

    def delete_emotional_state(self, date):
        """
        Delete an emotional state entry.

        Args:
            date (str): The date in YYYY-MM-DD format.
        """
        if date not in self.data:
            print("Entry for this date does not exist.")
            return

        del self.data[date]
        self.save_data()

    def get_emotional_state(self, date):
        """
        Get an emotional state entry.

        Args:
            date (str): The date in YYYY-MM-DD format.

        Returns:
            dict: The emotional state entry.
        """
        return self.data.get(date)

    def list_emotional_states(self):
        """
        List all emotional state entries.

        Returns:
            dict: All emotional state entries.
        """
        return self.data


def main():
    tracker = EmotionalStateTracker()

    while True:
        print("\n1. Add emotional state")
        print("2. Update emotional state")
        print("3. Delete emotional state")
        print("4. Get emotional state")
        print("5. List emotional states")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            state = input("Enter emotional state: ")
            note = input("Enter note (optional): ")
            tracker.add_emotional_state(date, state, note if note else None)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            state = input("Enter new emotional state (optional): ")
            note = input("Enter new note (optional): ")
            tracker.update_emotional_state(date, state if state else None, note if note else None)
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            tracker.delete_emotional_state(date)
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD): ")
            print(tracker.get_emotional_state(date))
        elif choice == '5':
            print(tracker.list_emotional_states())
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
