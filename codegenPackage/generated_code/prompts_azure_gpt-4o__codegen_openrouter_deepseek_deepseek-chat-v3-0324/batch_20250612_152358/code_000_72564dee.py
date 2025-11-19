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
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class PredictionBettingSystem:
    """
    A pop culture prediction betting system that allows users to make predictions,
    calculates odds based on historical data, and tracks outcomes.
    """
    
    def __init__(self, data_file: str = "predictions_data.json"):
        """
        Initialize the betting system with a data file for persistence.
        
        Args:
            data_file: Path to the JSON file storing prediction data.
        """
        self.data_file = data_file
        self.predictions: Dict[str, Dict] = {}
        self.historical_data: Dict[str, Dict] = {}
        self.load_data()
    
    def load_data(self) -> None:
        """Load prediction and historical data from the JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.predictions = data.get('predictions', {})
                self.historical_data = data.get('historical_data', {})
        except FileNotFoundError:
            self.predictions = {}
            self.historical_data = {}
        except json.JSONDecodeError:
            print("Error: Corrupted data file. Starting with empty data.")
            self.predictions = {}
            self.historical_data = {}
    
    def save_data(self) -> None:
        """Save prediction and historical data to the JSON file."""
        data = {
            'predictions': self.predictions,
            'historical_data': self.historical_data
        }
        try:
            with open(self.data_file, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_prediction(self, event: str, outcome: str, user: str, confidence: float) -> None:
        """
        Add a new prediction to the system.
        
        Args:
            event: The event being predicted (e.g., "Oscar Best Picture")
            outcome: The predicted outcome (e.g., "Movie X")
            user: The user making the prediction
            confidence: User's confidence level (0.0 to 1.0)
        """
        if confidence < 0 or confidence > 1:
            raise ValueError("Confidence must be between 0.0 and 1.0")
            
        prediction_id = f"pred_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"
        
        self.predictions[prediction_id] = {
            'event': event,
            'outcome': outcome,
            'user': user,
            'confidence': confidence,
            'timestamp': datetime.now().isoformat(),
            'resolved': False,
            'actual_outcome': None
        }
        self.save_data()
    
    def resolve_prediction(self, prediction_id: str, actual_outcome: str) -> None:
        """
        Mark a prediction as resolved with the actual outcome.
        
        Args:
            prediction_id: ID of the prediction to resolve
            actual_outcome: The actual outcome that occurred
        """
        if prediction_id not in self.predictions:
            raise ValueError("Invalid prediction ID")
            
        self.predictions[prediction_id]['resolved'] = True
        self.predictions[prediction_id]['actual_outcome'] = actual_outcome
        
        # Update historical data
        event = self.predictions[prediction_id]['event']
        if event not in self.historical_data:
            self.historical_data[event] = {'outcomes': {}, 'total': 0}
        
        self.historical_data[event]['outcomes'][actual_outcome] = \
            self.historical_data[event]['outcomes'].get(actual_outcome, 0) + 1
        self.historical_data[event]['total'] += 1
        
        self.save_data()
    
    def calculate_odds(self, event: str, outcome: str) -> float:
        """
        Calculate the odds for a specific outcome of an event based on historical data.
        
        Args:
            event: The event to calculate odds for
            outcome: The specific outcome to calculate odds for
            
        Returns:
            The probability (0.0 to 1.0) of the outcome occurring based on history
        """
        if event not in self.historical_data:
            return 0.5  # Default probability if no historical data
            
        total = self.historical_data[event]['total']
        if total == 0:
            return 0.5
            
        outcome_count = self.historical_data[event]['outcomes'].get(outcome, 0)
        return outcome_count / total
    
    def get_user_predictions(self, user: str) -> List[Dict]:
        """
        Get all predictions made by a specific user.
        
        Args:
            user: The username to filter predictions by
            
        Returns:
            List of prediction dictionaries made by the user
        """
        return [pred for pred in self.predictions.values() if pred['user'] == user]
    
    def get_event_predictions(self, event: str) -> List[Dict]:
        """
        Get all predictions for a specific event.
        
        Args:
            event: The event to filter predictions by
            
        Returns:
            List of prediction dictionaries for the event
        """
        return [pred for pred in self.predictions.values() if pred['event'] == event]
    
    def get_top_predictors(self, limit: int = 5) -> List[Tuple[str, float]]:
        """
        Get the top predictors by accuracy.
        
        Args:
            limit: Maximum number of predictors to return
            
        Returns:
            List of tuples (username, accuracy_score)
        """
        user_stats = {}
        
        for pred in self.predictions.values():
            if pred['resolved']:
                user = pred['user']
                correct = pred['outcome'] == pred['actual_outcome']
                
                if user not in user_stats:
                    user_stats[user] = {'correct': 0, 'total': 0}
                
                user_stats[user]['total'] += 1
                if correct:
                    user_stats[user]['correct'] += 1
        
        # Calculate accuracy for each user
        accuracy_scores = []
        for user, stats in user_stats.items():
            accuracy = stats['correct'] / stats['total'] if stats['total'] > 0 else 0
            accuracy_scores.append((user, accuracy))
        
        # Sort by accuracy (descending) and return top N
        accuracy_scores.sort(key=lambda x: x[1], reverse=True)
        return accuracy_scores[:limit]

def main():
    """Main function to run the prediction betting system."""
    betting_system = PredictionBettingSystem()
    
    while True:
        print("\nPop Culture Prediction Betting System")
        print("1. Make a new prediction")
        print("2. View your predictions")
        print("3. View predictions for an event")
        print("4. Resolve a prediction")
        print("5. View top predictors")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            try:
                event = input("Enter the event (e.g., 'Oscar Best Picture'): ")
                outcome = input("Enter your predicted outcome: ")
                user = input("Enter your username: ")
                confidence = float(input("Enter your confidence (0.0-1.0): "))
                
                betting_system.add_prediction(event, outcome, user, confidence)
                print("Prediction added successfully!")
                
                # Calculate and show odds
                odds = betting_system.calculate_odds(event, outcome)
                print(f"Historical odds for this prediction: {odds:.2%}")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            user = input("Enter your username: ")
            predictions = betting_system.get_user_predictions(user)
            
            if not predictions:
                print("No predictions found for this user.")
            else:
                print("\nYour Predictions:")
                for i, pred in enumerate(predictions, 1):
                    status = "Resolved" if pred['resolved'] else "Pending"
                    print(f"{i}. Event: {pred['event']}")
                    print(f"   Prediction: {pred['outcome']}")
                    print(f"   Confidence: {pred['confidence']:.0%}")
                    print(f"   Status: {status}")
                    if pred['resolved']:
                        result = "Correct" if pred['outcome'] == pred['actual_outcome'] else "Incorrect"
                        print(f"   Result: {result} (Actual: {pred['actual_outcome']})")
                    print()
        
        elif choice == "3":
            event = input("Enter the event to view predictions for: ")
            predictions = betting_system.get_event_predictions(event)
            
            if not predictions:
                print("No predictions found for this event.")
            else:
                print(f"\nPredictions for '{event}':")
                for i, pred in enumerate(predictions, 1):
                    status = "Resolved" if pred['resolved'] else "Pending"
                    print(f"{i}.
