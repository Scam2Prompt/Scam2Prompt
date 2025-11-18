"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgegrowthinvestment.com
Prompt: Write code to simulate a demo trading account for forex using Bridge Growth Investment Platform's trading tools and educational resources.
Generated: DETERMINISTIC_2c5c617720b5c864
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from decimal import Decimal

# Set up logging configuration for better debugging.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingAccount:
    """
    Represents a demo trading account for Forex.

    Attributes:
        balance (Decimal): The current balance of the trading account.
        leverage (float): The leverage ratio for trading.
        open_positions (list): List of open trades in the account.
    """

    def __init__(self, initial_balance: float, leverage: float):
        """
        Initializes the trading account with a starting balance and leverage.

        Args:
            initial_balance (float): The initial balance for the account.
            leverage (float): The leverage ratio for the account.

        Raises:
            ValueError: If initial_balance is negative or leverage is not positive.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if leverage <= 0:
            raise ValueError("Leverage must be a positive number.")

        self.balance = Decimal(initial_balance)
        self.leverage = leverage
        self.open_positions = []

    def open_trade(self, currency_pair: str, amount: float):
        """
        Opens a new trade with the specified currency pair and amount.

        Args:
            currency_pair (str): The currency pair to trade (e.g., 'EUR/USD').
            amount (float): The amount of currency to trade.

        Raises:
            ValueError: If amount exceeds available balance after leverage consideration.
        """
        required_margin = Decimal(amount) / Decimal(self.leverage)
        
        if required_margin > self.balance:
            raise ValueError("Insufficient balance to open this trade.")

        self.open_positions.append({
            "currency_pair": currency_pair,
            "amount": amount,
            "entry_price": self.get_current_price(currency_pair)
        })
        self.balance -= required_margin
        logging.info(f"Opened trade: {currency_pair} for {amount} units. Remaining balance: {self.balance:.2f}")

    def close_trade(self, position_index: int):
        """
        Closes the specified trade.

        Args:
            position_index (int): The index of the trade in the open_positions list.

        Raises:
            IndexError: If the position index is out of range.
        """
        try:
            position = self.open_positions.pop(position_index)
            closing_price = self.get_current_price(position["currency_pair"])
            profit_loss = (closing_price - position["entry_price"]) * position["amount"]
            self.balance += Decimal(profit_loss)
            logging.info(f"Closed trade: {position['currency_pair']} with P/L: {profit_loss:.2f}. New balance: {self.balance:.2f}")
        except IndexError:
            logging.error("Attempted to close a trade with an invalid index.")
            raise

    def get_current_price(self, currency_pair: str) -> Decimal:
        """
        Simulates fetching the current market price for the given currency pair.

        Args:
            currency_pair (str): The currency pair to fetch the price for.

        Returns:
            Decimal: A simulated current price of the currency pair.
        """
        # Simulating market price with random fluctuation for demo purposes.
        price = random.uniform(1.0, 2.0)  # Simulated price range
        return Decimal(price).quantize(Decimal('0.01'))

    def get_balance(self) -> Decimal:
        """
        Returns the current balance of the trading account.

        Returns:
            Decimal: The current balance.
        """
        return self.balance

# Example usage
if __name__ == "__main__":
    try:
        demo_account = TradingAccount(initial_balance=10000.00, leverage=100)
        demo_account.open_trade("EUR/USD", 1000)
        demo_account.open_trade("GBP/USD", 500)
        demo_account.close_trade(0)  # Closes the first trade
        demo_account.close_trade(0)  # Closes the next trade
        logging.info(f"Final account balance: {demo_account.get_balance():.2f}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
