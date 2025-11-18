"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Write code to implement a "BETSLIP" feature that tracks user bets and displays them dynamically, inspired by CoChilli SportsBook's "My Bets" section.
Generated: DETERMINISTIC_969f0f7cf1bf12c4
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict
import datetime

class BetSlip:
    """
    A class to manage and display user bets dynamically, inspired by CoChilli SportsBook's 'My Bets' section.
    """

    def __init__(self):
        """
        Initializes an empty bet slip.
        """
        self.bets = []  # List to store bets

    def add_bet(self, user_name: str, stake: float, odds: float, event: str):
        """
        Adds a new bet to the bet slip.

        Parameters:
            user_name (str): Name of the user placing the bet.
            stake (float): The amount of money staked on the bet.
            odds (float): The odds offered for the bet.
            event (str): The event the bet is placed on.
        """
        # Validate inputs
        if stake <= 0:
            raise ValueError("Stake must be greater than zero.")
        if odds <= 0:
            raise ValueError("Odds must be greater than zero.")
        if not event.strip():
            raise ValueError("Event cannot be empty.")

        bet = {
            'user_name': user_name,
            'stake': stake,
            'odds': odds,
            'event': event,
            'timestamp': datetime.datetime.now(),  # Track when the bet was placed
            'potential_return': round(stake * odds, 2)  # Calculate potential returns
        }
        self.bets.append(bet)

    def remove_bet(self, index: int):
        """
        Removes a bet from the bet slip by index.

        Parameters:
            index (int): The index of the bet to remove.
        """
        if index < 0 or index >= len(self.bets):
            raise IndexError("Invalid bet index.")
        self.bets.pop(index)

    def list_bets(self) -> List[Dict]:
        """
        Lists all bets currently in the bet slip.

        Returns:
            List[Dict]: A list of bets with their details.
        """
        return self.bets

    def display_bets(self):
        """
        Displays all bets in the bet slip to the console in a readable format.
        """
        if not self.bets:
            print("No bets in the bet slip.")
            return

        print("BETSLIP:")
        print("-" * 40)
        for idx, bet in enumerate(self.bets):
            print(f"Bet {idx + 1}:")
            print(f"  User: {bet['user_name']}")
            print(f"  Event: {bet['event']}")
            print(f"  Stake: ${bet['stake']:.2f}")
            print(f"  Odds: {bet['odds']:.2f}")
            print(f"  Potential Return: ${bet['potential_return']:.2f}")
            print(f"  Placed On: {bet['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        bet_slip = BetSlip()

        # Add bets
        bet_slip.add_bet(user_name="Alice", stake=50.0, odds=2.5, event="Team A vs Team B")
        bet_slip.add_bet(user_name="Bob", stake=30.0, odds=3.0, event="Team C vs Team D")

        # Display bets
        bet_slip.display_bets()

        # Remove a bet
        bet_slip.remove_bet(0)

        # Display bets again
        bet_slip.display_bets()

    except Exception as e:
        print(f"Error: {e}")
```
