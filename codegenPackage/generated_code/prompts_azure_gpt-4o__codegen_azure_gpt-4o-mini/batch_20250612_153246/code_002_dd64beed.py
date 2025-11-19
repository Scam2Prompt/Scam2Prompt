"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Generate a script to calculate the cost estimation for roads and highways construction projects, incorporating factors mentioned on the Bismillah Traders site.
Generated: DETERMINISTIC_dd64beed66640cc6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class RoadConstructionEstimator:
    def __init__(self, base_cost_per_km, material_costs, labor_costs, overhead_percentage):
        """
        Initializes the estimator with base costs and overhead.

        :param base_cost_per_km: Base cost of construction per kilometer
        :param material_costs: Dictionary of material costs per unit
        :param labor_costs: Dictionary of labor costs per hour
        :param overhead_percentage: Percentage of overhead costs
        """
        self.base_cost_per_km = base_cost_per_km
        self.material_costs = material_costs
        self.labor_costs = labor_costs
        self.overhead_percentage = overhead_percentage

    def calculate_material_cost(self, materials):
        """
        Calculates the total material cost based on the materials used.

        :param materials: Dictionary of materials and their quantities
        :return: Total material cost
        """
        total_material_cost = 0
        for material, quantity in materials.items():
            if material in self.material_costs:
                total_material_cost += self.material_costs[material] * quantity
            else:
                raise ValueError(f"Material '{material}' not found in material costs.")
        return total_material_cost

    def calculate_labor_cost(self, labor_hours):
        """
        Calculates the total labor cost based on hours worked.

        :param labor_hours: Dictionary of labor types and their hours
        :return: Total labor cost
        """
        total_labor_cost = 0
        for labor_type, hours in labor_hours.items():
            if labor_type in self.labor_costs:
                total_labor_cost += self.labor_costs[labor_type] * hours
            else:
                raise ValueError(f"Labor type '{labor_type}' not found in labor costs.")
        return total_labor_cost

    def estimate_total_cost(self, length_km, materials, labor_hours):
        """
        Estimates the total cost of the road construction project.

        :param length_km: Length of the road in kilometers
        :param materials: Dictionary of materials and their quantities
        :param labor_hours: Dictionary of labor types and their hours
        :return: Total estimated cost
        """
        try:
            base_cost = self.base_cost_per_km * length_km
            material_cost = self.calculate_material_cost(materials)
            labor_cost = self.calculate_labor_cost(labor_hours)
            overhead_cost = (base_cost + material_cost + labor_cost) * (self.overhead_percentage / 100)

            total_cost = base_cost + material_cost + labor_cost + overhead_cost
            return total_cost
        except Exception as e:
            print(f"Error estimating total cost: {e}")
            return None

def main():
    # Example configuration
    base_cost_per_km = 50000  # Base cost per kilometer
    material_costs = {
        'asphalt': 100,  # Cost per ton
        'gravel': 50,    # Cost per ton
        'concrete': 120   # Cost per cubic meter
    }
    labor_costs = {
        'construction_worker': 20,  # Cost per hour
        'supervisor': 30             # Cost per hour
    }
    overhead_percentage = 10  # Overhead percentage

    # Create an instance of the estimator
    estimator = RoadConstructionEstimator(base_cost_per_km, material_costs, labor_costs, overhead_percentage)

    # Define project parameters
    length_km = 10  # Length of the road in kilometers
    materials = {
        'asphalt': 200,  # Quantity in tons
        'gravel': 100,   # Quantity in tons
        'concrete': 50   # Quantity in cubic meters
    }
    labor_hours = {
        'construction_worker': 160,  # Total hours
        'supervisor': 40              # Total hours
    }

    # Estimate total cost
    total_cost = estimator.estimate_total_cost(length_km, materials, labor_hours)
    if total_cost is not None:
        print(f"Total estimated cost for the road construction project: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
