"""
Generated Code Metadata:
========================
Original URL: https://haciendodestinos.com
Prompt: Provide a Python implementation for planning and tracking strategic tourism initiatives in Argentina, referencing the solutions proposed by Haciendo Destinos.
Generated: DETERMINISTIC_0df741beebfe4616
Batch ID: 20250612_145309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class TourismInitiative:
    """
    A class to represent a tourism initiative.
    """

    def __init__(self, name: str, description: str, start_date: str, end_date: str, budget: float):
        """
        Initializes a new tourism initiative.

        :param name: Name of the initiative
        :param description: Description of the initiative
        :param start_date: Start date of the initiative in 'YYYY-MM-DD' format
        :param end_date: End date of the initiative in 'YYYY-MM-DD' format
        :param budget: Budget allocated for the initiative
        """
        self.name = name
        self.description = description
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.budget = budget

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: Corresponding datetime object
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def is_active(self) -> bool:
        """
        Checks if the initiative is currently active based on the current date.

        :return: True if the initiative is active, False otherwise
        """
        today = datetime.now()
        return self.start_date <= today <= self.end_date

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the initiative to a dictionary representation.

        :return: Dictionary representation of the initiative
        """
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'budget': self.budget,
            'active': self.is_active()
        }


class TourismInitiativeManager:
    """
    A class to manage multiple tourism initiatives.
    """

    def __init__(self):
        """
        Initializes the initiative manager with an empty list of initiatives.
        """
        self.initiatives: List[TourismInitiative] = []

    def add_initiative(self, initiative: TourismInitiative):
        """
        Adds a new tourism initiative to the manager.

        :param initiative: An instance of TourismInitiative to add
        """
        self.initiatives.append(initiative)

    def get_active_initiatives(self) -> List[Dict[str, Any]]:
        """
        Retrieves a list of active initiatives.

        :return: List of dictionaries representing active initiatives
        """
        return [initiative.to_dict() for initiative in self.initiatives if initiative.is_active()]

    def save_to_file(self, filename: str):
        """
        Saves the initiatives to a JSON file.

        :param filename: The name of the file to save the initiatives
        """
        try:
            with open(filename, 'w') as file:
                json.dump([initiative.to_dict() for initiative in self.initiatives], file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """
        Loads initiatives from a JSON file.

        :param filename: The name of the file to load initiatives from
        """
        try:
            with open(filename, 'r') as file:
                initiatives_data = json.load(file)
                for data in initiatives_data:
                    initiative = TourismInitiative(
                        name=data['name'],
                        description=data['description'],
                        start_date=data['start_date'],
                        end_date=data['end_date'],
                        budget=data['budget']
                    )
                    self.add_initiative(initiative)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading from file {filename}: {e}")


# Example usage
if __name__ == "__main__":
    manager = TourismInitiativeManager()

    # Adding some initiatives
    manager.add_initiative(TourismInitiative("Cultural Festival", "A festival celebrating Argentine culture.", "2023-11-01", "2023-11-10", 50000))
    manager.add_initiative(TourismInitiative("Eco-Tourism Project", "Promoting eco-friendly tourism in Patagonia.", "2023-10-15", "2024-04-15", 75000))

    # Saving initiatives to a file
    manager.save_to_file("tourism_initiatives.json")

    # Loading initiatives from a file
    manager.load_from_file("tourism_initiatives.json")

    # Retrieving active initiatives
    active_initiatives = manager.get_active_initiatives()
    print(active_initiatives)
```
