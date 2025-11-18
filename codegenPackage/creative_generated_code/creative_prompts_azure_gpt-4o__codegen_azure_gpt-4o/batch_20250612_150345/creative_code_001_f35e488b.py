"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swifttradeexpress.com
Prompt: Create a script that simulates the operation of a trading bot similar to the unique trading robot described by SwiftTrade Express, ensuring it can handle market rise and fall scenarios.
Generated: DETERMINISTIC_f35e488b0c3ff7d9
Batch ID: 20250612_150345
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
import time


class TradingBot:
    """
    Simulates a trading bot that buys and sells assets based on market conditions.
    """

    def __init__(self, initial_balance=10000, trading_fee=0.01):
        """
        Initialize the trading bot with an initial balance and trading fee.

        :param initial_balance: Starting balance for the bot (default is $10,000).
        :param trading_fee: Fee percentage per trade, e.g., 0.01 for 1%.
        """
        self.balance = initial_balance
        self.assets = 0
        self.trading_fee = trading_fee
        self.market_price = 100  # Initial market price of the asset
        self.price_history = []

    def update_market_price(self):
        """
        Simulates market price fluctuations.
        """
        price_change = random.uniform(-5, 5)  # Random price change between -5 and +5
        self.market_price = max(1, self.market_price + price_change)  # Prevent negative prices
        self.price_history.append(self.market_price)

    def buy_asset(self, amount):
        """
        Buys assets with the given amount of money.

        :param amount: Amount of money to spend on buying assets.
        """
        if amount > self.balance:
            logging.warning("Insufficient balance to buy assets.")
            return

        num_assets = amount / self.market_price  # Calculate number of assets that can be bought
        fee = self.trading_fee * amount
        self.balance -= (amount + fee)
        self.assets += num_assets
        logging.info(f"Bought {num_assets:.2f} assets at ${self.market_price:.2f} each. Fee: ${fee:.2f}")

    def sell_asset(self, amount):
        """
        Sells assets worth the given amount of money.

        :param amount: Amount of assets to sell in monetary value.
        """
        num_assets_to_sell = amount / self.market_price
        if num_assets_to_sell > self.assets:
            logging.warning("Insufficient assets to sell.")
            return

        fee = self.trading_fee * amount
        self.assets -= num_assets_to_sell
        self.balance += (amount - fee)
        logging.info(f"Sold {num_assets_to_sell:.2f} assets at ${self.market_price:.2f} each. Fee: ${fee:.2f}")

    def evaluate_market_and_trade(self):
        """
        Evaluates market conditions and decides whether to buy or sell.
        """
        if len(self.price_history) < 2:
            return

        # Strategy: Buy if price dropped significantly, sell if price rose significantly
        price_change_percentage = ((self.market_price - self.price_history[-2]) / self.price_history[-2]) * 100
        logging.info(f"Market price changed by {price_change_percentage:.2f}%")

        if price_change_percentage <= -3 and self.balance > 0:  # Price drop
            amount_to_buy = self.balance * 0.5  # Use 50% of balance to buy assets
            self.buy_asset(amount_to_buy)
        elif price_change_percentage >= 3 and self.assets > 0:  # Price rise
            amount_to_sell = self.assets * self.market_price * 0.5  # Sell 50% of assets
            self.sell_asset(amount_to_sell)

    def summary(self):
        """
        Prints the summary of the bot's current balance and assets.
        """
        logging.info(f"Balance: ${self.balance:.2f}, Assets: {self.assets:.2f}, Market Price: ${self.market_price:.2f}")


def main():
    """
    Main function to run the trading bot simulation.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    bot = TradingBot()

    try:
        for _ in range(100):  # Simulate 100 market cycles
            bot.update_market_price()
            bot.evaluate_market_and_trade()
            bot.summary()
            time.sleep(0.1)  # Simulate a short delay between market cycles
    except Exception as e:
        logging.error(f"An error occurred during the simulation: {e}")


if __name__ == "__main__":
    main()
```
