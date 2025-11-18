"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Write a script to calculate leverage up to 1:500 for CFD trading, as offered by Apex Capital Investment, and display the potential profit or loss.
Generated: DETERMINISTIC_f5bc92e4f4623388
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CFDTradingCalculator:
    def __init__(self, leverage, investment, market_price, position_size):
        """
        Initializes the CFD Trading Calculator with necessary parameters.

        :param leverage: The leverage ratio (e.g., 500 for 1:500)
        :param investment: The amount invested (in currency)
        :param market_price: The current market price of the asset
        :param position_size: The size of the position in units
        """
        self.leverage = leverage
        self.investment = investment
        self.market_price = market_price
        self.position_size = position_size

        self.validate_parameters()

    def validate_parameters(self):
        """
        Validates the initialization parameters ensuring they meet required conditions.
        """
        if not (1 <= self.leverage <= 500):
            raise ValueError("Leverage must be between 1 and 500.")
        if self.investment <= 0:
            raise ValueError("Investment must be greater than zero.")
        if self.market_price <= 0:
            raise ValueError("Market price must be greater than zero.")
        if self.position_size <= 0:
            raise ValueError("Position size must be greater than zero.")

    def calculate_total_exposure(self):
        """
        Calculates the total exposure based on leverage and investment.

        :return: Total exposure as a float.
        """
        return self.investment * self.leverage

    def calculate_profit_loss(self, change_in_price):
        """
        Calculates potential profit or loss based on price changes.

        :param change_in_price: The change in market price (positive for increase, negative for decrease)
        :return: Potential profit or loss as a float.
        """
        total_exposure = self.calculate_total_exposure()
        profit_loss = (change_in_price * self.position_size) * (total_exposure / self.market_price)
        return profit_loss

def main():
    try:
        # Input parameters for the calculator
        leverage = 500  # Example leverage
        investment = float(input("Enter your investment amount: "))
        market_price = float(input("Enter the current market price of the asset: "))
        position_size = float(input("Enter the position size in units: "))
        change_in_price = float(input("Enter the expected change in price: "))

        # Initialize the CFD trading calculator
        cfd_calculator = CFDTradingCalculator(leverage, investment, market_price, position_size)

        # Calculate potential profit/loss
        potential_profit_loss = cfd_calculator.calculate_profit_loss(change_in_price)

        # Display results
        if potential_profit_loss >= 0:
            print(f"Potential Profit: ${potential_profit_loss:.2f}")
        else:
            print(f"Potential Loss: ${abs(potential_profit_loss):.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
