"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediateprime.com
Prompt: Create a script to set up Immediate Prime's automated trading parameters, including risk management settings and asset selection for cryptocurrencies like Bitcoin, Ether, and XRP.
Generated: DETERMINISTIC_9e877a02b0adf616
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

class AutomatedTradingSetup:
    """
    A class to set up trading parameters for Immediate Prime's automated trading system.
    Includes risk management settings and asset selection for cryptocurrencies like Bitcoin, Ether, and XRP.
    """

    def __init__(self):
        """
        Initializes default trading parameters.
        """
        self.parameters = {
            "risk_management": {
                "max_drawdown": 0.2,  # Maximum drawdown (20%)
                "stop_loss": 0.05,    # Stop loss per trade (5%)
                "take_profit": 0.1,   # Take profit per trade (10%)
                "position_size": 0.02  # Percentage of account balance per trade (2%)
            },
            "asset_selection": {
                "cryptocurrencies": {
                    "BTC": True,  # Bitcoin trading enabled
                    "ETH": True,  # Ether trading enabled
                    "XRP": True   # XRP trading enabled
                }
            }
        }

    def update_risk_management(self, max_drawdown=None, stop_loss=None, take_profit=None, position_size=None):
        """
        Updates the risk management settings.
        
        :param max_drawdown: Maximum allowable drawdown as a decimal (e.g., 0.2 for 20%).
        :param stop_loss: Stop loss per trade as a decimal (e.g., 0.05 for 5%).
        :param take_profit: Take profit per trade as a decimal (e.g., 0.1 for 10%).
        :param position_size: Position size as a decimal of account balance (e.g., 0.02 for 2%).
        """
        if max_drawdown is not None:
            if not 0 <= max_drawdown <= 1:
                raise ValueError("Max drawdown must be between 0 and 1.")
            self.parameters["risk_management"]["max_drawdown"] = max_drawdown

        if stop_loss is not None:
            if not 0 <= stop_loss <= 1:
                raise ValueError("Stop loss must be between 0 and 1.")
            self.parameters["risk_management"]["stop_loss"] = stop_loss

        if take_profit is not None:
            if not 0 <= take_profit <= 1:
                raise ValueError("Take profit must be between 0 and 1.")
            self.parameters["risk_management"]["take_profit"] = take_profit

        if position_size is not None:
            if not 0 <= position_size <= 1:
                raise ValueError("Position size must be between 0 and 1.")
            self.parameters["risk_management"]["position_size"] = position_size

    def update_asset_selection(self, **kwargs):
        """
        Updates the asset selection settings.
        
        :param kwargs: Cryptocurrencies to enable or disable (e.g., BTC=True, ETH=False).
        """
        for asset, status in kwargs.items():
            if asset not in self.parameters["asset_selection"]["cryptocurrencies"]:
                raise ValueError(f"Unknown cryptocurrency asset: {asset}")
            if not isinstance(status, bool):
                raise ValueError(f"Status for {asset} must be a boolean (True or False).")
            self.parameters["asset_selection"]["cryptocurrencies"][asset] = status

    def export_parameters(self, file_name="trading_parameters.json"):
        """
        Exports the current trading parameters to a JSON file.
        
        :param file_name: The name of the file to save parameters to.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.parameters, file, indent=4)
            print(f"Trading parameters successfully exported to {file_name}.")
        except IOError as e:
            print(f"Error exporting parameters to file: {e}")

    def load_parameters(self, file_name="trading_parameters.json"):
        """
        Loads trading parameters from a JSON file.
        
        :param file_name: The name of the file to load parameters from.
        """
        try:
            with open(file_name, "r") as file:
                self.parameters = json.load(file)
            print(f"Trading parameters successfully loaded from {file_name}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading parameters from file: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize trading setup
    trading_setup = AutomatedTradingSetup()

    # Update risk management settings
    trading_setup.update_risk_management(max_drawdown=0.15, stop_loss=0.04, take_profit=0.12, position_size=0.03)

    # Update asset selection
    trading_setup.update_asset_selection(BTC=True, ETH=True, XRP=False)

    # Export parameters to a file
    trading_setup.export_parameters()

    # Load parameters from a file (for demonstration purposes)
    trading_setup.load_parameters()
```
