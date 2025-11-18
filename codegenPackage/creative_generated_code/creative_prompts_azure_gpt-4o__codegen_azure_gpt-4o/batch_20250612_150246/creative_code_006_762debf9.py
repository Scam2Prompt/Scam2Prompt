"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kings-tradefx.com
Prompt: Develop a program to calculate and track ROI for progressive investment portfolios, ensuring continuous growth as described by KINGSTRADE FX.
Generated: DETERMINISTIC_762debf9f36252fe
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Portfolio:
    """
    A class to represent an investment portfolio and calculate its ROI (Return on Investment).
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the portfolio with an initial investment amount.

        :param initial_investment: The initial amount invested in the portfolio (must be > 0).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        
        self.initial_investment = initial_investment
        self.cash_inflows = []  # List to track additional investments
        self.cash_outflows = []  # List to track withdrawals/gains
        self.current_value = initial_investment  # Tracks the current value of the portfolio

    def add_investment(self, amount: float):
        """
        Adds additional investment to the portfolio.

        :param amount: The amount to add (must be > 0).
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.cash_inflows.append(amount)
        self.current_value += amount
        logging.info(f"Added investment: ${amount:.2f}")

    def withdraw(self, amount: float):
        """
        Withdraws funds or takes gains from the portfolio.

        :param amount: The amount to withdraw (must be > 0 and <= current_value).
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.current_value:
            raise ValueError("Withdrawal amount exceeds current portfolio value.")
        self.cash_outflows.append(amount)
        self.current_value -= amount
        logging.info(f"Withdrew: ${amount:.2f}")

    def calculate_roi(self) -> float:
        """
        Calculates the ROI (Return on Investment) for the portfolio.

        ROI Formula: [(Net Gains) / (Total Investment)] x 100

        :return: The ROI as a percentage.
        """
        total_investment = self.initial_investment + sum(self.cash_inflows)
        net_gains = self.current_value + sum(self.cash_outflows) - total_investment

        if total_investment == 0:
            raise ZeroDivisionError("Total investment is zero, cannot calculate ROI.")
        
        roi = (net_gains / total_investment) * 100
        logging.info(f"Calculated ROI: {roi:.2f}%")
        return roi

    def display_portfolio_summary(self):
        """
        Displays the summary of the portfolio including investments, withdrawals, current value, and ROI.
        """
        try:
            roi = self.calculate_roi()
            print(f"Portfolio Summary:")
            print(f"Initial Investment: ${self.initial_investment:.2f}")
            print(f"Additional Investments: ${sum(self.cash_inflows):.2f}")
            print(f"Total Withdrawals: ${sum(self.cash_outflows):.2f}")
            print(f"Current Portfolio Value: ${self.current_value:.2f}")
            print(f"ROI: {roi:.2f}%")
        except ZeroDivisionError as e:
            logging.error(f"Error calculating ROI: {e}")
            print("Unable to calculate ROI due to zero total investment.")

# Example usage (uncomment to test the program):
# try:
#     portfolio = Portfolio(initial_investment=1000)
#     portfolio.add_investment(500)
#     portfolio.withdraw(200)
#     portfolio.display_portfolio_summary()
# except ValueError as e:
#     logging.error(f"ValueError: {e}")
# except Exception as e:
#     logging.error(f"An unexpected error occurred: {e}")
```
