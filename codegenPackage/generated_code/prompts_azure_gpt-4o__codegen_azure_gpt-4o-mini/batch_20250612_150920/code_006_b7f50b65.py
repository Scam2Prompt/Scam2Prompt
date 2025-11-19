"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Generate Python code to calculate the environmental impact of construction projects, considering methods like brick construction commonly used in Argentina.
Generated: DETERMINISTIC_b7f50b6547e3aa7b
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ConstructionProject:
    """
    A class to represent a construction project and calculate its environmental impact.
    """

    def __init__(self, project_name, area, material_type, material_quantity):
        """
        Initializes the ConstructionProject with the given parameters.

        :param project_name: Name of the construction project
        :param area: Area of the construction in square meters
        :param material_type: Type of construction material (e.g., 'brick', 'concrete')
        :param material_quantity: Quantity of the material used
        """
        self.project_name = project_name
        self.area = area
        self.material_type = material_type
        self.material_quantity = material_quantity
        self.emission_factors = {
            'brick': 0.5,  # kg CO2 per kg of brick
            'concrete': 0.9,  # kg CO2 per kg of concrete
            # Add more materials and their emission factors as needed
        }

    def calculate_emissions(self):
        """
        Calculates the total CO2 emissions for the construction project based on the material type and quantity.

        :return: Total CO2 emissions in kg
        :raises ValueError: If the material type is not recognized
        """
        if self.material_type not in self.emission_factors:
            raise ValueError(f"Material type '{self.material_type}' is not recognized.")

        emissions = self.material_quantity * self.emission_factors[self.material_type]
        return emissions

    def display_report(self):
        """
        Displays a report of the construction project's environmental impact.
        """
        try:
            total_emissions = self.calculate_emissions()
            print(f"Project Name: {self.project_name}")
            print(f"Area: {self.area} m²")
            print(f"Material Type: {self.material_type}")
            print(f"Material Quantity: {self.material_quantity} kg")
            print(f"Total CO2 Emissions: {total_emissions:.2f} kg")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    """
    Main function to execute the environmental impact calculation for a construction project.
    """
    # Example project data
    project_name = "Residential Building"
    area = 150  # in square meters
    material_type = "brick"
    material_quantity = 1000  # in kg

    # Create a ConstructionProject instance
    project = ConstructionProject(project_name, area, material_type, material_quantity)

    # Display the environmental impact report
    project.display_report()

if __name__ == "__main__":
    main()
```
