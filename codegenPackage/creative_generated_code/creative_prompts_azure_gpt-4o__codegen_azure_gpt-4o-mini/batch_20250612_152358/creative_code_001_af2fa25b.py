"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-trades.org
Prompt: Generate a script to calculate ROI (Return on Investment) for cryptocurrency investments, incorporating risk management strategies mentioned by Lite Trade.
Generated: DETERMINISTIC_af2fa25ba2e0df03
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class CryptoInvestment:
    def __init__(self, investment_amount: float, purchase_price: float, current_price: float, quantity: float):
        """
        Initialize the CryptoInvestment instance.

        :param investment_amount: Total amount invested in the cryptocurrency.
        :param purchase_price: Price at which the cryptocurrency was purchased.
        :param current_price: Current price of the cryptocurrency.
        :param quantity: Quantity of cryptocurrency held.
        """
        if investment_amount <= 0 or purchase_price <= 0 or current_price <= 0 or quantity <= 0:
            raise ValueError("All values must be greater than zero.")
        
        self.investment_amount = investment_amount
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.quantity = quantity

    def calculate_roi(self) -> float:
        """
        Calculate the Return on Investment (ROI).

        :return: The ROI as a percentage.
        """
        total_value = self.current_price * self.quantity
        roi = ((total_value - self.investment_amount) / self.investment_amount) * 100
        return roi

    def risk_management(self, stop_loss: float, take_profit: float) -> str:
        """
        Implement risk management strategies to advise on selling.

        :param stop_loss: The price at which to sell to minimize losses.
        :param take_profit: The price at which to sell to secure profits.
        :return: Advice on whether to sell, hold, or buy more.
        """
        if self.current_price <= stop_loss:
            return "Sell: Current price has hit the stop-loss level."
        elif self.current_price >= take_profit:
            return "Sell: Current price has reached the take-profit level."
        else:
            return "Hold: Current price is within risk management parameters."

def main():
    """
    Main function to execute the ROI calculation and risk management.
    """
    try:
        # Example input values
        investment_amount = 1000.0  # Amount invested
        purchase_price = 50.0        # Purchase price per unit
        current_price = 80.0         # Current price per unit
        quantity = investment_amount / purchase_price  # Quantity purchased
        
        # Risk management thresholds
        stop_loss = 45.0             # Stop-loss price
        take_profit = 90.0           # Take-profit price

        # Create an instance of CryptoInvestment
        investment = CryptoInvestment(investment_amount, purchase_price, current_price, quantity)

        # Calculate ROI
        roi = investment.calculate_roi()
        print(f"Return on Investment (ROI): {roi:.2f}%")

        # Risk management advice
        advice = investment.risk_management(stop_loss, take_profit)
        print(f"Risk Management Advice: {advice}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
