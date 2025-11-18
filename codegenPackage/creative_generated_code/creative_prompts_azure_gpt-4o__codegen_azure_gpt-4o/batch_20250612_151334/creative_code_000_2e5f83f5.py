"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Write Python code to simulate traffic signal timing and control, referencing the expertise of E.C. Power & Lighting Ltd. in traffic signal installations.
Generated: DETERMINISTIC_2e5f83f57a2d60b1
Batch ID: 20250612_151334
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

class TrafficSignal:
    """
    A class to simulate traffic signal timing and control.
    """
    def __init__(self, location, green_duration=30, yellow_duration=5, red_duration=30):
        """
        Initialize the traffic signal with durations for each signal light.

        :param location: String, location of the signal
        :param green_duration: Integer, duration of green light in seconds (default: 30)
        :param yellow_duration: Integer, duration of yellow light in seconds (default: 5)
        :param red_duration: Integer, duration of red light in seconds (default: 30)
        """
        self.location = location
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.current_light = "RED"
        self.running = False

    def change_light(self):
        """
        Change the traffic signal light based on the timing cycle.
        """
        while self.running:
            self.current_light = "GREEN"
            print(f"{self.location} Signal: GREEN light on for {self.green_duration} seconds.")
            time.sleep(self.green_duration)

            self.current_light = "YELLOW"
            print(f"{self.location} Signal: YELLOW light on for {self.yellow_duration} seconds.")
            time.sleep(self.yellow_duration)

            self.current_light = "RED"
            print(f"{self.location} Signal: RED light on for {self.red_duration} seconds.")
            time.sleep(self.red_duration)

    def start(self):
        """
        Start the traffic signal simulation.
        """
        if not self.running:
            self.running = True
            print(f"Starting traffic signal at {self.location}.")
            self.signal_thread = threading.Thread(target=self.change_light)
            self.signal_thread.start()

    def stop(self):
        """
        Stop the traffic signal simulation.
        """
        if self.running:
            print(f"Stopping traffic signal at {self.location}.")
            self.running = False
            self.signal_thread.join()

    def get_status(self):
        """
        Get the current status of the traffic signal.

        :return: String, current light
        """
        return self.current_light


if __name__ == "__main__":
    try:
        # Initialize a traffic signal system
        traffic_signal = TrafficSignal(location="Main Street", green_duration=20, yellow_duration=4, red_duration=20)

        # Start the traffic signal simulation
        traffic_signal.start()

        # Let the simulation run for a while (e.g., 1 minute)
        time.sleep(60)

        # Stop the traffic signal simulation
        traffic_signal.stop()

    except KeyboardInterrupt:
        # Gracefully handle a keyboard interrupt (CTRL+C)
        print("\nKeyboard Interrupt detected. Stopping simulation.")
        traffic_signal.stop()
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        traffic_signal.stop()
```
