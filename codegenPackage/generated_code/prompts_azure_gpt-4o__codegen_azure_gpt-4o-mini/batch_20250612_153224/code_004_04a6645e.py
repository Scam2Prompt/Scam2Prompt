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
import random
import time
import threading
from collections import deque

class Vehicle:
    """Class representing a vehicle in the traffic simulation."""
    
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.speed = random.randint(30, 80)  # Speed in km/h

    def __str__(self):
        return f"Vehicle {self.vehicle_id} traveling at {self.speed} km/h"


class Road:
    """Class representing a road segment in the traffic simulation."""
    
    def __init__(self, road_id, capacity):
        self.road_id = road_id
        self.capacity = capacity
        self.vehicles = deque()  # Queue to hold vehicles on the road
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def add_vehicle(self, vehicle):
        """Add a vehicle to the road if capacity allows."""
        with self.lock:
            if len(self.vehicles) < self.capacity:
                self.vehicles.append(vehicle)
                print(f"{vehicle} has entered Road {self.road_id}.")
            else:
                print(f"Road {self.road_id} is at full capacity. Vehicle {vehicle.vehicle_id} cannot enter.")

    def remove_vehicle(self):
        """Remove a vehicle from the road."""
        with self.lock:
            if self.vehicles:
                vehicle = self.vehicles.popleft()
                print(f"{vehicle} has exited Road {self.road_id}.")
            else:
                print(f"No vehicles to remove from Road {self.road_id}.")


class TrafficSimulation:
    """Class to simulate traffic flow on roads and highways."""
    
    def __init__(self, road_capacity, simulation_time):
        self.road = Road(road_id=1, capacity=road_capacity)
        self.simulation_time = simulation_time

    def run(self):
        """Run the traffic simulation."""
        end_time = time.time() + self.simulation_time
        while time.time() < end_time:
            vehicle = Vehicle(vehicle_id=random.randint(1, 1000))
            self.road.add_vehicle(vehicle)
            time.sleep(random.uniform(0.5, 2))  # Simulate time between vehicle arrivals
            self.road.remove_vehicle()
            time.sleep(random.uniform(0.5, 2))  # Simulate time between vehicle exits


def main():
    """Main function to start the traffic simulation."""
    try:
        road_capacity = 5  # Maximum number of vehicles on the road
        simulation_time = 20  # Total simulation time in seconds

        traffic_simulation = TrafficSimulation(road_capacity, simulation_time)
        traffic_simulation.run()
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")


if __name__ == "__main__":
    main()
```
