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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingParameters:
    """
    A class to manage trading parameters for Immediate Prime's automated trading system.
    """

    def __init__(self):
        self.parameters = {
            "risk_management": {},
            "asset_selection": []
        }

    def set_risk_management(self, max_drawdown: float, stop_loss: float, take_profit: float):
        """
        Set the risk management parameters.
        
        :param max_drawdown: Maximum acceptable drawdown as a percentage.
        :param stop_loss: Stop loss percentage.
        :param take_profit: Take profit percentage.
        """
        if not all(0 <= x <= 100 for x in [max_drawdown, stop_loss, take_profit]):
            logging.error("Risk management parameters must be between 0 and 100.")
            raise ValueError("Risk management parameters must be between 0 and 100.")

        self.parameters["risk_management"] = {
            "max_drawdown": max_drawdown,
            "stop_loss": stop_loss,
            "take_profit": take_profit
        }
        logging.info("Risk management parameters set successfully.")

    def add_asset(self, asset: str):
        """
        Add an asset to the trading portfolio.
        
        :param asset: The cryptocurrency asset to add (e.g., 'BTC', 'ETH', 'XRP').
        """
        allowed_assets = ['BTC', 'ETH', 'XRP']
        if asset not in allowed_assets:
            logging.error(f"Asset '{asset}' is not supported.")
            raise ValueError(f"Asset '{asset}' is not supported. Choose from {allowed_assets}.")

        if asset not in self.parameters["asset_selection"]:
            self.parameters["asset_selection"].append(asset)
            logging.info(f"Asset '{asset}' added to the portfolio.")
        else:
            logging.warning(f"Asset '{asset}' is already in the portfolio.")

    def remove_asset(self, asset: str):
        """
        Remove an asset from the trading portfolio.
        
        :param asset: The cryptocurrency asset to remove (e.g., 'BTC', 'ETH', 'XRP').
        """
        try:
            self.parameters["asset_selection"].remove(asset)
            logging.info(f"Asset '{asset}' removed from the portfolio.")
        except ValueError:
            logging.warning(f"Asset '{asset}' not found in the portfolio.")

    def get_parameters(self) -> Dict:
        """
        Get the current trading parameters.
        
        :return: A dictionary containing the trading parameters.
        """
        return self.parameters

    def save_parameters(self, filename: str):
        """
        Save the trading parameters to a JSON file.
        
        :param filename: The name of the file to save the parameters.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.parameters, file, indent=4)
            logging.info(f"Parameters saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save parameters to {filename}: {e}")
            raise

def main():
    """
    Main function to set up trading parameters for Immediate Prime.
    """
    trading_params = TradingParameters()
    
    # Set risk management parameters
    trading_params.set_risk_management(max_drawdown=20.0, stop_loss=5.0, take_profit=10.0)

    # Add selected assets
    for asset in ['BTC', 'ETH', 'XRP']:
        trading_params.add_asset(asset)

    # Optionally remove an asset
    trading_params.remove_asset('XRP')

    # Save parameters to a JSON file
    trading_params.save_parameters('trading_parameters.json')

if __name__ == "__main__":
    main()
```
