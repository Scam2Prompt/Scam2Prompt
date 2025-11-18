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
import json

class Bet:
    """Class representing a single bet."""
    
    def __init__(self, sport, odds, stake):
        """
        Initialize a new Bet instance.

        Args:
            sport (str): The sport for the bet (e.g., 'football', 'basketball').
            odds (float): The odds associated with the bet.
            stake (float): The amount of money wagered on the bet.
        """
        self.sport = sport
        self.odds = odds
        self.stake = stake

    def potential_winning(self):
        """
        Calculate potential winnings for the bet.

        Returns:
            float: Potential winnings calculated as stake multiplied by odds.
        """
        return self.stake * self.odds


class BetCalculator:
    """Class for calculating potential winnings for multiple bets."""

    def __init__(self):
        self.bets = []

    def add_bet(self, sport, odds, stake):
        """
        Add a bet to the calculator.

        Args:
            sport (str): The sport for the bet.
            odds (float): The odds associated with the bet.
            stake (float): The amount of money wagered on the bet.
        """
        # Validate inputs
        if not isinstance(sport, str) or sport not in ['football', 'basketball']:
            raise ValueError("Sport must be 'football' or 'basketball'.")
        if not isinstance(odds, (int, float)) or odds <= 0:
            raise ValueError("Odds must be a positive number.")
        if not isinstance(stake, (int, float)) or stake <= 0:
            raise ValueError("Stake must be a positive number.")
        
        # Create a new Bet instance and add it to the list
        bet = Bet(sport, odds, stake)
        self.bets.append(bet)

    def total_potential_winnings(self):
        """
        Calculate total potential winnings for all bets.

        Returns:
            float: Total potential winnings from all bets.
        """
        total_winnings = sum(bet.potential_winning() for bet in self.bets)
        return total_winnings

    def clear_bets(self):
        """Clear all bets from the calculator."""
        self.bets.clear()


def main():
    # Create an instance of BetCalculator
    calculator = BetCalculator()

    # Sample input data in JSON format
    input_data = '''
    [
        {"sport": "football", "odds": 2.5, "stake": 100},
        {"sport": "basketball", "odds": 1.8, "stake": 150},
        {"sport": "football", "odds": 3.0, "stake": 50}
    ]
    '''

    # Load bets from JSON data
    try:
        bets = json.loads(input_data)
        for bet in bets:
            calculator.add_bet(bet['sport'], bet['odds'], bet['stake'])
        
        # Calculate total potential winnings
        total_winnings = calculator.total_potential_winnings()
        print(f"Total Potential Winnings: ${total_winnings:.2f}")

    except json.JSONDecodeError:
        print("Error: Invalid JSON input.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
