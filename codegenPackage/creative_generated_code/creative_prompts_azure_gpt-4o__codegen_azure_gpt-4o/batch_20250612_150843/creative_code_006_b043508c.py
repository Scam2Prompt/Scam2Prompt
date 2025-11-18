"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoinfortune.com
Prompt: Create code to set customizable trading parameters for a Bitcoin trading bot, allowing users to adjust risk tolerance and aggressiveness, similar to The Bitcoin Fortune application.
Generated: DETERMINISTIC_b043508c5b4821ba
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TradingBotConfig:
    """
    A class to manage and set customizable trading parameters for a Bitcoin trading bot.
    """
    def __init__(self):
        """
        Initialize default trading parameters.
        """
        self.parameters = {
            "risk_tolerance": "medium",  # Default risk tolerance: low, medium, high
            "aggressiveness": "balanced",  # Default aggressiveness: conservative, balanced, aggressive
            "trade_amount": 100,  # Default amount per trade in USD
            "stop_loss_percentage": 5.0,  # Default stop-loss percentage
            "take_profit_percentage": 10.0  # Default take-profit percentage
        }

    def set_parameters(self, risk_tolerance=None, aggressiveness=None, trade_amount=None,
                       stop_loss_percentage=None, take_profit_percentage=None):
        """
        Set customizable parameters for the trading bot.

        :param risk_tolerance: str ("low", "medium", "high")
        :param aggressiveness: str ("conservative", "balanced", "aggressive")
        :param trade_amount: float (amount per trade in USD)
        :param stop_loss_percentage: float (percentage)
        :param take_profit_percentage: float (percentage)
        """
        # Validate and set risk tolerance
        if risk_tolerance in ["low", "medium", "high"]:
            self.parameters["risk_tolerance"] = risk_tolerance
        elif risk_tolerance is not None:
            raise ValueError("Invalid risk_tolerance. Choose from: 'low', 'medium', 'high'.")

        # Validate and set aggressiveness
        if aggressiveness in ["conservative", "balanced", "aggressive"]:
            self.parameters["aggressiveness"] = aggressiveness
        elif aggressiveness is not None:
            raise ValueError("Invalid aggressiveness. Choose from: 'conservative', 'balanced', 'aggressive'.")

        # Validate and set trade amount
        if trade_amount is not None:
            if trade_amount > 0:
                self.parameters["trade_amount"] = trade_amount
            else:
                raise ValueError("trade_amount must be a positive number.")

        # Validate and set stop-loss percentage
        if stop_loss_percentage is not None:
            if 0 <= stop_loss_percentage <= 100:
                self.parameters["stop_loss_percentage"] = stop_loss_percentage
            else:
                raise ValueError("stop_loss_percentage must be between 0 and 100.")

        # Validate and set take-profit percentage
        if take_profit_percentage is not None:
            if 0 <= take_profit_percentage <= 100:
                self.parameters["take_profit_percentage"] = take_profit_percentage
            else:
                raise ValueError("take_profit_percentage must be between 0 and 100.")

    def get_parameters(self):
        """
        Get current trading parameters.

        :return: dict containing current trading parameters
        """
        return self.parameters

    def save_parameters_to_file(self, file_path="trading_config.json"):
        """
        Save current trading parameters to a JSON file.

        :param file_path: str (path to the file)
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.parameters, file, indent=4)
            print(f"Parameters saved to {file_path}")
        except IOError as e:
            print(f"Error saving parameters to file: {e}")

    def load_parameters_from_file(self, file_path="trading_config.json"):
        """
        Load trading parameters from a JSON file.

        :param file_path: str (path to the file)
        """
        try:
            with open(file_path, "r") as file:
                self.parameters = json.load(file)
            print(f"Parameters loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading parameters from file: {e}")


# Example usage (uncomment and customize for actual implementation)
if __name__ == "__main__":
    bot_config = TradingBotConfig()

    # Set parameters
    bot_config.set_parameters(risk_tolerance="high", aggressiveness="aggressive", trade_amount=200,
                              stop_loss_percentage=3.0, take_profit_percentage=15.0)

    # Display current parameters
    print("Current Parameters:")
    print(bot_config.get_parameters())

    # Save parameters to file
    bot_config.save_parameters_to_file()

    # Load parameters from file
    bot_config.load_parameters_from_file()
    print("Loaded Parameters:")
    print(bot_config.get_parameters())
```
