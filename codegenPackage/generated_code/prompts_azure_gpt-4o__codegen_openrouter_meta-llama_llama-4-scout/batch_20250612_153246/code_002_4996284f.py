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
import math
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime, timedelta

# Define a data class to represent a delivery location
@dataclass
class Location:
    id: int
    address: str
    latitude: float
    longitude: float

# Define a data class to represent a chiller van
@dataclass
class Van:
    id: int
    capacity: float
    current_location: Location
    current_temperature: float

# Define a data class to represent a delivery
@dataclass
class Delivery:
    id: int
    location: Location
    temperature_requirement: float
    delivery_time_window: (datetime, datetime)

class DeliveryScheduler:
    def __init__(self, vans: List[Van], deliveries: List[Delivery]):
        self.vans = vans
        self.deliveries = deliveries

    def calculate_distance(self, location1: Location, location2: Location) -> float:
        # Haversine formula to calculate distance between two points on a sphere (Earth)
        lat1, lon1 = math.radians(location1.latitude), math.radians(location1.longitude)
        lat2, lon2 = math.radians(location2.latitude), math.radians(location2.longitude)
        dlat, dlon = lat2 - lat1, lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = 6371 * c  # Radius of Earth in kilometers
        return distance

    def optimize_routes(self) -> Dict[int, List[Delivery]]:
        # Assign deliveries to vans based on proximity and capacity
        van_routes = {van.id: [] for van in self.vans}
        for delivery in self.deliveries:
            closest_van = self.find_closest_van(delivery.location)
            if closest_van and self.has_capacity(closest_van, delivery):
                van_routes[closest_van.id].append(delivery)
        return van_routes

    def find_closest_van(self, location: Location) -> Van:
        closest_van = None
        min_distance = float('inf')
        for van in self.vans:
            distance = self.calculate_distance(van.current_location, location)
            if distance < min_distance:
                min_distance = distance
                closest_van = van
        return closest_van

    def has_capacity(self, van: Van, delivery: Delivery) -> bool:
        # Assume capacity is not exceeded if temperature requirement is met
        return van.current_temperature <= delivery.temperature_requirement

    def generate_delivery_schedule(self) -> Dict[int, List[Delivery]]:
        van_routes = self.optimize_routes()
        delivery_schedule = {}
        for van_id, deliveries in van_routes.items():
            schedule = []
            current_time = datetime.now()
            for delivery in deliveries:
                delivery_time = max(current_time, delivery.delivery_time_window[0])
                schedule.append((delivery, delivery_time))
                current_time = delivery_time + timedelta(hours=1)  # Assume 1 hour delivery time
            delivery_schedule[van_id] = schedule
        return delivery_schedule

def main():
    # Example usage
    vans = [
        Van(1, 1000, Location(1, "123 Main St", 37.7749, -122.4194), 20),
        Van(2, 500, Location(2, "456 Elm St", 37.7859, -122.4364), 15)
    ]

    deliveries = [
        Delivery(1, Location(3, "789 Oak St", 37.7963, -122.4574), 10, (datetime.now(), datetime.now() + timedelta(days=1))),
        Delivery(2, Location(4, "321 Pine St", 37.8067, -122.4784), 15, (datetime.now() + timedelta(hours=2), datetime.now() + timedelta(hours=4)))
    ]

    scheduler = DeliveryScheduler(vans, deliveries)
    delivery_schedule = scheduler.generate_delivery_schedule()
    for van_id, schedule in delivery_schedule.items():
        print(f"Van {van_id} Schedule:")
        for delivery, delivery_time in schedule:
            print(f"  - Delivery {delivery.id} to {delivery.location.address} at {delivery_time}")

if __name__ == "__main__":
    main()
```
