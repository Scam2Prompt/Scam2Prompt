"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Write a Python script to create a scheduling system for refuse and recycling collection, including features for tracking collection dates and locations specific to the City of York.
Generated: DETERMINISTIC_8d8f549c7a76ef3b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Optional

class CollectionSchedule:
    """A class to represent the refuse and recycling collection schedule."""

    def __init__(self):
        # Dictionary to hold collection schedules by address
        self.schedule: Dict[str, List[Dict[str, str]]] = {}

    def add_collection(self, address: str, collection_date: str, collection_type: str) -> None:
        """
        Add a new collection entry to the schedule.

        Args:
            address (str): The address for the collection.
            collection_date (str): The date of the collection (YYYY-MM-DD).
            collection_type (str): The type of collection ('refuse' or 'recycling').

        Raises:
            ValueError: If the date format is incorrect or if the collection type is invalid.
        """
        # Validate collection date format
        try:
            datetime.datetime.strptime(collection_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

        if collection_type not in ['refuse', 'recycling']:
            raise ValueError("Collection type must be 'refuse' or 'recycling'")

        if address not in self.schedule:
            self.schedule[address] = []

        self.schedule[address].append({
            'date': collection_date,
            'type': collection_type
        })

    def get_collection_dates(self, address: str) -> Optional[List[Dict[str, str]]]:
        """
        Retrieve collection dates for a specific address.

        Args:
            address (str): The address to retrieve the collection dates for.

        Returns:
            Optional[List[Dict[str, str]]]: A list of collection dates and types or None if no schedule exists.
        """
        return self.schedule.get(address, None)

    def save_schedule_to_file(self, filename: str) -> None:
        """
        Save the current collection schedule to a JSON file.

        Args:
            filename (str): The file where the schedule will be saved.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

    def load_schedule_from_file(self, filename: str) -> None:
        """
        Load the collection schedule from a JSON file.

        Args:
            filename (str): The file from which to load the schedule.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
        except IOError as e:
            print(f"Error loading schedule from file: {e}")

# Example usage
if __name__ == "__main__":
    schedule = CollectionSchedule()
    
    # Adding collection dates
    try:
        schedule.add_collection("123 Main St", "2023-10-01", "refuse")
        schedule.add_collection("123 Main St", "2023-10-15", "recycling")
        schedule.add_collection("456 Elm St", "2023-10-02", "refuse")
    except ValueError as e:
        print(e)

    # Retrieving collection dates for an address
    print(schedule.get_collection_dates("123 Main St"))

    # Save schedule to a file
    schedule.save_schedule_to_file("collection_schedule.json")

    # Load schedule from a file
    schedule.load_schedule_from_file("collection_schedule.json")
```
