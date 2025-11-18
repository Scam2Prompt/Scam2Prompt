"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plf3108.com
Prompt: Develop a Python program to calculate potential winnings for multi-sport bets, including football and basketball, based on the diverse betting markets highlighted on the 868 platform.
Generated: DETERMINISTIC_29a6da221aae97f8
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_potential_winnings(bets):
    """
    Calculate the potential winnings for a multi-sport bet.

    :param bets: A list of dictionaries where each dictionary represents a bet.
                 Each bet should include:
                 - 'sport': The sport (e.g., 'football', 'basketball').
                 - 'stake': The amount of money wagered.
                 - 'odds': The odds for the bet (decimal odds format).
    :return: The total potential winnings.
    """
    if not isinstance(bets, list):
        raise ValueError("Input should be a list of bets.")

    total_winnings = 0.0

    for bet in bets:
        # Validate bet dictionary structure
        if not isinstance(bet, dict):
            raise ValueError("Each bet must be represented as a dictionary.")
        if 'sport' not in bet or 'stake' not in bet or 'odds' not in bet:
            raise KeyError("Missing required keys in bet dictionary. Required keys: 'sport', 'stake', 'odds'.")
        
        # Validate bet values
        sport = bet['sport']
        stake = bet['stake']
        odds = bet['odds']

        if sport not in ['football', 'basketball']:
            raise ValueError(f"Invalid sport '{sport}'. Supported sports: 'football', 'basketball'.")
        if not isinstance(stake, (int, float)) or stake <= 0:
            raise ValueError("Stake must be a positive number.")
        if not isinstance(odds, (int, float)) or odds <= 1:
            raise ValueError("Odds must be a number greater than or equal to 1.")

        # Calculate winnings for the current bet
        winnings = stake * odds
        total_winnings += winnings

    return total_winnings


def main():
    """
    Main function to interact with the user and calculate potential winnings.
    """
    try:
        print("Welcome to the Multi-Sport Betting Winnings Calculator!")
        bets = []

        while True:
            # Collect bet details from user
            sport = input("Enter the sport ('football' or 'basketball'): ").strip().lower()
            stake = float(input("Enter your stake amount: "))
            odds = float(input("Enter the odds (decimal format): "))

            bet = {
                'sport': sport,
                'stake': stake,
                'odds': odds
            }

            bets.append(bet)

            # Check if the user wants to add more bets
            more_bets = input("Do you want to add another bet? (yes/no): ").strip().lower()
            if more_bets != 'yes':
                break

        # Calculate potential winnings
        total_winnings = calculate_potential_winnings(bets)
        print(f"Your total potential winnings are: ${total_winnings:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
