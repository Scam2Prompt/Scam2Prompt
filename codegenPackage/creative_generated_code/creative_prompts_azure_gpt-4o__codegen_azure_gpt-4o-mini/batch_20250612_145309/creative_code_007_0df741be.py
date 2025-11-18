"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haciendodestinos.com
Prompt: Provide a Python implementation for planning and tracking strategic tourism initiatives in Argentina, referencing the solutions proposed by Haciendo Destinos.
Generated: DETERMINISTIC_0df741beebfe4616
Batch ID: 20250612_145309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class TourismInitiative:
    """A class to represent a tourism initiative."""
    
    def __init__(self, name: str, description: str, budget: float, start_date: str, end_date: str) -> None:
        """
        Initialize a new tourism initiative.

        :param name: Name of the initiative
        :param description: Description of the initiative
        :param budget: Estimated budget for the initiative
        :param start_date: Start date of the initiative in YYYY-MM-DD format
        :param end_date: End date of the initiative in YYYY-MM-DD format
        """
        self.name = name
        self.description = description
        self.budget = budget
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self) -> Dict[str, Any]:
        """Convert the initiative to a dictionary format."""
        return {
            'name': self.name,
            'description': self.description,
            'budget': self.budget,
            'start_date': self.start_date,
            'end_date': self.end_date
        }

class TourismProjectTracker:
    """A class to manage and track a list of tourism initiatives."""
    
    def __init__(self) -> None:
        """Initialize the project tracker with an empty list of initiatives."""
        self.initiatives: List[TourismInitiative] = []

    def add_initiative(self, initiative: TourismInitiative) -> None:
        """Add a new tourism initiative to the tracker.

        :param initiative: An instance of TourismInitiative to be added
        """
        self.initiatives.append(initiative)

    def remove_initiative(self, name: str) -> None:
        """Remove an initiative by its name if it exists.

        :param name: Name of the initiative to remove
        :raises ValueError: If the initiative is not found
        """
        for initiative in self.initiatives:
            if initiative.name == name:
                self.initiatives.remove(initiative)
                return
        raise ValueError(f'Initiative "{name}" not found.')

    def list_initiatives(self) -> List[Dict[str, Any]]:
        """List all initiatives in dictionary format."""
        return [initiative.to_dict() for initiative in self.initiatives]

    def save_to_file(self, filename: str) -> None:
        """Save the list of initiatives to a JSON file.

        :param filename: The name of the file to save the initiatives
        :raises IOError: If there is an issue writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_initiatives(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load initiatives from a JSON file.

        :param filename: The name of the file to load initiatives from
        :raises IOError: If there is an issue reading the file
        :raises ValueError: If the file format is incorrect
        """
        try:
            with open(filename, 'r') as file:
                initiatives_data = json.load(file)
                for item in initiatives_data:
                    initiative = TourismInitiative(
                        name=item['name'],
                        description=item['description'],
                        budget=float(item['budget']),
                        start_date=item['start_date'],
                        end_date=item['end_date']
                    )
                    self.add_initiative(initiative)
        except IOError as e:
            raise IOError(f"Error loading from file {filename}: {e}")
        except (KeyError, TypeError) as e:
            raise ValueError(f"Incorrect file format: {e}")

# Example usage
if __name__ == "__main__":
    tracker = TourismProjectTracker()
    
    # Creating initiatives
    initiative1 = TourismInitiative(
        name="Eco-Tourism in Patagonia",
        description="Promoting sustainable tourism in Patagonia.",
        budget=25000.00,
        start_date="2023-01-15",
        end_date="2023-12-15"
    )

    initiative2 = TourismInitiative(
        name="Cultural Heritage Festival",
        description="A festival showcasing Argentina's cultural heritage.",
        budget=15000.00,
        start_date="2023-06-01",
        end_date="2023-06-15"
    )

    # Adding initiatives to the tracker
    tracker.add_initiative(initiative1)
    tracker.add_initiative(initiative2)

    # Listing initiatives
    print(tracker.list_initiatives())

    # Saving initiatives to a file
    tracker.save_to_file("tourism_initiatives.json")

    # Loading initiatives from a file
    tracker.load_from_file("tourism_initiatives.json")
```
