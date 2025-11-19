"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: Write a Python function to simulate weekly Bitcoin price prediction challenges, allowing users to input their predictions and calculate rewards based on accuracy.
Generated: DETERMINISTIC_6977228ad390a9fd
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BitcoinPricePredictionChallenge:
    def __init__(self):
        """Initialize the challenge with a random Bitcoin price."""
        self.actual_price = self.generate_actual_price()
        self.predictions = {}

    def generate_actual_price(self):
        """Generate a random Bitcoin price between $30,000 and $60,000."""
        return round(random.uniform(30000, 60000), 2)

    def submit_prediction(self, user_id, predicted_price):
        """
        Submit a user's prediction for the Bitcoin price.

        Args:
            user_id (str): The unique identifier for the user.
            predicted_price (float): The user's predicted Bitcoin price.

        Raises:
            ValueError: If the predicted price is not a valid number.
        """
        if not isinstance(predicted_price, (int, float)):
            raise ValueError("Predicted price must be a number.")
        
        self.predictions[user_id] = predicted_price

    def calculate_rewards(self):
        """
        Calculate rewards based on the accuracy of predictions.

        Returns:
            dict: A dictionary containing user IDs and their corresponding rewards.
        """
        rewards = {}
        for user_id, predicted_price in self.predictions.items():
            accuracy = self.calculate_accuracy(predicted_price)
            rewards[user_id] = self.determine_reward(accuracy)
        return rewards

    def calculate_accuracy(self, predicted_price):
        """
        Calculate the accuracy of the user's prediction.

        Args:
            predicted_price (float): The user's predicted Bitcoin price.

        Returns:
            float: The accuracy percentage of the prediction.
        """
        difference = abs(predicted_price - self.actual_price)
        accuracy = max(0, 100 - (difference / self.actual_price * 100))
        return accuracy

    def determine_reward(self, accuracy):
        """
        Determine the reward based on accuracy.

        Args:
            accuracy (float): The accuracy percentage of the prediction.

        Returns:
            str: A reward message based on the accuracy.
        """
        if accuracy >= 90:
            return "Gold Star"
        elif accuracy >= 75:
            return "Silver Star"
        elif accuracy >= 50:
            return "Bronze Star"
        else:
            return "No Reward"

    def get_actual_price(self):
        """Return the actual Bitcoin price for reference."""
        return self.actual_price

# Example usage
if __name__ == "__main__":
    challenge = BitcoinPricePredictionChallenge()
    print(f"Actual Bitcoin Price: ${challenge.get_actual_price()}")

    # Simulate user predictions
    try:
        challenge.submit_prediction("user1", 45000)
        challenge.submit_prediction("user2", 55000)
        challenge.submit_prediction("user3", 30000)

        rewards = challenge.calculate_rewards()
        print("Rewards based on predictions:")
        for user, reward in rewards.items():
            print(f"{user}: {reward}")
    except ValueError as e:
        print(f"Error: {e}")
```
