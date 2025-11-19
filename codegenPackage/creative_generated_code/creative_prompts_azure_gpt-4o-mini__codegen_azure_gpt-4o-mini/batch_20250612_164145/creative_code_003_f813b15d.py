"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flyvirtualfrontier.net
Prompt: Generate a script that updates flight schedules and data to enhance realism in a virtual airline simulation.
Generated: DETERMINISTIC_f813b15db461a769
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
from datetime import datetime, timedelta

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __repr__(self):
        return (f"Flight({self.flight_number}, {self.origin}, {self.destination}, "
                f"{self.departure_time}, {self.arrival_time})")

def load_flight_data(file_path):
    """Load flight data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            flights = [Flight(**flight) for flight in data['flights']]
            return flights
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []

def save_flight_data(file_path, flights):
    """Save updated flight data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump({'flights': [flight.__dict__ for flight in flights]}, file, indent=4)
    except IOError as e:
        print(f"Error while writing to file {file_path}: {e}")

def update_flight_schedule(flights):
    """Update flight schedules to add delays and cancellations for realism."""
    for flight in flights:
        # Randomly decide to cancel or delay the flight
        action = random.choice(['none', 'delay', 'cancel'])
        if action == 'delay':
            delay_minutes = random.randint(10, 120)  # Delay between 10 to 120 minutes
            flight.departure_time += timedelta(minutes=delay_minutes)
            flight.arrival_time += timedelta(minutes=delay_minutes)
            print(f"Delayed: {flight.flight_number} by {delay_minutes} minutes.")
        elif action == 'cancel':
            print(f"Cancelled: {flight.flight_number}.")
            flights.remove(flight)

def main():
    """Main function to run the flight schedule updating script."""
    flight_data_file = 'flights.json'
    
    # Load existing flight data
    flights = load_flight_data(flight_data_file)
    
    # Update flight schedules
    update_flight_schedule(flights)
    
    # Save updated flight data
    save_flight_data(flight_data_file, flights)

if __name__ == "__main__":
    main()
```

**Note:**
- Create a `flights.json` file in the same directory with the following structure to test the script:
```json
{
    "flights": [
        {
            "flight_number": "AA123",
            "origin": "JFK",
            "destination": "LAX",
            "departure_time": "2023-10-10T14:00:00",
            "arrival_time": "2023-10-10T17:00:00"
        },
        {
            "flight_number": "DL456",
            "origin": "ORD",
            "destination": "ATL",
            "departure_time": "2023-10-10T15:30:00",
            "arrival_time": "2023-10-10T17:30:00"
        }
    ]
}
```
