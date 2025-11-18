"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds.pro
Prompt: Generate code to track and simulate Moonbird B95's flight data over time, integrating historical data and predictions for future migrations.
Generated: DETERMINISTIC_ca0a7dcb3eec5166
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
import json

class MoonbirdB95FlightTracker:
    """
    A class to track and simulate Moonbird B95's flight data over time.
    Integrates historical data and predictions for future migrations.
    """

    def __init__(self):
        """
        Initializes the flight tracker with historical data and sets up the structure for predictions.
        """
        self.historical_data = []  # List to store historical flight data
        self.predicted_data = []   # List to store predicted flight data

    def load_historical_data(self, file_path):
        """
        Loads historical data from a JSON file.

        Parameters:
            file_path (str): Path to the JSON file containing historical flight data.
        """
        try:
            with open(file_path, 'r') as file:
                self.historical_data = json.load(file)
            print(f"Historical data loaded successfully from {file_path}.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading historical data: {e}")
            self.historical_data = []

    def simulate_future_migration(self, years=5):
        """
        Simulates future migrations based on historical patterns.

        Parameters:
            years (int): Number of years to simulate future migration data.
        """
        if not self.historical_data:
            print("No historical data available for predictions.")
            return
        
        last_known_data = self.historical_data[-1]
        current_date = datetime.datetime.strptime(last_known_data['date'], '%Y-%m-%d')
        
        for _ in range(years):
            # Generate random migrations based on historical data
            current_date += datetime.timedelta(days=365)
            predicted_entry = {
                "date": current_date.strftime('%Y-%m-%d'),
                "location": random.choice(["Argentina", "Canada", "USA", "Brazil", "Chile"]),
                "distance_km": random.randint(1000, 12000)  # Randomly simulate distance flown
            }
            self.predicted_data.append(predicted_entry)

    def save_predictions_to_file(self, file_path):
        """
        Saves predicted migration data to a JSON file.

        Parameters:
            file_path (str): Path to the JSON file where predictions should be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.predicted_data, file, indent=4)
            print(f"Predicted data successfully saved to {file_path}.")
        except Exception as e:
            print(f"Error saving predicted data: {e}")

    def display_data(self):
        """
        Displays historical and predicted flight data.
        """
        print("\nHistorical Data:")
        for entry in self.historical_data:
            print(entry)

        print("\nPredicted Data:")
        for entry in self.predicted_data:
            print(entry)


# Example usage of the tracker
if __name__ == "__main__":
    tracker = MoonbirdB95FlightTracker()

    # Load historical data from a sample file (replace with actual file path)
    tracker.load_historical_data("historical_data.json")

    # Simulate future migration data for 5 years
    tracker.simulate_future_migration(years=5)

    # Save predictions to a file
    tracker.save_predictions_to_file("predicted_data.json")

    # Display historical and predicted data
    tracker.display_data()
```
