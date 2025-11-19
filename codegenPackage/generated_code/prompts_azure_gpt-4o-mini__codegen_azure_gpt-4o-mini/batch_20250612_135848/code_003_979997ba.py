"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Develop a code example that integrates a fixed management fee structure into a project management application for luxury real estate developers.
Generated: DETERMINISTIC_979997ba3e3ab0af
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Project:
    """
    A class to represent a real estate project.

    Attributes:
        name (str): The name of the project.
        budget (float): The total budget for the project.
        management_fee_percentage (float): The fixed management fee percentage.
    """

    def __init__(self, name: str, budget: float, management_fee_percentage: float):
        """
        Initializes a new Project instance.

        Args:
            name (str): The name of the project.
            budget (float): The total budget for the project.
            management_fee_percentage (float): The fixed management fee percentage.

        Raises:
            ValueError: If budget or management_fee_percentage is negative.
        """
        if budget < 0:
            raise ValueError("Budget must be a non-negative value.")
        if not (0 <= management_fee_percentage <= 100):
            raise ValueError("Management fee percentage must be between 0 and 100.")

        self.name = name
        self.budget = budget
        self.management_fee_percentage = management_fee_percentage

    def calculate_management_fee(self) -> float:
        """
        Calculates the management fee based on the project's budget.

        Returns:
            float: The calculated management fee.
        """
        management_fee = (self.management_fee_percentage / 100) * self.budget
        return management_fee

    def __str__(self) -> str:
        """
        Returns a string representation of the project.

        Returns:
            str: A string describing the project.
        """
        return f"Project Name: {self.name}, Budget: ${self.budget:.2f}, Management Fee: ${self.calculate_management_fee():.2f}"


def main():
    """
    Main function to demonstrate the Project class functionality.
    """
    try:
        # Example project creation
        project_name = "Luxury Villa Development"
        project_budget = 5000000.00  # Total budget in dollars
        management_fee_percentage = 5.0  # Management fee percentage

        # Create a new project instance
        project = Project(project_name, project_budget, management_fee_percentage)

        # Output project details
        print(project)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
