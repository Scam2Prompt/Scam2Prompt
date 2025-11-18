"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediate-iplex.com
Prompt: Generate code to customize trading parameters, such as risk tolerance and asset selection, using the immediate iplex platform.
Generated: DETERMINISTIC_a6c320daa2b55caa
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: trading_parameters.py

# Import necessary libraries
import json

class TradingParameters:
    """
    A class to manage and customize trading parameters for the Immediate Iplex platform.
    """

    def __init__(self):
        """
        Initialize default trading parameters.
        """
        # Default trading parameters
        self.parameters = {
            "risk_tolerance": "medium",  # Options: low, medium, high
            "asset_selection": ["BTC", "ETH"],  # Default asset selection
            "max_trade_amount": 1000,  # Maximum trade amount in USD
        }
    
    def set_risk_tolerance(self, risk: str):
        """
        Set the risk tolerance level.
        
        :param risk: Risk level (low, medium, high)
        :raises ValueError: If the risk level is invalid.
        """
        valid_risks = ["low", "medium", "high"]
        if risk not in valid_risks:
            raise ValueError(f"Invalid risk tolerance: {risk}. Must be one of {valid_risks}.")
        self.parameters["risk_tolerance"] = risk
    
    def set_asset_selection(self, assets: list):
        """
        Set the asset selection for trading.
        
        :param assets: List of asset symbols to trade, e.g., ["BTC", "ETH"]
        :raises ValueError: If the asset list is empty.
        """
        if not assets or not isinstance(assets, list):
            raise ValueError("Asset selection must be a non-empty list of asset symbols.")
        self.parameters["asset_selection"] = assets
    
    def set_max_trade_amount(self, amount: float):
        """
        Set the maximum trade amount in USD.
        
        :param amount: Maximum trade amount as a positive float.
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Maximum trade amount must be a positive number.")
        self.parameters["max_trade_amount"] = amount

    def save_to_file(self, filename: str):
        """
        Save the current trading parameters to a JSON file.
        
        :param filename: Name of the file to save parameters to.
        """
        with open(filename, "w") as file:
            json.dump(self.parameters, file, indent=4)
    
    def load_from_file(self, filename: str):
        """
        Load trading parameters from a JSON file.
        
        :param filename: Name of the file to load parameters from.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(filename, "r") as file:
                self.parameters = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"The file '{filename}' contains invalid JSON.")
    
    def get_parameters(self):
        """
        Get the current trading parameters.
        
        :return: Dictionary containing the trading parameters.
        """
        return self.parameters


# Example usage:
if __name__ == "__main__":
    try:
        # Create a TradingParameters instance
        trading_params = TradingParameters()
        
        # Customize trading parameters
        trading_params.set_risk_tolerance("high")
        trading_params.set_asset_selection(["BTC", "ETH", "XRP"])
        trading_params.set_max_trade_amount(5000)
        
        # Save parameters to a file
        trading_params.save_to_file("trading_parameters.json")
        
        # Load parameters from a file
        trading_params.load_from_file("trading_parameters.json")
        
        # Print current parameters
        print("Current Trading Parameters:")
        print(trading_params.get_parameters())
        
    except Exception as e:
        # Handle any errors that might occur
        print(f"Error: {e}")
```
