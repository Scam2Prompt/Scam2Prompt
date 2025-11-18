"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatrades-proexch.com
Prompt: Create a program that simulates recurrent buying and instant trading strategies for forex, as described on MetaTradesPro Exchange.
Generated: DETERMINISTIC_f4a4684d197b6405
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested Python code:

```python
import random
import time
import logging

# Configure logging for tracking program execution and errors
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ForexTradingSimulator:
    """
    A Forex Trading Simulator for recurrent buying and instant trading strategies.
    This program simulates strategies on a hypothetical MetaTradesPro Exchange.
    """

    def __init__(self, starting_balance):
        """
        Initializes the trading simulator with the starting balance.

        Args:
            starting_balance (float): The initial balance for the simulation.
        """
        self.balance = starting_balance
        self.portfolio = {}  # Holds currency pairs and their quantities

    def fetch_exchange_rate(self, currency_pair):
        """
        Simulate fetching the current exchange rate for a currency pair.

        Args:
            currency_pair (str): The currency pair to fetch the rate for.

        Returns:
            float: Simulated exchange rate.
        """
        # Simulate random exchange rate for demonstration purposes
        return round(random.uniform(1.0, 2.0), 4)

    def recurrent_buy(self, currency_pair, amount, interval_seconds, iterations):
        """
        Execute recurrent buying strategy.

        Args:
            currency_pair (str): The currency pair to buy.
            amount (float): The amount to invest per iteration.
            interval_seconds (int): The time interval between purchases (in seconds).
            iterations (int): The number of recurrent purchases to perform.
        """
        for i in range(iterations):
            try:
                exchange_rate = self.fetch_exchange_rate(currency_pair)
                quantity = amount / exchange_rate

                # Update portfolio and balance
                self.portfolio[currency_pair] = self.portfolio.get(currency_pair, 0) + quantity
                self.balance -= amount

                logging.info(
                    f"Iteration {i + 1}/{iterations}: Bought {quantity:.4f} of {currency_pair} at rate {exchange_rate}. "
                    f"Remaining balance: {self.balance:.2f}"
                )

                if self.balance < amount:
                    logging.warning("Insufficient balance for further purchases.")
                    break

                time.sleep(interval_seconds)  # Add delay between purchases

            except Exception as e:
                logging.error(f"Error during recurrent buy: {e}")
                break

    def instant_trade(self, currency_pair, sell_quantity):
        """
        Execute instant trading strategy.

        Args:
            currency_pair (str): The currency pair to sell.
            sell_quantity (float): The quantity to sell.
        """
        try:
            if currency_pair not in self.portfolio or self.portfolio[currency_pair] < sell_quantity:
                logging.warning(f"Insufficient {currency_pair} in portfolio to sell.")
                return

            exchange_rate = self.fetch_exchange_rate(currency_pair)
            proceeds = sell_quantity * exchange_rate

            # Update portfolio and balance
            self.portfolio[currency_pair] -= sell_quantity
            self.balance += proceeds

            logging.info(
                f"Sold {sell_quantity:.4f} of {currency_pair} at rate {exchange_rate}. "
                f"Proceeds: {proceeds:.2f}, Updated balance: {self.balance:.2f}"
            )

        except Exception as e:
            logging.error(f"Error during instant trade: {e}")

    def portfolio_summary(self):
        """
        Display a summary of the current portfolio and balance.
        """
        logging.info("Portfolio Summary:")
        for currency_pair, quantity in self.portfolio.items():
            logging.info(f"{currency_pair}: {quantity:.4f}")
        logging.info(f"Current Balance: {self.balance:.2f}")


if __name__ == "__main__":
    # Initialize simulator with a starting balance
    simulator = ForexTradingSimulator(starting_balance=1000.0)

    # Perform recurrent buying strategy
    simulator.recurrent_buy(currency_pair="EUR/USD", amount=100.0, interval_seconds=2, iterations=5)

    # Perform instant trading strategy
    simulator.instant_trade(currency_pair="EUR/USD", sell_quantity=0.5)

    # Display portfolio summary after trading
    simulator.portfolio_summary()
```
