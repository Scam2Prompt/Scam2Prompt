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
import datetime
from typing import List, Dict

class GreenBitcoinChallenge:
    def __init__(self, participants: List[str], initial_price: float):
        """
        Initializes the challenge.
        
        :param participants: List of participant names.
        :param initial_price: The initial Bitcoin price to be used in predictions.
        """
        self.participants = participants
        self.initial_price = initial_price
        self.weekly_predictions = {}  # Stores participant predictions
        self.actual_prices = []       # Logs actual weekly Bitcoin prices
        self.rewards = {}             # Stores participant rewards

    def simulate_actual_price(self) -> float:
        """
        Simulates the actual Bitcoin price for the week using random fluctuations.
        
        :return: Simulated Bitcoin price for the current week.
        """
        fluctuation = random.uniform(-500, 500)  # Simulate price change within a range
        return round(self.initial_price + fluctuation, 2)

    def collect_predictions(self, predictions: Dict[str, float]):
        """
        Collects Bitcoin price predictions from participants.
        
        :param predictions: Dictionary containing participant names and their price predictions.
        """
        if set(predictions.keys()) != set(self.participants):
            raise ValueError("Predictions must be provided for all participants.")
        self.weekly_predictions = predictions

    def calculate_rewards(self, actual_price: float):
        """
        Calculates rewards based on prediction accuracy.
        
        :param actual_price: The actual Bitcoin price for the current week.
        """
        self.actual_prices.append(actual_price)
        prediction_accuracy = {
            participant: abs(actual_price - prediction)
            for participant, prediction in self.weekly_predictions.items()
        }

        # Sort participants by accuracy (lower is better)
        sorted_participants = sorted(prediction_accuracy.items(), key=lambda x: x[1])

        # Reward logic: Top 3 participants get rewards
        self.rewards = {
            sorted_participants[0][0]: 100,  # 1st place: $100
            sorted_participants[1][0]: 50,  # 2nd place: $50
            sorted_participants[2][0]: 25   # 3rd place: $25
        }

    def run_weekly_challenge(self, predictions: Dict[str, float]):
        """
        Runs the weekly Bitcoin price prediction challenge.
        
        :param predictions: Dictionary containing participant names and their price predictions.
        """
        try:
            # Collect predictions
            self.collect_predictions(predictions)

            # Simulate actual Bitcoin price
            actual_price = self.simulate_actual_price()
            print(f"Actual Bitcoin price: ${actual_price}")

            # Calculate and distribute rewards
            self.calculate_rewards(actual_price)
            print(f"Weekly rewards distributed: {self.rewards}")
        except Exception as e:
            print(f"Error occurred during the challenge: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize challenge with participants and initial Bitcoin price
    participants = ["Alice", "Bob", "Charlie", "Diana"]
    initial_price = 20000.0
    challenge = GreenBitcoinChallenge(participants, initial_price)

    # Simulate weekly predictions (values are examples, can be dynamically generated)
    weekly_predictions = {
        "Alice": 20250.0,
        "Bob": 19875.0,
        "Charlie": 20010.0,
        "Diana": 20100.0
    }

    # Run the weekly challenge
    challenge.run_weekly_challenge(weekly_predictions)
```
