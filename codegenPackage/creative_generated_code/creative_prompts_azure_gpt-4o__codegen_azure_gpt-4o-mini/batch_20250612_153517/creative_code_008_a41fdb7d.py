"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thinktech.com.pk
Prompt: Develop a script to calculate cost estimates for electrical projects, incorporating affordability principles from Think Tech Engineering.
Generated: DETERMINISTIC_a41fdb7dc30aee7c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ElectricalProjectEstimator:
    """
    A class to estimate costs for electrical projects based on various input parameters.
    Incorporates affordability principles from Think Tech Engineering.
    """

    def __init__(self):
        self.base_cost_per_unit = 100  # Base cost per unit of electrical work
        self.affordability_factor = 0.85  # Maximum percentage of budget to be spent on electrical work

    def calculate_cost(self, units: float, budget: float) -> float:
        """
        Calculate the estimated cost of an electrical project.

        :param units: The number of units of work to be performed.
        :param budget: The total budget available for the project.
        :return: Estimated cost of the project.
        :raises ValueError: If units or budget are negative.
        """
        if units < 0 or budget < 0:
            raise ValueError("Units and budget must be non-negative.")

        # Calculate preliminary cost based on units
        preliminary_cost = units * self.base_cost_per_unit
        
        # Apply affordability principle
        if preliminary_cost > budget * self.affordability_factor:
            raise ValueError("Estimated cost exceeds affordability based on the budget.")

        return preliminary_cost

    def generate_cost_estimate_report(self, units: float, budget: float) -> str:
        """
        Generate a cost estimate report in JSON format.

        :param units: The number of units of work to be performed.
        :param budget: The total budget available for the project.
        :return: JSON formatted string of the cost estimate report.
        :raises ValueError: If units or budget are negative or if cost exceeds budget.
        """
        estimated_cost = self.calculate_cost(units, budget)
        report = {
            "units": units,
            "budget": budget,
            "estimated_cost": estimated_cost,
            "affordability_status": estimated_cost <= budget * self.affordability_factor
        }
        return json.dumps(report, indent=4)

def main():
    estimator = ElectricalProjectEstimator()
    
    # Example inputs
    units = 10  # Number of units of electrical work
    budget = 1200  # Total project budget

    try:
        report = estimator.generate_cost_estimate_report(units, budget)
        print("Cost Estimate Report:")
        print(report)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
