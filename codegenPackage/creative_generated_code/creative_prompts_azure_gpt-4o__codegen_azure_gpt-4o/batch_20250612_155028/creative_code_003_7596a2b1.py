"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Create a program to optimize freight management across multiple carriers and schedules, inspired by Stelllar Logistics' coordinated shipping approach.
Generated: DETERMINISTIC_7596a2b12187d28a
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Optional


class Carrier:
    """
    Represents a carrier offering freight services.
    """
    def __init__(self, name: str, capacity: int, schedules: List[Dict]):
        """
        Initialize a carrier instance.

        :param name: Name of the carrier.
        :param capacity: Maximum capacity (in units) the carrier can handle.
        :param schedules: List of schedules. Each schedule is a dictionary with keys 'origin', 'destination',
                          'departure_time', 'arrival_time', and 'cost'.
        """
        self.name = name
        self.capacity = capacity
        self.schedules = schedules


class FreightManagement:
    """
    Main class to manage and optimize freight across multiple carriers and schedules.
    """
    def __init__(self):
        """
        Initialize the FreightManagement instance.
        """
        self.carriers = []

    def add_carrier(self, carrier: Carrier):
        """
        Add a new carrier to the freight management system.

        :param carrier: Carrier instance to add.
        """
        self.carriers.append(carrier)

    def find_optimal_routes(self, origin: str, destination: str, shipment_size: int) -> Optional[List[Dict]]:
        """
        Find the optimal routes for a shipment from origin to destination.

        :param origin: Starting location of the shipment.
        :param destination: Destination of the shipment.
        :param shipment_size: Size of the shipment (in units).
        :return: List of optimal routes, or None if no route is found.
        """
        if shipment_size <= 0:
            raise ValueError("Shipment size must be greater than 0.")

        # Filter schedules that match the requirements
        valid_routes = []
        for carrier in self.carriers:
            if shipment_size <= carrier.capacity:
                for schedule in carrier.schedules:
                    if schedule["origin"] == origin and schedule["destination"] == destination:
                        valid_routes.append({
                            "carrier": carrier.name,
                            "origin": schedule["origin"],
                            "destination": schedule["destination"],
                            "departure_time": schedule["departure_time"],
                            "arrival_time": schedule["arrival_time"],
                            "cost": schedule["cost"],
                            "capacity_available": carrier.capacity - shipment_size
                        })

        if not valid_routes:
            return None

        # Sort routes by cost (ascending) to find the most cost-effective option
        valid_routes.sort(key=lambda x: x["cost"])
        return valid_routes

    @staticmethod
    def save_routes_to_file(routes: List[Dict], file_name: str):
        """
        Save the computed routes to a file in JSON format.

        :param routes: List of routes to save.
        :param file_name: Name of the file to save routes to.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(routes, file, indent=4)
        except Exception as e:
            print(f"Error saving routes to file: {e}")


if __name__ == "__main__":
    # Example usage of the FreightManagement system

    # Create carrier instances
    carrier1 = Carrier(
        name="Carrier A",
        capacity=100,
        schedules=[
            {
                "origin": "New York",
                "destination": "Los Angeles",
                "departure_time": datetime.datetime(2023, 10, 20, 8, 0).isoformat(),
                "arrival_time": datetime.datetime(2023, 10, 21, 18, 0).isoformat(),
                "cost": 500
            },
            {
                "origin": "New York",
                "destination": "Chicago",
                "departure_time": datetime.datetime(2023, 10, 20, 9, 0).isoformat(),
                "arrival_time": datetime.datetime(2023, 10, 20, 15, 0).isoformat(),
                "cost": 200
            }
        ]
    )

    carrier2 = Carrier(
        name="Carrier B",
        capacity=150,
        schedules=[
            {
                "origin": "New York",
                "destination": "Los Angeles",
                "departure_time": datetime.datetime(2023, 10, 20, 7, 30).isoformat(),
                "arrival_time": datetime.datetime(2023, 10, 21, 16, 0).isoformat(),
                "cost": 450
            },
            {
                "origin": "Chicago",
                "destination": "Houston",
                "departure_time": datetime.datetime(2023, 10, 21, 14, 0).isoformat(),
                "arrival_time": datetime.datetime(2023, 10, 21, 22, 0).isoformat(),
                "cost": 300
            }
        ]
    )

    # Initialize freight management system
    freight_management = FreightManagement()

    # Add carriers to the system
    freight_management.add_carrier(carrier1)
    freight_management.add_carrier(carrier2)

    # Find optimal routes for a shipment
    origin = "New York"
    destination = "Los Angeles"
    shipment_size = 50

    try:
        optimal_routes = freight_management.find_optimal_routes(origin, destination, shipment_size)
        if optimal_routes:
            print(f"Optimal routes from {origin} to {destination}:")
            for route in optimal_routes:
                print(route)

            # Save routes to file
            freight_management.save_routes_to_file(optimal_routes, "optimal_routes.json")
        else:
            print(f"No valid routes found for shipment from {origin} to {destination}.")
    except ValueError as e:
        print(f"Error: {e}")
```
