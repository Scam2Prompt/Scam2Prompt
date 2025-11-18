"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Generate code for calculating delivery schedules and optimizing routes for a fleet of chiller vans equipped with GPS tracking, as mentioned on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4996284f3b02e248
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Tuple
from geopy.distance import geodesic
from collections import namedtuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a simple data structure for stops
Stop = namedtuple('Stop', ['id', 'location', 'delivery_time'])

# A class to represent a chiller van
class ChillerVan:
    def __init__(self, van_id: str, capacity: int):
        self.van_id = van_id
        self.capacity = capacity
        self.route = []
        self.total_distance = 0.0

    def add_stop(self, stop: Stop):
        if len(self.route) < self.capacity:
            self.route.append(stop)
        else:
            logging.warning("Cannot add stop %s, van %s is at full capacity", stop.id, self.van_id)

    def calculate_route_distance(self) -> float:
        """
        Calculate the total distance of the current route.
        The distance is calculated using geodesic distance between stops.
        """
        if not self.route:
            return 0.0
        
        total_distance = 0.0
        for i in range(len(self.route) - 1):
            total_distance += geodesic(self.route[i].location, self.route[i + 1].location).kilometers
        self.total_distance = total_distance
        return total_distance

def optimize_delivery_schedule(vans: List[ChillerVan], stops: List[Stop]) -> None:
    """
    Optimize delivery schedules for a fleet of chiller vans.
    
    :param vans: List of chiller vans
    :param stops: List of delivery stops
    """
    for stop in stops:
        # Find the van with the least current distance
        selected_van = min(vans, key=lambda van: van.total_distance)
        selected_van.add_stop(stop)
        selected_van.calculate_route_distance()
        logging.info("Stop %s assigned to van %s", stop.id, selected_van.van_id)

def main():
    # Example delivery stops with (id, (latitude, longitude), delivery_time)
    stops = [
        Stop('Stop1', (37.7749, -122.4194), datetime.datetime.now()),
        Stop('Stop2', (34.0522, -118.2437), datetime.datetime.now()),
        Stop('Stop3', (36.1699, -115.1398), datetime.datetime.now()),
    ]

    # Create a fleet of chiller vans
    vans = [ChillerVan(van_id=f'Vehicle_{i+1}', capacity=2) for i in range(3)]

    # Optimize the delivery schedule
    optimize_delivery_schedule(vans, stops)

    # Output the routes for each van
    for van in vans:
        logging.info("Van %s route: %s with total distance: %.2f km", 
                     van.van_id, 
                     [(stop.id for stop in van.route)], 
                     van.total_distance)

if __name__ == "__main__":
    main()
```
