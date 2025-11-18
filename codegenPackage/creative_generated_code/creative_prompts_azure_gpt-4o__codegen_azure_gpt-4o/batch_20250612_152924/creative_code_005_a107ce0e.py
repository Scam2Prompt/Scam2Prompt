"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uaeinterior.com
Prompt: Write code to simulate budget-friendly renovation plans for homes, incorporating cost-effective materials and designs, inspired by Amazing Interior's renovation services.
Generated: DETERMINISTIC_a107ce0e331daa79
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class RenovationPlan:
    """
    A class to simulate budget-friendly renovation plans for homes.
    Inspired by Amazing Interior's renovation services.
    """

    def __init__(self, budget):
        """
        Initialize the renovation plan with a given budget.

        :param budget: The total budget for the renovation (float).
        """
        if budget <= 0:
            raise ValueError("Budget must be greater than zero.")
        self.budget = budget
        self.materials = []
        self.designs = []
        self.costs = []

    def add_material(self, name, cost_per_unit, quantity):
        """
        Add a material to the renovation plan.

        :param name: Name of the material (str).
        :param cost_per_unit: Cost per unit of the material (float).
        :param quantity: Quantity of the material needed (int).
        """
        if cost_per_unit <= 0 or quantity <= 0:
            raise ValueError("Cost per unit and quantity must be greater than zero.")
        total_cost = cost_per_unit * quantity
        self.materials.append({
            "name": name,
            "cost_per_unit": cost_per_unit,
            "quantity": quantity,
            "total_cost": total_cost
        })

    def add_design(self, name, cost):
        """
        Add a design to the renovation plan.

        :param name: Name of the design (str).
        :param cost: Cost of the design (float).
        """
        if cost <= 0:
            raise ValueError("Design cost must be greater than zero.")
        self.designs.append({
            "name": name,
            "cost": cost
        })

    def calculate_total_cost(self):
        """
        Calculate the total cost of the renovation plan.

        :return: Total cost (float).
        """
        total_material_cost = sum(material["total_cost"] for material in self.materials)
        total_design_cost = sum(design["cost"] for design in self.designs)
        self.costs = {
            "materials": total_material_cost,
            "designs": total_design_cost,
            "total": total_material_cost + total_design_cost
        }
        return self.costs["total"]

    def is_within_budget(self):
        """
        Check if the renovation plan is within the budget.

        :return: True if within budget, False otherwise.
        """
        return self.calculate_total_cost() <= self.budget

    def generate_report(self, file_name="renovation_plan_report.json"):
        """
        Generate a detailed report of the renovation plan in JSON format.

        :param file_name: Name of the file to save the report (str).
        """
        report = {
            "budget": self.budget,
            "materials": self.materials,
            "designs": self.designs,
            "costs": self.costs,
            "within_budget": self.is_within_budget()
        }
        try:
            with open(file_name, "w") as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully generated: {file_name}")
        except IOError as e:
            print(f"Error writing to file: {e}")


# Example usage:

if __name__ == "__main__":
    try:
        # Create a renovation plan with a $5000 budget
        plan = RenovationPlan(5000)

        # Add materials
        plan.add_material("Paint", 20.0, 50)  # $20 per can, 50 cans
        plan.add_material("Flooring", 2.5, 200)  # $2.5 per sq.ft, 200 sq.ft

        # Add designs
        plan.add_design("Minimalist Living Room", 1000.0)
        plan.add_design("Modern Kitchen", 1500.0)

        # Check if the plan is within budget
        print("Total cost:", plan.calculate_total_cost())
        print("Within budget:", plan.is_within_budget())

        # Generate a report
        plan.generate_report()

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
