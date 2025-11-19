"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to assess the feasibility of adaptive reuse projects, using Carolina Capital's strategy as a reference point.
Generated: DETERMINISTIC_b1f50754e6d92215
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# adaptive_reuse_feasibility.py

import pandas as pd

class AdaptiveReuseProject:
    """
    Evaluates the feasibility of an adaptive reuse project based on Carolina Capital's strategy.
    """

    def __init__(self, project_data):
        """
        Initializes the AdaptiveReuseProject with project data.

        Args:
            project_data (dict): Dictionary containing project data.
                Required keys:
                    - 'purchase_price'
                    - 'rehabilitation_cost'
                    - 'projected_rent'
                    - 'vacancy_rate'
                    - 'operating_expenses'
                    - 'desired_cap_rate'
        """
        self.project_data = project_data

    def calculate_projected_income(self):
        """
        Calculates the projected annual income.

        Returns:
            float: Projected annual income.
        """
        try:
            projected_rent = self.project_data['projected_rent']
            vacancy_rate = self.project_data['vacancy_rate']
            gross_potential_income = projected_rent * 12
            vacancy_loss = gross_potential_income * vacancy_rate
            projected_income = gross_potential_income - vacancy_loss
            return projected_income
        except KeyError as e:
            raise ValueError(f"Missing required project data: {e}")

    def calculate_operating_expenses(self):
        """
        Calculates the annual operating expenses.

        Returns:
            float: Annual operating expenses.
        """
        try:
            operating_expenses = self.project_data['operating_expenses']
            return operating_expenses
        except KeyError as e:
            raise ValueError(f"Missing required project data: {e}")

    def calculate_net_operating_income(self):
        """
        Calculates the net operating income (NOI).

        Returns:
            float: Net operating income.
        """
        projected_income = self.calculate_projected_income()
        operating_expenses = self.calculate_operating_expenses()
        noi = projected_income - operating_expenses
        return noi

    def calculate_capitalization_rate(self):
        """
        Calculates the capitalization rate.

        Returns:
            float: Capitalization rate.
        """
        try:
            purchase_price = self.project_data['purchase_price']
            rehabilitation_cost = self.project_data['rehabilitation_cost']
            total_investment = purchase_price + rehabilitation_cost
            noi = self.calculate_net_operating_income()
            cap_rate = noi / total_investment
            return cap_rate
        except KeyError as e:
            raise ValueError(f"Missing required project data: {e}")

    def assess_feasibility(self):
        """
        Assesses the feasibility of the adaptive reuse project.

        Returns:
            bool: True if the project's cap rate meets the desired cap rate, False otherwise.
        """
        try:
            desired_cap_rate = self.project_data['desired_cap_rate']
            cap_rate = self.calculate_capitalization_rate()
            return cap_rate >= desired_cap_rate
        except KeyError as e:
            raise ValueError(f"Missing required project data: {e}")


def main():
    project_data = {
        'purchase_price': 1000000,
        'rehabilitation_cost': 500000,
        'projected_rent': 2000,
        'vacancy_rate': 0.05,
        'operating_expenses': 30000,
        'desired_cap_rate': 0.08
    }

    project = AdaptiveReuseProject(project_data)

    print("Project Data:")
    for key, value in project.project_data.items():
        print(f"{key}: {value}")

    print("\nProjected Income: $", project.calculate_projected_income())
    print("Operating Expenses: $", project.calculate_operating_expenses())
    print("Net Operating Income: $", project.calculate_net_operating_income())
    print("Capitalization Rate: ", project.calculate_capitalization_rate())
    print("Feasible: ", project.assess_feasibility())


if __name__ == "__main__":
    main()
```
