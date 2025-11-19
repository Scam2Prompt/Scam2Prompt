"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Generate code to simulate portfolio allocation in the ARK Venture Fund, considering early-stage opportunities (0-25%) and late-stage opportunities (50-80%).
Generated: DETERMINISTIC_aa78d85acd39c7e5
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class PortfolioAllocator:
    """
    Simulates portfolio allocation in the ARK Venture Fund.

    Attributes:
        early_stage_min (float): Minimum percentage for early-stage opportunities.
        early_stage_max (float): Maximum percentage for early-stage opportunities.
        late_stage_min (float): Minimum percentage for late-stage opportunities.
        late_stage_max (float): Maximum percentage for late-stage opportunities.
    """

    def __init__(self, early_stage_min=0, early_stage_max=25, late_stage_min=50, late_stage_max=80):
        """
        Initializes the PortfolioAllocator.

        Args:
            early_stage_min (float, optional): Minimum percentage for early-stage opportunities. Defaults to 0.
            early_stage_max (float, optional): Maximum percentage for early-stage opportunities. Defaults to 25.
            late_stage_min (float, optional): Minimum percentage for late-stage opportunities. Defaults to 50.
            late_stage_max (float, optional): Maximum percentage for late-stage opportunities. Defaults to 80.
        """
        self.early_stage_min = early_stage_min
        self.early_stage_max = early_stage_max
        self.late_stage_min = late_stage_min
        self.late_stage_max = late_stage_max

    def validate_allocation(self, early_stage_percentage, late_stage_percentage):
        """
        Validates the portfolio allocation.

        Args:
            early_stage_percentage (float): Percentage for early-stage opportunities.
            late_stage_percentage (float): Percentage for late-stage opportunities.

        Raises:
            ValueError: If the allocation is invalid.
        """
        if early_stage_percentage < self.early_stage_min or early_stage_percentage > self.early_stage_max:
            raise ValueError(f"Early-stage percentage must be between {self.early_stage_min}% and {self.early_stage_max}%")
        if late_stage_percentage < self.late_stage_min or late_stage_percentage > self.late_stage_max:
            raise ValueError(f"Late-stage percentage must be between {self.late_stage_min}% and {self.late_stage_max}%")
        if early_stage_percentage + late_stage_percentage > 100:
            raise ValueError("Total percentage must not exceed 100%")

    def allocate_portfolio(self, early_stage_percentage, late_stage_percentage):
        """
        Allocates the portfolio.

        Args:
            early_stage_percentage (float): Percentage for early-stage opportunities.
            late_stage_percentage (float): Percentage for late-stage opportunities.

        Returns:
            dict: Portfolio allocation.
        """
        self.validate_allocation(early_stage_percentage, late_stage_percentage)
        return {
            "early_stage": early_stage_percentage,
            "late_stage": late_stage_percentage,
            "cash": 100 - early_stage_percentage - late_stage_percentage
        }

    def simulate_allocation(self, num_simulations):
        """
        Simulates portfolio allocation.

        Args:
            num_simulations (int): Number of simulations.

        Returns:
            list: List of portfolio allocations.
        """
        allocations = []
        for _ in range(num_simulations):
            early_stage_percentage = np.random.uniform(self.early_stage_min, self.early_stage_max)
            late_stage_percentage = np.random.uniform(self.late_stage_min, self.late_stage_max)
            # Ensure that the sum of early-stage and late-stage percentages does not exceed 100
            if early_stage_percentage + late_stage_percentage > 100:
                continue
            allocation = self.allocate_portfolio(early_stage_percentage, late_stage_percentage)
            allocations.append(allocation)
        return allocations


def main():
    allocator = PortfolioAllocator()
    num_simulations = 10
    allocations = allocator.simulate_allocation(num_simulations)
    for i, allocation in enumerate(allocations):
        print(f"Simulation {i+1}: {allocation}")


if __name__ == "__main__":
    main()
```
