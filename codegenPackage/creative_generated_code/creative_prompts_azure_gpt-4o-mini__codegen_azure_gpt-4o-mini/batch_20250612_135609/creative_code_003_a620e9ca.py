"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: How can I implement a safety mechanism using differential switches like those available at Miraya Electric S.A.C. in an electrical project?
Generated: DETERMINISTIC_a620e9cabb13671e
Batch ID: 20250612_135609
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

class DifferentialSwitch:
    """Class to simulate a differential switch for electrical safety."""

    def __init__(self, threshold: float):
        """
        Initialize the DifferentialSwitch with a specified current threshold.

        :param threshold: The current threshold for triggering the switch (in Amperes).
        """
        self.threshold = threshold
        self.is_tripped = False

    def monitor_current(self, current: float):
        """
        Monitor the current passing through the switch and trip if it exceeds the threshold.

        :param current: The current flowing through the switch (in Amperes).
        """
        if current > self.threshold:
            self.trip()
        else:
            self.reset()

    def trip(self):
        """Trip the switch to disconnect the circuit."""
        self.is_tripped = True
        print("Differential switch tripped! Current exceeds threshold.")

    def reset(self):
        """Reset the switch status if current is within the safe limit."""
        if self.is_tripped:
            self.is_tripped = False
            print("Differential switch reset. Current is within safe limits.")

def simulate_current_flow(differential_switch: DifferentialSwitch):
    """
    Simulate random current flow in an electrical project.

    :param differential_switch: An instance of DifferentialSwitch to monitor.
    """
    try:
        while True:
            # Simulate random current flow (in Amperes)
            current_flow = random.uniform(0, 15)  # Simulated current between 0 and 15 Amperes
            print(f"Current Flow: {current_flow:.2f} A")
            differential_switch.monitor_current(current_flow)

            # Introduce a delay for simulation
            time.sleep(1)

    except KeyboardInterrupt:
        print("Simulation terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set the current threshold for the differential switch
    CURRENT_THRESHOLD = 10.0  # Threshold in Amperes

    # Create a differential switch instance
    differential_switch = DifferentialSwitch(threshold=CURRENT_THRESHOLD)

    # Start simulating current flow
    simulate_current_flow(differential_switch)
```
