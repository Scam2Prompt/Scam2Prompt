"""
Generated Code Metadata:
========================
Original URL: https://theimmediatealtex.com
Prompt: Create a Python script to configure trading preferences, including asset selection, trading hours, and risk management settings, for an automated trading system similar to Immediate Altex.
Generated: DETERMINISTIC_a2e4931bae0f7214
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
import logging
from datetime import datetime, time
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingPreferences:
    """
    Class to manage trading preferences for an automated trading system.
    Includes asset selection, trading hours, and risk management settings.
    """
    
    def __init__(self):
        """Initialize trading preferences with default values."""
        self.assets: List[str] = []
        self.trading_hours: Dict[str, Dict[str, time]] = {
            'start': {'hour': 9, 'minute': 30},
            'end': {'hour': 16, 'minute': 0}
        }
        self.risk_management: Dict[str, float] = {
            'max_position_size': 0.1,  # 10% of portfolio
            'stop_loss': 0.02,        # 2% loss
            'take_profit': 0.05,      # 5% gain
            'daily_loss_limit': 0.05  # 5% of portfolio
        }
        self.strategy_settings: Dict[str, any] = {}
    
    def add_asset(self, asset: str) -> bool:
        """Add an asset to the trading list."""
        if not isinstance(asset, str):
            logger.error("Asset must be a string")
            return False
        
        if asset in self.assets:
            logger.warning(f"Asset {asset} already exists in the list")
            return False
            
        self.assets.append(asset)
        logger.info(f"Added asset: {asset}")
        return True
    
    def remove_asset(self, asset: str) -> bool:
        """Remove an asset from the trading list."""
        if asset not in self.assets:
            logger.warning(f"Asset {asset} not found in the list")
            return False
            
        self.assets.remove(asset)
        logger.info(f"Removed asset: {asset}")
        return True
    
    def set_trading_hours(self, start_time: Dict[str, int], end_time: Dict[str, int]) -> bool:
        """Set the trading hours window."""
        try:
            start = time(hour=start_time['hour'], minute=start_time['minute'])
            end = time(hour=end_time['hour'], minute=end_time['minute'])
            
            if start >= end:
                logger.error("Start time must be before end time")
                return False
                
            self.trading_hours = {
                'start': start_time,
                'end': end_time
            }
            logger.info("Trading hours updated successfully")
            return True
        except (KeyError, ValueError) as e:
            logger.error(f"Invalid time format: {str(e)}")
            return False
    
    def update_risk_parameter(self, parameter: str, value: float) -> bool:
        """Update a risk management parameter."""
        if parameter not in self.risk_management:
            logger.error(f"Invalid risk parameter: {parameter}")
            return False
            
        if not isinstance(value, (int, float)) or value <= 0:
            logger.error("Value must be a positive number")
            return False
            
        self.risk_management[parameter] = value
        logger.info(f"Updated {parameter} to {value}")
        return True
    
    def set_strategy_setting(self, key: str, value: any) -> bool:
        """Set a strategy-specific setting."""
        if not isinstance(key, str):
            logger.error("Key must be a string")
            return False
            
        self.strategy_settings[key] = value
        logger.info(f"Set strategy setting {key} = {value}")
        return True
    
    def save_to_file(self, filename: str) -> bool:
        """Save preferences to a JSON file."""
        try:
            data = {
                'assets': self.assets,
                'trading_hours': self.trading_hours,
                'risk_management': self.risk_management,
                'strategy_settings': self.strategy_settings
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            
            logger.info(f"Preferences saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save preferences: {str(e)}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load preferences from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.assets = data.get('assets', [])
            self.trading_hours = data.get('trading_hours', self.trading_hours)
            self.risk_management = data.get('risk_management', self.risk_management)
            self.strategy_settings = data.get('strategy_settings', {})
            
            logger.info(f"Preferences loaded from {filename}")
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            return False
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in {filename}")
            return False
        except Exception as e:
            logger.error(f"Failed to load preferences: {str(e)}")
            return False
    
    def validate(self) -> bool:
        """Validate all preferences."""
        if not self.assets:
            logger.error("No assets selected")
            return False
            
        try:
            start = time(
                hour=self.trading_hours['start']['hour'],
                minute=self.trading_hours['start']['minute']
            )
            end = time(
                hour=self.trading_hours['end']['hour'],
                minute=self.trading_hours['end']['minute']
            )
            
            if start >= end:
                logger.error("Invalid trading hours: start must be before end")
                return False
        except (KeyError, ValueError) as e:
            logger.error(f"Invalid trading hours format: {str(e)}")
            return False
            
        for param, value in self.risk_management.items():
            if not isinstance(value, (int, float)) or value <= 0:
                logger.error(f"Invalid value for {param}: must be positive number")
                return False
                
        return True

# Example usage
if __name__ == "__main__":
    prefs = TradingPreferences()
    
    # Add assets
    prefs.add_asset("AAPL")
    prefs.add_asset("MSFT")
    prefs.add_asset("GOOGL")
    
    # Set trading hours (9:30 AM to 4:00 PM)
    prefs.set_trading_hours(
        {'hour': 9, 'minute': 30},
        {'hour': 16, 'minute': 0}
    )
    
    # Update risk parameters
    prefs.update_risk_parameter('stop_loss', 0.015)  # 1.5% stop loss
    prefs.update_risk_parameter('take_profit', 0.06)  # 6% take profit
    
    # Set strategy settings
    prefs.set_strategy_setting('rsi_period', 14)
    prefs.set_strategy_setting('ema_period', 50)
    
    # Save to file
    prefs.save_to_file('trading_preferences.json')
    
    # Validate preferences
    if prefs.validate():
        print("All preferences are valid")
    else:
        print("Invalid preferences detected")
```
