"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Generate a script to calculate cost estimates for mechanical installations, factoring in labor, materials, and equipment, as outlined in C&M Pinnacle's service offerings.
Generated: DETERMINISTIC_0215f8025ac85655
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CostEstimator:
    """
    A class to estimate costs for mechanical installations based on labor, materials, and equipment.
    """

    def __init__(self, labor_rate, material_costs, equipment_costs):
        """
        Initializes the CostEstimator with labor rate, material costs, and equipment costs.

        :param labor_rate: Hourly labor rate (float)
        :param material_costs: Dictionary of material costs (dict)
        :param equipment_costs: Dictionary of equipment costs (dict)
        """
        self.labor_rate = labor_rate
        self.material_costs = material_costs
        self.equipment_costs = equipment_costs

    def calculate_labor_cost(self, hours):
        """
        Calculates the labor cost based on hours worked.

        :param hours: Number of hours worked (float)
        :return: Labor cost (float)
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        return self.labor_rate * hours

    def calculate_material_cost(self, materials):
        """
        Calculates the total material cost based on the materials used.

        :param materials: Dictionary of materials and their quantities (dict)
        :return: Total material cost (float)
        """
        total_cost = 0.0
        for material, quantity in materials.items():
            if material not in self.material_costs:
                raise ValueError(f"Material '{material}' not found in cost list.")
            if quantity < 0:
                raise ValueError(f"Quantity for material '{material}' cannot be negative.")
            total_cost += self.material_costs[material] * quantity
        return total_cost

    def calculate_equipment_cost(self, equipment):
        """
        Calculates the total equipment cost based on the equipment used.

        :param equipment: Dictionary of equipment and their quantities (dict)
        :return: Total equipment cost (float)
        """
        total_cost = 0.0
        for item, quantity in equipment.items():
            if item not in self.equipment_costs:
                raise ValueError(f"Equipment '{item}' not found in cost list.")
            if quantity < 0:
                raise ValueError(f"Quantity for equipment '{item}' cannot be negative.")
            total_cost += self.equipment_costs[item] * quantity
        return total_cost

    def estimate_total_cost(self, hours, materials, equipment):
        """
        Estimates the total cost for the installation.

        :param hours: Number of hours worked (float)
        :param materials: Dictionary of materials and their quantities (dict)
        :param equipment: Dictionary of equipment and their quantities (dict)
        :return: Total estimated cost (float)
        """
        labor_cost = self.calculate_labor_cost(hours)
        material_cost = self.calculate_material_cost(materials)
        equipment_cost = self.calculate_equipment_cost(equipment)
        total_cost = labor_cost + material_cost + equipment_cost
        return total_cost

def main():
    # Example data for costs
    labor_rate = 50.0  # Example labor rate per hour
    material_costs = {
        'pipe': 2.5,
        'fittings': 1.0,
        'insulation': 0.75
    }
    equipment_costs = {
        'wrench': 10.0,
        'drill': 25.0
    }

    # Create an instance of CostEstimator
    estimator = CostEstimator(labor_rate, material_costs, equipment_costs)

    # Example input for estimation
    hours_worked = 10
    materials_used = {
        'pipe': 20,
        'fittings': 15
    }
    equipment_used = {
        'wrench': 2,
        'drill': 1
    }

    try:
        total_estimated_cost = estimator.estimate_total_cost(hours_worked, materials_used, equipment_used)
        print(f"Total Estimated Cost: ${total_estimated_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
