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
from typing import List, Dict, Any

class TradingParameter:
    """
    A class to represent trading parameters for a customizable trading system.
    """

    def __init__(self, asset: str, trading_times: List[str], risk_management: Dict[str, Any]):
        """
        Initialize the TradingParameter instance.

        :param asset: The asset to be traded (e.g., 'AAPL', 'BTC').
        :param trading_times: A list of trading time intervals (e.g., ['09:00-12:00', '13:00-16:00']).
        :param risk_management: A dictionary defining the risk management strategy.
        """
        self.asset = asset
        self.trading_times = trading_times
        self.risk_management = risk_management

    def validate_parameters(self) -> None:
        """
        Validates the trading parameters to ensure they meet required criteria.

        :raises ValueError: If any parameters are invalid.
        """
        if not self.asset:
            raise ValueError("Asset cannot be empty.")
        
        if not isinstance(self.trading_times, list) or not self.trading_times:
            raise ValueError("Trading times must be a non-empty list.")

        if not isinstance(self.risk_management, dict) or not self.risk_management:
            raise ValueError("Risk management must be a non-empty dictionary.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the trading parameters into a dictionary format.

        :return: A dictionary representation of the trading parameters.
        """
        return {
            "asset": self.asset,
            "trading_times": self.trading_times,
            "risk_management": self.risk_management
        }

    @staticmethod
    def load_from_json(file_path: str) -> 'TradingParameter':
        """
        Loads trading parameters from a JSON file.

        :param file_path: The path to the JSON file containing trading parameters.
        :return: An instance of TradingParameter.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file contents are not valid JSON.
        :raises ValueError: If the loaded parameters are invalid.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                trading_param = TradingParameter(
                    asset=data['asset'],
                    trading_times=data['trading_times'],
                    risk_management=data['risk_management']
                )
                trading_param.validate_parameters()
                return trading_param
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file: {file_path}") from e

    def save_to_json(self, file_path: str) -> None:
        """
        Saves the trading parameters to a JSON file.

        :param file_path: The path to the JSON file where trading parameters will be saved.
        :raises IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file: {file_path}") from e


# Example usage:
if __name__ == "__main__":
    # Define trading parameters
    try:
        trading_param = TradingParameter(
            asset="AAPL",
            trading_times=["09:00-12:00", "13:00-16:00"],
            risk_management={
                "max_loss_percentage": 5,
                "stop_loss": True
            }
        )
        
        # Validate and save to JSON
        trading_param.validate_parameters()
        trading_param.save_to_json("trading_parameters.json")

        # Load from JSON
        loaded_param = TradingParameter.load_from_json("trading_parameters.json")
        print("Loaded Trading Parameters:", loaded_param.to_dict())

    except Exception as e:
        print(f"An error occurred: {e}")
```
