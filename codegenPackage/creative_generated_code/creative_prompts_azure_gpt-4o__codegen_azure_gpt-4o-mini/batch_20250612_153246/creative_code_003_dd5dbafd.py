"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconelevator.in
Prompt: Create a program to model the design options for elevator cabins, allowing users to choose various designs as highlighted by ICON Elevator.
Generated: DETERMINISTIC_dd5dbafd77bbec43
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ElevatorCabin:
    """
    Class to represent an elevator cabin design.
    """

    def __init__(self, design_name, capacity, dimensions, materials, features):
        """
        Initialize an ElevatorCabin instance.
        
        :param design_name: Name of the elevator cabin design
        :param capacity: Maximum capacity of the cabin (number of people)
        :param dimensions: Dimensions of the cabin (width, depth, height)
        :param materials: Materials used in the design
        :param features: List of special features in the design
        """
        self.design_name = design_name
        self.capacity = capacity
        self.dimensions = dimensions  # (width, depth, height)
        self.materials = materials
        self.features = features

    def __str__(self):
        """Return a string representation of the elevator cabin design."""
        return f"Design: {self.design_name}, Capacity: {self.capacity}, Dimensions: {self.dimensions}, Materials: {self.materials}, Features: {self.features}"


class ElevatorDesignModel:
    """
    Class to manage the collection of elevator cabin designs.
    """

    def __init__(self):
        """Initialize an empty list of designs."""
        self.designs = []

    def add_design(self, design):
        """
        Add a new elevator cabin design to the collection.
        
        :param design: ElevatorCabin instance to add
        """
        self.designs.append(design)

    def list_designs(self):
        """Return a list of all available elevator cabin designs."""
        return self.designs

    def save_designs_to_file(self, file_path):
        """
        Save the list of designs to a JSON file.

        :param file_path: Path to the file where designs will be saved
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump([design.__dict__ for design in self.designs], json_file, indent=4)
            print(f"Designs successfully saved to {file_path}.")
        except IOError as e:
            print(f"Error saving designs to file: {e}")

    def load_designs_from_file(self, file_path):
        """
        Load elevator cabin designs from a JSON file.

        :param file_path: Path to the file from which designs will be loaded
        """
        try:
            with open(file_path, 'r') as json_file:
                designs_data = json.load(json_file)
                self.designs = [ElevatorCabin(**data) for data in designs_data]
            print(f"Designs successfully loaded from {file_path}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading designs from file: {e}")


def main():
    """Main function to demonstrate elevator cabin design management."""
    model = ElevatorDesignModel()

    # Example designs
    design1 = ElevatorCabin("Modern Glass", 8, (2, 1.5, 2.2), "Glass and Steel", ["Smart Control", "LED Lighting"])
    design2 = ElevatorCabin("Luxury Wood", 5, (1.5, 1.5, 2.5), "Wood and Steel", ["Mirror Finish", "Sound System"])
    
    # Adding designs to the model
    model.add_design(design1)
    model.add_design(design2)

    # Listing all designs
    print("Available Elevator Cabin Designs:")
    for design in model.list_designs():
        print(design)

    # Saving designs to a JSON file
    model.save_designs_to_file("elevator_designs.json")

    # Loading designs from a JSON file
    model.load_designs_from_file("elevator_designs.json")


if __name__ == "__main__":
    main()
```
