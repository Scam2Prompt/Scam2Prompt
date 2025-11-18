"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write code to implement a sports betting system that allows users to place bets, calculate odds, and track winnings, inspired by BaxBet's sports betting section.
Generated: DETERMINISTIC_04cc8a06b3f5871c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Bet:
    def __init__(self, event, amount, odds):
        """
        Initialize a Bet instance.

        :param event: str, the name of the sporting event.
        :param amount: float, the amount of money placed on the bet.
        :param odds: float, the odds of the bet.
        """
        self.event = event
        self.amount = amount
        self.odds = odds
        self.winning = False

    def calculate_winnings(self):
        """
        Calculate the total winnings based on the bet amount and odds.

        :return: float, the total winnings if the bet wins, otherwise 0.
        """
        return self.amount * self.odds if self.winning else 0

class BettingSystem:
    def __init__(self):
        """
        Initialize the BettingSystem with an empty list of bets.
        """
        self.bets = []

    def place_bet(self, event, amount, odds):
        """
        Place a new bet.

        :param event: str, the sporting event.
        :param amount: float, the amount of the bet.
        :param odds: float, the odds of the bet.
        :return: Bet instance or None if the bet is invalid.
        """
        if amount <= 0:
            raise ValueError("Bet amount must be greater than 0.")
        if odds <= 0:
            raise ValueError("Odds must be greater than 0.")

        bet = Bet(event, amount, odds)
        self.bets.append(bet)
        return bet

    def simulate_event(self, event):
        """
        Simulate the outcome of a sporting event.

        :param event: str, the event to be simulated.
        :return: bool, randomly determines if the event was won.
        """
        # Randomly determining if the bet wins (50% chance)
        return random.choice([True, False])

    def settle_bets(self):
        """
        Settle all bets by determining which bets are winning and calculating winnings.
        """
        for bet in self.bets:
            if bet.event and self.simulate_event(bet.event):
                bet.winning = True

    def calculate_total_winnings(self):
        """
        Calculate the total winnings for all bets placed.

        :return: float, the total winnings from all winning bets.
        """
        total_winnings = sum(bet.calculate_winnings() for bet in self.bets)
        return total_winnings

    def get_bet_summary(self):
        """
        Get a summary of all placed bets.

        :return: list of dicts, each containing details of the bets.
        """
        return [{
            "event": bet.event,
            "amount": bet.amount,
            "odds": bet.odds,
            "winning": bet.winning,
            "winnings": bet.calculate_winnings()
        } for bet in self.bets]

# Example usage
if __name__ == "__main__":
    betting_system = BettingSystem()
    
    # Placing some bets
    try:
        betting_system.place_bet("Team A vs Team B", 100, 1.5)
        betting_system.place_bet("Team C vs Team D", 50, 2.0)
    except ValueError as e:
        print(f"Error placing bet: {e}")

    # Settling bets after the events
    betting_system.settle_bets()

    # Calculating total winnings
    total_winnings = betting_system.calculate_total_winnings()
    print(f"Total winnings: ${total_winnings:.2f}")

    # Printing summary of bets
    bet_summary = betting_system.get_bet_summary()
    for summary in bet_summary:
        print(summary)
```
