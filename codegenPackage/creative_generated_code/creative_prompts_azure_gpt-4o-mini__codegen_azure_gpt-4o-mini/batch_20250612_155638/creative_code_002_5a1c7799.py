"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epsys.ro
Prompt: Create a function that calculates the potential winnings based on the betting amount and odds provided by Hondatoto for Togel Singapore.
Generated: DETERMINISTIC_5a1c779903d4b09b
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_winnings(bet_amount, odds):
    """
    Calculate the potential winnings based on the provided bet amount and odds.

    Parameters:
    bet_amount (float): The amount of money being bet.
    odds (float): The odds of the bet. This should be a decimal representation. 
                  For example, odds of 2.5 means for every 1 unit bet, you win 2.5 units.

    Returns:
    float: The potential winnings, or raises an error if inputs are invalid.

    Raises:
    ValueError: If bet_amount or odds is not a positive number.
    """
    # Validate input
    if not isinstance(bet_amount, (int, float)) or bet_amount <= 0:
        raise ValueError("Bet amount must be a positive number.")
    
    if not isinstance(odds, (int, float)) or odds <= 0:
        raise ValueError("Odds must be a positive number.")

    # Calculate potential winnings
    potential_winnings = bet_amount * odds
    
    return potential_winnings


# Example usage
if __name__ == "__main__":
    try:
        bet = 100  # Example bet amount
        odds = 2.5  # Example odds
        winnings = calculate_potential_winnings(bet, odds)
        print(f"Potential winnings for a bet of ${bet} at odds of {odds} is: ${winnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
