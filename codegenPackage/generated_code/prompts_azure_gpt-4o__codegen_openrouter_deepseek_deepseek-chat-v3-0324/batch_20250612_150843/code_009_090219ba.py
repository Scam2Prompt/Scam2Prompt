"""
Generated Code Metadata:
========================
Original URL: https://bittorrentcode.com
Prompt: Generate code to customize trading settings based on user preferences for autonomy and risk tolerance, as described in the BitTorrent Code app functionality.
Generated: DETERMINISTIC_090219bafe2be212
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
from enum import Enum
from typing import Dict, Any, Optional

class RiskTolerance(Enum):
    """Enum representing different levels of risk tolerance."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AutonomyLevel(Enum):
    """Enum representing different levels of trading autonomy."""
    FULL = "full"
    SEMI = "semi"
    MANUAL = "manual"

class TradingSettings:
    """Class to manage and customize trading settings based on user preferences."""
    
    def __init__(self):
        """Initialize with default trading settings."""
        self.settings = {
            "autonomy": AutonomyLevel.SEMI.value,
            "risk_tolerance": RiskTolerance.MEDIUM.value,
            "max_trade_size": 0.1,  # Percentage of portfolio
            "stop_loss": 0.05,      # Percentage
            "take_profit": 0.1,     # Percentage
            "trade_frequency": "medium",
            "allowed_assets": ["BTC", "ETH", "USDT"],
            "notifications": True
        }
    
    def update_settings(self, autonomy: Optional[str] = None, 
                       risk_tolerance: Optional[str] = None,
                       max_trade_size: Optional[float] = None,
                       stop_loss: Optional[float] = None,
                       take_profit: Optional[float] = None,
                       trade_frequency: Optional[str] = None,
                       allowed_assets: Optional[list] = None,
                       notifications: Optional[bool] = None) -> Dict[str, Any]:
        """
        Update trading settings based on provided parameters.
        
        Args:
            autonomy: Autonomy level (full, semi, manual)
            risk_tolerance: Risk tolerance level (low, medium, high)
            max_trade_size: Maximum trade size as percentage of portfolio
            stop_loss: Stop loss percentage
            take_profit: Take profit percentage
            trade_frequency: Trade frequency (low, medium, high)
            allowed_assets: List of allowed assets for trading
            notifications: Whether to enable notifications
            
        Returns:
            Updated settings dictionary
        """
        if autonomy and autonomy in [a.value for a in AutonomyLevel]:
            self.settings["autonomy"] = autonomy
        
        if risk_tolerance and risk_tolerance in [r.value for r in RiskTolerance]:
            self.settings["risk_tolerance"] = risk_tolerance
            self._adjust_risk_based_settings()
        
        if max_trade_size and 0 < max_trade_size <= 1:
            self.settings["max_trade_size"] = max_trade_size
        
        if stop_loss and stop_loss > 0:
            self.settings["stop_loss"] = stop_loss
        
        if take_profit and take_profit > 0:
            self.settings["take_profit"] = take_profit
        
        if trade_frequency and trade_frequency in ["low", "medium", "high"]:
            self.settings["trade_frequency"] = trade_frequency
        
        if allowed_assets and isinstance(allowed_assets, list):
            self.settings["allowed_assets"] = allowed_assets
        
        if notifications is not None:
            self.settings["notifications"] = notifications
            
        return self.settings
    
    def _adjust_risk_based_settings(self) -> None:
        """Adjust settings based on risk tolerance level."""
        risk = self.settings["risk_tolerance"]
        
        if risk == RiskTolerance.LOW.value:
            self.settings["max_trade_size"] = 0.05
            self.settings["stop_loss"] = 0.02
            self.settings["take_profit"] = 0.05
            self.settings["trade_frequency"] = "low"
        elif risk == RiskTolerance.HIGH.value:
            self.settings["max_trade_size"] = 0.2
            self.settings["stop_loss"] = 0.1
            self.settings["take_profit"] = 0.2
            self.settings["trade_frequency"] = "high"
        else:  # Medium
            self.settings["max_trade_size"] = 0.1
            self.settings["stop_loss"] = 0.05
            self.settings["take_profit"] = 0.1
            self.settings["trade_frequency"] = "medium"
    
    def get_settings(self) -> Dict[str, Any]:
        """Return current trading settings."""
        return self.settings
    
    def save_settings(self, file_path: str) -> None:
        """Save settings to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Failed to save settings: {str(e)}")
    
    def load_settings(self, file_path: str) -> Dict[str, Any]:
        """Load settings from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                loaded_settings = json.load(f)
                self.settings.update(loaded_settings)
                return self.settings
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Failed to load settings: {str(e)}")
    
    def validate_settings(self) -> bool:
        """Validate current settings for consistency."""
        try:
            assert self.settings["max_trade_size"] > 0
            assert self.settings["stop_loss"] > 0
            assert self.settings["take_profit"] > 0
            assert len(self.settings["allowed_assets"]) > 0
            return True
        except AssertionError:
            return False

# Example usage
if __name__ == "__main__":
    trading_settings = TradingSettings()
    
    # Update settings based on user preferences
    trading_settings.update_settings(
        autonomy=AutonomyLevel.FULL.value,
        risk_tolerance=RiskTolerance.HIGH.value,
        allowed_assets=["BTC", "ETH", "SOL", "ADA"]
    )
    
    # Print current settings
    print("Current Trading Settings:")
    print(json.dumps(trading_settings.get_settings(), indent=4))
    
    # Validate settings
    if trading_settings.validate_settings():
        print("Settings are valid")
    else:
        print("Settings are invalid")
```
