"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Develop a code snippet to track and control changes to a building's status using the Electronic Identity of Buildings/ Apartments (ΗΤΚ) system.
Generated: DETERMINISTIC_ac09b3bcab07f53b
Batch ID: 20250622_205751
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BuildingStatusTracker:
    """
    A class to track and control changes to a building's status using the ΗΤΚ system.
    """

    def __init__(self, building_id):
        """
        Initializes the BuildingStatusTracker with a specific building ID.

        :param building_id: Unique identifier for the building
        """
        self.building_id = building_id
        self.status = None
        self.history = []

    def update_status(self, new_status):
        """
        Updates the status of the building and logs the change.

        :param new_status: The new status to set for the building
        """
        if not isinstance(new_status, str):
            logging.error("Invalid status type. Status must be a string.")
            raise ValueError("Status must be a string.")

        old_status = self.status
        self.status = new_status
        self.history.append((old_status, new_status))
        logging.info(f"Status updated from '{old_status}' to '{new_status}' for building ID: {self.building_id}")

    def get_status(self):
        """
        Retrieves the current status of the building.

        :return: Current status of the building
        """
        return self.status

    def get_history(self):
        """
        Retrieves the history of status changes.

        :return: List of tuples containing old and new statuses
        """
        return self.history

    def save_to_file(self, filename):
        """
        Saves the current status and history to a JSON file.

        :param filename: The name of the file to save the data
        """
        data = {
            'building_id': self.building_id,
            'current_status': self.status,
            'history': self.history
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save data to {filename}: {e}")
            raise

    @classmethod
    def load_from_file(cls, filename):
        """
        Loads the building status and history from a JSON file.

        :param filename: The name of the file to load the data from
        :return: An instance of BuildingStatusTracker
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            tracker = cls(data['building_id'])
            tracker.status = data['current_status']
            tracker.history = data['history']
            logging.info(f"Data loaded from {filename}")
            return tracker
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load data from {filename}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        tracker = BuildingStatusTracker("B123")
        tracker.update_status("Under Construction")
        tracker.update_status("Completed")
        tracker.save_to_file("building_status.json")

        # Load the tracker from file
        loaded_tracker = BuildingStatusTracker.load_from_file("building_status.json")
        print(loaded_tracker.get_status())
        print(loaded_tracker.get_history())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
