"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: Write a code snippet to calculate the best travel route from London to Tortola, including flight and ferry options to the British Virgin Islands.
Generated: DETERMINISTIC_efe5d53fd3f0d33a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_route_calculator.py

import math
from typing import List, Dict

class TravelRoute:
    def __init__(self, name: str, duration: int, cost: float):
        """
        Initialize a travel route.

        Args:
        - name (str): The name of the travel route.
        - duration (int): The duration of the travel route in hours.
        - cost (float): The cost of the travel route.
        """
        self.name = name
        self.duration = duration
        self.cost = cost

class Flight(TravelRoute):
    def __init__(self, name: str, duration: int, cost: float, departure_airport: str, arrival_airport: str):
        """
        Initialize a flight.

        Args:
        - name (str): The name of the flight.
        - duration (int): The duration of the flight in hours.
        - cost (float): The cost of the flight.
        - departure_airport (str): The departure airport of the flight.
        - arrival_airport (str): The arrival airport of the flight.
        """
        super().__init__(name, duration, cost)
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport

class Ferry(TravelRoute):
    def __init__(self, name: str, duration: int, cost: float, departure_port: str, arrival_port: str):
        """
        Initialize a ferry.

        Args:
        - name (str): The name of the ferry.
        - duration (int): The duration of the ferry in hours.
        - cost (float): The cost of the ferry.
        - departure_port (str): The departure port of the ferry.
        - arrival_port (str): The arrival port of the ferry.
        """
        super().__init__(name, duration, cost)
        self.departure_port = departure_port
        self.arrival_port = arrival_port

def calculate_best_route(flights: List[Flight], ferries: List[Ferry]) -> Dict:
    """
    Calculate the best travel route from London to Tortola.

    Args:
    - flights (List[Flight]): A list of flights from London to the British Virgin Islands.
    - ferries (List[Ferry]): A list of ferries from the British Virgin Islands to Tortola.

    Returns:
    - A dictionary containing the best travel route and its details.
    """
    # Initialize the best route and its cost
    best_route = None
    best_cost = math.inf
    best_duration = math.inf

    # Iterate over all flights
    for flight in flights:
        # Iterate over all ferries
        for ferry in ferries:
            # Calculate the total duration and cost of the route
            total_duration = flight.duration + ferry.duration
            total_cost = flight.cost + ferry.cost

            # Check if this route is better than the current best route
            if total_cost < best_cost or (total_cost == best_cost and total_duration < best_duration):
                best_route = {
                    "flight": {
                        "name": flight.name,
                        "departure_airport": flight.departure_airport,
                        "arrival_airport": flight.arrival_airport,
                        "duration": flight.duration,
                        "cost": flight.cost
                    },
                    "ferry": {
                        "name": ferry.name,
                        "departure_port": ferry.departure_port,
                        "arrival_port": ferry.arrival_port,
                        "duration": ferry.duration,
                        "cost": ferry.cost
                    },
                    "total_duration": total_duration,
                    "total_cost": total_cost
                }
                best_cost = total_cost
                best_duration = total_duration

    return best_route

def main():
    try:
        # Define flights from London to the British Virgin Islands
        flights = [
            Flight("British Airways", 10, 800, "London Heathrow", "Tortola Terrance B. Lettsome International Airport"),
            Flight("Virgin Atlantic", 11, 850, "London Gatwick", "Tortola Terrance B. Lettsome International Airport"),
            Flight("American Airlines", 12, 900, "London Heathrow", "San Juan Luis Muñoz Marín International Airport")
        ]

        # Define ferries from the British Virgin Islands to Tortola
        ferries = [
            Ferry("Nanny Cay", 2, 100, "Road Town", "Tortola"),
            Ferry("Sandy Toes", 3, 120, "Jost Van Dyke", "Tortola")
        ]

        # Calculate the best travel route
        best_route = calculate_best_route(flights, ferries)

        # Print the best travel route
        if best_route:
            print("Best Travel Route:")
            print(f"Flight: {best_route['flight']['name']} from {best_route['flight']['departure_airport']} to {best_route['flight']['arrival_airport']}")
            print(f"Ferry: {best_route['ferry']['name']} from {best_route['ferry']['departure_port']} to {best_route['ferry']['arrival_port']}")
            print(f"Total Duration: {best_route['total_duration']} hours")
            print(f"Total Cost: ${best_route['total_cost']:.2f}")
        else:
            print("No travel routes found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
