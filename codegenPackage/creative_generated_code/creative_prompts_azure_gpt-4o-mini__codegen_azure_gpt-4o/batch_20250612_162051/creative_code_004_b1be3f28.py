"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Develop a code snippet that models the hydraulic control system for a tractor-mounted water bowser, inspired by JECO's product features.
Generated: DETERMINISTIC_b1be3f28dfef10c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for modeling the hydraulic control system of a tractor-mounted water bowser. It adheres to your requirements:

```python
import logging

# Configure logging to capture debug messages and errors
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class HydraulicControlSystem:
    """
    Class to model the hydraulic control system for a tractor-mounted water bowser.
    """

    def __init__(self, max_pressure: float, max_flow_rate: float):
        """
        Initialize the hydraulic control system with key parameters.
        
        :param max_pressure: Maximum allowable pressure in the system (in bars).
        :param max_flow_rate: Maximum allowable flow rate (in liters per minute).
        """
        self.max_pressure = max_pressure  # Maximum pressure (bars)
        self.max_flow_rate = max_flow_rate  # Maximum flow rate (L/min)
        self.current_pressure = 0.0  # Current system pressure (bars)
        self.current_flow_rate = 0.0  # Current flow rate (L/min)
        self.valve_state = "CLOSED"  # Valve state: OPEN or CLOSED

    def open_valve(self):
        """
        Opens the hydraulic control valve.
        """
        if self.valve_state == "OPEN":
            logging.warning("Valve is already open.")
            return
        self.valve_state = "OPEN"
        logging.info("Valve opened successfully.")

    def close_valve(self):
        """
        Closes the hydraulic control valve.
        """
        if self.valve_state == "CLOSED":
            logging.warning("Valve is already closed.")
            return
        self.valve_state = "CLOSED"
        logging.info("Valve closed successfully.")

    def set_pressure(self, pressure: float):
        """
        Set the hydraulic system pressure.
        
        :param pressure: Desired pressure in bars.
        :raises ValueError: If the pressure exceeds the maximum allowable limit.
        """
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure exceeds maximum allowable limit of {self.max_pressure} bars.")
        self.current_pressure = pressure
        logging.info(f"Pressure set to {pressure} bars.")

    def set_flow_rate(self, flow_rate: float):
        """
        Set the hydraulic system flow rate.
        
        :param flow_rate: Desired flow rate in liters per minute.
        :raises ValueError: If the flow rate exceeds the maximum allowable limit.
        """
        if flow_rate > self.max_flow_rate:
            raise ValueError(f"Flow rate exceeds maximum allowable limit of {self.max_flow_rate} L/min.")
        self.current_flow_rate = flow_rate
        logging.info(f"Flow rate set to {flow_rate} L/min.")

    def get_status(self):
        """
        Retrieves the current status of the hydraulic control system.
        
        :return: Dictionary containing current pressure, flow rate, and valve state.
        """
        status = {
            "Current Pressure (bars)": self.current_pressure,
            "Current Flow Rate (L/min)": self.current_flow_rate,
            "Valve State": self.valve_state
        }
        logging.debug(f"System status: {status}")
        return status


def main():
    """
    Main function to demonstrate the usage of the HydraulicControlSystem class.
    """
    try:
        # Initialize the hydraulic control system with maximum parameters
        bowser_system = HydraulicControlSystem(max_pressure=300, max_flow_rate=500)

        # Set system parameters
        bowser_system.set_pressure(250)
        bowser_system.set_flow_rate(400)

        # Open the valve
        bowser_system.open_valve()

        # Retrieve and print system status
        status = bowser_system.get_status()
        print("Hydraulic Control System Status:")
        for key, value in status.items():
            print(f"{key}: {value}")

        # Close the valve
        bowser_system.close_valve()

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
