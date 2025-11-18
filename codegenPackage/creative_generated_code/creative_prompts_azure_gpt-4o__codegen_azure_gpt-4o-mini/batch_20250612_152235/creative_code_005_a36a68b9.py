"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-claiim.pages.dev
Prompt: Develop a Python script to simulate weekly Bitcoin price prediction challenges and calculate rewards for participants based on their accuracy, as described in the Green Bitcoin gamified staking model.
Generated: DETERMINISTIC_a36a68b9a500d55f
Batch ID: 20250612_152235
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

class BitcoinPricePredictor:
    def __init__(self, actual_price: float):
        """
        Initializes the BitcoinPricePredictor with the actual market price of Bitcoin.

        :param actual_price: The actual price of Bitcoin for the week.
        """
        self.actual_price = actual_price

    def simulate_price_prediction(self) -> float:
        """
        Simulates a predicted price for Bitcoin, allowing for a random variance.

        :return: Simulated predicted price.
        """
        variance = random.uniform(-500, 500)  # Simulating a price variance
        predicted_price = self.actual_price + variance
        return round(predicted_price, 2)

class Participant:
    def __init__(self, name: str):
        """
        Initializes a participant in the Bitcoin prediction challenge.

        :param name: The name of the participant.
        """
        self.name = name
        self.predictions: List[float] = []
        self.reward: float = 0.0

    def make_prediction(self, predicted_price: float):
        """
        Records a participant's prediction.

        :param predicted_price: The predicted price of Bitcoin.
        """
        self.predictions.append(predicted_price)

    def calculate_reward(self, actual_price: float) -> float:
        """
        Calculates the reward based on prediction accuracy.

        :param actual_price: The actual price of Bitcoin.
        :return: The calculated reward for the participant.
        """
        if not self.predictions:
            raise ValueError("No predictions made.")
        
        for prediction in self.predictions:
            error = abs(prediction - actual_price)
            if error <= 100:  # Reward condition for accuracy
                self.reward += 10  # Reward points for accuracy

        return self.reward

def run_prediction_challenge(participants: List[Participant], actual_price: float) -> Dict[str, float]:
    """
    Runs the Bitcoin price prediction challenge.

    :param participants: List of participants in the challenge.
    :param actual_price: The actual price of Bitcoin.
    :return: Dictionary of participants and their rewards.
    """
    rewards = {}
    predictor = BitcoinPricePredictor(actual_price)

    for participant in participants:
        predicted_price = predictor.simulate_price_prediction()
        participant.make_prediction(predicted_price)
        participant.calculate_reward(actual_price)
        rewards[participant.name] = participant.reward

    return rewards

if __name__ == "__main__":
    # Example usage
    try:
        # Simulate a weekly Bitcoin price
        actual_bitcoin_price = 30000.00  # Example actual price
        participants = [Participant("Alice"), Participant("Bob"), Participant("Charlie")]

        # Run the prediction challenge
        rewards_distribution = run_prediction_challenge(participants, actual_bitcoin_price)

        # Display the results
        for name, reward in rewards_distribution.items():
            print(f"{name} earned a reward of: ${reward:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
