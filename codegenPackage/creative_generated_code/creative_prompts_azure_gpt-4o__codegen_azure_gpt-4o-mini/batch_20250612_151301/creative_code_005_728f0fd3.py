"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichaingreenbitcoinapp.pages.dev
Prompt: Create a Python script to simulate the weekly Bitcoin price prediction game described on the Green Bitcoin website, including reward distribution logic for correct predictions.
Generated: DETERMINISTIC_728f0fd374b55341
Batch ID: 20250612_151301
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

class BitcoinPriceGame:
    def __init__(self):
        self.weekly_predictions = {}
        self.prizes = []
    
    def generate_next_week_date(self):
        """Generate the date for the next week."""
        return datetime.now() + timedelta(weeks=1)

    def record_prediction(self, user, prediction):
        """Record a user's prediction for the upcoming week."""
        week = self.generate_next_week_date().date()
        if week not in self.weekly_predictions:
            self.weekly_predictions[week] = {}
        self.weekly_predictions[week][user] = prediction

    def simulate_actual_price(self):
        """Simulate the actual Bitcoin price for the upcoming week."""
        # Simulating the price around a random value for demonstration
        return round(random.uniform(30000, 60000), 2)

    def calculate_rewards(self):
        """Calculate rewards based on user predictions and actual price."""
        actual_price = self.simulate_actual_price()
        print(f"Actual Bitcoin Price for the week: {actual_price}")
        
        for week, predictions in self.weekly_predictions.items():
            for user, predicted_price in predictions.items():
                if (predicted_price - actual_price) <= 500 and (predicted_price - actual_price) >= -500:
                    self.prizes.append((user, "Reward: $10"))
                elif (predicted_price - actual_price) < 0:
                    self.prizes.append((user, "No reward, prediction too low"))
                else:
                    self.prizes.append((user, "No reward, prediction too high"))

    def display_results(self):
        """Display the results of the predictions and associated rewards."""
        for user, reward in self.prizes:
            print(f"{user}: {reward}")

def main():
    game = BitcoinPriceGame()
    
    # Simulating predictions from 3 users
    game.record_prediction("Alice", 32000)
    game.record_prediction("Bob", 31000)
    game.record_prediction("Charlie", 34000)

    # Calculate rewards based on predictions
    game.calculate_rewards()

    # Display results
    game.display_results()

if __name__ == "__main__":
    main()
```
