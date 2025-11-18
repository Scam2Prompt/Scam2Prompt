"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libra-profit.com
Prompt: Develop a feature for a crypto trading platform that allows users to customize trading parameters and switch between manual and automated trading modes, similar to Libra Profit.
Generated: DETERMINISTIC_c9b99dd567c630c7
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
from typing import Callable


class TradingPlatform:
    """
    A class representing a crypto trading platform with customizable trading parameters
    and support for manual and automated trading modes.
    """

    def __init__(self):
        """
        Initialize the trading platform with default parameters and mode settings.
        """
        self.trading_parameters = {
            "max_trade_amount": 1000.0,
            "min_trade_amount": 10.0,
            "target_profit_percent": 5.0,
            "stop_loss_percent": 2.0,
        }
        self.trading_mode = "manual"  # Modes: "manual" or "automated"
        self.is_running = False

    def set_trading_parameters(self, max_trade_amount: float, min_trade_amount: float,
                               target_profit_percent: float, stop_loss_percent: float):
        """
        Update trading parameters.

        :param max_trade_amount: Maximum trade amount in USD.
        :param min_trade_amount: Minimum trade amount in USD.
        :param target_profit_percent: Target profit percentage for trades.
        :param stop_loss_percent: Stop-loss percentage for trades.
        """
        if max_trade_amount <= 0 or min_trade_amount <= 0 or target_profit_percent <= 0 or stop_loss_percent <= 0:
            raise ValueError("All trading parameters must be positive values.")
        if min_trade_amount > max_trade_amount:
            raise ValueError("Minimum trade amount cannot exceed maximum trade amount.")
        self.trading_parameters.update({
            "max_trade_amount": max_trade_amount,
            "min_trade_amount": min_trade_amount,
            "target_profit_percent": target_profit_percent,
            "stop_loss_percent": stop_loss_percent,
        })
        print("Trading parameters updated successfully.")

    def switch_trading_mode(self, mode: str):
        """
        Switch between manual and automated trading modes.

        :param mode: The trading mode to switch to ("manual" or "automated").
        """
        if mode not in ["manual", "automated"]:
            raise ValueError("Invalid trading mode. Please choose 'manual' or 'automated'.")
        self.trading_mode = mode
        print(f"Trading mode switched to '{mode}'.")

    def start_trading(self, automated_strategy: Callable = None):
        """
        Start trading. If in automated mode, the provided strategy function will be used.

        :param automated_strategy: A function representing the automated trading strategy.
        """
        if self.trading_mode == "automated":
            if not automated_strategy:
                raise ValueError("Automated trading mode requires a strategy function.")
            self.is_running = True
            print("Automated trading mode activated. Starting trades...")
            while self.is_running:
                try:
                    automated_strategy(self.trading_parameters)
                    time.sleep(1)  # Simulate interval between trades
                except KeyboardInterrupt:
                    print("Automated trading stopped by user.")
                    self.is_running = False
                except Exception as e:
                    print(f"Error during automated trading: {e}")
        elif self.trading_mode == "manual":
            print("Manual trading mode activated. Awaiting user input...")
            self.is_running = True
            # Simulate user input for manual trading
            try:
                while self.is_running:
                    action = input("Enter 'trade' to execute a trade, or 'stop' to stop: ").strip().lower()
                    if action == "trade":
                        print("Manual trade executed.")
                    elif action == "stop":
                        print("Manual trading stopped.")
                        self.is_running = False
                    else:
                        print("Invalid input. Please enter 'trade' or 'stop'.")
            except KeyboardInterrupt:
                print("Manual trading stopped by user.")
                self.is_running = False
        else:
            raise ValueError("Invalid trading mode.")

    def stop_trading(self):
        """
        Stop trading activities.
        """
        self.is_running = False
        print("Trading stopped successfully.")


# Example automated trading strategy
def example_automated_strategy(params):
    """
    Example automated trading strategy.
    :param params: Trading parameters dictionary.
    """
    print(f"Executing automated trade with parameters: {params}")
    # Simulate trade logic here


# Example usage
if __name__ == "__main__":
    platform = TradingPlatform()
    platform.set_trading_parameters(max_trade_amount=5000.0, min_trade_amount=50.0,
                                    target_profit_percent=10.0, stop_loss_percent=3.0)
    platform.switch_trading_mode("automated")
    platform.start_trading(automated_strategy=example_automated_strategy)
```
