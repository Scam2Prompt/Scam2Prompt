"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoindapp.pages.dev
Prompt: Generate code to simulate weekly Bitcoin price prediction challenges using Green Bitcoin’s gamified staking mechanics.
Generated: DETERMINISTIC_39f23c09b3f8b4e0
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class BitcoinPredictionGame:
    """
    A class to represent a weekly Bitcoin price prediction game with gamified staking mechanics.
    """
    def __init__(self):
        self.weekly_predictions = {}
        self.weekly_results = {}
        self.players = {}
        self.start_of_week = datetime.datetime.now()
        self.end_of_week = self.start_of_week + datetime.timedelta(days=7)

    def register_player(self, player_id, initial_stake):
        """
        Register a new player with an initial stake.
        :param player_id: Unique identifier for the player.
        :param initial_stake: Initial stake amount for the player.
        """
        if player_id in self.players:
            raise ValueError(f"Player '{player_id}' is already registered.")
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than zero.")
        self.players[player_id] = {"stake": initial_stake, "total_earnings": 0}
        print(f"Player '{player_id}' registered successfully with a stake of {initial_stake} BTC.")

    def submit_prediction(self, player_id, predicted_price):
        """
        Submit a weekly Bitcoin price prediction for a player.
        :param player_id: Unique identifier for the player.
        :param predicted_price: Player's predicted Bitcoin price.
        """
        if player_id not in self.players:
            raise ValueError(f"Player '{player_id}' is not registered.")
        if player_id in self.weekly_predictions:
            raise ValueError(f"Player '{player_id}' has already submitted a prediction this week.")
        if predicted_price <= 0:
            raise ValueError("Predicted price must be greater than zero.")
        self.weekly_predictions[player_id] = predicted_price
        print(f"Prediction of {predicted_price} BTC submitted successfully for player '{player_id}'.")

    def simulate_weekly_price(self):
        """
        Simulate the actual Bitcoin price at the end of the week.
        :return: Simulated weekly price.
        """
        return round(random.uniform(20000, 30000), 2)  # Simulate price between $20,000 and $30,000

    def evaluate_predictions(self):
        """
        Evaluate weekly predictions, distribute rewards, and reset for the next week.
        """
        if datetime.datetime.now() < self.end_of_week:
            raise RuntimeError("The week is not over yet. Cannot evaluate predictions.")
        
        actual_price = self.simulate_weekly_price()
        print(f"Actual Bitcoin price for the week: {actual_price} BTC")

        closest_player = None
        closest_difference = float("inf")

        # Find the closest prediction
        for player_id, predicted_price in self.weekly_predictions.items():
            difference = abs(predicted_price - actual_price)
            if difference < closest_difference:
                closest_difference = difference
                closest_player = player_id

        # Reward the closest player
        if closest_player:
            reward = self.players[closest_player]["stake"] * 0.1  # 10% bonus
            self.players[closest_player]["total_earnings"] += reward
            print(f"Player '{closest_player}' is the winner with the closest prediction!")
            print(f"Reward of {reward} BTC added to player '{closest_player}' earnings.")
        else:
            print("No predictions were submitted this week.")

        # Reset weekly data
        self.weekly_predictions.clear()
        self.start_of_week = datetime.datetime.now()
        self.end_of_week = self.start_of_week + datetime.timedelta(days=7)
        print("Weekly predictions reset for the next week.")

    def get_player_info(self, player_id):
        """
        Get information about a player's current stake and total earnings.
        :param player_id: Unique identifier for the player.
        :return: Dictionary containing player's stake and total earnings.
        """
        if player_id not in self.players:
            raise ValueError(f"Player '{player_id}' is not registered.")
        return self.players[player_id]


# Example usage:
if __name__ == "__main__":
    game = BitcoinPredictionGame()

    # Register players
    game.register_player("Alice", 0.5)
    game.register_player("Bob", 1.0)

    # Submit predictions
    game.submit_prediction("Alice", 25000)
    game.submit_prediction("Bob", 26000)

    # Simulate end of the week and evaluate predictions
    # For testing purposes, simulate the passage of time
    game.end_of_week = datetime.datetime.now()  # Force end of week for testing
    game.evaluate_predictions()

    # Get player info
    print("Player info:", game.get_player_info("Alice"))
    print("Player info:", game.get_player_info("Bob"))
```
