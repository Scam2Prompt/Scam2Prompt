"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-3x-maxair.com
Prompt: Create a function that customizes trading parameters for the Immediate 3X Maxair software, allowing users to set their risk management strategies.
Generated: DETERMINISTIC_a623ac66a72a43cf
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Immediate 3X Maxair - Trading Parameters Customization Module
# This module allows users to customize their risk management strategies.

# Imports
import json

class TradingParameterError(Exception):
    """Custom exception for trading parameter validation errors."""
    pass

def customize_trading_parameters(risk_percentage: float, max_trade_limit: int, stop_loss: float, take_profit: float):
    """
    Customizes trading parameters for Immediate 3X Maxair software.
    
    Args:
        risk_percentage (float): Percentage of account capital to risk per trade (0-100).
        max_trade_limit (int): Maximum number of trades allowed concurrently (>0).
        stop_loss (float): Stop-loss percentage for each trade (0-100).
        take_profit (float): Take-profit percentage for each trade (0-100).
    
    Returns:
        dict: Dictionary of customized trading parameters.
    
    Raises:
        TradingParameterError: If any parameter is out of valid range.
    """
    
    # Validate inputs
    if not (0 <= risk_percentage <= 100):
        raise TradingParameterError("Risk percentage must be between 0 and 100.")
    if max_trade_limit <= 0:
        raise TradingParameterError("Max trade limit must be greater than 0.")
    if not (0 <= stop_loss <= 100):
        raise TradingParameterError("Stop-loss percentage must be between 0 and 100.")
    if not (0 <= take_profit <= 100):
        raise TradingParameterError("Take-profit percentage must be between 0 and 100.")
    
    # Create trading parameters dictionary
    trading_parameters = {
        "risk_percentage": risk_percentage,
        "max_trade_limit": max_trade_limit,
        "stop_loss": stop_loss,
        "take_profit": take_profit
    }
    
    # Save to a JSON file for persistence (simulating production-ready storage)
    try:
        with open("trading_parameters.json", "w") as file:
            json.dump(trading_parameters, file, indent=4)
    except IOError as e:
        raise TradingParameterError(f"Failed to save trading parameters to file: {e}")
    
    return trading_parameters

# Example usage:
if __name__ == "__main__":
    try:
        # Customize trading parameters with user-defined values
        params = customize_trading_parameters(risk_percentage=2.5, 
                                               max_trade_limit=10, 
                                               stop_loss=5.0, 
                                               take_profit=10.0)
        print("Trading parameters successfully customized:")
        print(params)
    except TradingParameterError as e:
        print(f"Error customizing trading parameters: {e}")
```
