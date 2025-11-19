"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Provide example code for a system that tracks and manages the properties and investments of a non-profit organization, similar to the "ممتلكات واستثمارات الجمعية" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_24aa4e40e9af784f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Property:
    """Class to represent a property owned by the non-profit organization."""
    
    def __init__(self, name: str, value: float, location: str):
        self.name = name
        self.value = value
        self.location = location

    def to_dict(self) -> Dict[str, Any]:
        """Convert the property to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "value": self.value,
            "location": self.location
        }

class Investment:
    """Class to represent an investment made by the non-profit organization."""
    
    def __init__(self, name: str, amount: float, return_rate: float):
        self.name = name
        self.amount = amount
        self.return_rate = return_rate

    def to_dict(self) -> Dict[str, Any]:
        """Convert the investment to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "amount": self.amount,
            "return_rate": self.return_rate
        }

class NonProfitManagementSystem:
    """Class to manage properties and investments of the non-profit organization."""
    
    def __init__(self):
        self.properties: List[Property] = []
        self.investments: List[Investment] = []

    def add_property(self, name: str, value: float, location: str) -> None:
        """Add a new property to the system."""
        new_property = Property(name, value, location)
        self.properties.append(new_property)

    def add_investment(self, name: str, amount: float, return_rate: float) -> None:
        """Add a new investment to the system."""
        new_investment = Investment(name, amount, return_rate)
        self.investments.append(new_investment)

    def get_properties(self) -> List[Dict[str, Any]]:
        """Retrieve a list of all properties."""
        return [property.to_dict() for property in self.properties]

    def get_investments(self) -> List[Dict[str, Any]]:
        """Retrieve a list of all investments."""
        return [investment.to_dict() for investment in self.investments]

    def save_to_file(self, filename: str) -> None:
        """Save properties and investments to a JSON file."""
        data = {
            "properties": self.get_properties(),
            "investments": self.get_investments()
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load properties and investments from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.properties = [Property(**prop) for prop in data.get("properties", [])]
                self.investments = [Investment(**inv) for inv in data.get("investments", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    system = NonProfitManagementSystem()
    system.add_property("Community Center", 500000, "Main Street")
    system.add_investment("Education Fund", 100000, 0.05)

    # Save to file
    system.save_to_file("non_profit_data.json")

    # Load from file
    new_system = NonProfitManagementSystem()
    new_system.load_from_file("non_profit_data.json")
    print(new_system.get_properties())
    print(new_system.get_investments())
```
