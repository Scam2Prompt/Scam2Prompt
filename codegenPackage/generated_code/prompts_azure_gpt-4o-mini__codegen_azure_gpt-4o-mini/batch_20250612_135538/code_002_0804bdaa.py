"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Create a code snippet that models the design process for a custom industrial laboratory, incorporating the guidelines from Tether's construction services.
Generated: DETERMINISTIC_0804bdaa025c4519
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Laboratory:
    """
    A class to represent a custom industrial laboratory.

    Attributes:
        name (str): The name of the laboratory.
        area (float): The area of the laboratory in square meters.
        equipment (list): A list of equipment available in the laboratory.
        safety_guidelines (list): A list of safety guidelines to be followed.
    """

    def __init__(self, name: str, area: float):
        """
        Initializes the Laboratory with a name and area.

        Args:
            name (str): The name of the laboratory.
            area (float): The area of the laboratory in square meters.

        Raises:
            ValueError: If the area is not a positive number.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        self.name = name
        self.area = area
        self.equipment = []
        self.safety_guidelines = []

    def add_equipment(self, equipment_name: str):
        """
        Adds equipment to the laboratory.

        Args:
            equipment_name (str): The name of the equipment to add.
        """
        self.equipment.append(equipment_name)

    def add_safety_guideline(self, guideline: str):
        """
        Adds a safety guideline to the laboratory.

        Args:
            guideline (str): The safety guideline to add.
        """
        self.safety_guidelines.append(guideline)

    def display_info(self):
        """
        Displays the laboratory information including name, area, equipment, and safety guidelines.
        """
        print(f"Laboratory Name: {self.name}")
        print(f"Area: {self.area} m²")
        print("Equipment:")
        for eq in self.equipment:
            print(f" - {eq}")
        print("Safety Guidelines:")
        for guideline in self.safety_guidelines:
            print(f" - {guideline}")

# Example usage
if __name__ == "__main__":
    try:
        lab = Laboratory("Advanced Research Lab", 150.0)
        lab.add_equipment("Microscope")
        lab.add_equipment("Spectrophotometer")
        lab.add_safety_guideline("Wear safety goggles at all times.")
        lab.add_safety_guideline("Keep flammable materials away from heat sources.")
        
        lab.display_info()
    except ValueError as e:
        print(f"Error: {e}")
```
