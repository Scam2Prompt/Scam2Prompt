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
import json

class OfficeSetupCostCalculator:
    """
    A class to calculate the total cost of setting up an office space.
    It includes costs for furniture, supplies, and interior design.
    """

    def __init__(self, furniture_costs, supplies_costs, design_costs):
        """
        Initializes the calculator with costs for furniture, supplies, and design.

        :param furniture_costs: Dictionary containing furniture items and their costs
        :param supplies_costs: Dictionary containing supplies items and their costs
        :param design_costs: Dictionary containing design items and their costs
        """
        self.furniture_costs = furniture_costs
        self.supplies_costs = supplies_costs
        self.design_costs = design_costs

    def calculate_total_cost(self):
        """
        Calculates the total cost of setting up the office.

        :return: Total cost as a float
        """
        try:
            total_furniture_cost = sum(self.furniture_costs.values())
            total_supplies_cost = sum(self.supplies_costs.values())
            total_design_cost = sum(self.design_costs.values())

            total_cost = total_furniture_cost + total_supplies_cost + total_design_cost
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

    def display_cost_breakdown(self):
        """
        Displays a breakdown of costs for furniture, supplies, and design.
        """
        try:
            print("Cost Breakdown:")
            print("Furniture Costs:")
            for item, cost in self.furniture_costs.items():
                print(f"  {item}: ${cost:.2f}")

            print("\nSupplies Costs:")
            for item, cost in self.supplies_costs.items():
                print(f"  {item}: ${cost:.2f}")

            print("\nDesign Costs:")
            for item, cost in self.design_costs.items():
                print(f"  {item}: ${cost:.2f}")

            total_cost = self.calculate_total_cost()
            if total_cost is not None:
                print(f"\nTotal Cost: ${total_cost:.2f}")
        except Exception as e:
            print(f"Error displaying cost breakdown: {e}")

def main():
    """
    Main function to execute the office setup cost calculator.
    """
    # Sample data for costs
    furniture_costs = {
        "Desk": 300.00,
        "Chair": 150.00,
        "Bookshelf": 200.00
    }

    supplies_costs = {
        "Stationery": 50.00,
        "Printer": 120.00,
        "Paper": 30.00
    }

    design_costs = {
        "Wall Paint": 250.00,
        "Lighting": 100.00,
        "Decor": 150.00
    }

    # Create an instance of the calculator
    calculator = OfficeSetupCostCalculator(furniture_costs, supplies_costs, design_costs)

    # Display the cost breakdown
    calculator.display_cost_breakdown()

if __name__ == "__main__":
    main()
```
