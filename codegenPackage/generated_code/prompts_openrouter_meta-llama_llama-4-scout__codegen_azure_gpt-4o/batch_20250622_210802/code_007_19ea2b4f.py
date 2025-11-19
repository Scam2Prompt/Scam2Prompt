"""
Generated Code Metadata:
========================
Original URL: https://fundfa.com
Prompt: "Design a funded trading program for Sarmaye Digital Funding (SDF), incorporating their rules and plans for cryptocurrency trading."
Generated: DETERMINISTIC_19ea2b4f7df17676
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("sdf_trading.log"), logging.StreamHandler()]
)

class SDFTradingProgram:
    """
    A funded trading program for Sarmaye Digital Funding (SDF).
    This program incorporates SDF's rules and plans for cryptocurrency trading.
    """

    def __init__(self, trading_plan_file):
        """
        Initialize the trading program with a trading plan.

        :param trading_plan_file: Path to the JSON file containing trading rules and plans.
        """
        self.trading_plan = self.load_trading_plan(trading_plan_file)
        self.account_balance = self.trading_plan.get("initial_balance", 0)
        self.max_drawdown = self.trading_plan.get("max_drawdown", 0.2)  # Default to 20%
        self.max_daily_loss = self.trading_plan.get("max_daily_loss", 0.05)  # Default to 5%
        self.trades = []

    def load_trading_plan(self, file_path):
        """
        Load trading rules and plans from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing trading rules and plans.
        """
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Trading plan file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding trading plan file.")
            raise

    def validate_trade(self, trade):
        """
        Validate a trade against SDF's rules.

        :param trade: Dictionary containing trade details (e.g., type, amount, price).
        :return: Boolean indicating whether the trade is valid.
        """
        if trade["amount"] <= 0:
            logging.warning("Trade amount must be positive.")
            return False

        if trade["amount"] * trade["price"] > self.account_balance:
            logging.warning("Insufficient balance for the trade.")
            return False

        return True

    def execute_trade(self, trade):
        """
        Execute a trade if it passes validation.

        :param trade: Dictionary containing trade details (e.g., type, amount, price).
        """
        if not self.validate_trade(trade):
            logging.error("Trade validation failed.")
            return

        # Update account balance based on trade type
        if trade["type"] == "buy":
            self.account_balance -= trade["amount"] * trade["price"]
        elif trade["type"] == "sell":
            self.account_balance += trade["amount"] * trade["price"]
        else:
            logging.error("Invalid trade type.")
            return

        self.trades.append(trade)
        logging.info(f"Trade executed: {trade}")
        self.check_risk_limits()

    def check_risk_limits(self):
        """
        Check if the account is within SDF's risk limits.
        """
        # Calculate drawdown
        initial_balance = self.trading_plan.get("initial_balance", 0)
        drawdown = (initial_balance - self.account_balance) / initial_balance

        if drawdown > self.max_drawdown:
            logging.error("Max drawdown limit exceeded. Trading halted.")
            raise Exception("Max drawdown limit exceeded.")

        # Calculate daily loss
        today = datetime.now().date()
        daily_loss = sum(
            trade["amount"] * trade["price"]
            for trade in self.trades
            if trade["timestamp"].date() == today and trade["type"] == "sell"
        )

        if daily_loss / initial_balance > self.max_daily_loss:
            logging.error("Max daily loss limit exceeded. Trading halted.")
            raise Exception("Max daily loss limit exceeded.")

    def get_account_summary(self):
        """
        Get a summary of the trading account.

        :return: Dictionary containing account balance and trade history.
        """
        return {
            "account_balance": self.account_balance,
            "trades": self.trades,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Load trading plan
        trading_program = SDFTradingProgram("trading_plan.json")

        # Example trades
        trade_1 = {
            "type": "buy",
            "amount": 1.5,
            "price": 20000,
            "timestamp": datetime.now(),
        }
        trade_2 = {
            "type": "sell",
            "amount": 0.5,
            "price": 21000,
            "timestamp": datetime.now(),
        }

        # Execute trades
        trading_program.execute_trade(trade_1)
        trading_program.execute_trade(trade_2)

        # Print account summary
        summary = trading_program.get_account_summary()
        logging.info(f"Account Summary: {summary}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
