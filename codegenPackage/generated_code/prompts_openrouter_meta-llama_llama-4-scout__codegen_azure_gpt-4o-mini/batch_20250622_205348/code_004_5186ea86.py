"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Create a code example for implementing a fixed management fee structure in a property development project management tool.
Generated: DETERMINISTIC_5186ea8624b3ccb0
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyDevelopmentProject:
    """
    A class to represent a property development project with a fixed management fee structure.
    """

    def __init__(self, project_name: str, total_budget: float, management_fee_percentage: float):
        """
        Initializes a new property development project.

        :param project_name: The name of the project.
        :param total_budget: The total budget allocated for the project.
        :param management_fee_percentage: The fixed management fee percentage of the total budget.
        """
        if total_budget <= 0:
            raise ValueError("Total budget must be greater than zero.")
        if not (0 <= management_fee_percentage <= 100):
            raise ValueError("Management fee percentage must be between 0 and 100.")

        self.project_name = project_name
        self.total_budget = total_budget
        self.management_fee_percentage = management_fee_percentage
        self.management_fee = self.calculate_management_fee()

    def calculate_management_fee(self) -> float:
        """
        Calculates the management fee based on the total budget and management fee percentage.

        :return: The calculated management fee.
        """
        return (self.management_fee_percentage / 100) * self.total_budget

    def display_project_details(self) -> None:
        """
        Displays the details of the project including the management fee.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Total Budget: ${self.total_budget:,.2f}")
        print(f"Management Fee Percentage: {self.management_fee_percentage}%")
        print(f"Management Fee: ${self.management_fee:,.2f}")

# Example usage
if __name__ == "__main__":
    try:
        project = PropertyDevelopmentProject("Greenfield Development", 1000000, 5)
        project.display_project_details()
    except ValueError as e:
        print(f"Error: {e}")
```
