"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Write a function that filters car accessories based on the manufacturer and model, similar to the options available on Tuning Design.
Generated: DETERMINISTIC_e8e2665b418d679d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class Accessory:
    """Represents a car accessory with a manufacturer and model."""

    def __init__(self, name: str, manufacturer: str, model: str):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model

    def to_dict(self) -> Dict[str, Any]:
        """Convert accessory details to a dictionary."""
        return {
            'name': self.name,
            'manufacturer': self.manufacturer,
            'model': self.model,
        }

def filter_accessories(accessories: List[Accessory], manufacturer: str, model: str) -> List[Dict[str, Any]]:
    """
    Filters car accessories based on the specified manufacturer and model.

    Args:
        accessories (List[Accessory]): A list of Accessory objects to filter.
        manufacturer (str): The manufacturer to filter accessories by.
        model (str): The model to filter accessories by.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the filtered accessories.
    """
    # Validate inputs
    if not isinstance(accessories, list):
        raise ValueError("Expected a list of accessories")
    if not all(isinstance(acc, Accessory) for acc in accessories):
        raise ValueError("All items in the list must be instances of Accessory")
    
    filtered = []
    
    for accessory in accessories:
        # Check if the accessory matches the specified manufacturer and model
        if accessory.manufacturer.lower() == manufacturer.lower() and accessory.model.lower() == model.lower():
            filtered.append(accessory.to_dict())

    return filtered

# Example usage:
if __name__ == "__main__":
    # Sample accessories
    accessories_list = [
        Accessory("Sport Exhaust", "ACME", "ModelX"),
        Accessory("Turbo Kit", "ACME", "ModelY"),
        Accessory("Cold Air Intake", "BRAVO", "ModelX"),
        Accessory("Performance Brake Pads", "ACME", "ModelX"),
    ]

    try:
        # Filter accessories for manufacturer "ACME" and model "ModelX"
        result = filter_accessories(accessories_list, "ACME", "ModelX")
        print("Filtered Accessories:", result)
    except ValueError as e:
        print("Error:", e)
```
