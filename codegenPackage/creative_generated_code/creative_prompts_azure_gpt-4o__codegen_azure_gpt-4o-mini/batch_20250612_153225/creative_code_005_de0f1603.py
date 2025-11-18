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
import random
from threading import Thread, Lock
from typing import List, Dict

class TrafficSignal:
    """Class representing a traffic signal with adaptive timing."""
    
    def __init__(self, id: str):
        self.id = id
        self.green_time = 30  # Default green light duration in seconds
        self.red_time = 30    # Default red light duration in seconds
        self.lock = Lock()

    def set_timing(self, green_time: int, red_time: int):
        """Set custom timing for green and red lights."""
        with self.lock:
            self.green_time = green_time
            self.red_time = red_time

    def run_signal(self):
        """Run the traffic signal in an infinite loop."""
        while True:
            self.activate_green_light()
            self.activate_red_light()

    def activate_green_light(self):
        """Simulate the green light activation."""
        print(f"Signal {self.id}: Green light ON for {self.green_time} seconds.")
        time.sleep(self.green_time)

    def activate_red_light(self):
        """Simulate the red light activation."""
        print(f"Signal {self.id}: Red light ON for {self.red_time} seconds.")
        time.sleep(self.red_time)


class AdaptiveTrafficControlSystem:
    """Class for managing multiple traffic signals in an adaptive manner."""
    
    def __init__(self, signals: List[TrafficSignal]):
        self.signals = signals
        self.active_signals = {}
        self.lock = Lock()

    def start_system(self):
        """Start the adaptive traffic control system."""
        for signal in self.signals:
            thread = Thread(target=signal.run_signal)
            thread.daemon = True  # Allow the program to exit even if threads are running
            thread.start()
            self.active_signals[signal.id] = thread

    def optimize_traffic(self):
        """Optimize traffic signal timings based on simulated traffic conditions."""
        while True:
            # Simulate traffic data collection
            traffic_data = self.collect_traffic_data()
            self.adjust_signal_timings(traffic_data)
            time.sleep(60)  # Optimize every minute

    def collect_traffic_data(self) -> Dict[str, int]:
        """Simulate the collection of traffic data."""
        # In a real scenario, this data would come from sensors
        return {signal.id: random.randint(5, 50) for signal in self.signals}

    def adjust_signal_timings(self, traffic_data: Dict[str, int]):
        """Adjust signal timings based on traffic data."""
        with self.lock:
            for signal_id, vehicle_count in traffic_data.items():
                signal = next((s for s in self.signals if s.id == signal_id), None)
                if signal:
                    # Adjust timings based on vehicle count
                    green_time = min(60, max(30, vehicle_count))  # Example adjustment logic
                    signal.set_timing(green_time, 60)  # Maintain a red time of 60 seconds

    def stop_system(self):
        """Stop all traffic signals safely."""
        for signal in self.signals:
            signal.lock.acquire()  # Prevent any timing changes during shutdown
        print("Traffic control system is shutting down.")


# Example usage
if __name__ == "__main__":
    # Create traffic signals for a simple intersection
    signals = [TrafficSignal(id=f"Signal-{i}") for i in range(4)]
    atcc = AdaptiveTrafficControlSystem(signals)

    try:
        atcc.start_system()
        atcc.optimize_traffic()
    except KeyboardInterrupt:
        atcc.stop_system()
```
