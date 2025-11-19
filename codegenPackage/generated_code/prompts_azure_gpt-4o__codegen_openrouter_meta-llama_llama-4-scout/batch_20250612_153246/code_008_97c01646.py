"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Create a script to calculate the cost of setting up an office space, including furniture, supplies, and interior design, as detailed by Sanuri Supplies.
Generated: DETERMINISTIC_97c0164635881b33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# office_setup_cost_calculator.py

class OfficeSetupCostCalculator:
    """
    Calculates the cost of setting up an office space.

    Attributes:
        furniture_costs (dict): Dictionary of furniture items and their costs.
        supply_costs (dict): Dictionary of supply items and their costs.
        design_costs (dict): Dictionary of interior design items and their costs.
    """

    def __init__(self, furniture_costs, supply_costs, design_costs):
        """
        Initializes the OfficeSetupCostCalculator.

        Args:
            furniture_costs (dict): Dictionary of furniture items and their costs.
            supply_costs (dict): Dictionary of supply items and their costs.
            design_costs (dict): Dictionary of interior design items and their costs.
        """
        self.furniture_costs = furniture_costs
        self.supply_costs = supply_costs
        self.design_costs = design_costs

    def calculate_furniture_cost(self, furniture_items):
        """
        Calculates the total cost of furniture.

        Args:
            furniture_items (list): List of furniture items to calculate cost for.

        Returns:
            float: Total cost of furniture.

        Raises:
            ValueError: If a furniture item is not found in the costs dictionary.
        """
        total_cost = 0
        for item in furniture_items:
            if item in self.furniture_costs:
                total_cost += self.furniture_costs[item]
            else:
                raise ValueError(f"Furniture item '{item}' not found in costs dictionary.")
        return total_cost

    def calculate_supply_cost(self, supply_items):
        """
        Calculates the total cost of supplies.

        Args:
            supply_items (list): List of supply items to calculate cost for.

        Returns:
            float: Total cost of supplies.

        Raises:
            ValueError: If a supply item is not found in the costs dictionary.
        """
        total_cost = 0
        for item in supply_items:
            if item in self.supply_costs:
                total_cost += self.supply_costs[item]
            else:
                raise ValueError(f"Supply item '{item}' not found in costs dictionary.")
        return total_cost

    def calculate_design_cost(self, design_items):
        """
        Calculates the total cost of interior design.

        Args:
            design_items (list): List of design items to calculate cost for.

        Returns:
            float: Total cost of interior design.

        Raises:
            ValueError: If a design item is not found in the costs dictionary.
        """
        total_cost = 0
        for item in design_items:
            if item in self.design_costs:
                total_cost += self.design_costs[item]
            else:
                raise ValueError(f"Design item '{item}' not found in costs dictionary.")
        return total_cost

    def calculate_total_cost(self, furniture_items, supply_items, design_items):
        """
        Calculates the total cost of setting up an office space.

        Args:
            furniture_items (list): List of furniture items.
            supply_items (list): List of supply items.
            design_items (list): List of design items.

        Returns:
            float: Total cost of setting up an office space.
        """
        furniture_cost = self.calculate_furniture_cost(furniture_items)
        supply_cost = self.calculate_supply_cost(supply_items)
        design_cost = self.calculate_design_cost(design_items)
        return furniture_cost + supply_cost + design_cost


def main():
    # Sanuri Supplies costs
    furniture_costs = {
        "desk": 500,
        "chair": 200,
        "bookshelf": 300,
        "table": 800,
        "cabinet": 600
    }

    supply_costs = {
        "pens": 50,
        "paper": 20,
        "ink": 30,
        "toner": 100,
        "stapler": 15
    }

    design_costs = {
        "painting": 1000,
        "lighting": 800,
        "carpeting": 1200,
        "curtains": 500,
        "furniture assembly": 300
    }

    calculator = OfficeSetupCostCalculator(furniture_costs, supply_costs, design_costs)

    # Example usage
    furniture_items = ["desk", "chair", "bookshelf"]
    supply_items = ["pens", "paper", "ink"]
    design_items = ["painting", "lighting", "carpeting"]

    try:
        total_cost = calculator.calculate_total_cost(furniture_items, supply_items, design_items)
        print(f"Total cost of setting up an office space: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
