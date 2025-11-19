"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Write a Python script to simulate traffic signal control using E.C. Power & Lighting Ltd.'s specifications for traffic signals.
Generated: DETERMINISTIC_b3939c8a75166c56
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class TrafficSignal:
    """
    A class to simulate traffic signal control.
    Based on E.C. Power & Lighting Ltd.'s specifications.
    """

    def __init__(self, green_duration=30, yellow_duration=5, red_duration=30):
        """
        Initializes the traffic signal durations.
        
        Args:
            green_duration (int): Duration for green light in seconds.
            yellow_duration (int): Duration for yellow light in seconds.
            red_duration (int): Duration for red light in seconds.
        """
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration

    def _display_signal(self, color):
        """
        Displays the traffic signal light with the given color.
        
        Args:
            color (str): The color of the signal light (green, yellow, red).
        """
        print(f"Signal is now {color.upper()}")

    def _simulate_light(self, color, duration):
        """
        Simulates the traffic signal light for a given duration.
        
        Args:
            color (str): The color of the signal light (green, yellow, red).
            duration (int): Duration for which the light stays active in seconds.
        """
        self._display_signal(color)
        time.sleep(duration)  # Simulating the light duration

    def run_signal_cycle(self):
        """
        Runs a single cycle of the traffic signal: green -> yellow -> red.
        """
        try:
            self._simulate_light("green", self.green_duration)
            self._simulate_light("yellow", self.yellow_duration)
            self._simulate_light("red", self.red_duration)
        except KeyboardInterrupt:
            print("\nTraffic signal simulation interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def start(self):
        """
        Starts the traffic signal simulation in an infinite loop.
        """
        print("Starting traffic signal simulation. Press Ctrl+C to stop.")
        try:
            while True:
                self.run_signal_cycle()
        except KeyboardInterrupt:
            print("\nTraffic signal simulation stopped.")


if __name__ == "__main__":
    # Initialize traffic signal with default durations
    traffic_signal = TrafficSignal()

    # Start the simulation
    traffic_signal.start()
```
