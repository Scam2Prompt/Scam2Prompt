"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polystack.tech
Prompt: Write code to implement an Adaptive Traffic Control System (ATCC) inspired by Polystack Technologies' industry solutions. Include features for real-time traffic optimization.
Generated: DETERMINISTIC_de0f1603e9b17c0b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
import random

# Adaptive Traffic Control System (ATCC)
class AdaptiveTrafficControlSystem:
    def __init__(self):
        # Initialize traffic data
        self.traffic_data = {
            "North": 0,
            "South": 0,
            "East": 0,
            "West": 0
        }
        # Default traffic signal duration (in seconds)
        self.signal_duration = {
            "North": 15,
            "South": 15,
            "East": 15,
            "West": 15
        }
        # Lock for thread-safe operations
        self.lock = threading.Lock()

    def collect_traffic_data(self):
        """Simulate real-time traffic data collection."""
        while True:
            with self.lock:
                # Generate synthetic traffic data for demonstration purposes
                for direction in self.traffic_data:
                    # Randomly simulate the number of vehicles in each direction
                    self.traffic_data[direction] = random.randint(0, 50)
            time.sleep(2)  # Simulate data collection every 2 seconds

    def optimize_signal_duration(self):
        """Optimize signal durations based on real-time traffic data."""
        while True:
            with self.lock:
                total_vehicles = sum(self.traffic_data.values())
                if total_vehicles > 0:
                    # Adjust signal duration proportionally to traffic density
                    for direction in self.signal_duration:
                        self.signal_duration[direction] = max(
                            10,  # Minimum signal duration
                            int((self.traffic_data[direction] / total_vehicles) * 60)  # Proportional duration
                        )
                else:
                    # Default signal duration if no vehicles are detected
                    for direction in self.signal_duration:
                        self.signal_duration[direction] = 15
            time.sleep(5)  # Update signal durations every 5 seconds

    def manage_traffic_signals(self):
        """Control traffic signals based on optimized durations."""
        while True:
            for direction in self.signal_duration:
                with self.lock:
                    duration = self.signal_duration[direction]
                print(f"Green light for {direction} - Duration: {duration} seconds")
                time.sleep(duration)  # Simulate the green signal duration
                print(f"Red light for {direction}")

    def start_system(self):
        """Start the Adaptive Traffic Control System."""
        try:
            # Create threads for data collection, optimization, and signal management
            data_thread = threading.Thread(target=self.collect_traffic_data, daemon=True)
            optimization_thread = threading.Thread(target=self.optimize_signal_duration, daemon=True)
            signal_thread = threading.Thread(target=self.manage_traffic_signals, daemon=True)

            # Start threads
            data_thread.start()
            optimization_thread.start()
            signal_thread.start()

            # Keep the main thread alive
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down the Adaptive Traffic Control System...")
        except Exception as e:
            print(f"Error occurred: {e}")

# Main entry point
if __name__ == "__main__":
    atcc = AdaptiveTrafficControlSystem()
    atcc.start_system()
```
