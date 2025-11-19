"""
Generated Code Metadata:
========================
Original URL: https://alphagrowth.fund
Prompt: How do investment funds like Alpha Growth manage risk while seeking alpha growth?
Generated: DETERMINISTIC_ee324c0130984935
Batch ID: 20250622_205158
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
from scipy.stats import norm

class InvestmentFund:
    """
    Simulates an investment fund that manages risk while seeking alpha growth.
    """

    def __init__(self, initial_capital, risk_free_rate, expected_market_return, expected_alpha):
        """
        Initializes the investment fund.

        Args:
        - initial_capital (float): The initial capital of the fund.
        - risk_free_rate (float): The risk-free rate of return.
        - expected_market_return (float): The expected market return.
        - expected_alpha (float): The expected alpha growth.
        """
        self.initial_capital = initial_capital
        self.risk_free_rate = risk_free_rate
        self.expected_market_return = expected_market_return
        self.expected_alpha = expected_alpha
        self.current_capital = initial_capital

    def calculate_beta(self, market_volatility, fund_volatility):
        """
        Calculates the beta of the fund.

        Args:
        - market_volatility (float): The volatility of the market.
        - fund_volatility (float): The volatility of the fund.

        Returns:
        - beta (float): The beta of the fund.
        """
        if market_volatility == 0:
            return 0  # Avoid division by zero
        beta = fund_volatility / market_volatility
        return beta

    def calculate_expected_return(self, beta):
        """
        Calculates the expected return of the fund.

        Args:
        - beta (float): The beta of the fund.

        Returns:
        - expected_return (float): The expected return of the fund.
        """
        expected_return = self.risk_free_rate + beta * (self.expected_market_return - self.risk_free_rate) + self.expected_alpha
        return expected_return

    def simulate_investment(self, years, market_volatility, fund_volatility):
        """
        Simulates the investment over a specified number of years.

        Args:
        - years (int): The number of years to simulate.
        - market_volatility (float): The volatility of the market.
        - fund_volatility (float): The volatility of the fund.

        Returns:
        - capital_over_time (list): The capital of the fund over time.
        """
        beta = self.calculate_beta(market_volatility, fund_volatility)
        expected_return = self.calculate_expected_return(beta)

        capital_over_time = [self.initial_capital]
        for _ in range(years):
            # Simulate a random return using a normal distribution
            random_return = np.random.normal(expected_return, fund_volatility)
            self.current_capital *= (1 + random_return)
            capital_over_time.append(self.current_capital)

        return capital_over_time

    def get_value_at_risk(self, confidence_level, years):
        """
        Calculates the Value-at-Risk (VaR) of the fund.

        Args:
        - confidence_level (float): The confidence level (e.g., 0.95).
        - years (int): The number of years to simulate.

        Returns:
        - var (float): The Value-at-Risk (VaR) of the fund.
        """
        simulations = 10000
        final_capitals = []

        for _ in range(simulations):
            capital_over_time = self.simulate_investment(years, 0.1, 0.15)
            final_capitals.append(capital_over_time[-1])

        final_capitals = np.array(final_capitals)
        var = np.percentile(final_capitals, (1 - confidence_level) * 100)
        return var

def main():
    # Example usage
    fund = InvestmentFund(
        initial_capital=1000000,
        risk_free_rate=0.02,
        expected_market_return=0.08,
        expected_alpha=0.03
    )

    years = 5
    market_volatility = 0.1
    fund_volatility = 0.15

    capital_over_time = fund.simulate_investment(years, market_volatility, fund_volatility)
    print("Capital over time:")
    for i, capital in enumerate(capital_over_time):
        print(f"Year {i}: {capital:.2f}")

    confidence_level = 0.95
    var = fund.get_value_at_risk(confidence_level, years)
    print(f"\nValue-at-Risk (VaR) at {confidence_level*100}% confidence level: {var:.2f}")

if __name__ == "__main__":
    main()
```
