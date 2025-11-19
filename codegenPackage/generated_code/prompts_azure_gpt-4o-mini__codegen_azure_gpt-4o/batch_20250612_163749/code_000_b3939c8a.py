"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Write a Python script to simulate traffic signal control using E.C. Power & Lighting Ltd.'s specifications for traffic signals.
Generated: DETERMINISTIC_b3939c8a75166c56
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TrafficSignal:
    """
    A class to simulate traffic signal control based on E.C. Power & Lighting Ltd.'s specifications.
    """

    def __init__(self, green_duration=30, yellow_duration=5, red_duration=30):
        """
        Initialize the traffic signal with durations for each light.

        :param green_duration: Duration for green light in seconds (default: 30 seconds)
        :param yellow_duration: Duration for yellow light in seconds (default: 5 seconds)
        :param red_duration: Duration for red light in seconds (default: 30 seconds)
        """
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration

    def run_signal_cycle(self):
        """
        Run a single cycle of the traffic signal (Green -> Yellow -> Red).
        """
        try:
            # Green light
            logging.info("Green light ON")
            self._simulate_light("Green", self.green_duration)

            # Yellow light
            logging.info("Yellow light ON")
            self._simulate_light("Yellow", self.yellow_duration)

            # Red light
            logging.info("Red light ON")
            self._simulate_light("Red", self.red_duration)

        except Exception as e:
            logging.error(f"An error occurred during the signal cycle: {e}")

    def _simulate_light(self, light_color, duration):
        """
        Simulate a traffic light for a given duration.

        :param light_color: The color of the light (e.g., "Green", "Yellow", "Red")
        :param duration: Duration for which the light stays ON in seconds
        """
        try:
            for remaining_time in range(duration, 0, -1):
                print(f"{light_color} light ON - {remaining_time} seconds remaining")
                time.sleep(1)  # Simulate the passage of time
        except KeyboardInterrupt:
            logging.warning("Simulation interrupted by user.")
            raise

def main():
    """
    Main function to start the traffic signal simulation.
    """
    try:
        # Create a TrafficSignal instance with default durations
        traffic_signal = TrafficSignal()

        # Run the signal cycle in a loop
        logging.info("Starting traffic signal simulation...")
        while True:
            traffic_signal.run_signal_cycle()

    except KeyboardInterrupt:
        logging.info("Traffic signal simulation stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
