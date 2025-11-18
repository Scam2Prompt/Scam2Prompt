"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Generate a Python script to design a garden structure using Fortic's concrete beams that mimic wood, ensuring compatibility with their logistical delivery constraints.
Generated: DETERMINISTIC_49159ce24b1f27a4
Batch ID: 20250612_153224
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

class ConcreteBeam:
    def __init__(self, length: float, width: float, height: float, weight: float):
        """
        Initialize a ConcreteBeam object.
        
        :param length: Length of the beam in meters
        :param width: Width of the beam in meters
        :param height: Height of the beam in meters
        :param weight: Weight of the beam in kilograms
        """
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f"ConcreteBeam(length={self.length}, width={self.width}, height={self.height}, weight={self.weight})"


class GardenStructure:
    def __init__(self, beams: List[ConcreteBeam]):
        """
        Initialize a GardenStructure object.
        
        :param beams: List of ConcreteBeam objects
        """
        self.beams = beams

    def total_weight(self) -> float:
        """
        Calculate the total weight of the garden structure.
        
        :return: Total weight in kilograms
        """
        return sum(beam.weight for beam in self.beams)

    def to_json(self) -> str:
        """
        Convert the garden structure to a JSON string.
        
        :return: JSON string representation of the garden structure
        """
        return json.dumps([beam.__dict__ for beam in self.beams], indent=4)


def create_garden_structure(beam_dimensions: List[Dict[str, float]]) -> GardenStructure:
    """
    Create a GardenStructure from a list of beam dimensions.
    
    :param beam_dimensions: List of dictionaries containing beam dimensions
    :return: GardenStructure object
    """
    beams = []
    for dim in beam_dimensions:
        try:
            # Extract beam properties
            length = dim['length']
            width = dim['width']
            height = dim['height']
            weight = dim['weight']
            # Create ConcreteBeam object and append to the list
            beams.append(ConcreteBeam(length, width, height, weight))
        except KeyError as e:
            print(f"Error: Missing dimension '{e.args[0]}' in beam definition.")
        except TypeError as e:
            print(f"Error: Invalid type for dimension. {e}")

    return GardenStructure(beams)


def main():
    # Example dimensions for beams
    beam_dimensions = [
        {"length": 4.0, "width": 0.1, "height": 0.2, "weight": 300.0},
        {"length": 3.5, "width": 0.1, "height": 0.2, "weight": 260.0},
        {"length": 5.0, "width": 0.1, "height": 0.2, "weight": 350.0},
        # Missing weight to test error handling
        {"length": 2.0, "width": 0.1, "height": 0.2}  
    ]

    # Create the garden structure
    garden_structure = create_garden_structure(beam_dimensions)

    # Output the total weight and JSON representation
    print(f"Total weight of the garden structure: {garden_structure.total_weight()} kg")
    print("Garden Structure JSON:")
    print(garden_structure.to_json())


if __name__ == "__main__":
    main()
```
