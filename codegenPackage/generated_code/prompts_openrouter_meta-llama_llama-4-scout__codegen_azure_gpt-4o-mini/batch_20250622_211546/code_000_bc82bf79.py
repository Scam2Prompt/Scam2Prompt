"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Design a hydraulic tube expansion system for a boiler tube expander, including a list of required components and specifications.
Generated: DETERMINISTIC_bc82bf79f0793462
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicTubeExpander:
    """
    A class to represent a hydraulic tube expansion system for a boiler tube expander.
    """

    def __init__(self, max_pressure: float, max_expansion: float):
        """
        Initializes the hydraulic tube expander with specified maximum pressure and expansion.

        :param max_pressure: Maximum pressure the system can handle in psi.
        :param max_expansion: Maximum expansion the system can achieve in inches.
        """
        self.max_pressure = max_pressure
        self.max_expansion = max_expansion
        self.current_pressure = 0.0
        self.current_expansion = 0.0

    def apply_pressure(self, pressure: float):
        """
        Applies pressure to the hydraulic system.

        :param pressure: Pressure to apply in psi.
        :raises ValueError: If the pressure exceeds the maximum limit.
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure exceeds maximum limit of {self.max_pressure} psi.")
        
        self.current_pressure = pressure
        print(f"Applied pressure: {self.current_pressure} psi")

    def expand_tube(self, expansion: float):
        """
        Expands the tube by a specified amount.

        :param expansion: Amount to expand the tube in inches.
        :raises ValueError: If the expansion exceeds the maximum limit.
        """
        if expansion < 0:
            raise ValueError("Expansion cannot be negative.")
        if self.current_expansion + expansion > self.max_expansion:
            raise ValueError(f"Expansion exceeds maximum limit of {self.max_expansion} inches.")
        
        self.current_expansion += expansion
        print(f"Current tube expansion: {self.current_expansion} inches")

    def reset_system(self):
        """
        Resets the hydraulic system to its initial state.
        """
        self.current_pressure = 0.0
        self.current_expansion = 0.0
        print("System reset to initial state.")

    def get_status(self):
        """
        Returns the current status of the hydraulic tube expander.

        :return: A dictionary containing the current pressure and expansion.
        """
        return {
            "current_pressure": self.current_pressure,
            "current_expansion": self.current_expansion
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a hydraulic tube expander with specified limits
        expander = HydraulicTubeExpander(max_pressure=3000, max_expansion=0.5)

        # Apply pressure and expand the tube
        expander.apply_pressure(2500)
        expander.expand_tube(0.2)

        # Get the current status of the expander
        status = expander.get_status()
        print(f"Expander Status: {status}")

        # Reset the system
        expander.reset_system()

    except ValueError as e:
        print(f"Error: {e}")
```
