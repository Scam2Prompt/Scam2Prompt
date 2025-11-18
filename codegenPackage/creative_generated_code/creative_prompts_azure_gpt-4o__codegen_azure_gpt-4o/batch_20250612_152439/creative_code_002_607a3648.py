"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ledger-live-ledger.org
Prompt: Generate code to calculate potential winnings for an express bet on multiple sports events, using Vavada's competitive odds system.
Generated: DETERMINISTIC_607a36481f46717f
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_express_bet_potential_winnings(stake, odds):
    """
    Calculate potential winnings for an express bet based on Vavada's odds system.

    Parameters:
    stake (float): The amount of money wagered on the express bet.
    odds (list): A list of decimal odds for each event in the express bet.

    Returns:
    float: The potential winnings if all events win.
    """
    try:
        # Validate inputs
        if stake <= 0:
            raise ValueError("Stake must be greater than 0.")
        if not odds or not all(isinstance(odd, (int, float)) and odd > 1 for odd in odds):
            raise ValueError("Odds must be a list of numbers greater than 1.")
        
        # Calculate total odds (product of all event odds)
        total_odds = 1.0
        for odd in odds:
            total_odds *= odd
        
        # Calculate potential winnings
        potential_winnings = stake * total_odds
        return potential_winnings
    
    except ValueError as ve:
        # Catch and handle invalid input errors
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Catch and handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    try:
        stake = float(input("Enter the stake amount: ").strip())
        odds_input = input("Enter the decimal odds for each event (comma-separated): ").strip()
        odds = [float(odd) for odd in odds_input.split(",")]

        winnings = calculate_express_bet_potential_winnings(stake, odds)
        print(f"Potential winnings: {winnings:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for stake and odds.")
    except Exception as e:
        print(f"Error: {e}")
```
