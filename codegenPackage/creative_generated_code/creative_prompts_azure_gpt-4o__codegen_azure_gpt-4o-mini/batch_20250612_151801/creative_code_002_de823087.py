"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Generate code for a waste management system that integrates a magnetic separator and an optical sorter, referencing the equipment described in Kubitz's automated processing configurations.
Generated: DETERMINISTIC_de823087593c6ea7
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Waste:
    """Class to represent waste materials."""
    def __init__(self, material_type, weight):
        self.material_type = material_type  # Type of waste (e.g., 'plastic', 'metal', 'organic')
        self.weight = weight                  # Weight of the waste in kilograms

class MagneticSeparator:
    """Class to represent a magnetic separator."""
    def __init__(self):
        self.processed_waste = []  # List to hold processed waste

    def process(self, waste: Waste):
        """Process waste using the magnetic separator.

        Args:
            waste (Waste): The waste object to process.
        """
        if waste.material_type == 'metal':
            self.processed_waste.append(waste)
            print(f"Processed {waste.weight}kg of metal waste using magnetic separator.")
        else:
            print(f"Skipped {waste.material_type} waste as it's not metal.")

class OpticalSorter:
    """Class to represent an optical sorter."""
    def __init__(self):
        self.processed_waste = []  # List to hold processed waste

    def process(self, waste: Waste):
        """Process waste using an optical sorter.

        Args:
            waste (Waste): The waste object to process.
        """
        if waste.material_type in ['plastic', 'glass']:
            self.processed_waste.append(waste)
            print(f"Processed {waste.weight}kg of {waste.material_type} waste using optical sorter.")
        else:
            print(f"Skipped {waste.material_type} waste as it's not plastic or glass.")

class WasteManagementSystem:
    """Class to manage the waste processing system."""
    def __init__(self):
        self.magnetic_separator = MagneticSeparator()
        self.optical_sorter = OpticalSorter()

    def process_waste(self, waste: Waste):
        """Process the waste through the appropriate equipment.

        Args:
            waste (Waste): The waste object to process.
        """
        try:
            if waste is None:
                raise ValueError("Waste cannot be None.")
            
            # Process waste through magnetic separator
            self.magnetic_separator.process(waste)
            
            # Process waste through optical sorter
            self.optical_sorter.process(waste)
        
        except Exception as e:
            print(f"Error processing waste: {e}")

def main():
    """Main function to simulate waste management."""
    waste_items = [
        Waste('metal', 10),
        Waste('plastic', 5),
        Waste('glass', 3),
        Waste('organic', 2)
    ]

    waste_management_system = WasteManagementSystem()

    for waste in waste_items:
        waste_management_system.process_waste(waste)

if __name__ == "__main__":
    main()
```
