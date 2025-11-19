"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Recommend a wooden chair design, similar to the "Елдорадо" or "Виола" chairs, to match a rectangular dining table made of solid wood.
Generated: DETERMINISTIC_7f6841637403ea58
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class Chair:
    def __init__(self, name, width, depth, height, arm_height, leg_thickness, material):
        """
        Initialize a Chair object.

        Args:
            name (str): Name of the chair design.
            width (float): Width of the chair in cm.
            depth (float): Depth of the chair in cm.
            height (float): Height of the chair in cm.
            arm_height (float): Height of the armrest in cm.
            leg_thickness (float): Thickness of the leg in cm.
            material (str): Material of the chair.
        """
        self.name = name
        self.width = width
        self.depth = depth
        self.height = height
        self.arm_height = arm_height
        self.leg_thickness = leg_thickness
        self.material = material

    def __str__(self):
        return f"Chair: {self.name}\nDimensions: {self.width}cm x {self.depth}cm x {self.height}cm\nMaterial: {self.material}"

class DiningTable:
    def __init__(self, width, length, material):
        """
        Initialize a DiningTable object.

        Args:
            width (float): Width of the table in cm.
            length (float): Length of the table in cm.
            material (str): Material of the table.
        """
        self.width = width
        self.length = length
        self.material = material

    def __str__(self):
        return f"Dining Table: {self.width}cm x {self.length}cm\nMaterial: {self.material}"

def recommend_chair(table, chair_designs):
    """
    Recommend a chair design based on the dining table.

    Args:
        table (DiningTable): The dining table object.
        chair_designs (list[Chair]): A list of chair design objects.

    Returns:
        Chair: A recommended chair design object.
    """
    # Define the ratio of chair width to table width
    ratio = 0.6

    # Calculate the recommended chair width
    recommended_width = table.width * ratio

    # Find the chair design with the closest width to the recommended width
    recommended_chair = min(chair_designs, key=lambda chair: abs(chair.width - recommended_width))

    return recommended_chair

def main():
    try:
        # Create a dining table object
        table = DiningTable(90, 200, "Solid Wood")

        # Create chair design objects
        eldorado = Chair("Елдорадо", 60, 80, 100, 65, 5, "Wood")
        viola = Chair("Виола", 55, 75, 95, 60, 4, "Wood")
        recommended = Chair("Recommended", 54, 78, 98, 62, 5, "Wood")

        # List of chair designs
        chair_designs = [eldorado, viola, recommended]

        # Recommend a chair design
        recommended_chair = recommend_chair(table, chair_designs)

        # Print the dining table and recommended chair design
        print(table)
        print("\n")
        print(recommended_chair)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
