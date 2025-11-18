"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediatealtex.com
Prompt: Develop a trading bot in Python that uses Immediate Altex's approach to automated trading, allowing users to choose between auto-trade and manual modes and generate consistent profits.
Generated: DETERMINISTIC_458d3b1ae26f52ff
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
import random

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DEFAULT_TRADE_AMOUNT = 100  # Default trade amount in USD
PROFIT_MARGIN_PERCENT = 0.5  # Target profit margin in percentage
SUPPORTED_MODES = ['auto', 'manual']  # Supported modes

class TradingBot:
    def __init__(self):
        """
        Initialize the trading bot with default settings.
        """
        self.mode = None
        self.balance = 10000  # Starting balance in USD
        self.trade_history = []  # List to store trade history
        self.running = False
    
    def choose_mode(self):
        """
        Allows the user to choose between auto-trade and manual trade modes.
        """
        while True:
            mode = input(f"Choose trading mode ({'/'.join(SUPPORTED_MODES)}): ").strip().lower()
            if mode in SUPPORTED_MODES:
                self.mode = mode
                logging.info(f"Trading mode set to: {self.mode}")
                return
            else:
                print("Invalid mode. Please choose 'auto' or 'manual'.")

    def execute_trade(self, amount):
        """
        Executes a single trade with the given amount and calculates the profit/loss.
        
        Args:
            amount (float): Amount to trade in USD.
        """
        # Simulate market behavior with random profit/loss
        price_change_percent = random.uniform(-1, 1)  # Price change in percentage
        profit_loss = amount * (price_change_percent / 100)

        # Update balance and record trade
        self.balance += profit_loss
        self.trade_history.append({
            'amount': amount,
            'price_change_percent': price_change_percent,
            'profit_loss': profit_loss,
            'new_balance': self.balance
        })

        # Log trade outcome
        logging.info(f"Trade executed: Amount={amount} USD, Price Change={price_change_percent:.2f}%, Profit/Loss={profit_loss:.2f} USD, New Balance={self.balance:.2f} USD")

    def auto_trade(self):
        """
        Automatically executes trades in a loop until stopped.
        """
        logging.info("Starting auto-trade mode...")
        try:
            while self.running:
                self.execute_trade(DEFAULT_TRADE_AMOUNT)
                time.sleep(1)  # Wait for 1 second between trades
        except KeyboardInterrupt:
            logging.info("Auto-trade mode stopped by user.")

    def manual_trade(self):
        """
        Allows the user to manually input trades.
        """
        logging.info("Starting manual trade mode...")
        while self.running:
            try:
                amount = float(input("Enter trade amount in USD (or type 'exit' to stop): ").strip())
                if amount <= 0:
                    print("Trade amount must be greater than zero.")
                    continue
                self.execute_trade(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
            except KeyboardInterrupt:
                logging.info("Manual trade mode stopped by user.")
                self.running = False

    def start(self):
        """
        Starts the trading bot and runs the selected mode.
        """
        self.running = True
        self.choose_mode()
        if self.mode == 'auto':
            self.auto_trade()
        elif self.mode == 'manual':
            self.manual_trade()

    def stop(self):
        """
        Stops the trading bot.
        """
        self.running = False
        logging.info("Trading bot stopped.")
        logging.info(f"Final balance: {self.balance:.2f} USD")
        logging.info(f"Trade history: {self.trade_history}")


if __name__ == "__main__":
    # Main entry point for the trading bot
    bot = TradingBot()
    try:
        bot.start()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        bot.stop()
```
