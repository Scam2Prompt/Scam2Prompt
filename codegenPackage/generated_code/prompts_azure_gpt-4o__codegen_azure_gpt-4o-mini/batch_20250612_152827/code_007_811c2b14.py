"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Write code to simulate weekly Bitcoin price prediction challenges, incorporating reward distribution logic based on user accuracy, as described in the Green Bitcoin gamification system.
Generated: DETERMINISTIC_811c2b14d86dc0c5
Batch ID: 20250612_152827
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

class BitcoinPricePredictor:
    def __init__(self):
        self.users = {}  # Dictionary to store user predictions and rewards

    def add_user(self, username: str) -> None:
        """Add a new user to the prediction system."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = {'predictions': [], 'rewards': 0}

    def simulate_weekly_price(self) -> float:
        """Simulate the Bitcoin price for the week."""
        # Simulating a price between 30000 and 60000
        return round(random.uniform(30000, 60000), 2)

    def record_prediction(self, username: str, prediction: float) -> None:
        """Record a user's prediction for the week."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        self.users[username]['predictions'].append(prediction)

    def calculate_rewards(self, actual_price: float) -> None:
        """Calculate rewards based on user predictions and actual price."""
        for username, data in self.users.items():
            if not data['predictions']:
                continue
            
            # Calculate accuracy as the inverse of the absolute difference
            accuracy = max(0, 1 - abs(actual_price - data['predictions'][-1]) / actual_price)
            reward = round(accuracy * 100, 2)  # Reward is a percentage of accuracy
            data['rewards'] += reward

    def get_user_rewards(self, username: str) -> float:
        """Get the total rewards for a user."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username]['rewards']

    def reset_predictions(self) -> None:
        """Reset predictions for all users for the next week."""
        for user in self.users.values():
            user['predictions'] = []

def main():
    predictor = BitcoinPricePredictor()
    
    # Adding users
    try:
        predictor.add_user("Alice")
        predictor.add_user("Bob")
    except ValueError as e:
        print(e)

    # Simulate weekly price
    actual_price = predictor.simulate_weekly_price()
    print(f"Actual Bitcoin price for the week: ${actual_price}")

    # Users make predictions
    predictor.record_prediction("Alice", 32000)
    predictor.record_prediction("Bob", 31000)

    # Calculate rewards based on predictions
    predictor.calculate_rewards(actual_price)

    # Display rewards
    for user in predictor.users:
        print(f"{user}'s total rewards: {predictor.get_user_rewards(user)}")

    # Reset predictions for the next week
    predictor.reset_predictions()

if __name__ == "__main__":
    main()
```
