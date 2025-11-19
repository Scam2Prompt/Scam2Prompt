"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavepass.in
Prompt: Write a function to calculate potential winnings in an online jackpot casino game.
Generated: DETERMINISTIC_3f0a16ad5cf1d4e2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_potential_winnings(bet_amount: Union[int, float], odds: Union[int, float]) -> Union[float, str]:
    """
    Calculate potential winnings for an online jackpot casino game.

    Parameters:
        bet_amount (Union[int, float]): The amount of money the player bets. Must be positive.
        odds (Union[int, float]): The multiplier for the bet. Must be positive.

    Returns:
        Union[float, str]: Potential winnings (bet_amount * odds) if inputs are valid,
                           otherwise returns an appropriate error message.
    """
    try:
        # Validate inputs
        if not isinstance(bet_amount, (int, float)) or not isinstance(odds, (int, float)):
            return "Error: Both bet_amount and odds must be numbers."
        if bet_amount <= 0:
            return "Error: bet_amount must be greater than 0."
        if odds <= 0:
            return "Error: odds must be greater than 0."
        
        # Calculate potential winnings
        potential_winnings = bet_amount * odds
        return round(potential_winnings, 2)  # Return rounded value for better readability
    except Exception as e:
        # Catch unexpected errors and return a message
        return f"Error: An unexpected exception occurred - {str(e)}"

# Example usage:
# winnings = calculate_potential_winnings(100, 2.5)
# print(winnings)  # Expected output: 250.0
```
