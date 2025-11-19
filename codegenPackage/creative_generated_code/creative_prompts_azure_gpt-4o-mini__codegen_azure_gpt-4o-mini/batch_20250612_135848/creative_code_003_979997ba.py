"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitaprojects.co.za
Prompt: Develop a code example that integrates a fixed management fee structure into a project management application for luxury real estate developers.
Generated: DETERMINISTIC_979997ba3e3ab0af
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Project:
    """
    Class to represent a project for luxury real estate developers.
    """

    def __init__(self, name: str, budget: float, management_fee_rate: float):
        """
        Initialize a new project.

        :param name: The name of the project.
        :param budget: The total budget for the project.
        :param management_fee_rate: The fixed management fee rate (as a decimal).
        """
        self.name = name
        self.budget = budget
        self.management_fee_rate = management_fee_rate
        self.management_fee = self.calculate_management_fee()

    def calculate_management_fee(self) -> float:
        """
        Calculate the management fee based on the project budget.

        :return: The calculated management fee.
        """
        if self.budget < 0:
            raise ValueError("Budget must be a non-negative value.")
        
        management_fee = self.budget * self.management_fee_rate
        return management_fee

    def total_project_cost(self) -> float:
        """
        Calculate the total cost of the project including management fee.

        :return: The total cost of the project.
        """
        total_cost = self.budget + self.management_fee
        return total_cost

    def __str__(self):
        """
        String representation of the project details.

        :return: A string summarizing the project details.
        """
        return (f"Project Name: {self.name}\n"
                f"Budget: ${self.budget:.2f}\n"
                f"Management Fee Rate: {self.management_fee_rate:.2%}\n"
                f"Management Fee: ${self.management_fee:.2f}\n"
                f"Total Project Cost: ${self.total_project_cost():.2f}")


def main():
    """
    Main function to execute the project management fee calculation.
    """
    try:
        # Example of creating a new project
        project_name = "Luxury Villa Development"
        project_budget = 5000000.00  # Example budget in dollars
        management_fee_rate = 0.05  # 5% management fee

        # Create a Project instance
        luxury_project = Project(project_name, project_budget, management_fee_rate)

        # Output project details
        print(luxury_project)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
