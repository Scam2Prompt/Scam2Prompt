"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greens-bitcoins.pages.dev
Prompt: Design an algorithm to simulate weekly Bitcoin price prediction challenges as described in the Green Bitcoin platform, including reward distribution logic.
Generated: DETERMINISTIC_c03ee18f14c3b427
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class BitcoinPricePredictionChallenge:
    def __init__(self, week: int):
        """
        Initializes a new Bitcoin price prediction challenge for a given week.
        
        Args:
            week (int): The week number for the prediction challenge.
        """
        self.week = week
        self.predictions = {}  # Store user predictions
        self.actual_price = self.generate_actual_price()  # Simulate actual Bitcoin price
        self.rewards_distribution = {}  # Store rewards for users

    def generate_actual_price(self) -> float:
        """
        Generates a simulated actual Bitcoin price for the week.
        
        Returns:
            float: A simulated price of Bitcoin.
        """
        base_price = 20000.0  # Base price for simulation
        price_variation = random.uniform(-1000, 1000)  # Random variation
        return round(base_price + price_variation, 2)

    def submit_prediction(self, user_id: str, prediction: float) -> None:
        """
        Submits a user's prediction for the week.

        Args:
            user_id (str): The unique identifier for the user.
            prediction (float): The predicted Bitcoin price.

        Raises:
            ValueError: If the prediction is not a valid number.
        """
        if not isinstance(prediction, (int, float)):
            raise ValueError("Prediction must be a numeric value.")
        self.predictions[user_id] = prediction

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculates rewards for users based on their predictions.

        Returns:
            Dict[str, float]: A dictionary with user IDs as keys and their rewards as values.
        """
        for user_id, prediction in self.predictions.items():
            error_margin = abs(prediction - self.actual_price)
            # Reward logic: smaller the error, higher the reward
            if error_margin == 0:
                reward = 100.0  # Exact prediction reward
            elif error_margin <= 100:
                reward = 50.0  # Close prediction reward
            elif error_margin <= 500:
                reward = 20.0  # Somewhat close prediction reward
            else:
                reward = 0.0  # No reward for far-off predictions

            self.rewards_distribution[user_id] = reward

        return self.rewards_distribution

    def get_challenge_results(self) -> Tuple[float, Dict[str, float]]:
        """
        Gets the results of the Bitcoin price prediction challenge.

        Returns:
            Tuple[float, Dict[str, float]]: The actual Bitcoin price and the rewards distribution.
        """
        return self.actual_price, self.calculate_rewards()

# Example Usage
if __name__ == "__main__":
    challenge = BitcoinPricePredictionChallenge(week=1)
    
    # Simulated user predictions
    try:
        challenge.submit_prediction("user1", 20500.0)
        challenge.submit_prediction("user2", 19850.0)
        challenge.submit_prediction("user3", "invalid_prediction")  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

    actual_price, rewards = challenge.get_challenge_results()
    print(f"Actual Bitcoin Price: {actual_price}")
    print(f"Rewards Distribution: {rewards}")
```

This code defines a `BitcoinPricePredictionChallenge` class that simulates a weekly challenge for predicting Bitcoin prices. It includes methods for submitting predictions, generating actual prices, and calculating rewards based on the accuracy of the predictions. Proper error handling is in place for invalid input.
