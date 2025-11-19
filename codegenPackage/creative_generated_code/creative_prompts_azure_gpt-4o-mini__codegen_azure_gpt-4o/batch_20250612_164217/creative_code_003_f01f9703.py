"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1wapdj.top
Prompt: Create a function to calculate potential winnings based on odds from the 1win betting site.
Generated: DETERMINISTIC_f01f9703f5f99613
Batch ID: 20250612_164217
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

def calculate_potential_winnings(stake: Union[int, float], odds: Union[int, float]) -> Union[float, str]:
    """
    Calculate potential winnings based on the stake and odds provided.

    Parameters:
    stake (Union[int, float]): The amount of money being wagered (must be positive).
    odds (Union[int, float]): The betting odds (must be positive).

    Returns:
    Union[float, str]: The potential winnings as a float, or an error message as a string if input validation fails.
    """
    try:
        # Validate input types and values
        if not isinstance(stake, (int, float)) or not isinstance(odds, (int, float)):
            return "Error: Stake and odds must be numeric values."
        if stake <= 0 or odds <= 0:
            return "Error: Stake and odds must be positive values."

        # Calculate potential winnings
        potential_winnings = stake * odds

        return round(potential_winnings, 2)  # Return rounded winnings for cleaner display

    except Exception as e:
        # Catch any unexpected exceptions and return an error message
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    stake_amount = 100  # Example stake
    betting_odds = 3.5  # Example odds
    result = calculate_potential_winnings(stake_amount, betting_odds)
    print(f"Potential Winnings: {result}")
```
