"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: Develop a script to calculate cost estimates for electrical projects, incorporating affordability principles from Think Tech Engineering.
Generated: DETERMINISTIC_a41fdb7dc30aee7c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_project_estimator.py

"""
Electrical Project Estimator
============================
This script calculates cost estimates for electrical projects based on affordability principles from Think Tech Engineering.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class ElectricalProjectEstimator:
    def __init__(self, project_name, project_type, material_costs, labor_costs):
        """
        Initializes the estimator with project details.

        Args:
            project_name (str): Name of the project.
            project_type (str): Type of electrical project (e.g., residential, commercial).
            material_costs (dict): Dictionary of material costs with units (e.g., {'copper_wire': 1.50, 'circuit_breaker': 20.00}).
            labor_costs (dict): Dictionary of labor costs with units (e.g., {'electrician': 50.00, 'assistant': 30.00}).
        """
        self.project_name = project_name
        self.project_type = project_type
        self.material_costs = material_costs
        self.labor_costs = labor_costs

    def calculate_material_cost(self, quantities):
        """
        Calculates the total material cost.

        Args:
            quantities (dict): Dictionary of material quantities (e.g., {'copper_wire': 100, 'circuit_breaker': 5}).

        Returns:
            float: Total material cost.
        """
        if set(quantities.keys()) != set(self.material_costs.keys()):
            raise ValueError("Material quantities do not match material costs")

        total_material_cost = sum(quantities[material] * self.material_costs[material] for material in quantities)
        return total_material_cost

    def calculate_labor_cost(self, labor_hours):
        """
        Calculates the total labor cost.

        Args:
            labor_hours (dict): Dictionary of labor hours (e.g., {'electrician': 10, 'assistant': 5}).

        Returns:
            float: Total labor cost.
        """
        if set(labor_hours.keys()) != set(self.labor_costs.keys()):
            raise ValueError("Labor hours do not match labor costs")

        total_labor_cost = sum(labor_hours[labor] * self.labor_costs[labor] for labor in labor_hours)
        return total_labor_cost

    def estimate_total_cost(self, quantities, labor_hours):
        """
        Estimates the total project cost.

        Args:
            quantities (dict): Dictionary of material quantities.
            labor_hours (dict): Dictionary of labor hours.

        Returns:
            float: Total project cost.
        """
        total_material_cost = self.calculate_material_cost(quantities)
        total_labor_cost = self.calculate_labor_cost(labor_hours)
        total_cost = total_material_cost + total_labor_cost
        return total_cost

    def apply_affordability_principles(self, total_cost):
        """
        Applies affordability principles from Think Tech Engineering.

        Args:
            total_cost (float): Total project cost.

        Returns:
            float: Adjusted project cost.
        """
        # Assume a 10% reduction in cost for affordable solutions
        adjusted_cost = total_cost * 0.9
        return adjusted_cost


def main():
    try:
        project_name = "Residential Electrical Project"
        project_type = "residential"

        material_costs = {
            'copper_wire': 1.50,
            'circuit_breaker': 20.00,
            'outlets': 5.00,
            'switches': 3.00
        }

        labor_costs = {
            'electrician': 50.00,
            'assistant': 30.00
        }

        estimator = ElectricalProjectEstimator(project_name, project_type, material_costs, labor_costs)

        quantities = {
            'copper_wire': 100,
            'circuit_breaker': 5,
            'outlets': 20,
            'switches': 10
        }

        labor_hours = {
            'electrician': 10,
            'assistant': 5
        }

        total_cost = estimator.estimate_total_cost(quantities, labor_hours)
        adjusted_cost = estimator.apply_affordability_principles(total_cost)

        print(f"Project Name: {project_name}")
        print(f"Project Type: {project_type}")
        print(f"Total Material Cost: ${estimator.calculate_material_cost(quantities):.2f}")
        print(f"Total Labor Cost: ${estimator.calculate_labor_cost(labor_hours):.2f}")
        print(f"Total Project Cost: ${total_cost:.2f}")
        print(f"Adjusted Project Cost (Affordable): ${adjusted_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
