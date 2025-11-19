"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Create a function that calculates the potential winnings based on the betting amount and odds provided by Hondatoto for Togel Singapore.
Generated: DETERMINISTIC_5a1c779903d4b09b
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_potential_winnings(bet_amount: float, odds: float) -> float:
    """
    Calculate the potential winnings based on the betting amount and odds.

    Parameters:
    bet_amount (float): The amount of money being bet.
    odds (float): The odds provided by Hondatoto for Togel Singapore.

    Returns:
    float: The potential winnings if the bet is successful.

    Raises:
    ValueError: If bet_amount or odds are negative or zero.
    TypeError: If bet_amount or odds are not of type float or int.
    """
    
    # Validate input types
    if not isinstance(bet_amount, (float, int)) or not isinstance(odds, (float, int)):
        raise TypeError("Both bet_amount and odds must be numbers (int or float).")
    
    # Validate input values
    if bet_amount <= 0:
        raise ValueError("Bet amount must be greater than zero.")
    if odds <= 0:
        raise ValueError("Odds must be greater than zero.")

    # Calculate potential winnings
    potential_winnings = bet_amount * odds
    
    return potential_winnings

# Example usage
if __name__ == "__main__":
    try:
        bet = 100.0  # Example bet amount
        odds = 2.5   # Example odds
        winnings = calculate_potential_winnings(bet, odds)
        print(f"Potential winnings: ${winnings:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
