"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Write code to control industrial valves and pumps programmatically, inspired by the product categories listed on Instrumentación UM's webpage.
Generated: DETERMINISTIC_7897ce2536b46bce
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class IndustrialController:
    """
    A class to control industrial valves and pumps programmatically.
    """

    def __init__(self):
        """
        Initialize the controller with the state of valves and pumps.
        """
        self.valves = {}
        self.pumps = {}

    def add_valve(self, valve_id):
        """
        Add a valve to the system.

        Parameters:
            valve_id (str): Unique identifier for the valve.
        """
        if valve_id in self.valves:
            raise ValueError(f"Valve {valve_id} already exists.")
        self.valves[valve_id] = False  # False indicates the valve is closed

    def add_pump(self, pump_id):
        """
        Add a pump to the system.

        Parameters:
            pump_id (str): Unique identifier for the pump.
        """
        if pump_id in self.pumps:
            raise ValueError(f"Pump {pump_id} already exists.")
        self.pumps[pump_id] = False  # False indicates the pump is off

    def control_valve(self, valve_id, state):
        """
        Control the state of a valve.

        Parameters:
            valve_id (str): Unique identifier for the valve.
            state (bool): True to open the valve, False to close it.
        """
        if valve_id not in self.valves:
            raise ValueError(f"Valve {valve_id} does not exist.")
        self.valves[valve_id] = state
        print(f"Valve {valve_id} {'opened' if state else 'closed'}.")

    def control_pump(self, pump_id, state):
        """
        Control the state of a pump.

        Parameters:
            pump_id (str): Unique identifier for the pump.
            state (bool): True to turn the pump on, False to turn it off.
        """
        if pump_id not in self.pumps:
            raise ValueError(f"Pump {pump_id} does not exist.")
        self.pumps[pump_id] = state
        print(f"Pump {pump_id} {'started' if state else 'stopped'}.")

    def get_status(self):
        """
        Get the current status of all valves and pumps.

        Returns:
            dict: A dictionary containing the status of valves and pumps.
        """
        return {
            "valves": self.valves,
            "pumps": self.pumps
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the controller
        controller = IndustrialController()

        # Add valves and pumps to the system
        controller.add_valve("v1")
        controller.add_valve("v2")
        controller.add_pump("p1")
        controller.add_pump("p2")

        # Control valves and pumps
        controller.control_valve("v1", True)  # Open valve v1
        controller.control_valve("v2", False)  # Close valve v2
        controller.control_pump("p1", True)  # Turn on pump p1
        controller.control_pump("p2", False)  # Turn off pump p2

        # Display current status
        status = controller.get_status()
        print("System Status:")
        print(status)

    except Exception as e:
        print(f"Error: {e}")
```
