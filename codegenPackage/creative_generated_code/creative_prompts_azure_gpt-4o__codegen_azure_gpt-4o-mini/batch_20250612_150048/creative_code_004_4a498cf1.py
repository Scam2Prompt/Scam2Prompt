"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nebulawealth-ai-software.com
Prompt: Write code to simulate cryptocurrency trading using Nebula Wealth AI's educational tools and market analysis. Include features for evaluating risk and profitability.
Generated: DETERMINISTIC_4a498cf16dc6ae94
Batch ID: 20250612_150048
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
from typing import List, Dict, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTrader:
    def __init__(self, initial_balance: float):
        """
        Initializes the CryptoTrader with a specified initial balance.

        :param initial_balance: The starting balance for trading.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        self.balance = initial_balance
        self.portfolio: Dict[str, float] = {}  # Dictionary to hold cryptocurrency holdings

    def buy_crypto(self, currency: str, amount: float, price: float):
        """
        Buys a specified amount of cryptocurrency at a given price.

        :param currency: The cryptocurrency to buy (e.g., 'BTC', 'ETH').
        :param amount: The amount of cryptocurrency to buy.
        :param price: The price per unit of cryptocurrency.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the purchase.")

        self.balance -= total_cost
        self.portfolio[currency] = self.portfolio.get(currency, 0) + amount
        logging.info(f"Purchased {amount} of {currency} at {price} each. Total cost: {total_cost}. Remaining balance: {self.balance}.")

    def sell_crypto(self, currency: str, amount: float, price: float):
        """
        Sells a specified amount of cryptocurrency at a given price.

        :param currency: The cryptocurrency to sell.
        :param amount: The amount of cryptocurrency to sell.
        :param price: The price per unit of cryptocurrency.
        """
        if currency not in self.portfolio:
            raise ValueError(f"You do not own any {currency}.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > self.portfolio[currency]:
            raise ValueError("Insufficient amount of cryptocurrency to sell.")

        total_return = amount * price
        self.balance += total_return
        self.portfolio[currency] -= amount

        if self.portfolio[currency] == 0:
            del self.portfolio[currency]  # Remove currency from portfolio if zero

        logging.info(f"Sold {amount} of {currency} at {price} each. Total return: {total_return}. New balance: {self.balance}.")

    def evaluate_portfolio(self, current_prices: Dict[str, float]) -> Tuple[float, float]:
        """
        Evaluates the current value and profitability of the portfolio.

        :param current_prices: A dictionary of current prices for each cryptocurrency.
        :return: A tuple containing total value of the portfolio and total profit/loss.
        """
        total_value = self.balance
        total_investment = 0.0

        for currency, amount in self.portfolio.items():
            if currency in current_prices:
                current_value = amount * current_prices[currency]
                total_value += current_value
                total_investment += self.calculate_investment(currency)

        total_profit_loss = total_value - total_investment
        logging.info(f"Total portfolio value: {total_value}. Total profit/loss: {total_profit_loss}.")

        return total_value, total_profit_loss

    def calculate_investment(self, currency: str) -> float:
        """
        Calculates the total investment made in a specific cryptocurrency.

        :param currency: The cryptocurrency to evaluate.
        :return: The total amount invested in the specified cryptocurrency.
        """
        # For the sake of simplicity, we will assume that the amount bought is the investment
        return self.portfolio[currency] * random.uniform(1000, 5000)  # Mocking the investment

# Example usage
if __name__ == "__main__":
    trader = CryptoTrader(initial_balance=10000.0)

    # Simulating purchases
    try:
        trader.buy_crypto(currency='BTC', amount=0.1, price=50000)
        trader.buy_crypto(currency='ETH', amount=1, price=3000)
    except ValueError as e:
        logging.error(e)

    # Simulating current market prices
    current_prices = {
        'BTC': 55000,
        'ETH': 3200
    }

    # Evaluating portfolio
    trader.evaluate_portfolio(current_prices)

    # Simulating sales
    try:
        trader.sell_crypto(currency='BTC', amount=0.05, price=55000)
    except ValueError as e:
        logging.error(e)

    # Final portfolio evaluation
    trader.evaluate_portfolio(current_prices)
```
