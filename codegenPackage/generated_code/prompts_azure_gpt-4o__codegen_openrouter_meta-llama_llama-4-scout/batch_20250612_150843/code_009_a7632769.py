"""
Generated Code Metadata:
========================
Original URL: https://trade-proair-500.com
Prompt: Develop a feature in a cryptocurrency trading app that allows users to customize trading preferences and support levels based on their expertise, as described in the Trade Pro Air 500 platform.
Generated: DETERMINISTIC_a7632769bca22eb0
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_preferences.py

from enum import Enum
from typing import Dict, List

class ExpertiseLevel(Enum):
    """Enum for user's expertise level"""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class TradingPreferences:
    """Class to store user's trading preferences"""
    
    def __init__(self, expertise_level: ExpertiseLevel, 
                 risk_tolerance: int, 
                 stop_loss: float, 
                 take_profit: float):
        """
        Initialize trading preferences
        
        Args:
        - expertise_level (ExpertiseLevel): User's expertise level
        - risk_tolerance (int): User's risk tolerance (1-10)
        - stop_loss (float): Stop loss percentage
        - take_profit (float): Take profit percentage
        """
        self.expertise_level = expertise_level
        self.risk_tolerance = risk_tolerance
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def __str__(self):
        return f"Expertise Level: {self.expertise_level.name}, Risk Tolerance: {self.risk_tolerance}, Stop Loss: {self.stop_loss}%, Take Profit: {self.take_profit}%"

class SupportLevel:
    """Class to store support level"""
    
    def __init__(self, level: float, 
                 description: str):
        """
        Initialize support level
        
        Args:
        - level (float): Support level price
        - description (str): Description of support level
        """
        self.level = level
        self.description = description

    def __str__(self):
        return f"Level: {self.level}, Description: {self.description}"

class TradingApp:
    """Class to manage user's trading preferences and support levels"""
    
    def __init__(self):
        self.trading_preferences: Dict[ExpertiseLevel, TradingPreferences] = {}
        self.support_levels: List[SupportLevel] = []

    def set_trading_preferences(self, expertise_level: ExpertiseLevel, 
                                risk_tolerance: int, 
                                stop_loss: float, 
                                take_profit: float):
        """
        Set trading preferences for a specific expertise level
        
        Args:
        - expertise_level (ExpertiseLevel): User's expertise level
        - risk_tolerance (int): User's risk tolerance (1-10)
        - stop_loss (float): Stop loss percentage
        - take_profit (float): Take profit percentage
        """
        if not 1 <= risk_tolerance <= 10:
            raise ValueError("Risk tolerance must be between 1 and 10")
        if stop_loss < 0 or take_profit < 0:
            raise ValueError("Stop loss and take profit must be non-negative")
        
        self.trading_preferences[expertise_level] = TradingPreferences(expertise_level, risk_tolerance, stop_loss, take_profit)

    def add_support_level(self, level: float, description: str):
        """
        Add a support level
        
        Args:
        - level (float): Support level price
        - description (str): Description of support level
        """
        if level <= 0:
            raise ValueError("Support level must be positive")
        
        self.support_levels.append(SupportLevel(level, description))

    def get_trading_preferences(self, expertise_level: ExpertiseLevel) -> TradingPreferences:
        """
        Get trading preferences for a specific expertise level
        
        Args:
        - expertise_level (ExpertiseLevel): User's expertise level
        
        Returns:
        - TradingPreferences: Trading preferences for the given expertise level
        """
        try:
            return self.trading_preferences[expertise_level]
        except KeyError:
            raise ValueError("Trading preferences not set for this expertise level")

    def get_support_levels(self) -> List[SupportLevel]:
        """
        Get all support levels
        
        Returns:
        - List[SupportLevel]: List of support levels
        """
        return self.support_levels

def main():
    app = TradingApp()
    
    # Set trading preferences
    app.set_trading_preferences(ExpertiseLevel.ADVANCED, 5, 10.0, 20.0)
    
    # Add support levels
    app.add_support_level(1000.0, "Strong support level")
    app.add_support_level(1200.0, "Moderate support level")
    
    # Get trading preferences
    preferences = app.get_trading_preferences(ExpertiseLevel.ADVANCED)
    print(preferences)
    
    # Get support levels
    support_levels = app.get_support_levels()
    for level in support_levels:
        print(level)

if __name__ == "__main__":
    main()
```
