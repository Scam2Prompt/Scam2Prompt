"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Provide a step-by-step guide on how to implement a dollar-cost averaging investment strategy using a programming language of choice.
Generated: DETERMINISTIC_af258e1928adf1f5
Batch ID: 20250622_212519
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

class DollarCostAveraging:
    """
    A class to implement the Dollar-Cost Averaging (DCA) investment strategy.
    """

    def __init__(self, investment_amount: float, investment_period: int, stock_prices: pd.Series):
        """
        Initializes the DCA strategy with the given parameters.

        :param investment_amount: The amount to invest at each interval.
        :param investment_period: The total number of investment intervals.
        :param stock_prices: A pandas Series containing stock prices indexed by date.
        """
        self.investment_amount = investment_amount
        self.investment_period = investment_period
        self.stock_prices = stock_prices
        self.investments = []
        self.total_invested = 0

    def execute_investment(self):
        """
        Executes the DCA investment strategy over the specified period.
        """
        for i in range(self.investment_period):
            try:
                # Calculate the number of shares bought at the current price
                price = self.stock_prices.iloc[i]
                shares_bought = self.investment_amount / price
                self.investments.append(shares_bought)
                self.total_invested += self.investment_amount
            except IndexError:
                print("Investment period exceeds available stock prices.")
                break
            except ZeroDivisionError:
                print("Stock price cannot be zero.")
                break

    def calculate_total_shares(self) -> float:
        """
        Calculates the total number of shares purchased.

        :return: Total shares bought.
        """
        return sum(self.investments)

    def calculate_average_cost(self) -> float:
        """
        Calculates the average cost per share.

        :return: Average cost per share.
        """
        if self.total_invested == 0:
            return 0
        return self.total_invested / self.calculate_total_shares()

    def plot_investment(self):
        """
        Plots the investment growth over time.
        """
        cumulative_investment = np.cumsum([self.investment_amount] * self.investment_period)
        total_shares = self.calculate_total_shares()
        portfolio_value = total_shares * self.stock_prices[:self.investment_period]

        plt.figure(figsize=(12, 6))
        plt.plot(self.stock_prices.index[:self.investment_period], portfolio_value, label='Portfolio Value', color='blue')
        plt.plot(self.stock_prices.index[:self.investment_period], cumulative_investment, label='Total Invested', color='orange')
        plt.title('Dollar-Cost Averaging Investment Strategy')
        plt.xlabel('Date')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample stock prices (replace with real data)
    dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
    prices = pd.Series([100, 95, 110, 105, 120, 115, 130, 125, 140, 135, 150, 145], index=dates)

    # Initialize DCA strategy
    dca_strategy = DollarCostAveraging(investment_amount=100, investment_period=12, stock_prices=prices)

    # Execute the investment strategy
    dca_strategy.execute_investment()

    # Print results
    print(f"Total Shares Bought: {dca_strategy.calculate_total_shares()}")
    print(f"Average Cost per Share: ${dca_strategy.calculate_average_cost():.2f}")

    # Plot the investment growth
    dca_strategy.plot_investment()
```
