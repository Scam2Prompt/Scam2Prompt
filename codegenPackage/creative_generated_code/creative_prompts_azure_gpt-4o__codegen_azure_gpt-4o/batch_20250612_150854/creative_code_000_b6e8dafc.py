"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-growth.io
Prompt: Write Python code to simulate a cryptocurrency trading strategy using a demo account feature like the one described on the Immediate Growth platform. Include functionality for testing trades with "fake" currency.
Generated: DETERMINISTIC_b6e8dafc2954dffc
Batch ID: 20250612_150854
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

class DemoAccount:
    """
    DemoAccount simulates a cryptocurrency trading account with fake currency.
    """
    def __init__(self, initial_balance=10000):
        """
        Initialize demo account with a fake balance.
        :param initial_balance: Starting balance for the demo account.
        """
        self.balance = initial_balance
        self.portfolio = {}  # Dictionary to track owned cryptocurrencies
        logging.info(f"Demo account initialized with balance: ${initial_balance}")

    def place_order(self, cryptocurrency, price, quantity, order_type):
        """
        Place a buy or sell order with fake currency.
        :param cryptocurrency: The name of the cryptocurrency (e.g., 'BTC').
        :param price: Price per unit of the cryptocurrency.
        :param quantity: Amount of cryptocurrency to buy or sell.
        :param order_type: 'buy' or 'sell'.
        """
        try:
            total_cost = price * quantity

            if order_type == 'buy':
                if total_cost > self.balance:
                    raise ValueError("Insufficient balance to place buy order.")
                self.balance -= total_cost
                self.portfolio[cryptocurrency] = self.portfolio.get(cryptocurrency, 0) + quantity
                logging.info(f"Bought {quantity} {cryptocurrency} at ${price} each.")

            elif order_type == 'sell':
                if cryptocurrency not in self.portfolio or self.portfolio[cryptocurrency] < quantity:
                    raise ValueError("Insufficient holdings to place sell order.")
                self.balance += total_cost
                self.portfolio[cryptocurrency] -= quantity
                if self.portfolio[cryptocurrency] == 0:
                    del self.portfolio[cryptocurrency]
                logging.info(f"Sold {quantity} {cryptocurrency} at ${price} each.")

            else:
                raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")

        except ValueError as e:
            logging.error(f"Order failed: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    def show_balance(self):
        """
        Display current balance.
        """
        logging.info(f"Current balance: ${self.balance}")
        return self.balance

    def show_portfolio(self):
        """
        Display current portfolio.
        """
        logging.info(f"Current portfolio: {self.portfolio}")
        return self.portfolio

class CryptoTradingStrategy:
    """
    A simple cryptocurrency trading strategy simulator.
    """
    def __init__(self, demo_account):
        """
        Initialize trading strategy with a demo account.
        :param demo_account: Instance of DemoAccount.
        """
        self.demo_account = demo_account

    def simulate_trading(self):
        """
        Simulate random trading to test strategies.
        """
        cryptocurrencies = ['BTC', 'ETH', 'LTC']
        for _ in range(10):  # Simulate 10 trades
            try:
                crypto = random.choice(cryptocurrencies)
                price = random.uniform(100, 50000)  # Random price
                quantity = random.uniform(0.01, 2)  # Random quantity
                order_type = random.choice(['buy', 'sell'])

                logging.info(f"Attempting trade: {order_type} {quantity:.4f} {crypto} at ${price:.2f}")
                self.demo_account.place_order(crypto, price, quantity, order_type)

            except Exception as e:
                logging.error(f"An error occurred during simulated trading: {e}")

        # Display final account state
        logging.info("Final account state:")
        self.demo_account.show_balance()
        self.demo_account.show_portfolio()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Main function to test the trading strategy
if __name__ == "__main__":
    demo_account = DemoAccount(initial_balance=10000)
    strategy = CryptoTradingStrategy(demo_account)
    strategy.simulate_trading()
```
