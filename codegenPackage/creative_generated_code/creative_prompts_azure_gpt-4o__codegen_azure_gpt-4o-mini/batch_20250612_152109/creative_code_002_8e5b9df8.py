"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Generate code to compare the weight and dimensions of different Parrillas listed on Meat Master and suggest the most portable option for outdoor grilling.
Generated: DETERMINISTIC_8e5b9df8e1f90a1f
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class Parrilla:
    """
    A class to represent a Parrilla (grill) with its specifications.
    """

    def __init__(self, name, weight, width, depth, height):
        """
        Initialize a Parrilla instance.

        :param name: Name of the Parrilla
        :param weight: Weight of the Parrilla in kilograms
        :param width: Width of the Parrilla in centimeters
        :param depth: Depth of the Parrilla in centimeters
        :param height: Height of the Parrilla in centimeters
        """
        self.name = name
        self.weight = weight
        self.dimensions = (width, depth, height)

    def volume(self):
        """
        Calculate the volume of the Parrilla based on its dimensions.

        :return: Volume in cubic centimeters
        """
        width, depth, height = self.dimensions
        return width * depth * height


def suggest_most_portable(parrillas):
    """
    Suggests the most portable Parrilla based on weight and dimensions.

    :param parrillas: List of Parrilla objects
    :return: The most portable Parrilla object
    """
    if not parrillas:
        raise ValueError("The list of Parrillas cannot be empty.")

    # Sort Parrillas by weight and then by volume (ascending order)
    sorted_parrillas = sorted(parrillas, key=lambda p: (p.weight, p.volume()))

    # Return the most portable option
    return sorted_parrillas[0]


# Example usage with error handling
if __name__ == "__main__":
    try:
        # Sample data for Parrillas
        parrilla_data = [
            {'name': 'Parrilla A', 'weight': 10, 'width': 50, 'depth': 40, 'height': 20},
            {'name': 'Parrilla B', 'weight': 8, 'width': 45, 'depth': 35, 'height': 18},
            {'name': 'Parrilla C', 'weight': 12, 'width': 60, 'depth': 45, 'height': 25},
        ]

        # Create Parrilla objects
        parrillas = [Parrilla(**data) for data in parrilla_data]

        # Suggest the most portable option
        most_portable = suggest_most_portable(parrillas)

        print(f"The most portable Parrilla is: {most_portable.name} "
              f"with a weight of {most_portable.weight} kg and dimensions {most_portable.dimensions} cm.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
