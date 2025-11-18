"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbtcwebb.pages.dev
Prompt: Write a Python function to simulate weekly Bitcoin price prediction challenges, allowing users to input their predictions and calculate rewards based on accuracy.
Generated: DETERMINISTIC_6977228ad390a9fd
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BitcoinPricePredictor:
    def __init__(self, actual_price: float):
        """
        Initialize the BitcoinPricePredictor with the actual price of Bitcoin.
        
        :param actual_price: The actual price of Bitcoin for the week (float).
        """
        if actual_price <= 0:
            raise ValueError("Actual price must be a positive number.")
        self.actual_price = actual_price

    def get_user_prediction(self) -> float:
        """
        Get the user's predicted Bitcoin price.
        
        :return: User's predicted price (float).
        """
        while True:
            try:
                prediction = float(input("Enter your Bitcoin price prediction for this week: "))
                return prediction
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def calculate_reward(self, user_prediction: float) -> float:
        """
        Calculate the reward based on the accuracy of the user's prediction.
        
        :param user_prediction: The predicted price input by the user (float).
        :return: The reward based on the prediction accuracy (float).
        """
        if user_prediction <= 0:
            raise ValueError("Prediction must be a positive number.")
        
        # Calculate the absolute difference between actual and predicted price
        difference = abs(self.actual_price - user_prediction)
        
        # Reward logic: closer predictions yield higher rewards
        if difference == 0:
            return 100  # Exact match
        elif difference <= 100:
            return 50   # Close prediction
        elif difference <= 500:
            return 20   # Somewhat close prediction
        else:
            return 0    # Poor prediction

    def simulate_challenge(self):
        """
        Simulate the Bitcoin price prediction challenge where users make predictions
        and receive rewards based on their accuracy.
        """
        user_prediction = self.get_user_prediction()
        reward = self.calculate_reward(user_prediction)
        print(f"Your prediction: {user_prediction}")
        print(f"Actual Bitcoin price: {self.actual_price}")
        print(f"Your reward: {reward}")

if __name__ == "__main__":
    # Simulate a weekly Bitcoin price challenge with a randomly generated actual price
    actual_price = random.uniform(10000, 60000)  # Simulate actual price between 10,000 and 60,000
    predictor = BitcoinPricePredictor(actual_price)
    predictor.simulate_challenge()
```
