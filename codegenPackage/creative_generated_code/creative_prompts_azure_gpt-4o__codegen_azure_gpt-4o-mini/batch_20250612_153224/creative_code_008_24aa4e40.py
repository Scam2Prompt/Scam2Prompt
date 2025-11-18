"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Provide example code for a system that tracks and manages the properties and investments of a non-profit organization, similar to the "ممتلكات واستثمارات الجمعية" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_24aa4e40e9af784f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# NonProfitPropertyInvestmentManager.py

import json
from typing import List, Dict, Any

class PropertyInvestment:
    """Class to represent a property investment for a non-profit organization."""

    def __init__(self, name: str, value: float, location: str, description: str):
        self.name = name
        self.value = value
        self.location = location
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the property investment to a dictionary."""
        return {
            "name": self.name,
            "value": self.value,
            "location": self.location,
            "description": self.description,
        }

class NonProfitPropertyInvestmentManager:
    """Class to manage properties and investments for a non-profit organization."""

    def __init__(self):
        self.investments: List[PropertyInvestment] = []

    def add_investment(self, investment: PropertyInvestment):
        """Add a new investment to the list."""
        self.investments.append(investment)
        print(f"Investment '{investment.name}' added successfully.")

    def remove_investment(self, name: str):
        """Remove an investment by its name."""
        original_count = len(self.investments)
        self.investments = [inv for inv in self.investments if inv.name != name]
        if len(self.investments) < original_count:
            print(f"Investment '{name}' removed successfully.")
        else:
            print(f"Investment '{name}' not found.")

    def list_investments(self) -> List[Dict[str, Any]]:
        """Return a list of all investments as dictionaries."""
        return [investment.to_dict() for investment in self.investments]

    def save_to_file(self, file_path: str) -> None:
        """Save the investments to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.list_investments(), file, indent=4)
            print(f"Investments saved to '{file_path}' successfully.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """Load investments from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                investments_data = json.load(file)
                self.investments = [
                    PropertyInvestment(**data) for data in investments_data
                ]
            print(f"Investments loaded from '{file_path}' successfully.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = NonProfitPropertyInvestmentManager()

    # Add investments
    manager.add_investment(PropertyInvestment("Community Center", 300000.00, "123 Main St, Samira", "A community center for various activities."))
    manager.add_investment(PropertyInvestment("Youth Camp", 150000.00, "456 Oak Rd, Samira", "A camp for youth engagement and activities."))

    # List investments
    print("Current Investments:")
    print(manager.list_investments())

    # Save to file
    manager.save_to_file("investments.json")

    # Load from file
    manager.load_from_file("investments.json")

    # Remove an investment
    manager.remove_investment("Community Center")
    print("Investments after removal:")
    print(manager.list_investments())
```
