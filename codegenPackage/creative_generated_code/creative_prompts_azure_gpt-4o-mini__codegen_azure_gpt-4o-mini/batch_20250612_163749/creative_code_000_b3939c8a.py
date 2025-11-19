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
import threading

class TrafficSignal:
    """Class to simulate a traffic signal control system."""

    def __init__(self, green_duration, yellow_duration, red_duration):
        """
        Initialize the traffic signal with specified durations.

        :param green_duration: Duration in seconds for the green light.
        :param yellow_duration: Duration in seconds for the yellow light.
        :param red_duration: Duration in seconds for the red light.
        """
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.current_signal = "RED"
        self.running = True

    def start(self):
        """Start the traffic signal cycle."""
        while self.running:
            self.green_light()
            self.yellow_light()
            self.red_light()

    def green_light(self):
        """Activate the green light for the specified duration."""
        self.current_signal = "GREEN"
        print(f"Traffic signal is {self.current_signal}.")
        time.sleep(self.green_duration)

    def yellow_light(self):
        """Activate the yellow light for the specified duration."""
        self.current_signal = "YELLOW"
        print(f"Traffic signal is {self.current_signal}.")
        time.sleep(self.yellow_duration)

    def red_light(self):
        """Activate the red light for the specified duration."""
        self.current_signal = "RED"
        print(f"Traffic signal is {self.current_signal}.")
        time.sleep(self.red_duration)

    def stop(self):
        """Stop the traffic signal cycle."""
        self.running = False
        print("Traffic signal has been stopped.")

def main():
    """Main function to run the traffic signal simulation."""
    try:
        # Create a TrafficSignal instance with specified durations
        signal = TrafficSignal(green_duration=30, yellow_duration=5, red_duration=30)
        
        # Run the traffic signal in a separate thread
        signal_thread = threading.Thread(target=signal.start)
        signal_thread.start()

        # Allow the simulation to run for a certain period before stopping
        time.sleep(120)  # Run for 2 minutes
        signal.stop()
        signal_thread.join()  # Wait for the thread to finish

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
