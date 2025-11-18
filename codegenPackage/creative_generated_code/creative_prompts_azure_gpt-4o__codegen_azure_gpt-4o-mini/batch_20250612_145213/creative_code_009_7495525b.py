"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Create a system to manage express bets and calculate potential winnings based on the Vavada platform's description of combining multiple events into one bet.
Generated: DETERMINISTIC_7495525b0e76c4be
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Bet:
    """
    Represents a single bet on an event with odds and stake.
    """
    def __init__(self, event_name: str, odds: float, stake: float):
        if odds <= 0:
            raise ValueError("Odds must be greater than 0")
        if stake <= 0:
            raise ValueError("Stake must be greater than 0")
        
        self.event_name = event_name
        self.odds = odds
        self.stake = stake

    def potential_winnings(self) -> float:
        """
        Calculate potential winnings for this bet.

        Returns:
            float: The potential winnings based on the odds and stake.
        """
        return self.odds * self.stake


class ExpressBet:
    """
    Represents a combined express bet made up of multiple individual bets.
    """
    def __init__(self, bets: List[Bet]):
        if not bets:
            raise ValueError("At least one bet must be included in an express bet.")
        self.bets = bets

    def total_stake(self) -> float:
        """
        Calculate total stake for all individual bets.

        Returns:
            float: Total stake of all bets in the express bet.
        """
        return sum(bet.stake for bet in self.bets)

    def combined_odds(self) -> float:
        """
        Calculate combined odds for the express bet.
        
        Returns:
            float: The product of all individual odds.
        """
        combined = 1.0
        for bet in self.bets:
            combined *= bet.odds
        return combined

    def potential_winnings(self) -> float:
        """
        Calculate potential winnings for the express bet.

        Returns:
            float: The potential winnings based on combined odds and total stake.
        """
        return self.combined_odds() * self.total_stake()


def main():
    """
    Main function to demonstrate the use of Bet and ExpressBet classes.
    """
    try:
        # Create individual bets
        bet1 = Bet('Team A vs Team B', 1.5, 10)
        bet2 = Bet('Team C vs Team D', 2.0, 20)
        bet3 = Bet('Team E vs Team F', 1.8, 15)

        # Combine individual bets into an express bet
        express_bet = ExpressBet([bet1, bet2, bet3])

        # Output the results
        print(f"Total Stake: ${express_bet.total_stake():.2f}")
        print(f"Combined Odds: {express_bet.combined_odds():.2f}")
        print(f"Potential Winnings: ${express_bet.potential_winnings():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
