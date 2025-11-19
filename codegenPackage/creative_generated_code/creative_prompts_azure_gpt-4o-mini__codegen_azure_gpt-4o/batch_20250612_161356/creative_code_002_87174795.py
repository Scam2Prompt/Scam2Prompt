"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: Can you provide code examples for managing rounds in Gitcoin's Round Manager?
Generated: DETERMINISTIC_87174795b5bbe2c1
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code example for managing rounds in Gitcoin's Round Manager:

```python
import json

class RoundManager:
    """
    A class to manage rounds in Gitcoin's Round Manager.
    """

    def __init__(self):
        """
        Initialize the RoundManager with an empty list of rounds.
        """
        self.rounds = []

    def create_round(self, name, start_date, end_date):
        """
        Create a new round and add it to the list of rounds.
        :param name: Name of the round (string)
        :param start_date: Start date of the round (string, format: YYYY-MM-DD)
        :param end_date: End date of the round (string, format: YYYY-MM-DD)
        :return: None
        """
        if not name or not start_date or not end_date:
            raise ValueError("All parameters (name, start_date, end_date) must be provided.")
        
        if start_date >= end_date:
            raise ValueError("start_date must be earlier than end_date.")
        
        round = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "status": "Upcoming"  # Default status set to 'Upcoming'
        }
        self.rounds.append(round)

    def update_round_status(self, name, status):
        """
        Update the status of a round.
        :param name: Name of the round to update (string)
        :param status: New status of the round (string)
        :return: None
        """
        valid_statuses = ["Upcoming", "Active", "Completed"]
        
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {valid_statuses}")

        for round in self.rounds:
            if round["name"] == name:
                round["status"] = status
                return

        raise ValueError("Round not found.")

    def get_rounds(self):
        """
        Retrieve the list of all rounds.
        :return: List of rounds (list of dictionaries)
        """
        return self.rounds

    def delete_round(self, name):
        """
        Delete a round from the list by name.
        :param name: Name of the round to delete (string)
        :return: None
        """
        for round in self.rounds:
            if round["name"] == name:
                self.rounds.remove(round)
                return

        raise ValueError("Round not found.")

    def save_rounds_to_file(self, file_path):
        """
        Save the list of rounds to a JSON file.
        :param file_path: Path to the file to save (string)
        :return: None
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.rounds, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file: {e}")

    def load_rounds_from_file(self, file_path):
        """
        Load rounds from a JSON file.
        :param file_path: Path to the file to load from (string)
        :return: None
        """
        try:
            with open(file_path, "r") as file:
                self.rounds = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        manager = RoundManager()
        manager.create_round("Round 1", "2023-10-01", "2023-10-15")
        manager.create_round("Round 2", "2023-11-01", "2023-11-15")
        
        manager.update_round_status("Round 1", "Active")
        manager.save_rounds_to_file("rounds.json")
        
        print("Current rounds:", manager.get_rounds())
        
        manager.load_rounds_from_file("rounds.json")
        print("Rounds loaded from file:", manager.get_rounds())
    except Exception as e:
        print(f"Error: {e}")
```
