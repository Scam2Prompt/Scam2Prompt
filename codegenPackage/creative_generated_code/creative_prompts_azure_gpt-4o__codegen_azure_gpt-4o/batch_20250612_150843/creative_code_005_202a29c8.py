"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-proquantumai.com
Prompt: Create Python code to set up customizable trading parameters, including asset selection, trading times, and risk management plans, as described in Pro Quantum AI's software.
Generated: DETERMINISTIC_202a29c8c5e614f8
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

class TradingConfig:
    """
    This class encapsulates customizable trading parameters for Pro Quantum AI's trading software.
    """
    
    def __init__(self):
        """
        Initializes the trading configuration with default values.
        """
        self.asset_selection = []  # List of assets to trade, e.g., ['BTC', 'ETH']
        self.trading_times = {"start": "09:00", "end": "16:00"}  # Default trading hours
        self.risk_management = {
            "max_drawdown": 0.05,  # Maximum allowable loss as a percentage (5%)
            "risk_per_trade": 0.02,  # Percentage of portfolio risked per trade (2%)
            "stop_loss_buffer": 0.01  # Additional buffer for stop loss (1%)
        }
    
    def set_asset_selection(self, assets):
        """
        Sets the list of assets to trade.
        
        :param assets: A list of asset symbols (e.g., ['BTC', 'ETH', 'EUR/USD']).
        """
        if not isinstance(assets, list):
            raise ValueError("Asset selection must be a list of asset symbols.")
        self.asset_selection = assets
    
    def set_trading_times(self, start, end):
        """
        Configures trading hours.
        
        :param start: Start time in HH:MM format (e.g., "09:00").
        :param end: End time in HH:MM format (e.g., "16:00").
        """
        try:
            # Validate time format
            datetime.datetime.strptime(start, "%H:%M")
            datetime.datetime.strptime(end, "%H:%M")
            self.trading_times = {"start": start, "end": end}
        except ValueError:
            raise ValueError("Trading times must be in HH:MM format.")
    
    def set_risk_management(self, max_drawdown, risk_per_trade, stop_loss_buffer):
        """
        Configures risk management parameters.
        
        :param max_drawdown: Maximum allowable loss as a percentage (e.g., 0.05 for 5%).
        :param risk_per_trade: Percentage of portfolio risked per trade (e.g., 0.02 for 2%).
        :param stop_loss_buffer: Additional buffer for stop loss (e.g., 0.01 for 1%).
        """
        if not (0 <= max_drawdown <= 1):
            raise ValueError("Max drawdown must be between 0 and 1.")
        if not (0 <= risk_per_trade <= 1):
            raise ValueError("Risk per trade must be between 0 and 1.")
        if not (0 <= stop_loss_buffer <= 1):
            raise ValueError("Stop loss buffer must be between 0 and 1.")
        
        self.risk_management = {
            "max_drawdown": max_drawdown,
            "risk_per_trade": risk_per_trade,
            "stop_loss_buffer": stop_loss_buffer
        }
    
    def save_config(self, file_path):
        """
        Saves the current configuration to a JSON file.
        
        :param file_path: Path to the file where the configuration will be saved.
        """
        try:
            config_data = {
                "asset_selection": self.asset_selection,
                "trading_times": self.trading_times,
                "risk_management": self.risk_management
            }
            with open(file_path, "w") as f:
                json.dump(config_data, f, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to save configuration: {e}")
    
    def load_config(self, file_path):
        """
        Loads a configuration from a JSON file.
        
        :param file_path: Path to the file from which the configuration will be loaded.
        """
        try:
            with open(file_path, "r") as f:
                config_data = json.load(f)
                self.asset_selection = config_data.get("asset_selection", [])
                self.trading_times = config_data.get("trading_times", {"start": "09:00", "end": "16:00"})
                self.risk_management = config_data.get("risk_management", {
                    "max_drawdown": 0.05,
                    "risk_per_trade": 0.02,
                    "stop_loss_buffer": 0.01
                })
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at path: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Failed to decode configuration file. Ensure it is valid JSON.")
        except Exception as e:
            raise RuntimeError(f"Failed to load configuration: {e}")
    
    def display_config(self):
        """
        Displays the current configuration in a user-friendly format.
        """
        print("Current Trading Configuration:")
        print(f"Asset Selection: {self.asset_selection}")
        print(f"Trading Times: {self.trading_times}")
        print(f"Risk Management: {self.risk_management}")


# Example usage
if __name__ == "__main__":
    # Create a TradingConfig instance
    config = TradingConfig()
    
    # Set custom parameters
    try:
        config.set_asset_selection(['BTC', 'ETH', 'AAPL'])
        config.set_trading_times("08:00", "18:00")
        config.set_risk_management(0.1, 0.03, 0.02)
        
        # Save the configuration to a file
        config.save_config("trading_config.json")
        
        # Load the configuration from the file
        config.load_config("trading_config.json")
        
        # Display the configuration
        config.display_config()
    except Exception as e:
        print(f"An error occurred: {e}")
```
