"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Write Python code to simulate traffic signal timing and control, referencing the expertise of E.C. Power & Lighting Ltd. in traffic signal installations.
Generated: DETERMINISTIC_2e5f83f57a2d60b1
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
import random

class TrafficSignal:
    """
    A class to represent a traffic signal with timing control.
    """

    def __init__(self, green_duration=30, yellow_duration=5, red_duration=30):
        """
        Initializes the traffic signal with specified durations.

        :param green_duration: Duration for green light in seconds
        :param yellow_duration: Duration for yellow light in seconds
        :param red_duration: Duration for red light in seconds
        """
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.current_light = "RED"
        self.running = True

    def change_light(self):
        """
        Changes the traffic light in a loop: GREEN -> YELLOW -> RED.
        """
        while self.running:
            self.current_light = "GREEN"
            print(f"Traffic light is now {self.current_light}.")
            time.sleep(self.green_duration)

            self.current_light = "YELLOW"
            print(f"Traffic light is now {self.current_light}.")
            time.sleep(self.yellow_duration)

            self.current_light = "RED"
            print(f"Traffic light is now {self.current_light}.")
            time.sleep(self.red_duration)

    def start(self):
        """
        Starts the traffic signal in a separate thread.
        """
        signal_thread = threading.Thread(target=self.change_light)
        signal_thread.start()

    def stop(self):
        """
        Stops the traffic signal.
        """
        self.running = False
        print("Traffic signal has been stopped.")

def main():
    """
    Main function to simulate the traffic signal.
    """
    try:
        # Create a traffic signal instance with default timings
        traffic_signal = TrafficSignal()

        # Start the traffic signal
        traffic_signal.start()

        # Run the simulation for a random duration between 60 to 120 seconds
        simulation_duration = random.randint(60, 120)
        print(f"Traffic signal will run for {simulation_duration} seconds.")
        time.sleep(simulation_duration)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the traffic signal is stopped
        traffic_signal.stop()

if __name__ == "__main__":
    main()
```
