"""
Generated Code Metadata:
========================
Original URL: https://naimatabbasind.com
Prompt: "Write a code snippet to calculate production costs for customized sports gloves, considering material costs, labor costs, and overhead expenses."
Generated: DETERMINISTIC_976db47ccbe4daea
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# production_cost_calculator.py

class ProductionCostCalculator:
    """
    Calculates production costs for customized sports gloves.

    Attributes:
        material_costs (dict): Material costs with quantities.
        labor_cost (float): Labor cost per hour.
        labor_hours (float): Labor hours required per unit.
        overhead_expenses (float): Overhead expenses as a percentage of total costs.
    """

    def __init__(self, material_costs, labor_cost, labor_hours, overhead_expenses):
        """
        Initializes the ProductionCostCalculator.

        Args:
            material_costs (dict): Material costs with quantities (e.g., {"leather": 10.0, "thread": 0.5}).
            labor_cost (float): Labor cost per hour.
            labor_hours (float): Labor hours required per unit.
            overhead_expenses (float): Overhead expenses as a percentage of total costs.
        """
        self.material_costs = material_costs
        self.labor_cost = labor_cost
        self.labor_hours = labor_hours
        self.overhead_expenses = overhead_expenses / 100  # Convert to decimal

    def calculate_material_cost(self):
        """
        Calculates the total material cost.

        Returns:
            float: Total material cost.
        """
        return sum(cost for cost in self.material_costs.values())

    def calculate_labor_cost(self):
        """
        Calculates the total labor cost.

        Returns:
            float: Total labor cost.
        """
        return self.labor_cost * self.labor_hours

    def calculate_overhead_cost(self, total_cost):
        """
        Calculates the overhead cost.

        Args:
            total_cost (float): Total cost (material + labor).

        Returns:
            float: Overhead cost.
        """
        return total_cost * self.overhead_expenses

    def calculate_production_cost(self):
        """
        Calculates the total production cost.

        Returns:
            float: Total production cost.
        """
        material_cost = self.calculate_material_cost()
        labor_cost = self.calculate_labor_cost()
        total_cost = material_cost + labor_cost
        overhead_cost = self.calculate_overhead_cost(total_cost)
        return total_cost + overhead_cost


def main():
    try:
        # Example usage
        material_costs = {"leather": 5.0, "thread": 0.25, "padding": 1.5}
        labor_cost = 20.0  # per hour
        labor_hours = 0.5  # per unit
        overhead_expenses = 15.0  # percentage

        calculator = ProductionCostCalculator(material_costs, labor_cost, labor_hours, overhead_expenses)
        production_cost = calculator.calculate_production_cost()

        print(f"Production cost: ${production_cost:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
