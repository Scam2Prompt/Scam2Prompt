"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatecode.org
Prompt: Write code to simulate Immediate Code's reinvestment strategy for cryptocurrency profits, ensuring adherence to risk thresholds.
Generated: DETERMINISTIC_eaf8746714d701e1
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from decimal import Decimal

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoReinvestmentStrategy:
    """
    A class to simulate Immediate Code's reinvestment strategy for cryptocurrency profits.
    """

    def __init__(self, initial_balance, reinvestment_threshold, risk_tolerance):
        """
        Initialize the strategy with parameters.

        :param initial_balance: Decimal, initial balance in the account.
        :param reinvestment_threshold: Decimal, percentage of profits to reinvest (e.g., 0.5 for 50%).
        :param risk_tolerance: Decimal, maximum percentage of total balance to reinvest (e.g., 0.3 for 30%).
        """
        self.balance = Decimal(initial_balance)
        self.reinvestment_threshold = Decimal(reinvestment_threshold)
        self.risk_tolerance = Decimal(risk_tolerance)
        self.profits = Decimal(0)

    def add_profit(self, profit):
        """
        Record profits from trading.

        :param profit: Decimal, profit amount to add.
        """
        if profit <= 0:
            logging.error("Profit must be a positive value.")
            raise ValueError("Profit must be a positive value.")
        self.profits += Decimal(profit)
        logging.info(f"Added profit: {profit}. Current profits: {self.profits}")

    def reinvest(self):
        """
        Perform reinvestment based on the strategy parameters.

        :return: Decimal, amount reinvested.
        """
        reinvestment_amount = self.profits * self.reinvestment_threshold
        max_allowed_reinvestment = self.balance * self.risk_tolerance

        if reinvestment_amount > max_allowed_reinvestment:
            logging.warning("Reinvestment amount exceeds risk tolerance. Adjusting to maximum allowed reinvestment.")
            reinvestment_amount = max_allowed_reinvestment

        self.balance += reinvestment_amount
        self.profits -= reinvestment_amount

        logging.info(f"Reinvested: {reinvestment_amount}. New balance: {self.balance}. Remaining profits: {self.profits}")
        return reinvestment_amount

    def get_balance(self):
        """
        Retrieve the current balance.

        :return: Decimal, current balance.
        """
        return self.balance

    def get_profits(self):
        """
        Retrieve the current profits.

        :return: Decimal, current profits.
        """
        return self.profits


# Example usage
if __name__ == "__main__":
    try:
        # Initialize strategy
        strategy = CryptoReinvestmentStrategy(initial_balance=1000, reinvestment_threshold=0.5, risk_tolerance=0.3)

        # Simulate profits and reinvestment
        strategy.add_profit(200)
        reinvested = strategy.reinvest()

        # Display final results
        logging.info(f"Final balance: {strategy.get_balance()}, Remaining profits: {strategy.get_profits()}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
