"""
Generated Code Metadata:
========================
Original URL: https://securespend.io
Prompt: Generate a code snippet for a betting system that allows users to place bets on various togel markets like Togel Hongkong and Togel Singapore.
Generated: DETERMINISTIC_c3131d3953676f22
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BettingSystem:
    def __init__(self):
        # Initialize the betting markets
        self.markets = {
            "Togel Hongkong": [],
            "Togel Singapore": []
        }

    def place_bet(self, market_name, bet_amount, bet_number):
        """
        Place a bet on a specified market.

        :param market_name: The name of the market to bet on.
        :param bet_amount: The amount of money to bet.
        :param bet_number: The number the user is betting on.
        :raises ValueError: If the market is invalid or bet amount is non-positive.
        """
        if market_name not in self.markets:
            raise ValueError(f"Invalid market name: {market_name}. Available markets: {list(self.markets.keys())}")
        
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Store the bet in the market
        self.markets[market_name].append((bet_amount, bet_number))
        print(f"Bet placed: {bet_amount} on number {bet_number} in {market_name}.")

    def draw_winner(self, market_name):
        """
        Draw a winner for the specified market.

        :param market_name: The name of the market to draw a winner from.
        :raises ValueError: If the market is invalid or has no bets placed.
        :return: The winning number and the list of winning bets.
        """
        if market_name not in self.markets:
            raise ValueError(f"Invalid market name: {market_name}. Available markets: {list(self.markets.keys())}")

        if not self.markets[market_name]:
            raise ValueError(f"No bets placed in {market_name}.")

        # Randomly select a winning number
        winning_number = random.randint(1, 49)  # Assuming numbers range from 1 to 49
        winning_bets = [bet for bet in self.markets[market_name] if bet[1] == winning_number]

        # Clear the bets after drawing
        self.markets[market_name] = []

        return winning_number, winning_bets

    def get_market_bets(self, market_name):
        """
        Retrieve all bets placed in a specified market.

        :param market_name: The name of the market to retrieve bets from.
        :raises ValueError: If the market is invalid.
        :return: List of bets placed in the market.
        """
        if market_name not in self.markets:
            raise ValueError(f"Invalid market name: {market_name}. Available markets: {list(self.markets.keys())}")

        return self.markets[market_name]

# Example usage
if __name__ == "__main__":
    betting_system = BettingSystem()

    try:
        betting_system.place_bet("Togel Hongkong", 100, 23)
        betting_system.place_bet("Togel Singapore", 50, 15)

        winning_number, winning_bets = betting_system.draw_winner("Togel Hongkong")
        print(f"Winning number in Togel Hongkong: {winning_number}")
        print(f"Winning bets: {winning_bets}")

    except ValueError as e:
        print(f"Error: {e}")
```
