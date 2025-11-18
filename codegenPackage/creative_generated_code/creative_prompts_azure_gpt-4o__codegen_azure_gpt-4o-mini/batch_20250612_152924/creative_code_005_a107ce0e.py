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
import random

class RenovationPlan:
    """
    A class to represent a budget-friendly renovation plan for a home.
    """

    def __init__(self, budget):
        """
        Initialize the RenovationPlan with a budget.

        :param budget: Total budget for the renovation
        """
        self.budget = budget
        self.plans = []
        self.costs = {
            'Paint': 200,
            'Flooring': 1200,
            'Cabinets': 1000,
            'Lighting': 300,
            'Countertops': 800,
            'Backsplash': 600,
            'Appliances': 1500
        }

    def add_plan(self, plan_name, materials):
        """
        Add a renovation plan with materials to the plans list.

        :param plan_name: Name of the renovation plan
        :param materials: List of materials for the plan
        """
        total_cost = self.calculate_cost(materials)
        if total_cost <= self.budget:
            self.plans.append({'name': plan_name, 'materials': materials, 'cost': total_cost})
        else:
            raise ValueError(f"Total cost {total_cost} exceeds budget {self.budget}")

    def calculate_cost(self, materials):
        """
        Calculate the total cost of the given materials.

        :param materials: List of materials to calculate
        :return: Total cost of materials
        """
        return sum(self.costs[material] for material in materials if material in self.costs)

    def suggest_plan(self):
        """
        Suggest a random renovation plan from available options.

        :return: A suggested plan or None if no plans available
        """
        if self.plans:
            return random.choice(self.plans)
        return None

    def display_plans(self):
        """
        Display all available renovation plans.
        """
        if self.plans:
            for plan in self.plans:
                print(f"Plan: {plan['name']}, Materials: {', '.join(plan['materials'])}, Cost: ${plan['cost']}")
        else:
            print("No renovation plans available.")

def main():
    """
    Main function to run the renovation plan simulation.
    """
    # Set the budget for renovation
    budget = 3000
    renovation = RenovationPlan(budget)

    # Define materials for different plans
    plan1_materials = ['Paint', 'Flooring', 'Lighting']
    plan2_materials = ['Cabinets', 'Countertops', 'Paint']

    try:
        # Add plans
        renovation.add_plan("Living Room Refresh", plan1_materials)
        renovation.add_plan("Kitchen Upgrade", plan2_materials)

        # Display all plans
        renovation.display_plans()

        # Suggest a random plan
        suggested_plan = renovation.suggest_plan()
        if suggested_plan:
            print(f"Suggested Plan: {suggested_plan['name']} with a cost of ${suggested_plan['cost']}")
        else:
            print("No plans available for suggestion.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
