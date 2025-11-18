"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Write code to simulate traffic flow on roads and highways, referencing the turnkey road construction services offered by Bismillah Traders.
Generated: DETERMINISTIC_04a6645e30613153
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading
from collections import deque

# Constants for simulation
NUM_ROADS = 5
MAX_CARS_ON_ROAD = 10
SIMULATION_TIME = 60  # seconds
CAR_ARRIVAL_INTERVAL = 1  # seconds

class Road:
    """Class representing a road with traffic flow."""
    
    def __init__(self, road_id):
        self.road_id = road_id
        self.cars = deque()  # Using deque for efficient car management
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def add_car(self, car):
        """Add a car to the road if there is space."""
        with self.lock:  # Ensure the operation is thread-safe
            if len(self.cars) < MAX_CARS_ON_ROAD:
                self.cars.append(car)
                print(f"Car {car} added to Road {self.road_id}.")
            else:
                print(f"Road {self.road_id} is full. Car {car} cannot enter.")

    def remove_car(self):
        """Remove a car from the road if available."""
        with self.lock:
            if self.cars:
                car = self.cars.popleft()
                print(f"Car {car} left Road {self.road_id}.")
                return car
            else:
                print(f"Road {self.road_id} is empty. No cars to remove.")
                return None

class TrafficSimulator:
    """Class to simulate traffic flow on multiple roads."""
    
    def __init__(self):
        self.roads = [Road(i) for i in range(NUM_ROADS)]
        self.simulation_time = SIMULATION_TIME

    def simulate_traffic(self):
        """Start the traffic simulation."""
        start_time = time.time()
        while (time.time() - start_time) < self.simulation_time:
            for road in self.roads:
                # Randomly decide whether to add or remove a car
                if random.choice([True, False]):
                    car_id = random.randint(1000, 9999)
                    road.add_car(car_id)

                road.remove_car()

            time.sleep(CAR_ARRIVAL_INTERVAL)  # Wait before the next iteration

def main():
    """Main function to run the traffic simulation."""
    try:
        simulator = TrafficSimulator()
        print("Starting traffic simulation...")
        simulator.simulate_traffic()
        print("Traffic simulation completed.")
    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    main()
```
