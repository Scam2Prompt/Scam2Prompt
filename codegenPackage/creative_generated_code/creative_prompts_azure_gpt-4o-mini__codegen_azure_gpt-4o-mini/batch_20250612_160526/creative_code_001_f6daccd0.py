"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://screciclados.mx
Prompt: How can I implement a recycling management system that tracks electronic waste, inspired by the practices of SCR Reciclados?
Generated: DETERMINISTIC_f6daccd07b85d5c6
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class ElectronicWaste:
    """Class to represent electronic waste items."""
    
    def __init__(self, item_id: str, description: str, weight: float, date_collected: str):
        self.item_id = item_id
        self.description = description
        self.weight = weight
        self.date_collected = self._validate_date(date_collected)

    def _validate_date(self, date_str: str) -> str:
        """Validate and format the date."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format is YYYY-MM-DD.")

    def to_dict(self) -> Dict:
        """Convert the electronic waste item to a dictionary."""
        return {
            "item_id": self.item_id,
            "description": self.description,
            "weight": self.weight,
            "date_collected": self.date_collected
        }

class RecyclingManager:
    """Class to manage a collection of electronic waste."""
    
    def __init__(self):
        self.electronic_waste_list: List[ElectronicWaste] = []

    def add_waste(self, item_id: str, description: str, weight: float, date_collected: str):
        """Add a new electronic waste item to the manager."""
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        new_item = ElectronicWaste(item_id, description, weight, date_collected)
        self.electronic_waste_list.append(new_item)

    def remove_waste(self, item_id: str):
        """Remove an electronic waste item by its ID."""
        self.electronic_waste_list = [item for item in self.electronic_waste_list if item.item_id != item_id]

    def get_waste_summary(self) -> List[Dict]:
        """Get a summary of all electronic waste items."""
        return [item.to_dict() for item in self.electronic_waste_list]

    def save_to_file(self, filepath: str):
        """Save the current electronic waste list to a JSON file."""
        try:
            with open(filepath, 'w') as json_file:
                json.dump(self.get_waste_summary(), json_file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving file {filepath}: {e}")

    def load_from_file(self, filepath: str):
        """Load electronic waste items from a JSON file."""
        try:
            with open(filepath, 'r') as json_file:
                waste_items = json.load(json_file)
                for item in waste_items:
                    self.add_waste(item['item_id'], item['description'], item['weight'], item['date_collected'])
        except IOError as e:
            raise IOError(f"Error loading file {filepath}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from {filepath}: {e}")

# Example usage
if __name__ == "__main__":
    recycling_manager = RecyclingManager()
    
    # Adding electronic waste items
    recycling_manager.add_waste("001", "Old Laptop", 2.5, "2023-02-15")
    recycling_manager.add_waste("002", "Broken Phone", 0.5, "2023-03-01")

    # Save to file
    recycling_manager.save_to_file("electronic_waste.json")

    # Load from file
    recycling_manager.load_from_file("electronic_waste.json")

    # Print summary
    print(recycling_manager.get_waste_summary())
```
