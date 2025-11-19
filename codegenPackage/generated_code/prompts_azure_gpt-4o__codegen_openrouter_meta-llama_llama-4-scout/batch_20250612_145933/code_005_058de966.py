"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Write a script to model the risk-adjusted returns across multiple investment cycles, as emphasized in Bi-Verse's investment philosophy.
Generated: DETERMINISTIC_058de9669186d214
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Investment:
    def __init__(self, initial_investment, returns, risk_free_rate, risk_tolerance):
        """
        Initialize an Investment object.

        Args:
        - initial_investment (float): The initial amount invested.
        - returns (list or np.array): A list or array of returns for each cycle.
        - risk_free_rate (float): The risk-free rate of return.
        - risk_tolerance (float): The investor's risk tolerance.
        """
        self.initial_investment = initial_investment
        self.returns = np.array(returns)
        self.risk_free_rate = risk_free_rate
        self.risk_tolerance = risk_tolerance

    def calculate_risk_adjusted_returns(self):
        """
        Calculate the risk-adjusted returns using the Sharpe Ratio.

        Returns:
        - sharpe_ratio (float): The Sharpe Ratio for the investment.
        """
        excess_returns = self.returns - self.risk_free_rate
        volatility = np.std(self.returns)
        if volatility == 0:
            raise ValueError("Volatility is zero. Cannot calculate Sharpe Ratio.")
        sharpe_ratio = np.mean(excess_returns) / volatility
        return sharpe_ratio

    def simulate_investment_cycles(self, num_cycles):
        """
        Simulate multiple investment cycles.

        Args:
        - num_cycles (int): The number of cycles to simulate.

        Returns:
        - A pandas DataFrame with the results of each cycle.
        """
        results = []
        current_investment = self.initial_investment
        for i in range(num_cycles):
            # Simulate a return for this cycle
            cycle_return = np.random.normal(np.mean(self.returns), np.std(self.returns))
            current_investment *= (1 + cycle_return)
            results.append({
                'Cycle': i+1,
                'Return': cycle_return,
                'Investment Value': current_investment
            })
        return pd.DataFrame(results)

    def evaluate_investment(self, num_cycles):
        """
        Evaluate the investment by simulating multiple cycles and calculating risk-adjusted returns.

        Args:
        - num_cycles (int): The number of cycles to simulate.

        Returns:
        - A tuple containing the Sharpe Ratio and a DataFrame with the results of each cycle.
        """
        sharpe_ratio = self.calculate_risk_adjusted_returns()
        results_df = self.simulate_investment_cycles(num_cycles)
        return sharpe_ratio, results_df


def main():
    # Example usage
    initial_investment = 10000
    returns = [0.03, 0.05, -0.02, 0.01, 0.04]  # Example returns
    risk_free_rate = 0.01
    risk_tolerance = 0.05
    num_cycles = 100

    investment = Investment(initial_investment, returns, risk_free_rate, risk_tolerance)
    sharpe_ratio, results_df = investment.evaluate_investment(num_cycles)

    print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
    print(results_df)

    # Plot the investment value over time
    plt.figure(figsize=(10,6))
    plt.plot(results_df['Cycle'], results_df['Investment Value'])
    plt.xlabel('Cycle')
    plt.ylabel('Investment Value')
    plt.title('Investment Value Over Time')
    plt.show()


if __name__ == "__main__":
    main()
```
