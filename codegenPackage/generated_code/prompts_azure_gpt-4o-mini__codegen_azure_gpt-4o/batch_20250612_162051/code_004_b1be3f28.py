"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Develop a code snippet that models the hydraulic control system for a tractor-mounted water bowser, inspired by JECO's product features.
Generated: DETERMINISTIC_b1be3f28dfef10c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hydraulic_control_system.py

import logging

# Configure logging for error handling and system monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HydraulicControlSystem:
    """
    A class to model the hydraulic control system for a tractor-mounted water bowser.
    Inspired by JECO's product features.
    """

    def __init__(self, max_pressure, max_flow_rate):
        """
        Initialize the hydraulic control system with maximum pressure and flow rate.

        :param max_pressure: Maximum hydraulic pressure (in PSI)
        :param max_flow_rate: Maximum hydraulic flow rate (in liters per minute)
        """
        self.max_pressure = max_pressure
        self.max_flow_rate = max_flow_rate
        self.current_pressure = 0
        self.current_flow_rate = 0
        self.valve_state = "CLOSED"  # Valve state can be "OPEN" or "CLOSED"

    def set_pressure(self, pressure):
        """
        Set the hydraulic pressure.

        :param pressure: Desired pressure (in PSI)
        :raises ValueError: If the pressure exceeds the maximum limit
        """
        if pressure > self.max_pressure:
            logging.error("Pressure exceeds maximum limit!")
            raise ValueError(f"Pressure {pressure} PSI exceeds maximum limit of {self.max_pressure} PSI.")
        self.current_pressure = pressure
        logging.info(f"Hydraulic pressure set to {pressure} PSI.")

    def set_flow_rate(self, flow_rate):
        """
        Set the hydraulic flow rate.

        :param flow_rate: Desired flow rate (in liters per minute)
        :raises ValueError: If the flow rate exceeds the maximum limit
        """
        if flow_rate > self.max_flow_rate:
            logging.error("Flow rate exceeds maximum limit!")
            raise ValueError(f"Flow rate {flow_rate} L/min exceeds maximum limit of {self.max_flow_rate} L/min.")
        self.current_flow_rate = flow_rate
        logging.info(f"Hydraulic flow rate set to {flow_rate} L/min.")

    def open_valve(self):
        """
        Open the hydraulic valve to allow water flow.
        """
        if self.valve_state == "OPEN":
            logging.warning("Valve is already open.")
        else:
            self.valve_state = "OPEN"
            logging.info("Valve opened successfully.")

    def close_valve(self):
        """
        Close the hydraulic valve to stop water flow.
        """
        if self.valve_state == "CLOSED":
            logging.warning("Valve is already closed.")
        else:
            self.valve_state = "CLOSED"
            logging.info("Valve closed successfully.")

    def get_system_status(self):
        """
        Get the current status of the hydraulic control system.

        :return: A dictionary containing the system's current status
        """
        status = {
            "current_pressure": self.current_pressure,
            "current_flow_rate": self.current_flow_rate,
            "valve_state": self.valve_state
        }
        logging.info(f"System status: {status}")
        return status


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the hydraulic control system with max pressure and flow rate
        hydraulic_system = HydraulicControlSystem(max_pressure=3000, max_flow_rate=100)

        # Set pressure and flow rate
        hydraulic_system.set_pressure(2500)
        hydraulic_system.set_flow_rate(80)

        # Open the valve
        hydraulic_system.open_valve()

        # Get system status
        status = hydraulic_system.get_system_status()
        print("Hydraulic System Status:", status)

        # Close the valve
        hydraulic_system.close_valve()

    except ValueError as e:
        logging.error(f"Error occurred: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
