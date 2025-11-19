"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Develop a library function that calculates the estimated costs for fit-out works based on material and labor inputs in a contracting context.
Generated: DETERMINISTIC_1e0f48c751fe221e
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FitOutCostEstimator:
    """
    A class to estimate the costs for fit-out works based on material and labor inputs.
    """

    def __init__(self):
        """
        Initializes the FitOutCostEstimator with default values.
        """
        self.material_costs = {}
        self.labor_costs = {}

    def add_material_cost(self, material_name: str, cost_per_unit: float):
        """
        Adds a material cost to the estimator.

        :param material_name: Name of the material
        :param cost_per_unit: Cost per unit of the material
        :raises ValueError: If cost_per_unit is negative
        """
        if cost_per_unit < 0:
            raise ValueError("Cost per unit cannot be negative.")
        self.material_costs[material_name] = cost_per_unit

    def add_labor_cost(self, labor_type: str, cost_per_hour: float):
        """
        Adds a labor cost to the estimator.

        :param labor_type: Type of labor (e.g., electrician, plumber)
        :param cost_per_hour: Cost per hour of labor
        :raises ValueError: If cost_per_hour is negative
        """
        if cost_per_hour < 0:
            raise ValueError("Cost per hour cannot be negative.")
        self.labor_costs[labor_type] = cost_per_hour

    def estimate_cost(self, materials: dict, labor: dict) -> float:
        """
        Estimates the total cost based on materials and labor inputs.

        :param materials: A dictionary with material names as keys and quantities as values
        :param labor: A dictionary with labor types as keys and hours as values
        :return: Total estimated cost
        :raises KeyError: If a material or labor type is not found
        """
        total_cost = 0.0

        # Calculate material costs
        for material, quantity in materials.items():
            if material not in self.material_costs:
                raise KeyError(f"Material '{material}' not found in material costs.")
            total_cost += self.material_costs[material] * quantity

        # Calculate labor costs
        for labor_type, hours in labor.items():
            if labor_type not in self.labor_costs:
                raise KeyError(f"Labor type '{labor_type}' not found in labor costs.")
            total_cost += self.labor_costs[labor_type] * hours

        return total_cost

# Example usage:
if __name__ == "__main__":
    estimator = FitOutCostEstimator()
    estimator.add_material_cost("Drywall", 12.50)
    estimator.add_material_cost("Paint", 25.00)
    estimator.add_labor_cost("Electrician", 50.00)
    estimator.add_labor_cost("Painter", 40.00)

    materials_needed = {
        "Drywall": 100,  # 100 units of drywall
        "Paint": 10      # 10 units of paint
    }

    labor_needed = {
        "Electrician": 8,  # 8 hours of electrician work
        "Painter": 5        # 5 hours of painter work
    }

    try:
        total_estimated_cost = estimator.estimate_cost(materials_needed, labor_needed)
        print(f"Total Estimated Cost: ${total_estimated_cost:.2f}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
