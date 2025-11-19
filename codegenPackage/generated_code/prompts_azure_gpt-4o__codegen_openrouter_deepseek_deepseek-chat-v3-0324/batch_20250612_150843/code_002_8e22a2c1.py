"""
Generated Code Metadata:
========================
Original URL: https://1k-daily-profits.com
Prompt: Create a script to automate the process of setting trading parameters, such as risk tolerance and preferred assets, inspired by the customization features of the 1K Daily Profit software.
Generated: DETERMINISTIC_8e22a2c1bd7dc970
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
import os
from typing import Dict, List, Optional, Union

class TradingParameterConfigurator:
    """
    A class to automate the process of setting trading parameters such as risk tolerance
    and preferred assets. Inspired by customization features of trading software.
    """
    
    def __init__(self, config_file: str = "trading_config.json"):
        """
        Initialize the configurator with a configuration file.
        
        Args:
            config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.default_config = {
            "risk_tolerance": "medium",
            "preferred_assets": ["BTC", "ETH", "XRP"],
            "daily_profit_target": 1000,
            "stop_loss_percentage": 2.0,
            "take_profit_percentage": 5.0,
            "trading_hours": "09:00-17:00"
        }
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Union[str, List[str], float, int]]:
        """
        Load configuration from file or create default if file doesn't exist.
        
        Returns:
            Dictionary containing the configuration parameters.
        """
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            return self.default_config.copy()
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config: {e}. Using default configuration.")
            return self.default_config.copy()

    def save_config(self) -> bool:
        """
        Save the current configuration to file.
        
        Returns:
            True if save was successful, False otherwise.
        """
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except IOError as e:
            print(f"Error saving config: {e}")
            return False

    def set_risk_tolerance(self, level: str) -> bool:
        """
        Set the risk tolerance level.
        
        Args:
            level: Risk level (low, medium, high)
            
        Returns:
            True if successful, False otherwise
        """
        valid_levels = ["low", "medium", "high"]
        if level.lower() not in valid_levels:
            print(f"Invalid risk level. Must be one of: {valid_levels}")
            return False
        
        self.config["risk_tolerance"] = level.lower()
        return self.save_config()

    def set_preferred_assets(self, assets: List[str]) -> bool:
        """
        Set the preferred trading assets.
        
        Args:
            assets: List of asset symbols (e.g., ["BTC", "ETH"])
            
        Returns:
            True if successful, False otherwise
        """
        if not isinstance(assets, list) or not all(isinstance(a, str) for a in assets):
            print("Assets must be a list of strings")
            return False
        
        self.config["preferred_assets"] = [a.upper() for a in assets]
        return self.save_config()

    def set_daily_profit_target(self, amount: float) -> bool:
        """
        Set the daily profit target.
        
        Args:
            amount: Target amount in USD
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print("Daily profit target must be positive")
            return False
        
        self.config["daily_profit_target"] = amount
        return self.save_config()

    def set_stop_loss(self, percentage: float) -> bool:
        """
        Set the stop loss percentage.
        
        Args:
            percentage: Stop loss percentage (e.g., 2.0 for 2%)
            
        Returns:
            True if successful, False otherwise
        """
        if percentage <= 0 or percentage > 100:
            print("Stop loss percentage must be between 0 and 100")
            return False
        
        self.config["stop_loss_percentage"] = percentage
        return self.save_config()

    def set_take_profit(self, percentage: float) -> bool:
        """
        Set the take profit percentage.
        
        Args:
            percentage: Take profit percentage (e.g., 5.0 for 5%)
            
        Returns:
            True if successful, False otherwise
        """
        if percentage <= 0 or percentage > 100:
            print("Take profit percentage must be between 0 and 100")
            return False
        
        self.config["take_profit_percentage"] = percentage
        return self.save_config()

    def set_trading_hours(self, hours: str) -> bool:
        """
        Set the preferred trading hours.
        
        Args:
            hours: Trading hours in format "HH:MM-HH:MM"
            
        Returns:
            True if successful, False otherwise
        """
        try:
            start, end = hours.split('-')
            # Simple validation of time format
            if len(start) != 5 or len(end) != 5 or start[2] != ':' or end[2] != ':':
                raise ValueError
            int(start.replace(':', ''))
            int(end.replace(':', ''))
        except ValueError:
            print("Invalid time format. Use HH:MM-HH:MM")
            return False
        
        self.config["trading_hours"] = hours
        return self.save_config()

    def get_config(self) -> Dict[str, Union[str, List[str], float, int]]:
        """
        Get the current configuration.
        
        Returns:
            Dictionary containing all configuration parameters.
        """
        return self.config.copy()

    def reset_to_defaults(self) -> bool:
        """
        Reset all parameters to default values.
        
        Returns:
            True if successful, False otherwise
        """
        self.config = self.default_config.copy()
        return self.save_config()


# Example usage
if __name__ == "__main__":
    configurator = TradingParameterConfigurator()
    
    # Set some parameters
    configurator.set_risk_tolerance("high")
    configurator.set_preferred_assets(["BTC", "LTC", "ADA"])
    configurator.set_daily_profit_target(1500)
    configurator.set_stop_loss(1.5)
    configurator.set_take_profit(7.5)
    configurator.set_trading_hours("08:00-16:00")
    
    # Display current config
    print("Current Configuration:")
    print(json.dumps(configurator.get_config(), indent=4))
```
