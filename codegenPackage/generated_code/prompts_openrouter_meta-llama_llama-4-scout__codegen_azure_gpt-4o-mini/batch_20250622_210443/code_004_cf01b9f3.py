"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-web.pages.dev
Prompt: Design a weekly Bitcoin price prediction challenge using Green Bitcoin's gamified staking system, including the rules, rewards structure, and user interface.
Generated: DETERMINISTIC_cf01b9f36919535f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta

class BitcoinPricePredictionChallenge:
    def __init__(self):
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(weeks=1)
        self.participants = {}
        self.price_history = self.generate_price_history()
        self.reward_pool = 1000  # Total reward pool in tokens

    def generate_price_history(self):
        """Simulate Bitcoin price history for the week."""
        base_price = 30000  # Starting price
        price_history = {}
        for i in range(7):
            date = self.start_date + timedelta(days=i)
            price = base_price + random.randint(-500, 500)  # Simulate price fluctuation
            price_history[date.strftime('%Y-%m-%d')] = price
        return price_history

    def register_participant(self, user_id):
        """Register a new participant for the challenge."""
        if user_id in self.participants:
            raise ValueError("User is already registered.")
        self.participants[user_id] = None  # Initialize with no prediction

    def make_prediction(self, user_id, predicted_price):
        """Allow a participant to make a price prediction."""
        if user_id not in self.participants:
            raise ValueError("User is not registered.")
        self.participants[user_id] = predicted_price

    def calculate_rewards(self):
        """Calculate rewards based on the accuracy of predictions."""
        actual_price = self.price_history[self.end_date.strftime('%Y-%m-%d')]
        rewards = {}
        for user_id, predicted_price in self.participants.items():
            if predicted_price is None:
                continue  # Skip users who did not make a prediction
            accuracy = max(0, 1 - abs(predicted_price - actual_price) / actual_price)
            rewards[user_id] = accuracy * self.reward_pool
        return rewards

    def display_results(self):
        """Display the results of the challenge."""
        rewards = self.calculate_rewards()
        print("Weekly Bitcoin Price Prediction Challenge Results:")
        print(f"Actual Price on {self.end_date.strftime('%Y-%m-%d')}: ${self.price_history[self.end_date.strftime('%Y-%m-%d')]}")
        for user_id, reward in rewards.items():
            print(f"User: {user_id}, Reward: {reward:.2f} tokens")

# Example usage
if __name__ == "__main__":
    challenge = BitcoinPricePredictionChallenge()
    
    # Register participants
    try:
        challenge.register_participant("user1")
        challenge.register_participant("user2")
        
        # Make predictions
        challenge.make_prediction("user1", 30500)
        challenge.make_prediction("user2", 29000)
        
        # Display results after the challenge ends
        challenge.display_results()
    except ValueError as e:
        print(f"Error: {e}")
```
