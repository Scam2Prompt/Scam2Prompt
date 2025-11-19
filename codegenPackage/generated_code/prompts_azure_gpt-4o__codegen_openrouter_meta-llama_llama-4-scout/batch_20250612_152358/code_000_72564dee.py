"""
Generated Code Metadata:
========================
Original URL: https://poppredict.vercel.app
Prompt: Write a Python script to simulate a pop culture prediction betting system, including user input for predictions and calculating odds based on historical data.
Generated: DETERMINISTIC_72564dee3cd7c218
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class PopCulturePredictionSystem:
    def __init__(self):
        self.historical_data = self.load_historical_data()
        self.predictions = {}

    def load_historical_data(self):
        """Load historical data from file"""
        if os.path.exists('historical_data.json'):
            with open('historical_data.json', 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_historical_data(self):
        """Save historical data to file"""
        with open('historical_data.json', 'w') as f:
            json.dump(self.historical_data, f)

    def add_historical_data(self, event, outcome):
        """Add historical data"""
        if event in self.historical_data:
            if outcome in self.historical_data[event]:
                self.historical_data[event][outcome] += 1
            else:
                self.historical_data[event][outcome] = 1
        else:
            self.historical_data[event] = {outcome: 1}
        self.save_historical_data()

    def calculate_odds(self, event, outcome):
        """Calculate odds based on historical data"""
        if event in self.historical_data:
            total_outcomes = sum(self.historical_data[event].values())
            if outcome in self.historical_data[event]:
                return 1 / (self.historical_data[event][outcome] / total_outcomes)
            else:
                return 1 / (1 / total_outcomes)  # assume 1 occurrence for unknown outcome
        else:
            return 1.0  # assume equal odds for unknown event

    def get_user_prediction(self, event):
        """Get user prediction for an event"""
        while True:
            prediction = input(f"Enter your prediction for {event}: ")
            if prediction:
                return prediction
            else:
                print("Please enter a prediction.")

    def place_bet(self, event):
        """Place a bet on an event"""
        print(f"Available outcomes for {event}:")
        if event in self.historical_data:
            for i, outcome in enumerate(self.historical_data[event]):
                print(f"{i+1}. {outcome} (odds: {self.calculate_odds(event, outcome):.2f})")
        else:
            print("No historical data available. Assuming equal odds.")
            num_outcomes = int(input("Enter the number of possible outcomes: "))
            outcomes = []
            for i in range(num_outcomes):
                outcome = input(f"Enter outcome {i+1}: ")
                outcomes.append(outcome)
            for outcome in outcomes:
                print(f"{outcome} (odds: 1.0)")
        
        prediction = self.get_user_prediction(event)
        if event not in self.predictions:
            self.predictions[event] = []
        self.predictions[event].append(prediction)
        print(f"Bet placed: {event} - {prediction}")

    def display_bets(self):
        """Display all bets"""
        for event, predictions in self.predictions.items():
            print(f"Bets for {event}:")
            for i, prediction in enumerate(predictions):
                print(f"Bet {i+1}: {prediction}")

def main():
    system = PopCulturePredictionSystem()
    while True:
        print("\n1. Place a bet")
        print("2. Display bets")
        print("3. Add historical data")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            event = input("Enter the event: ")
            system.place_bet(event)
        elif choice == "2":
            system.display_bets()
        elif choice == "3":
            event = input("Enter the event: ")
            outcome = input("Enter the outcome: ")
            system.add_historical_data(event, outcome)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
