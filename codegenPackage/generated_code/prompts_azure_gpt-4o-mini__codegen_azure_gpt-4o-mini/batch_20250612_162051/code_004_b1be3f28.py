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
class HydraulicControlSystem:
    """
    A class to model the hydraulic control system for a tractor-mounted water bowser.
    This system controls the flow and pressure of water for efficient operation.
    """

    def __init__(self, max_pressure: float, max_flow_rate: float):
        """
        Initializes the hydraulic control system with specified maximum pressure and flow rate.

        :param max_pressure: Maximum pressure in the hydraulic system (in psi).
        :param max_flow_rate: Maximum flow rate of water (in gallons per minute).
        """
        self.max_pressure = max_pressure
        self.max_flow_rate = max_flow_rate
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0

    def set_pressure(self, pressure: float):
        """
        Sets the current pressure of the hydraulic system.

        :param pressure: Desired pressure to set (in psi).
        :raises ValueError: If the pressure exceeds maximum limits.
        """
        if pressure < 0 or pressure > self.max_pressure:
            raise ValueError(f"Pressure must be between 0 and {self.max_pressure} psi.")
        self.current_pressure = pressure

    def set_flow_rate(self, flow_rate: float):
        """
        Sets the current flow rate of water.

        :param flow_rate: Desired flow rate to set (in gallons per minute).
        :raises ValueError: If the flow rate exceeds maximum limits.
        """
        if flow_rate < 0 or flow_rate > self.max_flow_rate:
            raise ValueError(f"Flow rate must be between 0 and {self.max_flow_rate} GPM.")
        self.current_flow_rate = flow_rate

    def operate(self):
        """
        Operates the hydraulic system, simulating the flow of water based on current settings.
        """
        if self.current_pressure == 0 or self.current_flow_rate == 0:
            print("Hydraulic system is not operational. Please set pressure and flow rate.")
            return

        print(f"Operating hydraulic system at {self.current_pressure} psi and {self.current_flow_rate} GPM.")

    def reset_system(self):
        """
        Resets the hydraulic system to its initial state.
        """
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0
        print("Hydraulic system has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a hydraulic control system with specified limits
        hydraulic_system = HydraulicControlSystem(max_pressure=3000, max_flow_rate=100)

        # Set pressure and flow rate
        hydraulic_system.set_pressure(1500)
        hydraulic_system.set_flow_rate(50)

        # Operate the system
        hydraulic_system.operate()

        # Reset the system
        hydraulic_system.reset_system()

    except ValueError as e:
        print(f"Error: {e}")
```
