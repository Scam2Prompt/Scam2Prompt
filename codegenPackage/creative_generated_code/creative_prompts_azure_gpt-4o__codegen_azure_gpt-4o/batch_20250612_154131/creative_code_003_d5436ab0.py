"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write code to simulate portfolio diversification for the ARK Venture Fund, considering its allocation percentages for early-stage (0-25%) and late-stage (50-80%) opportunities.
Generated: DETERMINISTIC_d5436ab0574f6f2c
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class PortfolioDiversification:
    """
    Class to simulate portfolio diversification for ARK Venture Fund.
    Allocation percentages:
    - Early-stage opportunities: 0-25%
    - Late-stage opportunities: 50-80%
    """

    def __init__(self):
        # Allocation limits
        self.early_stage_min = 0
        self.early_stage_max = 25
        self.late_stage_min = 50
        self.late_stage_max = 80

    def simulate_allocation(self):
        """
        Simulates portfolio allocation percentages for early-stage and late-stage opportunities.
        Ensures the total allocation is within 100% and respects constraints.

        Returns:
            dict: Allocation percentages for early-stage and late-stage opportunities.
        """
        while True:
            # Random allocation for early-stage within bounds
            early_stage_allocation = random.randint(self.early_stage_min, self.early_stage_max)

            # Remaining percentage available for late-stage (maximum 100%)
            remaining_percentage = 100 - early_stage_allocation

            # Ensure late-stage allocation is within bounds and fits the portfolio
            if self.late_stage_min <= remaining_percentage <= self.late_stage_max:
                late_stage_allocation = remaining_percentage
                return {
                    "early_stage": early_stage_allocation,
                    "late_stage": late_stage_allocation,
                }

    def display_allocation(self, allocation):
        """
        Displays the simulated allocation in a user-friendly format.

        Args:
            allocation (dict): Allocation percentages for early-stage and late-stage opportunities.
        """
        print("Portfolio Diversification Allocation:")
        print(f"  Early-stage opportunities: {allocation['early_stage']}%")
        print(f"  Late-stage opportunities: {allocation['late_stage']}%")


def main():
    """
    Main function to run the portfolio diversification simulation.
    """
    try:
        # Create a PortfolioDiversification instance
        portfolio_simulator = PortfolioDiversification()

        # Simulate allocation
        allocation = portfolio_simulator.simulate_allocation()

        # Display the allocation
        portfolio_simulator.display_allocation(allocation)

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the program
    main()
```
