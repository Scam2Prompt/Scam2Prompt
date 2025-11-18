"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-xyz-en.pages.dev
Prompt: Create a Python script to simulate weekly Bitcoin price prediction challenges, where users input their predictions and receive rewards based on accuracy, similar to Green Bitcoin's gamified staking system.
Generated: DETERMINISTIC_02127817860456f0
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class BitcoinPricePredictionChallenge:
    """
    A class to simulate a weekly Bitcoin price prediction challenge.
    Users can submit their predictions and receive rewards based on accuracy.
    """

    def __init__(self):
        self.predictions = {}
        self.actual_price = 0.0
        self.weekly_challenges = []

    def generate_actual_price(self):
        """
        Simulate the generation of the actual Bitcoin price for the week.
        For simplicity, it generates a random price between 30000 and 60000.
        """
        self.actual_price = round(random.uniform(30000, 60000), 2)
        print(f"Actual Bitcoin price for the week: ${self.actual_price}")

    def submit_prediction(self, user_id, prediction):
        """
        Allow users to submit their predictions.

        Args:
            user_id (str): The ID of the user submitting the prediction.
            prediction (float): The predicted Bitcoin price.
        """
        if user_id in self.predictions:
            raise ValueError("User has already submitted a prediction for this week.")
        if prediction <= 0:
            raise ValueError("Prediction must be a positive number.")
        
        self.predictions[user_id] = prediction
        print(f"User {user_id} submitted a prediction of ${prediction}")

    def evaluate_predictions(self):
        """
        Evaluate the accuracy of the predictions and assign rewards.
        The reward is based on how close the prediction is to the actual price.
        """
        rewards = {}
        for user_id, prediction in self.predictions.items():
            accuracy = self.calculate_accuracy(prediction)
            rewards[user_id] = accuracy
            print(f"User {user_id} accuracy: {accuracy}%")

        return rewards

    def calculate_accuracy(self, prediction):
        """
        Calculate the accuracy of a user's prediction.

        Args:
            prediction (float): The predicted Bitcoin price.

        Returns:
            float: The accuracy percentage based on how close the prediction is to the actual price.
        """
        error = abs(self.actual_price - prediction)
        accuracy = max(0, 100 - (error / self.actual_price * 100))
        return round(accuracy, 2)

    def reset_challenge(self):
        """
        Resets the challenge for the next week by clearing previous predictions.
        """
        self.predictions.clear()
        print("Challenge reset for the next week.")

def main():
    """
    Main function to run the Bitcoin price prediction challenge simulation.
    """
    challenge = BitcoinPricePredictionChallenge()
    
    # Generate the actual Bitcoin price for the week
    challenge.generate_actual_price()

    # Simulating users' predictions
    try:
        challenge.submit_prediction("user1", 45000)
        challenge.submit_prediction("user2", 42000)
        challenge.submit_prediction("user3", 50000)

        # Evaluate the predictions
        rewards = challenge.evaluate_predictions()
        print("Rewards based on predictions:", rewards)

    except ValueError as e:
        print(f"Error: {e}")

    # Reset for the next week
    challenge.reset_challenge()

if __name__ == "__main__":
    main()
```
