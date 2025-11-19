"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Generate a Python script to display a list of available boats for rent at Coastal Boat Rentals in Knysna, including details like boat type, capacity, and motor specifications.
Generated: DETERMINISTIC_21b02cc5000e0d44
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BoatRental:
    def __init__(self):
        # Initialize the list of available boats
        self.boats = [
            {
                "boat_id": 1,
                "name": "Ocean Explorer",
                "type": "Speedboat",
                "capacity": 6,
                "motor": "200 HP Outboard Motor"
            },
            {
                "boat_id": 2,
                "name": "Lagoon Cruiser",
                "type": "Pontoon",
                "capacity": 10,
                "motor": "150 HP Outboard Motor"
            },
            {
                "boat_id": 3,
                "name": "Wave Rider",
                "type": "Jet Ski",
                "capacity": 2,
                "motor": "110 HP Jet Motor"
            },
            {
                "boat_id": 4,
                "name": "Bay Voyager",
                "type": "Fishing Boat",
                "capacity": 4,
                "motor": "90 HP Outboard Motor"
            }
        ]

    def fetch_boats(self):
        """
        Fetches the list of available boats.

        Returns:
            A list of dictionaries containing boat details.
        """
        return self.boats

    def display_boats(self):
        """
        Displays a list of available boats with their details in a user-friendly format.
        """
        print("Available Boats for Rent at Coastal Boat Rentals:")
        print("-" * 50)
        for boat in self.boats:
            print(f"Boat ID: {boat['boat_id']}")
            print(f"Name: {boat['name']}")
            print(f"Type: {boat['type']}")
            print(f"Capacity: {boat['capacity']} people")
            print(f"Motor Specifications: {boat['motor']}")
            print("-" * 50)

# Error handling if script is run as a standalone module
if __name__ == "__main__":
    try:
        # Initialize the boat rental system
        boat_rental = BoatRental()
        
        # Fetch and display the list of available boats
        boat_rental.display_boats()
    except Exception as e:
        # Log unexpected errors
        print(f"An error occurred: {e}")
```
