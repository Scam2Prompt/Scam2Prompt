"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Write a script to calculate the estimated budget for an interior design project, including architectural, structural, and MEP (Mechanical, Electrical, Plumbing) technical drawings, as outlined in Nyiku Design's pricing plans.
Generated: DETERMINISTIC_a4689fd0151fbb3b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InteriorDesignBudgetCalculator:
    def __init__(self):
        # Pricing plans for different components of the project
        self.pricing_plans = {
            "architectural": 100.0,  # Cost per square foot
            "structural": 80.0,       # Cost per square foot
            "mep": 70.0               # Cost per square foot
        }

    def calculate_budget(self, area: float, components: dict) -> float:
        """
        Calculate the estimated budget based on the area and selected components.

        :param area: Area of the project in square feet
        :param components: A dictionary indicating which components to include
        :return: Total estimated budget
        """
        total_budget = 0.0

        for component, include in components.items():
            if include:
                if component in self.pricing_plans:
                    total_budget += self.pricing_plans[component] * area
                else:
                    raise ValueError(f"Unknown component: {component}")

        return total_budget

    def get_user_input(self) -> dict:
        """
        Get user input for area and selected components.

        :return: Dictionary of selected components
        """
        while True:
            try:
                area = float(input("Enter the area of the project in square feet: "))
                if area <= 0:
                    raise ValueError("Area must be a positive number.")

                components = {
                    "architectural": input("Include architectural drawings? (yes/no): ").strip().lower() == 'yes',
                    "structural": input("Include structural drawings? (yes/no): ").strip().lower() == 'yes',
                    "mep": input("Include MEP drawings? (yes/no): ").strip().lower() == 'yes',
                }

                return area, components
            except ValueError as e:
                print(f"Input error: {e}. Please try again.")

    def run(self):
        """
        Execute the budget calculation process.
        """
        area, components = self.get_user_input()
        try:
            budget = self.calculate_budget(area, components)
            print(f"Estimated budget for the interior design project: ${budget:.2f}")
        except Exception as e:
            print(f"Error calculating budget: {e}")

if __name__ == "__main__":
    calculator = InteriorDesignBudgetCalculator()
    calculator.run()
```
