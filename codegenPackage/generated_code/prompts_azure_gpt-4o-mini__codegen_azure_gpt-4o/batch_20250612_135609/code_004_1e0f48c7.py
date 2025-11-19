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
# fit_out_costs.py

class FitOutCostCalculator:
    """
    A library class to calculate estimated costs for fit-out works based on material and labor inputs.
    """

    def __init__(self):
        """
        Initializes the FitOutCostCalculator instance.
        """
        self.material_costs = {}
        self.labor_costs = {}

    def add_material_cost(self, material_name, cost_per_unit):
        """
        Adds or updates the cost of a material.

        :param material_name: str - Name of the material.
        :param cost_per_unit: float - Cost per unit of the material.
        :raises ValueError: If cost_per_unit is negative.
        """
        if cost_per_unit < 0:
            raise ValueError("Cost per unit cannot be negative.")
        self.material_costs[material_name] = cost_per_unit

    def add_labor_cost(self, role, hourly_rate):
        """
        Adds or updates the hourly rate for a labor role.

        :param role: str - Name of the labor role (e.g., carpenter, electrician).
        :param hourly_rate: float - Hourly rate for the labor role.
        :raises ValueError: If hourly_rate is negative.
        """
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self.labor_costs[role] = hourly_rate

    def calculate_material_cost(self, material_quantities):
        """
        Calculates the total material cost based on quantities provided.

        :param material_quantities: dict - A dictionary where keys are material names and values are quantities.
        :return: float - Total material cost.
        :raises KeyError: If a material in material_quantities is not found in material_costs.
        """
        total_cost = 0.0
        for material, quantity in material_quantities.items():
            if material not in self.material_costs:
                raise KeyError(f"Material '{material}' not found in material costs.")
            total_cost += self.material_costs[material] * quantity
        return total_cost

    def calculate_labor_cost(self, labor_hours):
        """
        Calculates the total labor cost based on hours worked.

        :param labor_hours: dict - A dictionary where keys are labor roles and values are hours worked.
        :return: float - Total labor cost.
        :raises KeyError: If a labor role in labor_hours is not found in labor_costs.
        """
        total_cost = 0.0
        for role, hours in labor_hours.items():
            if role not in self.labor_costs:
                raise KeyError(f"Labor role '{role}' not found in labor costs.")
            total_cost += self.labor_costs[role] * hours
        return total_cost

    def calculate_total_cost(self, material_quantities, labor_hours):
        """
        Calculates the total fit-out cost based on material and labor inputs.

        :param material_quantities: dict - A dictionary where keys are material names and values are quantities.
        :param labor_hours: dict - A dictionary where keys are labor roles and values are hours worked.
        :return: float - Total fit-out cost.
        """
        material_cost = self.calculate_material_cost(material_quantities)
        labor_cost = self.calculate_labor_cost(labor_hours)
        return material_cost + labor_cost


# Example usage (uncomment to test):
# calculator = FitOutCostCalculator()
# calculator.add_material_cost("Wood", 50.0)
# calculator.add_material_cost("Paint", 20.0)
# calculator.add_labor_cost("Carpenter", 30.0)
# calculator.add_labor_cost("Painter", 25.0)
# material_quantities = {"Wood": 10, "Paint": 5}
# labor_hours = {"Carpenter": 8, "Painter": 6}
# total_cost = calculator.calculate_total_cost(material_quantities, labor_hours)
# print(f"Total fit-out cost: ${total_cost:.2f}")
```
