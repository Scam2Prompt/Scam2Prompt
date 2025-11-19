"""
Generated Code Metadata:
========================
Original URL: https://thebitcoindecoder.com
Prompt: Create a script that simulates adjustable assistance and autonomy levels for a cryptocurrency trading app, allowing users to customize their trading preferences and risk tolerance as described in the Bitcoin Decoder app.
Generated: DETERMINISTIC_48319b8e2e4b9187
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
from typing import Dict, Optional, Union

class AutonomyLevel(Enum):
    """Enum representing different autonomy levels for trading."""
    FULL_AUTONOMY = "full_autonomy"
    SEMI_AUTONOMY = "semi_autonomy"
    MANUAL = "manual"

class AssistanceLevel(Enum):
    """Enum representing different assistance levels for trading."""
    AGGRESSIVE = "aggressive"
    MODERATE = "moderate"
    CONSERVATIVE = "conservative"

class TradingPreferences:
    """Class to manage user trading preferences and risk tolerance."""
    
    def __init__(self):
        self.autonomy_level = AutonomyLevel.MANUAL
        self.assistance_level = AssistanceLevel.MODERATE
        self.risk_tolerance = 50  # Default to medium risk (0-100 scale)
        self.preferred_coins = ["BTC", "ETH"]  # Default preferred cryptocurrencies
        self.trading_hours = {"start": "09:00", "end": "17:00"}  # Default trading hours
        self.max_daily_loss = 5  # Percentage of portfolio
        self.take_profit = 10  # Percentage
        self.stop_loss = 5  # Percentage
        
    def update_preferences(
        self,
        autonomy_level: Optional[AutonomyLevel] = None,
        assistance_level: Optional[AssistanceLevel] = None,
        risk_tolerance: Optional[int] = None,
        preferred_coins: Optional[list] = None,
        trading_hours: Optional[Dict[str, str]] = None,
        max_daily_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        stop_loss: Optional[float] = None
    ) -> None:
        """Update user trading preferences with validation."""
        if autonomy_level is not None:
            if not isinstance(autonomy_level, AutonomyLevel):
                raise ValueError("Invalid autonomy level")
            self.autonomy_level = autonomy_level
            
        if assistance_level is not None:
            if not isinstance(assistance_level, AssistanceLevel):
                raise ValueError("Invalid assistance level")
            self.assistance_level = assistance_level
            
        if risk_tolerance is not None:
            if not 0 <= risk_tolerance <= 100:
                raise ValueError("Risk tolerance must be between 0 and 100")
            self.risk_tolerance = risk_tolerance
            
        if preferred_coins is not None:
            if not isinstance(preferred_coins, list):
                raise ValueError("Preferred coins must be a list")
            self.preferred_coins = preferred_coins
            
        if trading_hours is not None:
            if not all(key in trading_hours for key in ["start", "end"]):
                raise ValueError("Trading hours must include 'start' and 'end'")
            self.trading_hours = trading_hours
            
        if max_daily_loss is not None:
            if max_daily_loss < 0 or max_daily_loss > 100:
                raise ValueError("Max daily loss must be between 0 and 100")
            self.max_daily_loss = max_daily_loss
            
        if take_profit is not None:
            if take_profit < 0:
                raise ValueError("Take profit must be positive")
            self.take_profit = take_profit
            
        if stop_loss is not None:
            if stop_loss < 0:
                raise ValueError("Stop loss must be positive")
            self.stop_loss = stop_loss
    
    def to_dict(self) -> Dict[str, Union[str, int, float, list, dict]]:
        """Convert preferences to dictionary for storage or transmission."""
        return {
            "autonomy_level": self.autonomy_level.value,
            "assistance_level": self.assistance_level.value,
            "risk_tolerance": self.risk_tolerance,
            "preferred_coins": self.preferred_coins,
            "trading_hours": self.trading_hours,
            "max_daily_loss": self.max_daily_loss,
            "take_profit": self.take_profit,
            "stop_loss": self.stop_loss
        }
    
    def from_dict(self, data: Dict[str, Union[str, int, float, list, dict]]) -> None:
        """Load preferences from dictionary."""
        try:
            self.autonomy_level = AutonomyLevel(data["autonomy_level"])
            self.assistance_level = AssistanceLevel(data["assistance_level"])
            self.risk_tolerance = data["risk_tolerance"]
            self.preferred_coins = data["preferred_coins"]
            self.trading_hours = data["trading_hours"]
            self.max_daily_loss = data["max_daily_loss"]
            self.take_profit = data["take_profit"]
            self.stop_loss = data["stop_loss"]
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid preference data: {str(e)}")

class TradingSimulator:
    """Simulator for cryptocurrency trading with adjustable autonomy and assistance."""
    
    def __init__(self, preferences: TradingPreferences):
        self.preferences = preferences
        self.portfolio = {}  # Simulated portfolio
        self.trade_history = []  # Simulated trade history
        
    def adjust_autonomy(self, new_level: AutonomyLevel) -> None:
        """Adjust the autonomy level for trading."""
        self.preferences.update_preferences(autonomy_level=new_level)
        
    def adjust_assistance(self, new_level: AssistanceLevel) -> None:
        """Adjust the assistance level for trading."""
        self.preferences.update_preferences(assistance_level=new_level)
        
    def simulate_trade(self, coin: str, amount: float, price: float, action: str) -> bool:
        """Simulate a trade based on current preferences."""
        if coin not in self.preferences.preferred_coins:
            return False
            
        if action not in ["buy", "sell"]:
            return False
            
        # Simulate trade execution based on autonomy level
        if self.preferences.autonomy_level == AutonomyLevel.FULL_AUTONOMY:
            self._execute_trade(coin, amount, price, action)
            return True
        elif self.preferences.autonomy_level == AutonomyLevel.SEMI_AUTONOMY:
            # In semi-autonomy, we might add additional checks or confirmations
            self._execute_trade(coin, amount, price, action)
            return True
        else:  # Manual
            # In manual mode, trades would need user confirmation
            return False
    
    def _execute_trade(self, coin: str, amount: float, price: float, action: str) -> None:
        """Internal method to execute a trade and update portfolio."""
        trade = {
            "coin": coin,
            "amount": amount,
            "price": price,
            "action": action,
            "timestamp": "2023-01-01T00:00:00"  # Simulated timestamp
        }
        self.trade_history.append(trade)
        
        if action == "buy":
            self.portfolio[coin] = self.portfolio.get(coin, 0) + amount
        else:
            self.portfolio[coin] = self.portfolio.get(coin, 0) - amount
            
    def save_preferences(self, filename: str) -> None:
        """Save preferences to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.preferences.to_dict(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save preferences: {str(e)}")
    
    def load_preferences(self, filename: str) -> None:
        """Load preferences from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.preferences.from_dict(data)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load preferences: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create new preferences
    preferences = TradingPreferences()
    
    # Update preferences
    preferences.update_preferences(
        autonomy_level=AutonomyLevel.SEMI_AUTONOMY,
        assistance_level=AssistanceLevel.MODERATE,
        risk_tolerance=70,
        preferred_coins=["BTC", "ETH", "SOL"],
        max_daily_loss=3,
        take_profit=15,
        stop_loss=7
    )
    
    # Create simulator with preferences
    simulator = TradingSimulator(preferences)
    
    # Simulate some trades
    simulator.simulate_trade("BTC", 0.1, 50000, "buy")
    simulator.simulate_trade("ETH", 1, 3000, "buy")
    
    # Save preferences to file
    simulator.save_preferences("trading_preferences.json")
    
    # Load preferences from file
    new_simulator = TradingSimulator(TradingPreferences())
    new_simulator.load_preferences("trading_preferences.json")
```
