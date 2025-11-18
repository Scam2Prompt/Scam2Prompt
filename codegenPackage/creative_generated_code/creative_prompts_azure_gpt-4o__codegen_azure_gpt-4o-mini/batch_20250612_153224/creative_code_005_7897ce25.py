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
import logging
from typing import List, Dict

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Valve:
    """Class to represent an industrial valve."""

    def __init__(self, id: int, state: str = "closed"):
        """Initialize a valve with an ID and its state (open/closed)."""
        self.id = id
        self.state = state  # Initial state

    def open(self):
        """Open the valve."""
        if self.state != "open":
            self.state = "open"
            logging.info(f"Valve {self.id} opened.")
        else:
            logging.warning(f"Valve {self.id} is already open.")

    def close(self):
        """Close the valve."""
        if self.state != "closed":
            self.state = "closed"
            logging.info(f"Valve {self.id} closed.")
        else:
            logging.warning(f"Valve {self.id} is already closed.")

class Pump:
    """Class to represent an industrial pump."""

    def __init__(self, id: int, state: str = "stopped"):
        """Initialize a pump with an ID and its state (running/stopped)."""
        self.id = id
        self.state = state  # Initial state

    def start(self):
        """Start the pump."""
        if self.state != "running":
            self.state = "running"
            logging.info(f"Pump {self.id} started.")
        else:
            logging.warning(f"Pump {self.id} is already running.")

    def stop(self):
        """Stop the pump."""
        if self.state != "stopped":
            self.state = "stopped"
            logging.info(f"Pump {self.id} stopped.")
        else:
            logging.warning(f"Pump {self.id} is already stopped.")

class ControlSystem:
    """Class to manage a collection of valves and pumps."""

    def __init__(self):
        """Initialize the control system with empty lists for valves and pumps."""
        self.valves: List[Valve] = []
        self.pumps: List[Pump] = []

    def add_valve(self, valve: Valve):
        """Add a valve to the control system."""
        self.valves.append(valve)
        logging.info(f"Added valve {valve.id} to the control system.")

    def add_pump(self, pump: Pump):
        """Add a pump to the control system."""
        self.pumps.append(pump)
        logging.info(f"Added pump {pump.id} to the control system.")

    def operate_valve(self, valve_id: int, action: str):
        """Operate a valve by opening or closing it based on the action."""
        try:
            valve = next(v for v in self.valves if v.id == valve_id)
            if action == "open":
                valve.open()
            elif action == "close":
                valve.close()
            else:
                logging.error("Invalid action for valve operation.")
        except StopIteration:
            logging.error(f"Valve {valve_id} not found in the control system.")

    def operate_pump(self, pump_id: int, action: str):
        """Operate a pump by starting or stopping it based on the action."""
        try:
            pump = next(p for p in self.pumps if p.id == pump_id)
            if action == "start":
                pump.start()
            elif action == "stop":
                pump.stop()
            else:
                logging.error("Invalid action for pump operation.")
        except StopIteration:
            logging.error(f"Pump {pump_id} not found in the control system.")

# Example usage (this part would typically be in a separate module or script):

if __name__ == "__main__":
    # Initialize control system
    control_system = ControlSystem()

    # Create and add valves
    valve1 = Valve(1)
    valve2 = Valve(2)
    control_system.add_valve(valve1)
    control_system.add_valve(valve2)

    # Create and add pumps
    pump1 = Pump(1)
    pump2 = Pump(2)
    control_system.add_pump(pump1)
    control_system.add_pump(pump2)

    # Operate valves and pumps
    control_system.operate_valve(1, "open")
    control_system.operate_valve(2, "close")
    control_system.operate_pump(1, "start")
    control_system.operate_pump(2, "stop")
```
