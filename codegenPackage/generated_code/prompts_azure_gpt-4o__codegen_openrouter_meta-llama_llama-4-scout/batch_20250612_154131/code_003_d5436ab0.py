"""
Generated Code Metadata:
========================
Original URL: https://arkventureshares.com
Prompt: Write code to simulate portfolio diversification for the ARK Venture Fund, considering its allocation percentages for early-stage (0-25%) and late-stage (50-80%) opportunities.
Generated: DETERMINISTIC_d5436ab0574f6f2c
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

class PortfolioDiversificationSimulator:
    """
    Simulates portfolio diversification for the ARK Venture Fund.

    Attributes:
        early_stage_allocation (float): Allocation percentage for early-stage opportunities (0-25%).
        late_stage_allocation (float): Allocation percentage for late-stage opportunities (50-80%).
        total_investment (float): Total investment amount.
    """

    def __init__(self, early_stage_allocation, late_stage_allocation, total_investment):
        """
        Initializes the simulator with allocation percentages and total investment amount.

        Args:
            early_stage_allocation (float): Allocation percentage for early-stage opportunities.
            late_stage_allocation (float): Allocation percentage for late-stage opportunities.
            total_investment (float): Total investment amount.

        Raises:
            ValueError: If early-stage allocation is not between 0 and 25.
            ValueError: If late-stage allocation is not between 50 and 80.
            ValueError: If total investment amount is not positive.
        """
        if not 0 <= early_stage_allocation <= 25:
            raise ValueError("Early-stage allocation must be between 0 and 25")
        if not 50 <= late_stage_allocation <= 80:
            raise ValueError("Late-stage allocation must be between 50 and 80")
        if total_investment <= 0:
            raise ValueError("Total investment amount must be positive")

        self.early_stage_allocation = early_stage_allocation / 100
        self.late_stage_allocation = late_stage_allocation / 100
        self.total_investment = total_investment

    def simulate_portfolio(self):
        """
        Simulates the portfolio diversification.

        Returns:
            dict: Dictionary containing the allocation amounts for early-stage and late-stage opportunities.
        """
        early_stage_investment = self.total_investment * self.early_stage_allocation
        late_stage_investment = self.total_investment * self.late_stage_allocation

        return {
            "early_stage": early_stage_investment,
            "late_stage": late_stage_investment,
            "unallocated": self.total_investment - (early_stage_investment + late_stage_investment)
        }

    def run_simulation(self, num_simulations):
        """
        Runs multiple simulations of the portfolio diversification.

        Args:
            num_simulations (int): Number of simulations to run.

        Returns:
            list: List of dictionaries containing the allocation amounts for each simulation.
        """
        results = []
        for _ in range(num_simulations):
            results.append(self.simulate_portfolio())

        return results

def main():
    try:
        simulator = PortfolioDiversificationSimulator(15, 65, 1000000)
        results = simulator.run_simulation(10)

        for i, result in enumerate(results):
            print(f"Simulation {i+1}:")
            print(f"Early-stage: ${result['early_stage']:.2f}")
            print(f"Late-stage: ${result['late_stage']:.2f}")
            print(f"Unallocated: ${result['unallocated']:.2f}")
            print()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
