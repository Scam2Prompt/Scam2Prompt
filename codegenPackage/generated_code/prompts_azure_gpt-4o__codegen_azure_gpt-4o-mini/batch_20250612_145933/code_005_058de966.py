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

class InvestmentCycle:
    """
    A class to model an investment cycle and calculate risk-adjusted returns.
    """

    def __init__(self, returns: np.ndarray, risk_free_rate: float):
        """
        Initializes the InvestmentCycle with returns and risk-free rate.

        :param returns: A numpy array of investment returns.
        :param risk_free_rate: The risk-free rate of return.
        """
        self.returns = returns
        self.risk_free_rate = risk_free_rate

    def calculate_sharpe_ratio(self) -> float:
        """
        Calculates the Sharpe Ratio for the investment cycle.

        :return: The Sharpe Ratio.
        """
        excess_returns = self.returns - self.risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns)

    def calculate_sortino_ratio(self) -> float:
        """
        Calculates the Sortino Ratio for the investment cycle.

        :return: The Sortino Ratio.
        """
        downside_returns = self.returns[self.returns < self.risk_free_rate]
        expected_return = np.mean(self.returns) - self.risk_free_rate
        downside_deviation = np.std(downside_returns) if len(downside_returns) > 0 else 0
        return expected_return / downside_deviation if downside_deviation > 0 else np.nan

def simulate_investment_cycles(num_cycles: int, num_periods: int, risk_free_rate: float) -> pd.DataFrame:
    """
    Simulates multiple investment cycles and calculates risk-adjusted returns.

    :param num_cycles: Number of investment cycles to simulate.
    :param num_periods: Number of periods in each investment cycle.
    :param risk_free_rate: The risk-free rate of return.
    :return: A DataFrame containing the Sharpe and Sortino ratios for each cycle.
    """
    results = {
        'Cycle': [],
        'Sharpe Ratio': [],
        'Sortino Ratio': []
    }

    for cycle in range(num_cycles):
        # Simulate random returns for the investment cycle
        simulated_returns = np.random.normal(loc=0.1, scale=0.2, size=num_periods)  # mean return, std dev
        investment_cycle = InvestmentCycle(simulated_returns, risk_free_rate)

        # Calculate risk-adjusted returns
        results['Cycle'].append(cycle + 1)
        results['Sharpe Ratio'].append(investment_cycle.calculate_sharpe_ratio())
        results['Sortino Ratio'].append(investment_cycle.calculate_sortino_ratio())

    return pd.DataFrame(results)

def plot_results(results: pd.DataFrame):
    """
    Plots the Sharpe and Sortino ratios for the investment cycles.

    :param results: A DataFrame containing the results to plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(results['Cycle'], results['Sharpe Ratio'], marker='o', label='Sharpe Ratio', color='blue')
    plt.plot(results['Cycle'], results['Sortino Ratio'], marker='o', label='Sortino Ratio', color='orange')
    plt.title('Risk-Adjusted Returns Across Investment Cycles')
    plt.xlabel('Investment Cycle')
    plt.ylabel('Ratio')
    plt.xticks(results['Cycle'])
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """
    Main function to execute the investment cycle simulation and plotting.
    """
    try:
        num_cycles = 10  # Number of investment cycles to simulate
        num_periods = 12  # Number of periods in each investment cycle (e.g., months)
        risk_free_rate = 0.03  # Example risk-free rate (3%)

        # Simulate investment cycles
        results = simulate_investment_cycles(num_cycles, num_periods, risk_free_rate)

        # Plot the results
        plot_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
