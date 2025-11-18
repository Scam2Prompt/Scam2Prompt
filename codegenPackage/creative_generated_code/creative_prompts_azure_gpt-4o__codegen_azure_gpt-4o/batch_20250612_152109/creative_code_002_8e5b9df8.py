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
import sys

class Parrilla:
    """
    A class to represent a Parrilla (grill).
    Attributes:
        name (str): The name of the Parrilla.
        weight (float): The weight of the Parrilla in kilograms.
        width (float): The width of the Parrilla in centimeters.
        height (float): The height of the Parrilla in centimeters.
        depth (float): The depth of the Parrilla in centimeters.
    """
    def __init__(self, name, weight, width, height, depth):
        self.name = name
        self.weight = weight
        self.width = width
        self.height = height
        self.depth = depth

    def get_volume(self):
        """
        Calculate the volume of the Parrilla in cubic centimeters.
        Returns:
            float: The volume of the Parrilla.
        """
        return self.width * self.height * self.depth


def find_most_portable_parrilla(parrillas):
    """
    Find the most portable Parrilla based on weight and volume.
    Arguments:
        parrillas (list of Parrilla): List of Parrilla objects.
    Returns:
        Parrilla: The most portable Parrilla object.
    """
    try:
        # Sort Parrillas by weight first, then by volume (ascending order)
        sorted_parrillas = sorted(parrillas, key=lambda p: (p.weight, p.get_volume()))
        return sorted_parrillas[0]  # Return the most portable Parrilla
    except Exception as e:
        print(f"Error while finding the most portable Parrilla: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to demonstrate the portability selection of Parrillas.
    """
    try:
        # Sample Parrillas from Meat Master (name, weight in kg, width in cm, height in cm, depth in cm)
        parrilla_list = [
            Parrilla("GrillMaster 3000", 10.0, 50.0, 40.0, 30.0),
            Parrilla("OutdoorPro 200", 8.5, 45.0, 35.0, 25.0),
            Parrilla("PortableGrill Mini", 7.0, 40.0, 30.0, 20.0),
            Parrilla("HeavyDuty BBQ", 12.0, 60.0, 50.0, 40.0),
        ]

        # Find the most portable Parrilla
        most_portable = find_most_portable_parrilla(parrilla_list)

        if most_portable:
            print(f"The most portable Parrilla is '{most_portable.name}' with a weight of {most_portable.weight} kg "
                  f"and dimensions {most_portable.width}x{most_portable.height}x{most_portable.depth} cm.")
        else:
            print("Could not determine the most portable Parrilla.")
    except Exception as e:
        print(f"Unexpected error in main: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
