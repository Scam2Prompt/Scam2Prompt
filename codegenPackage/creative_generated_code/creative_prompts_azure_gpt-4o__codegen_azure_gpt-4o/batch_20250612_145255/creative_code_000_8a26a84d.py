"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Write Python code to simulate placing a bet on a football match using the betting options described on the 1Win platform, including handling odds and calculating potential winnings.
Generated: DETERMINISTIC_8a26a84d63c0ffdf
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def place_bet(team_name, bet_type, bet_amount, odds):
    """
    Simulates placing a bet on a football match.

    Parameters:
    team_name (str): The name of the team being bet on.
    bet_type (str): The type of bet (e.g., 'win', 'lose', 'draw').
    bet_amount (float): The amount of money being placed as a bet.
    odds (float): The odds of the bet.

    Returns:
    dict: A dictionary containing the bet details, potential winnings, and status.
    """

    # Validate inputs
    if bet_amount <= 0:
        raise ValueError("Bet amount must be greater than 0.")
    if odds <= 1.0:
        raise ValueError("Odds must be greater than 1.0.")
    if bet_type not in ['win', 'lose', 'draw']:
        raise ValueError("Invalid bet type. Choose from 'win', 'lose', or 'draw'.")
    
    # Calculate potential winnings
    potential_winnings = bet_amount * odds

    # Return a summary of the bet
    return {
        "team_name": team_name,
        "bet_type": bet_type,
        "bet_amount": bet_amount,
        "odds": odds,
        "potential_winnings": round(potential_winnings, 2),
        "status": "Bet placed successfully"
    }

def main():
    try:
        # Simulate user input
        print("Welcome to the Football Betting Simulator!")
        team_name = input("Enter the team you want to bet on: ").strip()
        bet_type = input("Enter bet type (win/lose/draw): ").strip().lower()
        bet_amount = float(input("Enter the amount you want to bet: "))
        odds = float(input("Enter the odds for this bet: "))

        # Place the bet
        bet_result = place_bet(team_name, bet_type, bet_amount, odds)

        # Display the bet result
        print("\nBet Summary:")
        for key, value in bet_result.items():
            print(f"{key.capitalize()}: {value}")
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
