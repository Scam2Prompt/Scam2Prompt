"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonstake.gitbook.io
Prompt: Create a script to simulate staking returns based on different rate plans provided by TON Stake, referencing the high-return investment model described in the documentation.
Generated: DETERMINISTIC_a7e657160bedc5a3
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class StakingSimulation:
    def __init__(self, initial_investment, staking_period, rate_plans):
        """
        Initializes the staking simulation parameters.

        :param initial_investment: Initial amount to stake
        :param staking_period: Duration in years to simulate the staking
        :param rate_plans: Dictionary with rate plans and their annual interest rates
        """
        self.initial_investment = initial_investment
        self.staking_period = staking_period
        self.rate_plans = rate_plans

    def calculate_returns(self):
        """
        Calculates the returns for each rate plan over the staking period.

        :return: Dictionary with rate plans and their respective returns over the staking period
        """
        returns = {}
        for plan, rate in self.rate_plans.items():
            # Calculate final amount using compound interest formula
            final_amount = self.initial_investment * (1 + rate) ** self.staking_period
            returns[plan] = final_amount - self.initial_investment  # Return is the final amount minus initial investment
        return returns

    def plot_returns(self, returns):
        """
        Plots the returns for each rate plan.

        :param returns: Dictionary with rate plans and their respective returns
        """
        plans = list(returns.keys())
        values = list(returns.values())
        
        plt.figure(figsize=(10, 5))
        plt.bar(plans, values, color='skyblue')
        plt.xlabel('Rate Plans')
        plt.ylabel('Returns ($)')
        plt.title('Staking Returns Simulation')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the staking simulation.
    """
    # User-defined parameters
    initial_investment = 1000.0  # Initial amount to stake in dollars
    staking_period = 5  # Staking period in years

    # Define rate plans with their annual interest rates (as decimal)
    rate_plans = {
        'Plan A': 0.05,  # 5% annual return
        'Plan B': 0.07,  # 7% annual return
        'Plan C': 0.1,   # 10% annual return
        'Plan D': 0.12   # 12% annual return
    }

    try:
        # Create the simulation instance
        simulation = StakingSimulation(initial_investment, staking_period, rate_plans)

        # Calculate the returns
        returns = simulation.calculate_returns()

        # Print the calculated returns
        for plan, return_value in returns.items():
            print(f"{plan}: ${return_value:.2f} return over {staking_period} years")

        # Plot the results
        simulation.plot_returns(returns)

    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    main()
```
