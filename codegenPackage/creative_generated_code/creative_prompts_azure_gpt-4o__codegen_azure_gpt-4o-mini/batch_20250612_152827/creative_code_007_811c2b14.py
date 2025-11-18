"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Write code to simulate weekly Bitcoin price prediction challenges, incorporating reward distribution logic based on user accuracy, as described in the Green Bitcoin gamification system.
Generated: DETERMINISTIC_811c2b14d86dc0c5
Batch ID: 20250612_152827
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
    def __init__(self):
        self.users = {}  # Stores user predictions and rewards
        self.current_price = 0.0  # Current Bitcoin price
        self.last_updated = datetime.now()  # Last updated time of Bitcoin price

    def update_bitcoin_price(self):
        """
        Simulate updating the Bitcoin price. 
        In a real application, this would fetch data from an API.
        For simulation, we're just using a random float.
        """
        self.current_price = round(random.uniform(30000, 60000), 2)
        self.last_updated = datetime.now()
        print(f"[{self.last_updated}] Bitcoin price updated: ${self.current_price}")

    def submit_prediction(self, user_id, predicted_price):
        """
        Allows users to submit their price predictions for the week.
        
        :param user_id: Unique identifier for the user
        :param predicted_price: User's predicted price for Bitcoin
        """
        if user_id not in self.users:
            self.users[user_id] = {'predictions': [], 'reward': 0}
        
        self.users[user_id]['predictions'].append(predicted_price)
        print(f"User {user_id} submitted prediction: ${predicted_price}")

    def evaluate_predictions(self):
        """
        Evaluates user predictions against the current Bitcoin price,
        calculates rewards based on accuracy, and updates user rewards.
        """
        if not self.users:
            print("No predictions to evaluate.")
            return
        
        print("Evaluating predictions...")
        for user_id, data in self.users.items():
            if data['predictions']:
                user_prediction = data['predictions'][-1]  # Get last prediction
                accuracy = self.calculate_accuracy(user_prediction)
                reward = self.calculate_reward(accuracy)
                data['reward'] += reward
                print(f"User {user_id} prediction: ${user_prediction}, "
                      f"actual: ${self.current_price}, "
                      f"accuracy: {accuracy:.2f}%, "
                      f"reward: ${reward:.2f}")

    def calculate_accuracy(self, predicted_price):
        """
        Calculate accuracy of the prediction.

        :param predicted_price: The predicted price by the user
        :return: Accuracy as a percentage
        """
        difference = abs(predicted_price - self.current_price)
        maximum_difference = self.current_price * 0.05  # 5% margin
        accuracy = max(0, 100 - (difference / maximum_difference * 100))
        return accuracy

    def calculate_reward(self, accuracy):
        """
        Calculate rewards based on accuracy.

        :param accuracy: Accuracy percentage of the prediction
        :return: Reward amount
        """
        if accuracy > 80:
            return 10.0  # High accuracy reward
        elif accuracy > 50:
            return 5.0  # Moderate accuracy reward
        else:
            return 1.0  # Low accuracy reward

    def reset_challenge(self):
        """
        Resets the challenge for the next week.
        """
        self.users.clear()
        self.current_price = 0.0
        print("Challenge reset for the next week.")

# Example usage
if __name__ == "__main__":
    challenge = BitcoinPricePredictionChallenge()
    challenge.update_bitcoin_price()

    # Simulate user predictions
    challenge.submit_prediction("user1", 35000)
    challenge.submit_prediction("user2", 40000)
    challenge.submit_prediction("user3", 30000)

    # Evaluate predictions
    challenge.evaluate_predictions()

    # Reset for next week
    challenge.reset_challenge()
```
