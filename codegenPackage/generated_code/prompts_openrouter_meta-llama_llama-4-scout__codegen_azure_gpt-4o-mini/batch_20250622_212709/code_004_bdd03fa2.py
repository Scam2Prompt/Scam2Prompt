"""
Generated Code Metadata:
========================
Original URL: https://vidrosdu.blogspot.com
Prompt: Provide a Python script to create a glass installation plan, including material selection and measurement validation, based on the tips provided in the VIDROS DU blog.
Generated: DETERMINISTIC_bdd03fa284cae3c9
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class GlassInstallationPlan:
    def __init__(self):
        self.materials = []
        self.measurements = {}

    def add_material(self, material_name, quantity):
        """Add a material to the installation plan."""
        if not isinstance(material_name, str) or not isinstance(quantity, (int, float)):
            raise ValueError("Material name must be a string and quantity must be a number.")
        self.materials.append({'name': material_name, 'quantity': quantity})

    def set_measurement(self, dimension, value):
        """Set a measurement for the installation plan."""
        if not isinstance(dimension, str) or not self.validate_measurement(value):
            raise ValueError("Dimension must be a string and value must be a positive number.")
        self.measurements[dimension] = value

    @staticmethod
    def validate_measurement(value):
        """Validate that the measurement value is a positive number."""
        return isinstance(value, (int, float)) and value > 0

    def generate_plan(self):
        """Generate the installation plan summary."""
        if not self.materials:
            raise ValueError("No materials added to the installation plan.")
        if not self.measurements:
            raise ValueError("No measurements set for the installation plan.")

        plan_summary = {
            'materials': self.materials,
            'measurements': self.measurements
        }
        return plan_summary

    def display_plan(self):
        """Display the installation plan in a readable format."""
        try:
            plan = self.generate_plan()
            print("Glass Installation Plan:")
            print("Materials:")
            for material in plan['materials']:
                print(f" - {material['name']}: {material['quantity']}")
            print("Measurements:")
            for dimension, value in plan['measurements'].items():
                print(f" - {dimension}: {value}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage of the GlassInstallationPlan class
    try:
        installation_plan = GlassInstallationPlan()
        installation_plan.add_material("Tempered Glass", 10)
        installation_plan.add_material("Silicone Sealant", 5)
        installation_plan.set_measurement("Height", 2.5)  # in meters
        installation_plan.set_measurement("Width", 1.5)   # in meters
        installation_plan.display_plan()
    except Exception as e:
        print(f"An error occurred: {e}")
```
