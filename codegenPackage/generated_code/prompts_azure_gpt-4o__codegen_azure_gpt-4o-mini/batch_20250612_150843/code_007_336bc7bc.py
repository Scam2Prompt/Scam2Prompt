"""
Generated Code Metadata:
========================
Original URL: https://the-immediateduac.com
Prompt: Develop a customizable trading parameter system that allows users to set assets, trading times, and risk management plans, inspired by IMMEDIATE DUAC's personalization features.
Generated: DETERMINISTIC_336bc7bcda2d70fb
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class TradingParameter:
    """
    A class to represent trading parameters for a customizable trading system.
    """

    def __init__(self, asset: str, trading_times: List[str], risk_management: Dict[str, Any]):
        """
        Initializes the TradingParameter with asset, trading times, and risk management plan.

        :param asset: The asset to be traded (e.g., 'AAPL', 'BTC').
        :param trading_times: A list of trading times in 'HH:MM' format.
        :param risk_management: A dictionary containing risk management parameters.
        """
        self.asset = asset
        self.trading_times = trading_times
        self.risk_management = risk_management

    def validate(self) -> None:
        """
        Validates the trading parameters to ensure they meet the required criteria.

        :raises ValueError: If any parameter is invalid.
        """
        if not isinstance(self.asset, str) or not self.asset:
            raise ValueError("Asset must be a non-empty string.")
        
        if not isinstance(self.trading_times, list) or not all(isinstance(t, str) for t in self.trading_times):
            raise ValueError("Trading times must be a list of strings.")
        
        if not isinstance(self.risk_management, dict):
            raise ValueError("Risk management must be a dictionary.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the trading parameters to a dictionary format.

        :return: A dictionary representation of the trading parameters.
        """
        return {
            "asset": self.asset,
            "trading_times": self.trading_times,
            "risk_management": self.risk_management
        }

    def save_to_file(self, filename: str) -> None:
        """
        Saves the trading parameters to a JSON file.

        :param filename: The name of the file to save the parameters to.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'TradingParameter':
        """
        Loads trading parameters from a JSON file.

        :param filename: The name of the file to load the parameters from.
        :return: An instance of TradingParameter.
        :raises IOError: If there is an error reading the file.
        :raises ValueError: If the file content is invalid.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                trading_param = cls(data['asset'], data['trading_times'], data['risk_management'])
                trading_param.validate()  # Validate loaded parameters
                return trading_param
        except IOError as e:
            raise IOError(f"Error reading from file {filename}: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid data in file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a trading parameter instance
        trading_param = TradingParameter(
            asset='AAPL',
            trading_times=['09:30', '10:00', '15:30'],
            risk_management={
                'max_drawdown': 0.1,
                'stop_loss': 0.05,
                'take_profit': 0.15
            }
        )

        # Validate and save to file
        trading_param.validate()
        trading_param.save_to_file('trading_parameters.json')

        # Load from file
        loaded_param = TradingParameter.load_from_file('trading_parameters.json')
        print("Loaded Trading Parameters:", loaded_param.to_dict())

    except Exception as e:
        print(f"An error occurred: {e}")
```
