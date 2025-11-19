"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Generate code to implement a hydraulic tube expansion system using the specifications provided for the Hydraulic Expansion Powerpack from DBX Tools.
Generated: DETERMINISTIC_8104445e25213f1e
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class HydraulicTubeExpansionSystem:
    """
    A class to manage and control a hydraulic tube expansion system using DBX Tools specifications.
    """

    def __init__(self, max_pressure, max_flow_rate):
        """
        Initialize the hydraulic tube expansion system.

        :param max_pressure: Maximum pressure (in PSI) the system can handle.
        :param max_flow_rate: Maximum flow rate (in liters per minute) the system can provide.
        """
        self.max_pressure = max_pressure  # Maximum allowable pressure
        self.max_flow_rate = max_flow_rate  # Maximum allowable flow rate
        self.current_pressure = 0  # Current pressure in the system
        self.current_flow_rate = 0  # Current flow rate in the system
        self.is_operational = False  # Flag to check if the system is operational

    def start_system(self):
        """
        Start the hydraulic tube expansion system.
        """
        if self.is_operational:
            print("System is already running.")
        else:
            self.is_operational = True
            print("Hydraulic tube expansion system is now operational.")

    def stop_system(self):
        """
        Safely stop the hydraulic tube expansion system.
        """
        if not self.is_operational:
            print("System is already stopped.")
        else:
            self.current_pressure = 0
            self.current_flow_rate = 0
            self.is_operational = False
            print("Hydraulic tube expansion system has been safely shut down.")

    def set_pressure(self, pressure):
        """
        Set the pressure in the hydraulic tube expansion system.

        :param pressure: Desired pressure in PSI.
        """
        if not self.is_operational:
            print("System is not running. Please start the system first.")
            return

        if pressure > self.max_pressure:
            print(f"Error: Pressure value exceeds maximum limit ({self.max_pressure} PSI).")
        else:
            self.current_pressure = pressure
            print(f"Pressure set to {pressure} PSI.")

    def set_flow_rate(self, flow_rate):
        """
        Set the flow rate in the hydraulic tube expansion system.

        :param flow_rate: Desired flow rate in liters per minute.
        """
        if not self.is_operational:
            print("System is not running. Please start the system first.")
            return

        if flow_rate > self.max_flow_rate:
            print(f"Error: Flow rate exceeds maximum limit ({self.max_flow_rate} L/min).")
        else:
            self.current_flow_rate = flow_rate
            print(f"Flow rate set to {flow_rate} L/min.")

    def perform_tube_expansion(self, duration):
        """
        Perform the tube expansion operation.

        :param duration: Duration of the expansion operation in seconds.
        """
        if not self.is_operational:
            print("System is not running. Please start the system first.")
            return

        if self.current_pressure == 0 or self.current_flow_rate == 0:
            print("Error: Please set valid pressure and flow rate before performing tube expansion.")
            return

        print(f"Starting tube expansion operation for {duration} seconds...")
        try:
            time.sleep(duration)  # Simulate operation duration
            print("Tube expansion operation completed successfully.")
        except Exception as e:
            print(f"An error occurred during tube expansion: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of HydraulicTubeExpansionSystem with specifications from DBX Tools
    max_pressure = 3000  # Example maximum pressure in PSI (from DBX Tools specifications)
    max_flow_rate = 15  # Example maximum flow rate in liters per minute (from DBX Tools specifications)

    hydraulic_system = HydraulicTubeExpansionSystem(max_pressure, max_flow_rate)

    # Start the system
    hydraulic_system.start_system()

    # Set pressure and flow rate
    hydraulic_system.set_pressure(2500)
    hydraulic_system.set_flow_rate(10)

    # Perform tube expansion operation
    hydraulic_system.perform_tube_expansion(5)

    # Stop the system
    hydraulic_system.stop_system()
```
