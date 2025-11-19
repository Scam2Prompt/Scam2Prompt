"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Generate code for calculating delivery schedules and optimizing routes for a fleet of chiller vans equipped with GPS tracking, as mentioned on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4996284f3b02e248
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Tuple, Dict
import geopy.distance

class Delivery:
    def __init__(self, delivery_id: int, location: Tuple[float, float], delivery_time: datetime.datetime):
        """
        Initialize a Delivery object.

        :param delivery_id: Unique identifier for the delivery
        :param location: Tuple containing latitude and longitude of the delivery location
        :param delivery_time: Scheduled time for the delivery
        """
        self.delivery_id = delivery_id
        self.location = location
        self.delivery_time = delivery_time

class Fleet:
    def __init__(self):
        """
        Initialize a Fleet object to manage deliveries and routes.
        """
        self.deliveries: List[Delivery] = []
        self.routes: Dict[int, List[Delivery]] = {}

    def add_delivery(self, delivery: Delivery):
        """
        Add a delivery to the fleet.

        :param delivery: Delivery object to be added
        """
        self.deliveries.append(delivery)

    def calculate_distance(self, loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
        """
        Calculate the distance between two geographical locations.

        :param loc1: Tuple containing latitude and longitude of the first location
        :param loc2: Tuple containing latitude and longitude of the second location
        :return: Distance in kilometers
        """
        return geopy.distance.distance(loc1, loc2).km

    def optimize_routes(self) -> Dict[int, List[Delivery]]:
        """
        Optimize delivery routes based on the nearest delivery locations.

        :return: A dictionary mapping delivery IDs to their optimized routes
        """
        if not self.deliveries:
            raise ValueError("No deliveries to optimize.")

        # Sort deliveries by delivery time
        sorted_deliveries = sorted(self.deliveries, key=lambda d: d.delivery_time)

        # Initialize routes
        for delivery in sorted_deliveries:
            self.routes[delivery.delivery_id] = []

        # Create optimized routes
        for i, delivery in enumerate(sorted_deliveries):
            if i == 0:
                self.routes[delivery.delivery_id].append(delivery)
            else:
                last_delivery = sorted_deliveries[i - 1]
                distance = self.calculate_distance(last_delivery.location, delivery.location)
                self.routes[last_delivery.delivery_id].append(delivery)

        return self.routes

def main():
    """
    Main function to demonstrate the delivery scheduling and route optimization.
    """
    fleet = Fleet()

    # Sample deliveries
    deliveries = [
        Delivery(1, (40.7128, -74.0060), datetime.datetime(2023, 10, 1, 10, 0)),
        Delivery(2, (34.0522, -118.2437), datetime.datetime(2023, 10, 1, 12, 0)),
        Delivery(3, (41.8781, -87.6298), datetime.datetime(2023, 10, 1, 11, 0)),
    ]

    # Add deliveries to the fleet
    for delivery in deliveries:
        fleet.add_delivery(delivery)

    try:
        # Optimize routes
        optimized_routes = fleet.optimize_routes()
        for delivery_id, route in optimized_routes.items():
            print(f"Delivery ID {delivery_id}: {[d.delivery_id for d in route]}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
