"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astedex.com
Prompt: Create a script to switch between Simple Mode and Pro Mode in Aster's trading interface and execute trades with different leverage settings.
Generated: DETERMINISTIC_e9079be2e34623ac
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class TradingInterface:
    def __init__(self):
        """Initialize trading interface with default settings."""
        self.mode = "Simple"  # Default mode is Simple Mode
        self.leverage = 1     # Default leverage is 1 for Simple Mode

    def switch_mode(self, mode):
        """
        Switch between Simple Mode and Pro Mode.

        Args:
            mode (str): Desired mode, either 'Simple' or 'Pro'.

        Raises:
            ValueError: If an invalid mode is provided.
        """
        if mode not in ["Simple", "Pro"]:
            raise ValueError("Invalid mode. Please choose 'Simple' or 'Pro'.")
        
        self.mode = mode
        self.leverage = 1 if mode == "Simple" else 10  # Simple Mode uses 1x leverage, Pro Mode uses 10x leverage

        logging.info(f"Switched to {mode} Mode with leverage set to {self.leverage}.")

    def execute_trade(self, trade_amount, direction):
        """
        Execute a trade with the current mode and leverage settings.

        Args:
            trade_amount (float): The amount to trade.
            direction (str): The direction of the trade, either 'buy' or 'sell'.

        Raises:
            ValueError: If trade amount is non-positive or direction is invalid.
        """
        if trade_amount <= 0:
            raise ValueError("Trade amount must be positive.")
        if direction not in ["buy", "sell"]:
            raise ValueError("Invalid trade direction. Please use 'buy' or 'sell'.")
        
        # Simulate trade execution
        logging.info(f"Executing trade: {direction} ${trade_amount} with {self.leverage}x leverage in {self.mode} Mode.")

# Main execution block
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Initialize the trading interface
        trading_interface = TradingInterface()

        # Switch mode and execute trades
        trading_interface.switch_mode("Pro")  # Switch to Pro Mode
        trading_interface.execute_trade(1000, "buy")  # Execute a buy trade in Pro Mode

        trading_interface.switch_mode("Simple")  # Switch back to Simple Mode
        trading_interface.execute_trade(500, "sell")  # Execute a sell trade in Simple Mode

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
