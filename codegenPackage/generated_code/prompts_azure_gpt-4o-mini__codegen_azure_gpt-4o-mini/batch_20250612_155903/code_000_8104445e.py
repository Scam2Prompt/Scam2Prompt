"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate code to implement a hydraulic tube expansion system using the specifications provided for the Hydraulic Expansion Powerpack from DBX Tools.
Generated: DETERMINISTIC_8104445e25213f1e
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicExpansionPowerpack:
    """
    A class to represent a hydraulic tube expansion system using the specifications
    provided for the Hydraulic Expansion Powerpack from DBX Tools.
    """

    def __init__(self, max_pressure: float, max_flow_rate: float):
        """
        Initializes the hydraulic powerpack with specified maximum pressure and flow rate.

        :param max_pressure: Maximum pressure in psi
        :param max_flow_rate: Maximum flow rate in GPM
        """
        self.max_pressure = max_pressure  # Maximum pressure in psi
        self.max_flow_rate = max_flow_rate  # Maximum flow rate in GPM
        self.current_pressure = 0.0  # Current pressure in psi
        self.current_flow_rate = 0.0  # Current flow rate in GPM

    def apply_pressure(self, pressure: float):
        """
        Applies pressure to the hydraulic system.

        :param pressure: Pressure to apply in psi
        :raises ValueError: If the pressure exceeds the maximum limit
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure exceeds maximum limit of {self.max_pressure} psi.")
        
        self.current_pressure = pressure
        print(f"Applied pressure: {self.current_pressure} psi")

    def set_flow_rate(self, flow_rate: float):
        """
        Sets the flow rate for the hydraulic system.

        :param flow_rate: Flow rate to set in GPM
        :raises ValueError: If the flow rate exceeds the maximum limit
        """
        if flow_rate < 0:
            raise ValueError("Flow rate cannot be negative.")
        if flow_rate > self.max_flow_rate:
            raise ValueError(f"Flow rate exceeds maximum limit of {self.max_flow_rate} GPM.")
        
        self.current_flow_rate = flow_rate
        print(f"Set flow rate: {self.current_flow_rate} GPM")

    def expand_tube(self):
        """
        Expands the tube using the current pressure and flow rate.
        Raises an error if the system is not properly configured.
        """
        if self.current_pressure == 0:
            raise RuntimeError("Cannot expand tube: Pressure is not applied.")
        if self.current_flow_rate == 0:
            raise RuntimeError("Cannot expand tube: Flow rate is not set.")
        
        # Simulate tube expansion process
        print(f"Expanding tube with pressure: {self.current_pressure} psi and flow rate: {self.current_flow_rate} GPM.")
        # Here you would implement the actual expansion logic

    def reset_system(self):
        """
        Resets the hydraulic system to its initial state.
        """
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0
        print("System reset: Pressure and flow rate set to 0.")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the hydraulic powerpack
        powerpack = HydraulicExpansionPowerpack(max_pressure=3000, max_flow_rate=10)

        # Configure the system
        powerpack.apply_pressure(2500)
        powerpack.set_flow_rate(5)

        # Perform tube expansion
        powerpack.expand_tube()

        # Reset the system after use
        powerpack.reset_system()

    except Exception as e:
        print(f"An error occurred: {e}")
```
