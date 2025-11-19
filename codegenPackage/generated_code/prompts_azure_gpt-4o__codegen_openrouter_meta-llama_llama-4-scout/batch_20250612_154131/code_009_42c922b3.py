"""
Generated Code Metadata:
========================
Original URL: https://arkventureshares.com
Prompt: Write code to simulate the impact of leverage on the ARK Venture Fund's portfolio volatility, considering its exposure to disruptive innovation sectors.
Generated: DETERMINISTIC_42c922b3b216273c
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
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

class ARK_Venture_Fund:
    def __init__(self, portfolio_returns, leverage_ratio, confidence_level=0.95):
        """
        Initialize the ARK Venture Fund portfolio.

        Parameters:
        portfolio_returns (list or np.array): Historical returns of the portfolio.
        leverage_ratio (float): Leverage ratio of the fund.
        confidence_level (float, optional): Confidence level for VaR calculation. Defaults to 0.95.
        """
        self.portfolio_returns = np.array(portfolio_returns)
        self.leverage_ratio = leverage_ratio
        self.confidence_level = confidence_level

    def calculate_volatility(self):
        """
        Calculate the portfolio volatility.

        Returns:
        float: Portfolio volatility (standard deviation of returns).
        """
        return np.std(self.portfolio_returns)

    def calculate_leveraged_volatility(self):
        """
        Calculate the leveraged portfolio volatility.

        Returns:
        float: Leveraged portfolio volatility.
        """
        return self.calculate_volatility() * self.leverage_ratio

    def calculate_value_at_risk(self):
        """
        Calculate the Value-at-Risk (VaR) of the portfolio.

        Returns:
        float: VaR of the portfolio.
        """
        mean_return = np.mean(self.portfolio_returns)
        volatility = self.calculate_volatility()
        var = mean_return - (norm.ppf(self.confidence_level) * volatility)
        return var

    def calculate_leveraged_value_at_risk(self):
        """
        Calculate the leveraged Value-at-Risk (VaR) of the portfolio.

        Returns:
        float: Leveraged VaR of the portfolio.
        """
        return self.calculate_value_at_risk() * self.leverage_ratio

    def simulate_portfolio_volatility(self, num_simulations=10000):
        """
        Simulate the portfolio volatility.

        Parameters:
        num_simulations (int, optional): Number of simulations. Defaults to 10000.

        Returns:
        np.array: Simulated portfolio returns.
        """
        simulated_returns = np.random.normal(np.mean(self.portfolio_returns), np.std(self.portfolio_returns), num_simulations)
        return simulated_returns

    def plot_volatility_distribution(self, num_simulations=10000):
        """
        Plot the distribution of simulated portfolio returns.

        Parameters:
        num_simulations (int, optional): Number of simulations. Defaults to 10000.
        """
        simulated_returns = self.simulate_portfolio_volatility(num_simulations)
        plt.hist(simulated_returns, bins=50, density=True)
        plt.xlabel('Return')
        plt.ylabel('Frequency')
        plt.title('Simulated Portfolio Returns Distribution')
        plt.show()

def main():
    # Historical returns of the ARK Venture Fund portfolio
    portfolio_returns = np.array([0.03, 0.05, -0.02, 0.01, 0.04, -0.03, 0.02, 0.06, -0.01, 0.03])

    # Leverage ratio of the fund
    leverage_ratio = 2.0

    # Create an instance of the ARK_Venture_Fund class
    fund = ARK_Venture_Fund(portfolio_returns, leverage_ratio)

    # Calculate and print the portfolio volatility
    volatility = fund.calculate_volatility()
    print(f"Portfolio Volatility: {volatility:.4f}")

    # Calculate and print the leveraged portfolio volatility
    leveraged_volatility = fund.calculate_leveraged_volatility()
    print(f"Leveraged Portfolio Volatility: {leveraged_volatility:.4f}")

    # Calculate and print the Value-at-Risk (VaR)
    var = fund.calculate_value_at_risk()
    print(f"Value-at-Risk (VaR): {var:.4f}")

    # Calculate and print the leveraged Value-at-Risk (VaR)
    leveraged_var = fund.calculate_leveraged_value_at_risk()
    print(f"Leveraged Value-at-Risk (VaR): {leveraged_var:.4f}")

    # Plot the distribution of simulated portfolio returns
    fund.plot_volatility_distribution()

if __name__ == "__main__":
    main()
```
