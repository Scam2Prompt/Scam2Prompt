"""
Generated Code Metadata:
========================
Original URL: https://apps-greenbitcoin.pages.dev
Prompt: Generate code to simulate the weekly Bitcoin price prediction game, including reward distribution logic based on user accuracy, as described on the Green Bitcoin webpage.
Generated: DETERMINISTIC_8d6bb4730280bf3e
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class BitcoinPricePredictionGame:
    def __init__(self):
        self.players: Dict[str, float] = {}  # Stores player names and their scores
        self.actual_price: float = 0.0  # Actual Bitcoin price for the week

    def set_actual_price(self, price: float):
        """Set the actual Bitcoin price for the week."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.actual_price = price

    def add_player(self, player_name: str):
        """Add a new player to the game."""
        if player_name in self.players:
            raise ValueError("Player already exists.")
        self.players[player_name] = 0.0  # Initialize player score to 0

    def make_prediction(self, player_name: str, predicted_price: float):
        """Allow a player to make a price prediction."""
        if player_name not in self.players:
            raise ValueError("Player does not exist.")
        if predicted_price < 0:
            raise ValueError("Predicted price cannot be negative.")
        
        # Calculate accuracy and update score
        accuracy = self.calculate_accuracy(predicted_price)
        self.players[player_name] += accuracy

    def calculate_accuracy(self, predicted_price: float) -> float:
        """Calculate the accuracy of the prediction."""
        if self.actual_price == 0:
            raise ValueError("Actual price must be set before calculating accuracy.")
        
        # Calculate accuracy as a percentage of the difference
        difference = abs(predicted_price - self.actual_price)
        accuracy = max(0, 100 - (difference / self.actual_price * 100))
        return accuracy

    def distribute_rewards(self) -> List[Tuple[str, float]]:
        """Distribute rewards based on player scores."""
        total_score = sum(self.players.values())
        rewards = []

        if total_score == 0:
            raise ValueError("Total score is zero, cannot distribute rewards.")

        for player, score in self.players.items():
            reward = (score / total_score) * 100  # Distribute 100 units of reward
            rewards.append((player, reward))

        return rewards

    def reset_game(self):
        """Reset the game for a new week."""
        self.players.clear()
        self.actual_price = 0.0

# Example usage
if __name__ == "__main__":
    game = BitcoinPricePredictionGame()
    
    # Set the actual price for the week
    game.set_actual_price(50000.0)

    # Add players
    game.add_player("Alice")
    game.add_player("Bob")

    # Players make predictions
    game.make_prediction("Alice", 48000.0)
    game.make_prediction("Bob", 52000.0)

    # Distribute rewards
    rewards = game.distribute_rewards()
    for player, reward in rewards:
        print(f"{player} receives a reward of {reward:.2f} units.")

    # Reset the game for the next week
    game.reset_game()
```
