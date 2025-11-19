"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Write a Python script to calculate the environmental impact of a construction project, factoring in metrics like hours worked and resources used, inspired by INARO S.A.S.'s focus on project optimization.
Generated: DETERMINISTIC_45328cf5a54939f9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class EnvironmentalImpactCalculator:
    """
    Calculates the environmental impact of a construction project.

    Attributes:
        hours_worked (float): Total hours worked on the project.
        resources_used (dict): Dictionary of resources used, with units.
    """

    def __init__(self, hours_worked=0, resources_used=None):
        """
        Initializes the EnvironmentalImpactCalculator.

        Args:
            hours_worked (float, optional): Total hours worked. Defaults to 0.
            resources_used (dict, optional): Dictionary of resources used. Defaults to None.
        """
        self.hours_worked = hours_worked
        self.resources_used = resources_used if resources_used else {}

    def add_resource(self, name, quantity, unit):
        """
        Adds a resource to the resources used.

        Args:
            name (str): Name of the resource.
            quantity (float): Quantity of the resource used.
            unit (str): Unit of the resource (e.g., kg, liters, etc.).
        """
        self.resources_used[name] = {"quantity": quantity, "unit": unit}

    def calculate_carbon_footprint(self):
        """
        Calculates the carbon footprint based on hours worked and resources used.

        Returns:
            float: Carbon footprint in kg CO2e.
        """
        # Define emission factors (kg CO2e per unit)
        emission_factors = {
            "electricity": 0.643,  # kg CO2e per kWh
            "fuel": 0.243,  # kg CO2e per liter
            "concrete": 0.130,  # kg CO2e per kg
            "steel": 2.860,  # kg CO2e per kg
        }

        carbon_footprint = 0

        # Calculate carbon footprint from hours worked (assuming 0.025 kg CO2e per hour)
        carbon_footprint += self.hours_worked * 0.025

        # Calculate carbon footprint from resources used
        for resource, details in self.resources_used.items():
            if resource in emission_factors:
                carbon_footprint += details["quantity"] * emission_factors[resource]
            else:
                print(f"Warning: No emission factor found for {resource}.")

        return carbon_footprint

    def calculate_water_usage(self):
        """
        Calculates the water usage based on resources used.

        Returns:
            float: Water usage in liters.
        """
        water_usage = 0

        # Define water usage factors (liters per unit)
        water_usage_factors = {
            "concrete": 100,  # liters per kg
            "steel": 10,  # liters per kg
        }

        for resource, details in self.resources_used.items():
            if resource in water_usage_factors:
                water_usage += details["quantity"] * water_usage_factors[resource]

        return water_usage

    def calculate_waste_generation(self):
        """
        Calculates the waste generation based on resources used.

        Returns:
            float: Waste generation in kg.
        """
        waste_generation = 0

        # Define waste generation factors (kg per unit)
        waste_generation_factors = {
            "concrete": 0.1,  # kg per kg
            "steel": 0.05,  # kg per kg
        }

        for resource, details in self.resources_used.items():
            if resource in waste_generation_factors:
                waste_generation += details["quantity"] * waste_generation_factors[resource]

        return waste_generation


def main():
    try:
        calculator = EnvironmentalImpactCalculator(hours_worked=1000)

        calculator.add_resource("electricity", 1000, "kWh")
        calculator.add_resource("fuel", 500, "liters")
        calculator.add_resource("concrete", 10000, "kg")
        calculator.add_resource("steel", 5000, "kg")

        carbon_footprint = calculator.calculate_carbon_footprint()
        water_usage = calculator.calculate_water_usage()
        waste_generation = calculator.calculate_waste_generation()

        print(f"Carbon Footprint: {carbon_footprint:.2f} kg CO2e")
        print(f"Water Usage: {water_usage:.2f} liters")
        print(f"Waste Generation: {waste_generation:.2f} kg")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
