"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-st.pages.dev
Prompt: Generate code to implement a weekly Bitcoin price prediction game using $GBTC tokens, as described in the Green Bitcoin gamified staking system.
Generated: DETERMINISTIC_0cf6937e6d5aa8b5
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict, List
import random

class GreenBitcoinGame:
    """
    A weekly Bitcoin price prediction game using $GBTC tokens.
    Players stake their $GBTC tokens to predict the Bitcoin price at the end of the week.
    """

    def __init__(self):
        # Dictionary to store player data: {player_name: {'stake': float, 'prediction': float}}
        self.players: Dict[str, Dict[str, float]] = {}
        self.current_week_predictions: List[Dict[str, float]] = []
        self.bitcoin_price_at_start: float = self.get_bitcoin_price()
    
    def get_bitcoin_price(self) -> float:
        """
        Mock method to fetch Bitcoin price. In production, integrate a live Bitcoin price API.
        Returns the current Bitcoin price.
        """
        # Mock Bitcoin price with a random float value for the example
        return round(random.uniform(20000, 60000), 2)

    def register_player(self, player_name: str, stake: float, prediction: float):
        """
        Register a player for the weekly game.

        :param player_name: Name of the player
        :param stake: Amount of $GBTC tokens to stake
        :param prediction: The player's predicted Bitcoin price at the end of the week
        """
        if stake <= 0:
            raise ValueError("Stake must be greater than zero.")
        
        if player_name in self.players:
            raise ValueError(f"Player '{player_name}' is already registered.")
        
        self.players[player_name] = {
            "stake": stake,
            "prediction": prediction
        }
        print(f"Player '{player_name}' registered successfully with a stake of {stake} $GBTC and a prediction of ${prediction}.")
    
    def start_weekly_game(self):
        """
        Start the weekly game and reset previous week's data.
        """
        self.players.clear()
        self.current_week_predictions.clear()
        self.bitcoin_price_at_start = self.get_bitcoin_price()
        print(f"Weekly game started. Bitcoin price at start: ${self.bitcoin_price_at_start}.")
    
    def end_weekly_game(self):
        """
        End the weekly game and determine the winner.
        """
        if not self.players:
            print("No players registered for the week. Game ended.")
            return
        
        bitcoin_price_at_end = self.get_bitcoin_price()
        print(f"Bitcoin price at end of the week: ${bitcoin_price_at_end}.")
        
        # Determine the closest prediction
        closest_player = None
        closest_difference = float('inf')

        for player_name, details in self.players.items():
            prediction = details["prediction"]
            difference = abs(prediction - bitcoin_price_at_end)
            if difference < closest_difference:
                closest_difference = difference
                closest_player = player_name

        if closest_player:
            winner_details = self.players[closest_player]
            print(f"Winner: {closest_player} with a prediction of ${winner_details['prediction']} "
                  f"and a stake of {winner_details['stake']} $GBTC.")
        else:
            print("No valid predictions. No winner this week.")
    
    def display_registered_players(self):
        """
        Display all registered players and their predictions.
        """
        if not self.players:
            print("No players registered yet.")
            return
        
        print("Registered players:")
        for player_name, details in self.players.items():
            print(f"- {player_name}: Stake = {details['stake']} $GBTC, Prediction = ${details['prediction']}")

# Example usage
if __name__ == "__main__":
    game = GreenBitcoinGame()
    game.start_weekly_game()
    game.register_player("Alice", 10, 45000)
    game.register_player("Bob", 5, 40000)
    game.register_player("Charlie", 7, 47000)
    game.display_registered_players()
    game.end_weekly_game()
```

This code implements a weekly Bitcoin price prediction game using $GBTC tokens. Players can register with their predictions and stakes, and at the end of the week, the closest prediction wins.
