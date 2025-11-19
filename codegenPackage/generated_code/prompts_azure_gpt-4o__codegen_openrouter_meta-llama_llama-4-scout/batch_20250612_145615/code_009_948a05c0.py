"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Develop a program to calculate the environmental impact of architectural materials used in projects like those described by Linea 7, emphasizing sustainability and livability.
Generated: DETERMINISTIC_948a05c00322f84c
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class Material:
    """Represents an architectural material with its environmental impact data."""

    def __init__(self, name, material_type, energy_consumption, water_consumption, 
                 greenhouse_gas_emissions, recyclable, reusable):
        """
        Initializes a Material object.

        Args:
            name (str): Name of the material.
            material_type (str): Type of the material (e.g., steel, concrete, wood).
            energy_consumption (float): Energy consumption of the material in kWh/kg.
            water_consumption (float): Water consumption of the material in liters/kg.
            greenhouse_gas_emissions (float): Greenhouse gas emissions of the material in kg CO2e/kg.
            recyclable (bool): Whether the material is recyclable.
            reusable (bool): Whether the material is reusable.
        """
        self.name = name
        self.material_type = material_type
        self.energy_consumption = energy_consumption
        self.water_consumption = water_consumption
        self.greenhouse_gas_emissions = greenhouse_gas_emissions
        self.recyclable = recyclable
        self.reusable = reusable

    def calculate_environmental_impact(self, quantity):
        """
        Calculates the environmental impact of a given quantity of the material.

        Args:
            quantity (float): Quantity of the material in kg.

        Returns:
            dict: Environmental impact data, including energy consumption, water consumption, 
                  and greenhouse gas emissions.
        """
        energy_impact = self.energy_consumption * quantity
        water_impact = self.water_consumption * quantity
        emissions_impact = self.greenhouse_gas_emissions * quantity

        return {
            "energy_consumption": energy_impact,
            "water_consumption": water_impact,
            "greenhouse_gas_emissions": emissions_impact
        }


class Project:
    """Represents an architectural project with its materials and environmental impact data."""

    def __init__(self, name):
        """
        Initializes a Project object.

        Args:
            name (str): Name of the project.
        """
        self.name = name
        self.materials = []

    def add_material(self, material, quantity):
        """
        Adds a material to the project.

        Args:
            material (Material): Material object.
            quantity (float): Quantity of the material in kg.
        """
        self.materials.append((material, quantity))

    def calculate_total_environmental_impact(self):
        """
        Calculates the total environmental impact of all materials in the project.

        Returns:
            dict: Total environmental impact data, including energy consumption, water consumption, 
                  and greenhouse gas emissions.
        """
        total_energy_impact = 0
        total_water_impact = 0
        total_emissions_impact = 0

        for material, quantity in self.materials:
            impact = material.calculate_environmental_impact(quantity)
            total_energy_impact += impact["energy_consumption"]
            total_water_impact += impact["water_consumption"]
            total_emissions_impact += impact["greenhouse_gas_emissions"]

        return {
            "energy_consumption": total_energy_impact,
            "water_consumption": total_water_impact,
            "greenhouse_gas_emissions": total_emissions_impact
        }

    def assess_sustainability(self):
        """
        Assesses the sustainability of the project based on its environmental impact.

        Returns:
            str: Sustainability assessment (e.g., "sustainable", "moderately sustainable", "not sustainable").
        """
        total_impact = self.calculate_total_environmental_impact()

        if total_impact["greenhouse_gas_emissions"] < 1000 and total_impact["energy_consumption"] < 5000:
            return "sustainable"
        elif total_impact["greenhouse_gas_emissions"] < 5000 and total_impact["energy_consumption"] < 20000:
            return "moderately sustainable"
        else:
            return "not sustainable"


def main():
    try:
        # Create materials
        steel = Material("Steel", "metal", 10.5, 2.1, 2.5, True, False)
        concrete = Material("Concrete", "cement", 5.2, 10.5, 0.2, False, False)
        wood = Material("Wood", "wood", 1.1, 0.5, 0.1, False, True)

        # Create project
        project = Project("Linea7 Project")

        # Add materials to project
        project.add_material(steel, 10000)
        project.add_material(concrete, 50000)
        project.add_material(wood, 5000)

        # Calculate environmental impact
        total_impact = project.calculate_total_environmental_impact()

        # Print results
        print("Environmental Impact:")
        print(f"Energy Consumption: {total_impact['energy_consumption']} kWh")
        print(f"Water Consumption: {total_impact['water_consumption']} liters")
        print(f"Greenhouse Gas Emissions: {total_impact['greenhouse_gas_emissions']} kg CO2e")

        # Assess sustainability
        sustainability = project.assess_sustainability()
        print(f"\nSustainability Assessment: {sustainability}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
