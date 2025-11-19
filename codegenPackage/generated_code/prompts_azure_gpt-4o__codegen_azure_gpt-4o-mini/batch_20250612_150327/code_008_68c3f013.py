"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a function to calculate the carbon footprint reduction achieved by switching to FSC-certified materials, inspired by PDC Brush's practices.
Generated: DETERMINISTIC_68c3f01328340858
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarbonFootprintCalculator:
    """
    A class to calculate the carbon footprint reduction achieved by switching to FSC-certified materials.
    """

    def __init__(self, current_material_footprint, fsc_material_footprint):
        """
        Initializes the CarbonFootprintCalculator with the current and FSC-certified material footprints.

        :param current_material_footprint: The carbon footprint of the current materials (in kg CO2e).
        :param fsc_material_footprint: The carbon footprint of the FSC-certified materials (in kg CO2e).
        """
        if current_material_footprint < 0 or fsc_material_footprint < 0:
            raise ValueError("Carbon footprint values must be non-negative.")

        self.current_material_footprint = current_material_footprint
        self.fsc_material_footprint = fsc_material_footprint

    def calculate_reduction(self):
        """
        Calculates the carbon footprint reduction achieved by switching to FSC-certified materials.

        :return: The reduction in carbon footprint (in kg CO2e).
        """
        reduction = self.current_material_footprint - self.fsc_material_footprint
        
        if reduction < 0:
            raise ValueError("FSC material footprint cannot be greater than current material footprint.")
        
        return reduction

    def display_reduction(self):
        """
        Displays the carbon footprint reduction in a user-friendly format.
        """
        try:
            reduction = self.calculate_reduction()
            print(f"Carbon footprint reduction achieved by switching to FSC-certified materials: {reduction} kg CO2e")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Example values for current and FSC-certified material footprints
        current_footprint = 1000  # kg CO2e
        fsc_footprint = 600       # kg CO2e

        calculator = CarbonFootprintCalculator(current_footprint, fsc_footprint)
        calculator.display_reduction()
    except Exception as e:
        print(f"An error occurred: {e}")
```
