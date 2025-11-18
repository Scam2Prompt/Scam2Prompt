"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vfmadvisory.com
Prompt: Write a script to simulate project financing scenarios, including raising finance and underwriting, based on VfM Advisory's consulting services.
Generated: DETERMINISTIC_976b98147329f444
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ProjectFinancingSimulation:
    """
    A class to simulate project financing scenarios, including raising finance and underwriting.
    """

    def __init__(self, project_name, total_project_cost, consulting_fees_percentage):
        """
        Initialize the financing simulation.

        :param project_name: Name of the project
        :param total_project_cost: The total cost of the project
        :param consulting_fees_percentage: Percentage of consulting fees charged by VfM Advisory
        """
        self.project_name = project_name
        self.total_project_cost = total_project_cost
        self.consulting_fees_percentage = consulting_fees_percentage
        self.raised_finance = 0
        self.underwriting_amount = 0

    def raise_finance(self, amount):
        """
        Simulate raising finance for the project.

        :param amount: Amount to raise
        :return: Updated raised finance
        """
        try:
            if amount <= 0:
                raise ValueError("Finance amount must be greater than zero.")
            self.raised_finance += amount
            return self.raised_finance
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_consulting_fees(self):
        """
        Calculate consulting fees based on VfM Advisory's services.

        :return: Consulting fees
        """
        return round(self.total_project_cost * (self.consulting_fees_percentage / 100), 2)

    def underwrite_project(self, percentage):
        """
        Simulate underwriting a portion of the project's cost.

        :param percentage: Percentage of the project cost to underwrite
        :return: Updated underwriting amount
        """
        try:
            if percentage <= 0 or percentage > 100:
                raise ValueError("Underwriting percentage must be between 0 and 100.")
            self.underwriting_amount = round(self.total_project_cost * (percentage / 100), 2)
            return self.underwriting_amount
        except ValueError as e:
            print(f"Error: {e}")

    def simulate_scenario(self):
        """
        Simulate a financing scenario by randomly raising finance and underwriting.

        :return: A dictionary summarizing the scenario
        """
        # Randomly simulate raising finance between 10% and 50% of the total project cost
        random_raise_percentage = random.uniform(10, 50)
        raised_finance_amount = round(self.total_project_cost * (random_raise_percentage / 100), 2)
        self.raise_finance(raised_finance_amount)

        # Randomly simulate underwriting between 20% and 70% of the total project cost
        random_underwriting_percentage = random.uniform(20, 70)
        underwriting_amount = self.underwrite_project(random_underwriting_percentage)

        # Calculate consulting fees
        consulting_fees = self.calculate_consulting_fees()

        # Return a summary of the scenario
        return {
            "Project Name": self.project_name,
            "Total Project Cost": self.total_project_cost,
            "Raised Finance": self.raised_finance,
            "Underwriting Amount": underwriting_amount,
            "Consulting Fees": consulting_fees
        }


if __name__ == "__main__":
    # Example usage of the simulation

    # Define project parameters
    project_name = "Green Energy Project"
    total_project_cost = 5000000  # $5,000,000
    consulting_fees_percentage = 2.5  # 2.5% consulting fees

    # Create a simulation instance
    simulation = ProjectFinancingSimulation(project_name, total_project_cost, consulting_fees_percentage)

    # Simulate a scenario
    scenario_summary = simulation.simulate_scenario()

    # Print the scenario summary
    print("Project Financing Scenario Summary:")
    for key, value in scenario_summary.items():
        print(f"{key}: ${value if isinstance(value, (int, float)) else value}")
```
