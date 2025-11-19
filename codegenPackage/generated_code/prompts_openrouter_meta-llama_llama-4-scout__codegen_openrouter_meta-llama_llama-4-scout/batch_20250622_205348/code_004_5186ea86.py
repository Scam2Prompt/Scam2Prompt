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
# management_fee_structure.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class FeeType(Enum):
    """Management fee types."""
    FIXED = "fixed"
    PERCENTAGE = "percentage"

@dataclass
class ManagementFee:
    """Management fee data class."""
    fee_type: FeeType
    amount: float  # amount in currency (e.g., dollars)

@dataclass
class Project:
    """Project data class."""
    id: int
    name: str
    management_fee: ManagementFee
    total_project_cost: float  # total project cost in currency (e.g., dollars)

class ManagementFeeCalculator:
    """Management fee calculator class."""

    def calculate_management_fee(self, project: Project) -> float:
        """Calculates the management fee for a given project.

        Args:
            project (Project): The project to calculate the management fee for.

        Returns:
            float: The calculated management fee.

        Raises:
            ValueError: If the project management fee type is not supported.
        """
        if project.management_fee.fee_type == FeeType.FIXED:
            return project.management_fee.amount
        elif project.management_fee.fee_type == FeeType.PERCENTAGE:
            return (project.management_fee.amount / 100) * project.total_project_cost
        else:
            raise ValueError("Unsupported management fee type")

    def calculate_total_project_cost_with_fee(self, project: Project) -> float:
        """Calculates the total project cost including the management fee.

        Args:
            project (Project): The project to calculate the total cost for.

        Returns:
            float: The total project cost including the management fee.

        Raises:
            ValueError: If the project management fee type is not supported.
        """
        management_fee = self.calculate_management_fee(project)
        return project.total_project_cost + management_fee

def main():
    try:
        # Create a project with a fixed management fee
        project = Project(
            id=1,
            name="Example Project",
            management_fee=ManagementFee(FeeType.FIXED, 10000.0),
            total_project_cost=1000000.0
        )

        calculator = ManagementFeeCalculator()

        # Calculate and print the management fee
        management_fee = calculator.calculate_management_fee(project)
        print(f"Management Fee: ${management_fee:.2f}")

        # Calculate and print the total project cost including the management fee
        total_project_cost_with_fee = calculator.calculate_total_project_cost_with_fee(project)
        print(f"Total Project Cost with Fee: ${total_project_cost_with_fee:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
