"""
Generated Code Metadata:
========================
Original URL: https://polystack.tech
Prompt: Write code to implement an Adaptive Traffic Control System (ATCC) inspired by Polystack Technologies' industry solutions. Include features for real-time traffic optimization.
Generated: DETERMINISTIC_de0f1603e9b17c0b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import List, Dict

class TrafficSignal:
    def __init__(self, intersection_id: str):
        """
        Initialize a traffic signal at a given intersection.

        :param intersection_id: Unique identifier for the intersection
        """
        self.intersection_id = intersection_id
        self.green_time = 30  # Default green light duration in seconds
        self.red_time = 30    # Default red light duration in seconds
        self.current_state = 'RED'  # Initial state of the signal

    def change_signal(self):
        """
        Change the traffic signal state from RED to GREEN or vice versa.
        """
        if self.current_state == 'RED':
            self.current_state = 'GREEN'
            print(f"Signal at {self.intersection_id} is now GREEN for {self.green_time} seconds.")
            time.sleep(self.green_time)
        else:
            self.current_state = 'RED'
            print(f"Signal at {self.intersection_id} is now RED for {self.red_time} seconds.")
            time.sleep(self.red_time)

class TrafficSensor:
    def __init__(self, intersection_id: str):
        """
        Initialize a traffic sensor at a given intersection.

        :param intersection_id: Unique identifier for the intersection
        """
        self.intersection_id = intersection_id

    def get_traffic_data(self) -> int:
        """
        Simulate getting real-time traffic data.

        :return: Number of vehicles detected
        """
        # Simulating traffic data with random values
        vehicle_count = random.randint(0, 100)
        print(f"Traffic data for {self.intersection_id}: {vehicle_count} vehicles detected.")
        return vehicle_count

class AdaptiveTrafficControlSystem:
    def __init__(self):
        """
        Initialize the Adaptive Traffic Control System with traffic signals and sensors.
        """
        self.signals: Dict[str, TrafficSignal] = {}
        self.sensors: Dict[str, TrafficSensor] = {}

    def add_intersection(self, intersection_id: str):
        """
        Add a new intersection with a traffic signal and sensor.

        :param intersection_id: Unique identifier for the intersection
        """
        self.signals[intersection_id] = TrafficSignal(intersection_id)
        self.sensors[intersection_id] = TrafficSensor(intersection_id)

    def optimize_traffic(self):
        """
        Optimize traffic signals based on real-time traffic data.
        """
        for intersection_id in self.signals.keys():
            vehicle_count = self.sensors[intersection_id].get_traffic_data()
            # Adjust green time based on vehicle count
            if vehicle_count > 50:
                self.signals[intersection_id].green_time = 60  # Increase green time for heavy traffic
            else:
                self.signals[intersection_id].green_time = 30  # Default green time

            # Change the signal state
            self.signals[intersection_id].change_signal()

    def run(self):
        """
        Run the Adaptive Traffic Control System in a loop.
        """
        try:
            while True:
                self.optimize_traffic()
                time.sleep(5)  # Wait before the next optimization cycle
        except KeyboardInterrupt:
            print("Traffic control system stopped.")

if __name__ == "__main__":
    # Create an instance of the Adaptive Traffic Control System
    atcc = AdaptiveTrafficControlSystem()
    
    # Add intersections to the system
    atcc.add_intersection("Intersection_1")
    atcc.add_intersection("Intersection_2")
    
    # Start the traffic control system
    atcc.run()
```
