"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-nova.com
Prompt: Write Python code to simulate the concept of dollar-cost averaging (DCA) as described on Immediate Nova V5, where fixed amounts are invested regularly into a stock portfolio, regardless of market conditions.
Generated: DETERMINISTIC_2ef1465fea856833
Batch ID: 20250612_150854
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

class DollarCostAveraging:
    def __init__(self, initial_investment: float, monthly_investment: float, investment_duration: int, stock_prices: np.ndarray):
        """
        Initialize the DollarCostAveraging simulation.

        :param initial_investment: Initial investment amount (in dollars).
        :param monthly_investment: Fixed monthly investment amount (in dollars).
        :param investment_duration: Total investment duration (in months).
        :param stock_prices: An array of stock prices over the investment duration.
        """
        self.initial_investment = initial_investment
        self.monthly_investment = monthly_investment
        self.investment_duration = investment_duration
        self.stock_prices = stock_prices
        self.total_invested = 0
        self.shares_owned = 0

    def simulate_investment(self):
        """
        Simulate the dollar-cost averaging investment strategy.
        """
        # Initial investment
        self.total_invested += self.initial_investment
        self.shares_owned += self.initial_investment / self.stock_prices[0]

        # Monthly investments
        for month in range(1, self.investment_duration):
            self.total_invested += self.monthly_investment
            try:
                # Calculate shares bought this month
                shares_bought = self.monthly_investment / self.stock_prices[month]
                self.shares_owned += shares_bought
            except ZeroDivisionError:
                print(f"Error: Stock price is zero at month {month}. Skipping this month.")
                continue

    def calculate_total_value(self) -> float:
        """
        Calculate the total value of the investment.

        :return: Total value of the investment based on current stock prices.
        """
        current_price = self.stock_prices[-1]  # Assuming the last price is current
        return self.shares_owned * current_price

    def print_summary(self):
        """
        Print a summary of the investment results.
        """
        total_value = self.calculate_total_value()
        print(f"Total Amount Invested: ${self.total_invested:.2f}")
        print(f"Current Value of Investment: ${total_value:.2f}")
        print(f"Total Shares Owned: {self.shares_owned:.4f}")
        print(f"Profit/Loss: ${total_value - self.total_invested:.2f}")

def main():
    # Example stock prices for 12 months
    stock_prices = np.array([100, 90, 80, 110, 120, 100, 95, 105, 125, 130, 115, 140])

    # Initialize DCA simulation
    dca = DollarCostAveraging(initial_investment=1000, monthly_investment=200, investment_duration=12, stock_prices=stock_prices)

    # Run the simulation
    dca.simulate_investment()

    # Print the summary of results
    dca.print_summary()

if __name__ == "__main__":
    main()
```
