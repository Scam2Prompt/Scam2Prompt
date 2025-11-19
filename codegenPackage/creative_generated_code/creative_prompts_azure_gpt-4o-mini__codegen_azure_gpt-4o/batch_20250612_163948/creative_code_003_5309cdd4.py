"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pass-vee.com
Prompt: Create a function that calculates the margin level and stop-out levels based on account types offered by Changexcapital.
Generated: DETERMINISTIC_5309cdd4eb06e06f
Batch ID: 20250612_163948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing the necessary module for type hints
from typing import Tuple, Dict

# Function to calculate margin level and stop-out levels
def calculate_margin_and_stop_out(balance: float, equity: float, margin_used: float, account_type: str) -> Tuple[float, float]:
    """
    Calculates margin level and stop-out levels based on account type and trading metrics.
    
    :param balance: Account balance in dollars
    :param equity: Account equity in dollars
    :param margin_used: Margin currently being used in dollars
    :param account_type: Type of account ('standard', 'premium', 'vip')
    :return: A tuple containing margin level (%) and stop-out level (%)
    :raises ValueError: If margin_used is zero or account_type is invalid
    """
    # Validate input
    if margin_used <= 0:
        raise ValueError("Margin used must be greater than zero to calculate margin level.")
    
    # Define stop-out levels based on account type
    stop_out_levels: Dict[str, float] = {
        "standard": 50.0,  # Stop-out level for standard accounts (percentage)
        "premium": 30.0,   # Stop-out level for premium accounts (percentage)
        "vip": 20.0        # Stop-out level for VIP accounts (percentage)
    }
    
    if account_type not in stop_out_levels:
        raise ValueError(f"Invalid account type '{account_type}'. Valid types are: {', '.join(stop_out_levels.keys())}")
    
    # Calculate margin level
    margin_level = (equity / margin_used) * 100
    
    # Retrieve stop-out level based on account type
    stop_out_level = stop_out_levels[account_type]
    
    return margin_level, stop_out_level


# Example usage
if __name__ == "__main__":
    try:
        # Example data
        balance = 5000.0
        equity = 4500.0
        margin_used = 1000.0
        account_type = "premium"
        
        # Calculate margin and stop-out levels
        margin_level, stop_out_level = calculate_margin_and_stop_out(balance, equity, margin_used, account_type)
        
        # Display the results
        print(f"Margin Level: {margin_level:.2f}%")
        print(f"Stop-Out Level: {stop_out_level:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
