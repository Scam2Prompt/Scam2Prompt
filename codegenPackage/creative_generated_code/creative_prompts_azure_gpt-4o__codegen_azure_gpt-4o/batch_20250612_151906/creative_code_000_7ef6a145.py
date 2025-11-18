"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Write Python code to calculate the potential profit of a trade using the leverage and spread details for the "STANDARD" account type offered by S D STAR FX LTD.
Generated: DETERMINISTIC_7ef6a14504b2b453
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

# Define a function to calculate potential profit
def calculate_trade_profit(account_type: str, trade_balance: float, leverage: int, spread: float) -> Union[float, str]:
    """
    Calculate the potential profit of a trade based on account type, trade balance, leverage, and spread.

    Parameters:
        account_type (str): Type of account (e.g., "STANDARD").
        trade_balance (float): Initial amount of money used for the trade.
        leverage (int): Leverage ratio offered by the broker.
        spread (float): Spread percentage applied to the trade.

    Returns:
        float: Potential profit of the trade if account type is valid.
        str: Error message if account type is invalid.
    """
    try:
        # Validate account type
        if account_type.upper() != "STANDARD":
            return "Error: Unsupported account type. Only 'STANDARD' is supported."
        
        # Validate input values
        if trade_balance <= 0:
            return "Error: Trade balance must be greater than zero."
        if leverage <= 0:
            return "Error: Leverage must be greater than zero."
        if spread < 0:
            return "Error: Spread cannot be negative."

        # Calculate margin (money required to open the trade)
        margin = trade_balance / leverage

        # Calculate potential profit (assuming spread reduces the profit)
        potential_profit = trade_balance - (spread / 100 * trade_balance)

        return round(potential_profit, 2)
    
    except Exception as e:
        # Catch any unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define trade parameters
    account_type = "STANDARD"
    trade_balance = 1000.0  # Example balance in USD
    leverage = 50           # Example leverage ratio
    spread = 1.5            # Example spread percentage

    # Calculate potential profit
    result = calculate_trade_profit(account_type, trade_balance, leverage, spread)

    # Output result
    print(f"Potential Profit: {result}")
```
