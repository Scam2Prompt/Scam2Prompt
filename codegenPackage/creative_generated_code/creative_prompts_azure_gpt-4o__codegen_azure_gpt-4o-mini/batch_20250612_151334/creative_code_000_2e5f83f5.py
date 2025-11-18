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
    A class to simulate a traffic signal with timing control.
    Each signal can be in one of three states: RED, GREEN, or YELLOW.
    The timing for each state can be customized.
    """

    def __init__(self, green_time=30, yellow_time=5, red_time=30):
        """
        Initializes the TrafficSignal with the specified timing for each state.

        Parameters:
        green_time (int): Duration for the green light in seconds.
        yellow_time (int): Duration for the yellow light in seconds.
        red_time (int): Duration for the red light in seconds.
        """
        self.green_time = green_time
        self.yellow_time = yellow_time
        self.red_time = red_time
        self.current_state = "RED"
        self.running = False

    def start(self):
        """Starts the traffic signal cycle in a separate thread."""
        self.running = True
        threading.Thread(target=self.run_signal_cycle, daemon=True).start()

    def stop(self):
        """Stops the traffic signal cycle."""
        self.running = False

    def run_signal_cycle(self):
        """Main loop to control the traffic signal states."""
        while self.running:
            self.change_state("GREEN", self.green_time)
            self.change_state("YELLOW", self.yellow_time)
            self.change_state("RED", self.red_time)

    def change_state(self, new_state, duration):
        """
        Changes the current state of the traffic signal and waits for the specified duration.

        Parameters:
        new_state (str): The new state of the traffic signal (GREEN, YELLOW, RED).
        duration (int): The duration to stay in the new state.
        """
        self.current_state = new_state
        print(f"Signal is now {self.current_state}. Duration: {duration} seconds.")
        time.sleep(duration)

    def get_current_state(self):
        """Returns the current state of the traffic signal."""
        return self.current_state


if __name__ == "__main__":
    # Example of creating and running a traffic signal
    try:
        signal = TrafficSignal(green_time=30, yellow_time=5, red_time=30)
        signal.start()

        # Run the signal for a specific period or until user interruption
        time.sleep(120)  # Run for 2 minutes
    except KeyboardInterrupt:
        print("Traffic signal simulation interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        signal.stop()
        print("Traffic signal simulation stopped.")
```
