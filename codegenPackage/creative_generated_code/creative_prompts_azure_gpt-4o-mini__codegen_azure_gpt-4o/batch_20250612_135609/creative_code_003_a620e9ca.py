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
# safety_mechanism.py
# Author: [Your Name]
# Date: [Today's Date]
# Description: Implements a safety mechanism for differential switches in an electrical project.

import time

class DifferentialSwitch:
    """
    Represents a differential switch object.
    This class simulates the behavior of a differential switch.
    """

    def __init__(self, name: str, threshold_current: float):
        """
        Initializes the differential switch with a name and a threshold current.
        :param name: Name of the differential switch (e.g., "Main Switch")
        :param threshold_current: Current threshold (in Amperes) that triggers the switch.
        """
        self.name = name
        self.threshold_current = threshold_current
        self.is_tripped = False

    def detect_fault(self, current: float) -> bool:
        """
        Simulates fault detection based on the current value.
        :param current: Current value (in Amperes).
        :return: True if fault detected, False otherwise.
        """
        if current > self.threshold_current:
            self.is_tripped = True
            return True
        return False

    def reset(self):
        """
        Resets the differential switch after a fault.
        """
        self.is_tripped = False


class ElectricalSafetySystem:
    """
    Represents the safety system that monitors and operates multiple differential switches.
    """

    def __init__(self):
        """
        Initializes the electrical safety system with an empty list of differential switches.
        """
        self.switches = []

    def add_switch(self, switch: DifferentialSwitch):
        """
        Adds a differential switch to the system.
        :param switch: Instance of DifferentialSwitch to add.
        """
        self.switches.append(switch)

    def monitor_system(self, current_values: dict):
        """
        Monitors the system for faults across all switches.
        :param current_values: Dictionary mapping switch names to current readings.
        """
        for switch in self.switches:
            current = current_values.get(switch.name, 0)
            if switch.detect_fault(current):
                print(f"ALERT: {switch.name} has tripped due to excessive current ({current}A).")
                print("Safety mechanism engaged! Please check the circuit.")
            else:
                print(f"{switch.name} is operating normally (Current: {current}A).")

    def reset_system(self):
        """
        Resets all differential switches in the system.
        """
        for switch in self.switches:
            if switch.is_tripped:
                switch.reset()
                print(f"{switch.name} has been reset.")


# Main Program
if __name__ == "__main__":
    try:
        # Create system instance
        safety_system = ElectricalSafetySystem()

        # Add differential switches to the system
        safety_system.add_switch(DifferentialSwitch(name="Main Switch", threshold_current=30.0))
        safety_system.add_switch(DifferentialSwitch(name="Sub Switch 1", threshold_current=20.0))
        safety_system.add_switch(DifferentialSwitch(name="Sub Switch 2", threshold_current=25.0))

        # Simulate monitoring loop
        while True:
            # Example current readings (replace with actual sensor values in real-world usage)
            current_readings = {
                "Main Switch": 15.0,
                "Sub Switch 1": 22.5,
                "Sub Switch 2": 35.0
            }

            print("\nMonitoring System...")
            safety_system.monitor_system(current_readings)

            # Simulate resetting the system (manual intervention in real usage)
            user_input = input("\nReset switches? (yes/no): ").strip().lower()
            if user_input == 'yes':
                safety_system.reset_system()

            # Wait before next monitoring cycle
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nSystem monitoring stopped.")
    except Exception as e:
        print(f"Error occurred: {e}")
```
