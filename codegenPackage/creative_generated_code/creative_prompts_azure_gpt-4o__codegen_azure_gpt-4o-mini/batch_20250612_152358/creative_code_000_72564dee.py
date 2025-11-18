"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Write a Python script to simulate a pop culture prediction betting system, including user input for predictions and calculating odds based on historical data.
Generated: DETERMINISTIC_72564dee3cd7c218
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BettingSystem:
    def __init__(self):
        # Initialize the predictions and historical data
        self.predictions = {}
        self.historical_data = {
            'movie': 0.6,  # Example: 60% success rate for movie predictions
            'music': 0.7,  # Example: 70% success rate for music predictions
            'tv_show': 0.5  # Example: 50% success rate for TV show predictions
        }

    def get_odds(self, category):
        """Calculate and return odds based on historical data."""
        if category not in self.historical_data:
            raise ValueError(f"Invalid category '{category}'. Valid categories are {list(self.historical_data.keys())}.")
        
        # Calculate odds as the inverse of the success rate
        success_rate = self.historical_data[category]
        odds = 1 / success_rate
        return odds

    def place_bet(self, category, prediction):
        """Place a bet on a given prediction in a specified category."""
        if category not in self.historical_data:
            raise ValueError(f"Invalid category '{category}'. Valid categories are {list(self.historical_data.keys())}.")
        
        self.predictions[prediction] = category
        print(f"Bet placed: {prediction} in category '{category}'.")

    def simulate_outcome(self, prediction):
        """Simulate the outcome of the prediction based on historical odds."""
        if prediction not in self.predictions:
            raise ValueError(f"No bet found for prediction '{prediction}'.")

        category = self.predictions[prediction]
        success_rate = self.historical_data[category]

        # Simulate outcome based on success rate
        outcome = random.random() < success_rate
        return outcome

    def run(self):
        """Main loop for the betting system."""
        print("Welcome to the Pop Culture Prediction Betting System!")
        
        while True:
            try:
                category = input("Enter category (movie, music, tv_show) or 'exit' to quit: ").strip().lower()
                if category == 'exit':
                    break

                prediction = input("Enter your prediction: ").strip()
                self.place_bet(category, prediction)

                odds = self.get_odds(category)
                print(f"The odds for your bet are: {odds:.2f}")

                # Simulate the outcome
                outcome = self.simulate_outcome(prediction)
                if outcome:
                    print(f"Congratulations! Your prediction '{prediction}' was correct!")
                else:
                    print(f"Sorry! Your prediction '{prediction}' was incorrect.")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    betting_system = BettingSystem()
    betting_system.run()
```
