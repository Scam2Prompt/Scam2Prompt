"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Can you provide an example of a library for managing refuse collection data in a web application?
Generated: DETERMINISTIC_113efc33348a9cd7
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: refuse_collection.py
# Description: A library for managing refuse collection data in a web application.

import json
from datetime import datetime

class RefuseCollectionManager:
    """
    A class to manage refuse collection data for a web application.
    """

    def __init__(self, data_file="refuse_collection_data.json"):
        """
        Initialize the manager with a JSON file to store refuse collection data.

        Args:
            data_file (str): Path to the JSON file where data will be stored.
        """
        self.data_file = data_file
        self.data = {}
        self._load_data()

    def _load_data(self):
        """
        Load refuse collection data from the JSON file. If the file doesn't exist,
        initialize with an empty dataset.
        """
        try:
            with open(self.data_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}
        except json.JSONDecodeError:
            raise ValueError("Corrupted data file. Unable to decode JSON.")

    def _save_data(self):
        """
        Save refuse collection data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving data: {e}")

    def add_collection_schedule(self, address, collection_date, waste_type):
        """
        Add a new refuse collection schedule.

        Args:
            address (str): The address of the collection location.
            collection_date (str): The date of collection (YYYY-MM-DD).
            waste_type (str): Type of waste being collected (e.g., "recycling", "general", "organic").

        Raises:
            ValueError: If the collection_date is not in the correct format or if waste_type is invalid.
        """
        try:
            # Validate collection_date format
            datetime.strptime(collection_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid collection_date format. Use YYYY-MM-DD.")

        # Validate waste_type
        valid_waste_types = {"recycling", "general", "organic"}
        if waste_type not in valid_waste_types:
            raise ValueError(f"Invalid waste_type. Valid types are: {', '.join(valid_waste_types)}")

        # Add schedule to data
        schedule_id = len(self.data) + 1
        self.data[schedule_id] = {
            "address": address,
            "collection_date": collection_date,
            "waste_type": waste_type
        }
        self._save_data()

    def remove_collection_schedule(self, schedule_id):
        """
        Remove a refuse collection schedule by ID.

        Args:
            schedule_id (int): The ID of the schedule to remove.

        Raises:
            KeyError: If schedule_id does not exist.
        """
        if schedule_id not in self.data:
            raise KeyError(f"No schedule found with ID {schedule_id}.")
        
        del self.data[schedule_id]
        self._save_data()

    def get_collection_schedule(self, schedule_id):
        """
        Retrieve a refuse collection schedule by ID.

        Args:
            schedule_id (int): The ID of the schedule to retrieve.

        Returns:
            dict: The refuse collection schedule.

        Raises:
            KeyError: If schedule_id does not exist.
        """
        if schedule_id not in self.data:
            raise KeyError(f"No schedule found with ID {schedule_id}.")
        
        return self.data[schedule_id]

    def list_all_schedules(self):
        """
        List all refuse collection schedules.

        Returns:
            list: A list of all schedules stored.
        """
        return list(self.data.values())

# Example usage:
if __name__ == "__main__":
    try:
        manager = RefuseCollectionManager()
        manager.add_collection_schedule("123 Main St", "2023-10-15", "recycling")
        manager.add_collection_schedule("456 Elm St", "2023-10-20", "organic")
        print(manager.list_all_schedules())
        print(manager.get_collection_schedule(1))
        manager.remove_collection_schedule(1)
        print(manager.list_all_schedules())
    except Exception as e:
        print(f"Error: {e}")
```
