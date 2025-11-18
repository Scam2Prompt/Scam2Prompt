"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediateduac.com
Prompt: Develop a customizable trading parameter system that allows users to set assets, trading times, and risk management plans, inspired by IMMEDIATE DUAC's personalization features.
Generated: DETERMINISTIC_336bc7bcda2d70fb
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
import datetime

class TradingParameterSystem:
    """
    A customizable trading parameter system to set assets, trading times, and risk management plans.
    """

    def __init__(self):
        """
        Initializes the trading parameter system with default values.
        """
        self.parameters = {
            "assets": [],
            "trading_hours": {"start_time": "09:00", "end_time": "16:00"},
            "risk_management": {"max_risk_percent": 2, "stop_loss_percent": 1, "take_profit_percent": 3}
        }

    def set_assets(self, assets):
        """
        Set assets for trading.
        :param assets: List of asset names (e.g., ["AAPL", "GOOGL", "BTC"]).
        """
        if not isinstance(assets, list) or not all(isinstance(asset, str) for asset in assets):
            raise ValueError("Assets must be a list of strings.")
        self.parameters["assets"] = assets

    def set_trading_hours(self, start_time, end_time):
        """
        Set trading hours.
        :param start_time: Start time in "HH:MM" format (24-hour clock).
        :param end_time: End time in "HH:MM" format (24-hour clock).
        """
        try:
            datetime.datetime.strptime(start_time, "%H:%M")
            datetime.datetime.strptime(end_time, "%H:%M")
        except ValueError:
            raise ValueError("Start and end times must be in 'HH:MM' format.")
        
        self.parameters["trading_hours"] = {"start_time": start_time, "end_time": end_time}

    def set_risk_management(self, max_risk_percent, stop_loss_percent, take_profit_percent):
        """
        Set risk management parameters.
        :param max_risk_percent: Maximum percentage of portfolio risk per trade (e.g., 2).
        :param stop_loss_percent: Stop loss percentage (e.g., 1).
        :param take_profit_percent: Take profit percentage (e.g., 3).
        """
        if not all(isinstance(param, (int, float)) and param > 0 for param in [max_risk_percent, stop_loss_percent, take_profit_percent]):
            raise ValueError("Risk management parameters must be positive numbers.")
        
        self.parameters["risk_management"] = {
            "max_risk_percent": max_risk_percent,
            "stop_loss_percent": stop_loss_percent,
            "take_profit_percent": take_profit_percent
        }

    def get_parameters(self):
        """
        Retrieve the current trading parameters.
        :return: Dictionary of current trading parameters.
        """
        return self.parameters

    def save_parameters_to_file(self, file_path):
        """
        Save trading parameters to a JSON file.
        :param file_path: Path to the file where parameters will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.parameters, file, indent=4)
        except Exception as e:
            raise IOError(f"An error occurred while saving parameters to file: {e}")

    def load_parameters_from_file(self, file_path):
        """
        Load trading parameters from a JSON file.
        :param file_path: Path to the file where parameters will be loaded from.
        """
        try:
            with open(file_path, 'r') as file:
                self.parameters = json.load(file)
        except Exception as e:
            raise IOError(f"An error occurred while loading parameters from file: {e}")

# Example usage:
if __name__ == "__main__":
    trading_system = TradingParameterSystem()

    # Customizing trading parameters
    trading_system.set_assets(["AAPL", "GOOGL", "BTC"])
    trading_system.set_trading_hours("08:00", "18:00")
    trading_system.set_risk_management(max_risk_percent=2, stop_loss_percent=1, take_profit_percent=5)

    # Retrieve and display parameters
    print("Current Trading Parameters:")
    print(trading_system.get_parameters())

    # Save parameters to a file
    trading_system.save_parameters_to_file("trading_parameters.json")

    # Load parameters from a file
    trading_system.load_parameters_from_file("trading_parameters.json")
    print("\nLoaded Trading Parameters:")
    print(trading_system.get_parameters())
```
