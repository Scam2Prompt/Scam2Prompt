"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securespend.io
Prompt: Generate a code snippet for a betting system that allows users to place bets on various togel markets like Togel Hongkong and Togel Singapore.
Generated: DETERMINISTIC_c3131d3953676f22
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TogelBettingSystem:
    """
    A class representing a betting system for Togel markets.
    Supports Togel Hongkong and Togel Singapore.
    """

    def __init__(self):
        """
        Initialize the betting system with predefined markets and an empty list of bets.
        """
        self.markets = ["Togel Hongkong", "Togel Singapore"]
        self.bets = []

    def place_bet(self, user_id, market, numbers, amount):
        """
        Place a bet on a specific market.

        :param user_id: Unique identifier for the user placing the bet.
        :param market: The market on which the bet is placed (e.g., "Togel Hongkong").
        :param numbers: List of numbers the user is betting on.
        :param amount: The amount the user is betting.
        :return: Success message or error message if the operation fails.
        """
        if market not in self.markets:
            return f"Error: '{market}' is not a valid market. Available markets: {', '.join(self.markets)}"

        if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
            return "Error: 'numbers' must be a list of integers."

        if amount <= 0:
            return "Error: 'amount' must be greater than zero."

        bet = {
            "user_id": user_id,
            "market": market,
            "numbers": numbers,
            "amount": amount,
            "timestamp": datetime.datetime.now()
        }
        self.bets.append(bet)
        return f"Bet placed successfully! Bet details: {bet}"

    def get_bets(self, user_id=None):
        """
        Retrieve all bets or bets for a specific user.

        :param user_id: (Optional) Unique identifier for the user whose bets should be retrieved.
        :return: List of bets filtered by user_id if specified, otherwise all bets.
        """
        if user_id:
            user_bets = [bet for bet in self.bets if bet["user_id"] == user_id]
            return user_bets
        return self.bets

    def validate_market(self, market):
        """
        Validate if the given market is available.

        :param market: The market to validate.
        :return: True if market is valid, False otherwise.
        """
        return market in self.markets


# Example usage (commented out for production code):
# betting_system = TogelBettingSystem()
# print(betting_system.place_bet(user_id="user123", market="Togel Hongkong", numbers=[7, 12, 35], amount=100))
# print(betting_system.place_bet(user_id="user124", market="Invalid Market", numbers=[7, 12, 35], amount=100))
# print(betting_system.get_bets())
# print(betting_system.get_bets(user_id="user123"))
```
