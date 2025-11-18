"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-evrixedge.com
Prompt: Write code to customize trading parameters in Evrix Edge's automated trading software, including risk management settings and asset selection.
Generated: DETERMINISTIC_90786471f4fe3e1f
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# trading_parameters.py

# Import necessary modules
import json

class TradingParameters:
    """
    A class to handle customizable trading parameters for Evrix Edge's automated trading software.
    """

    def __init__(self):
        """
        Initialize default trading parameters.
        """
        self.parameters = {
            "risk_management": {
                "max_drawdown_percent": 5,  # Maximum allowable portfolio drawdown percentage
                "stop_loss_percent": 2,    # Stop-loss percentage per trade
                "take_profit_percent": 5,  # Take-profit percentage per trade
                "position_size_percent": 1   # Percentage of portfolio to allocate to a single trade
            },
            "asset_selection": {
                "assets": ["BTC", "ETH", "XRP"],  # Default selected assets for trading
                "excluded_assets": []            # Assets to exclude from trading
            }
        }

    def update_risk_management(self, max_drawdown=None, stop_loss=None, take_profit=None, position_size=None):
        """
        Update risk management parameters with new values.
        :param max_drawdown: New maximum drawdown percentage.
        :param stop_loss: New stop-loss percentage.
        :param take_profit: New take-profit percentage.
        :param position_size: New position size percentage.
        """
        try:
            if max_drawdown is not None:
                self.parameters["risk_management"]["max_drawdown_percent"] = max_drawdown
            if stop_loss is not None:
                self.parameters["risk_management"]["stop_loss_percent"] = stop_loss
            if take_profit is not None:
                self.parameters["risk_management"]["take_profit_percent"] = take_profit
            if position_size is not None:
                self.parameters["risk_management"]["position_size_percent"] = position_size
        except Exception as e:
            raise ValueError(f"Error updating risk management parameters: {e}")

    def update_asset_selection(self, assets=None, excluded_assets=None):
        """
        Update asset selection parameters.
        :param assets: A list of assets to include for trading.
        :param excluded_assets: A list of assets to exclude from trading.
        """
        try:
            if assets is not None:
                self.parameters["asset_selection"]["assets"] = assets
            if excluded_assets is not None:
                self.parameters["asset_selection"]["excluded_assets"] = excluded_assets
        except Exception as e:
            raise ValueError(f"Error updating asset selection parameters: {e}")

    def save_parameters_to_file(self, file_path):
        """
        Save current trading parameters to a JSON file.
        :param file_path: Path to the file where parameters will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.parameters, file, indent=4)
        except Exception as e:
            raise IOError(f"Error saving parameters to file: {e}")

    def load_parameters_from_file(self, file_path):
        """
        Load trading parameters from a JSON file.
        :param file_path: Path to the file from which parameters will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.parameters = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from file: {file_path}")
        except Exception as e:
            raise IOError(f"Error reading parameters from file: {e}")

    def get_parameters(self):
        """
        Retrieve current trading parameters.
        :return: A dictionary of current trading parameters.
        """
        return self.parameters


# Example usage:
if __name__ == "__main__":
    # Initialize the TradingParameters class
    tp = TradingParameters()

    # Update risk management settings
    tp.update_risk_management(max_drawdown=7, stop_loss=3, take_profit=6, position_size=2)

    # Update asset selection
    tp.update_asset_selection(assets=["BTC", "ETH", "ADA"], excluded_assets=["XRP"])

    # Save parameters to a file
    tp.save_parameters_to_file("trading_parameters.json")

    # Load parameters from a file
    tp.load_parameters_from_file("trading_parameters.json")

    # Display the current parameters
    print("Current Trading Parameters:")
    print(json.dumps(tp.get_parameters(), indent=4))
```
