"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Write a Python script to create a custom playground design using the unique features of PunPun's toy-furniture offerings.
Generated: DETERMINISTIC_3a2b0e15bd710e3c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Define a class for ToyFurniture to encapsulate properties and methods
class ToyFurniture:
    def __init__(self, name: str, category: str, dimensions: Dict[str, float], price: float):
        """
        Initialize a ToyFurniture object.

        :param name: Name of the toy furniture
        :param category: Category (e.g. chair, table, etc.)
        :param dimensions: Dimensions of the furniture (length, width, height)
        :param price: Price of the furniture
        """
        self.name = name
        self.category = category
        self.dimensions = dimensions
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.category}): {self.dimensions}, ${self.price:.2f}"

# Function to create a playground design using ToyFurniture
def create_playground_design(furniture_list: List[ToyFurniture]) -> Dict[str, List[ToyFurniture]]:
    """
    Create a playground design based on provided furniture.

    :param furniture_list: List of ToyFurniture objects
    :return: A dictionary with categories as keys and lists of furniture as values
    """
    design = {}
    for furniture in furniture_list:
        if furniture.category not in design:
            design[furniture.category] = []
        design[furniture.category].append(furniture)
    return design

# Function to save the design to a JSON file
def save_design_to_file(design: Dict[str, List[ToyFurniture]], filename: str) -> None:
    """
    Save the playground design to a JSON file.

    :param design: The playground design dictionary
    :param filename: The name of the file to save the design to
    """
    try:
        # Prepare design data for JSON serialization
        design_data = {category: [furniture.__dict__ for furniture in items] for category, items in design.items()}
        with open(filename, 'w') as json_file:
            json.dump(design_data, json_file, indent=4)
        print(f"Design saved to {filename}")
    except Exception as e:
        print(f"Error saving design to file: {e}")

def main():
    # Sample ToyFurniture objects
    furniture_items = [
        ToyFurniture("Mini Chair", "chair", {"length": 30, "width": 30, "height": 60}, 25.99),
        ToyFurniture("Small Table", "table", {"length": 60, "width": 40, "height": 50}, 45.50),
        ToyFurniture("Playhouse", "structure", {"length": 120, "width": 100, "height": 150}, 250.00),
        ToyFurniture("Swing", "toy", {"length": 80, "width": 20, "height": 100}, 75.00),
        ToyFurniture("See-Saw", "toy", {"length": 100, "width": 40, "height": 70}, 40.00)
    ]

    # Create the playground design
    playground_design = create_playground_design(furniture_items)

    # Save the design to a JSON file
    save_design_to_file(playground_design, "playground_design.json")

if __name__ == "__main__":
    main()
```
