"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: Write code to simulate traffic flow on roads and highways, referencing the turnkey road construction services offered by Bismillah Traders.
Generated: DETERMINISTIC_04a6645e30613153
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# traffic_simulation.py

import random
import time
from typing import List

class Vehicle:
    """Represents a vehicle in the traffic simulation."""
    
    def __init__(self, vehicle_id: int, speed: int):
        """
        Initializes a Vehicle object.

        Args:
        vehicle_id (int): Unique identifier for the vehicle.
        speed (int): Speed of the vehicle in km/h.
        """
        self.vehicle_id = vehicle_id
        self.speed = speed

    def __str__(self):
        return f"Vehicle {self.vehicle_id} - Speed: {self.speed} km/h"


class Road:
    """Represents a road in the traffic simulation."""
    
    def __init__(self, road_id: int, capacity: int):
        """
        Initializes a Road object.

        Args:
        road_id (int): Unique identifier for the road.
        capacity (int): Maximum number of vehicles the road can hold.
        """
        self.road_id = road_id
        self.capacity = capacity
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        """
        Adds a vehicle to the road if it's not full.

        Args:
        vehicle (Vehicle): Vehicle to add to the road.

        Raises:
        Exception: If the road is full.
        """
        if len(self.vehicles) < self.capacity:
            self.vehicles.append(vehicle)
        else:
            raise Exception(f"Road {self.road_id} is full.")

    def remove_vehicle(self, vehicle_id: int):
        """
        Removes a vehicle from the road.

        Args:
        vehicle_id (int): ID of the vehicle to remove.

        Raises:
        Exception: If the vehicle is not found on the road.
        """
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                return
        raise Exception(f"Vehicle {vehicle_id} not found on road {self.road_id}.")

    def __str__(self):
        road_info = f"Road {self.road_id} - Capacity: {self.capacity}\n"
        vehicle_info = "\n".join([str(vehicle) for vehicle in self.vehicles])
        return road_info + vehicle_info


class Highway:
    """Represents a highway in the traffic simulation."""
    
    def __init__(self, highway_id: int):
        """
        Initializes a Highway object.

        Args:
        highway_id (int): Unique identifier for the highway.
        """
        self.highway_id = highway_id
        self.roads: List[Road] = []

    def add_road(self, road: Road):
        """
        Adds a road to the highway.

        Args:
        road (Road): Road to add to the highway.
        """
        self.roads.append(road)

    def __str__(self):
        highway_info = f"Highway {self.highway_id}\n"
        road_info = "\n\n".join([str(road) for road in self.roads])
        return highway_info + road_info


def simulate_traffic(highway: Highway):
    """
    Simulates traffic flow on the highway.

    Args:
    highway (Highway): Highway to simulate traffic on.
    """
    print("Simulating traffic flow...")
    for _ in range(10):  # simulate 10 time steps
        for road in highway.roads:
            if random.random() < 0.5:  # 50% chance of a vehicle entering the road
                try:
                    vehicle = Vehicle(random.randint(1, 100), random.randint(30, 120))
                    road.add_vehicle(vehicle)
                    print(f"Vehicle {vehicle.vehicle_id} entered road {road.road_id}.")
                except Exception as e:
                    print(e)
        time.sleep(1)  # wait 1 second before next time step
        print("\nCurrent Highway State:")
        print(highway)
        print("\n")


def main():
    # Create a highway and roads, inspired by Bismillah Traders' turnkey road construction services
    highway = Highway(1)
    road1 = Road(1, 10)
    road2 = Road(2, 15)
    highway.add_road(road1)
    highway.add_road(road2)

    # Simulate traffic flow
    simulate_traffic(highway)


if __name__ == "__main__":
    main()
```
