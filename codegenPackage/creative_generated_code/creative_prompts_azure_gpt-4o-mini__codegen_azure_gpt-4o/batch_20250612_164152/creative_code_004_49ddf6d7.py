"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket-frontend-green.vercel.app
Prompt: Create a function that calculates potential winnings based on the betting odds for the upcoming elections on a prediction market.
Generated: DETERMINISTIC_49ddf6d76cd0cb56
Batch ID: 20250612_164152
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

def calculate_winnings(stake: float, odds: Union[float, str]) -> float:
    """
    Calculate potential winnings based on betting odds.

    Args:
        stake (float): The amount of money being bet. Must be greater than 0.
        odds (Union[float, str]): The odds for the bet. Can be:
                                  - Decimal odds (e.g., 2.5)
                                  - Fractional odds as a string (e.g., "3/2")
    
    Returns:
        float: Potential winnings (including the stake).

    Raises:
        ValueError: If the stake is less than or equal to 0.
        ValueError: If the odds are invalid or improperly formatted.
    """
    # Validate stake
    if stake <= 0:
        raise ValueError("Stake must be greater than 0.")

    # Handle decimal odds
    if isinstance(odds, float):
        if odds <= 1:  # Decimal odds must be greater than 1
            raise ValueError("Decimal odds must be greater than 1.")
        winnings = stake * odds

    # Handle fractional odds
    elif isinstance(odds, str):
        try:
            # Split the fractional odds into numerator and denominator
            numerator, denominator = map(int, odds.split('/'))
            if numerator <= 0 or denominator <= 0:
                raise ValueError("Invalid fractional odds format.")
            winnings = stake * (numerator / denominator + 1)
        except (ValueError, ZeroDivisionError):
            raise ValueError("Invalid fractional odds format.")

    # Invalid odds type
    else:
        raise ValueError("Odds must be either a float (decimal) or a fractional string (e.g., '3/2').")

    return round(winnings, 2)  # Round winnings to 2 decimal places for precision


# Example usage
if __name__ == "__main__":
    try:
        # Test with decimal odds
        print("Decimal Odds Example:")
        stake_amount = 100
        decimal_odds = 2.5
        print(f"Stake: ${stake_amount}, Odds: {decimal_odds}, Winnings: ${calculate_winnings(stake_amount, decimal_odds)}")

        # Test with fractional odds
        print("\nFractional Odds Example:")
        fractional_odds = "3/2"
        print(f"Stake: ${stake_amount}, Odds: {fractional_odds}, Winnings: ${calculate_winnings(stake_amount, fractional_odds)}")
    except ValueError as e:
        print(f"Error: {e}")
```
