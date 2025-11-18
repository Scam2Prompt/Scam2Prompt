"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradegpt360-evix.com
Prompt: Create a script to simulate trading autonomy and support settings, allowing users to adjust their trading preferences as described in the TradeGPT 360 Evix application.
Generated: DETERMINISTIC_2936e76cb1b2b714
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
TradeGPT 360 Evix - Simulated Trading Autonomy Script

This Python script simulates trading autonomy and supports settings
that allow users to adjust their trading preferences dynamically.
The script is designed for flexibility, error handling, and 
production-readiness.

Features:
- Adjustable trading preferences (e.g., risk level, trading frequency, etc.)
- Simulated buy/sell operations
- Logging of trading actions
"""

import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("trading_simulation.log"),
        logging.StreamHandler()
    ]
)

class TradeGPT360Evix:
    def __init__(self, initial_balance=10000.0):
        """
        Initialize the trading simulation with default parameters.

        Args:
            initial_balance (float): Starting balance for trading.
        """
        self.balance = initial_balance
        self.preferences = {
            "risk_level": "medium",  # Options: "low", "medium", "high"
            "trading_frequency": "daily",  # Options: "hourly", "daily", "weekly"
            "stop_loss": 0.05,  # Percentage limit to trigger stop-loss
            "take_profit": 0.1  # Percentage limit to trigger take-profit
        }
        self.positions = []
        logging.info("Trading simulation initialized with balance: $%.2f", self.balance)

    def update_preferences(self, preferences):
        """
        Update trading preferences with user-defined values.

        Args:
            preferences (dict): Dictionary containing updated preferences.
        """
        try:
            # Validate and update preferences
            for key, value in preferences.items():
                if key in self.preferences:
                    self.preferences[key] = value
                    logging.info("Preference updated: %s -> %s", key, str(value))
                else:
                    logging.warning("Invalid preference key: %s", key)
        except Exception as e:
            logging.error("Failed to update preferences: %s", str(e))
            raise ValueError("Error updating preferences.") from e

    def simulate_trade(self, action, amount):
        """
        Simulate a trading action (buy/sell).

        Args:
            action (str): The trading action ("buy" or "sell").
            amount (float): The amount to trade.

        Raises:
            ValueError: If the action is invalid or the amount exceeds the balance.
        """
        try:
            if action not in ["buy", "sell"]:
                raise ValueError("Invalid action. Must be 'buy' or 'sell'.")
            
            if amount <= 0:
                raise ValueError("Trade amount must be positive.")
            
            if action == "buy":
                if amount > self.balance:
                    raise ValueError("Insufficient balance for buy action.")
                self.balance -= amount
                self.positions.append(amount)
                logging.info("Bought position: $%.2f | Balance: $%.2f", amount, self.balance)

            elif action == "sell":
                if len(self.positions) == 0:
                    raise ValueError("No positions available to sell.")
                position_to_sell = self.positions.pop(0)
                profit = position_to_sell * (1 + self.preferences['take_profit'])
                self.balance += profit
                logging.info("Sold position: $%.2f | Profit: $%.2f | Balance: $%.2f", position_to_sell, profit - position_to_sell, self.balance)
        except Exception as e:
            logging.error("Failed to execute trade: %s", str(e))
            raise e

    def show_status(self):
        """
        Display the current trading status (balance, positions, preferences).
        """
        status = {
            "balance": self.balance,
            "positions": self.positions,
            "preferences": self.preferences
        }
        logging.info("Current trading status: %s", json.dumps(status, indent=4))
        print(json.dumps(status, indent=4))

    @staticmethod
    def validate_preferences(preferences):
        """
        Validate user preferences before updating.

        Args:
            preferences (dict): Dictionary containing preferences to validate.

        Returns:
            bool: True if preferences are valid, False otherwise.
        """
        valid_keys = ["risk_level", "trading_frequency", "stop_loss", "take_profit"]
        valid_risk_levels = ["low", "medium", "high"]
        valid_frequencies = ["hourly", "daily", "weekly"]

        for key, value in preferences.items():
            if key not in valid_keys:
                logging.warning("Invalid preference key: %s", key)
                return False
            if key == "risk_level" and value not in valid_risk_levels:
                logging.warning("Invalid risk level: %s", value)
                return False
            if key == "trading_frequency" and value not in valid_frequencies:
                logging.warning("Invalid trading frequency: %s", value)
                return False
            if key in ["stop_loss", "take_profit"] and (not isinstance(value, float) or value <= 0):
                logging.warning("Invalid percentage value for %s: %s", key, value)
                return False
        return True


# Example usage
if __name__ == "__main__":
    try:
        # Initialize trading simulation
        trading_simulation = TradeGPT360Evix()

        # Update preferences
        new_preferences = {
            "risk_level": "high",
            "trading_frequency": "hourly",
            "stop_loss": 0.03,
            "take_profit": 0.15
        }

        if trading_simulation.validate_preferences(new_preferences):
            trading_simulation.update_preferences(new_preferences)
        else:
            logging.error("Invalid preferences provided.")

        # Perform trades
        trading_simulation.simulate_trade("buy", 500)
        trading_simulation.simulate_trade("sell", 500)

        # Show status
        trading_simulation.show_status()

    except Exception as e:
        logging.critical("An error occurred in the trading simulation: %s", str(e))
```
