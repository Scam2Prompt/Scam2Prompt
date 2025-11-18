"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Write Python code to simulate the operation of a hydraulic tube expansion system, referencing the features of the Hydraulic Expansion Powerpack (HEP 500) described on the DBX Tools website.
Generated: DETERMINISTIC_21833d51d3583d92
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class HydraulicExpansionPowerpack:
    """
    A class to simulate the operation of a Hydraulic Tube Expansion System.
    This simulates the operation of the HEP 500 model.
    """

    def __init__(self, max_pressure: float, max_expansion: float):
        """
        Initializes the HydraulicExpansionPowerpack instance.

        :param max_pressure: Maximum pressure in bars that the system can handle.
        :param max_expansion: Maximum expansion in millimeters.
        """
        self.max_pressure = max_pressure
        self.max_expansion = max_expansion
        self.current_pressure = 0.0
        self.current_expansion = 0.0
        self.is_operational = False

    def start_system(self):
        """Starts the hydraulic expansion system."""
        if not self.is_operational:
            self.is_operational = True
            print("Hydraulic Expansion Powerpack started.")
        else:
            print("System is already operational.")

    def stop_system(self):
        """Stops the hydraulic expansion system."""
        if self.is_operational:
            self.is_operational = False
            self.current_pressure = 0.0
            self.current_expansion = 0.0
            print("Hydraulic Expansion Powerpack stopped.")
        else:
            print("System is not operational.")

    def apply_pressure(self, pressure: float):
        """
        Applies pressure to the system.

        :param pressure: The pressure to apply in bars.
        :raises ValueError: If pressure exceeds maximum limit.
        """
        if not self.is_operational:
            raise RuntimeError("Cannot apply pressure. The system is not operational.")
        
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure cannot exceed maximum limit of {self.max_pressure} bars.")
        
        self.current_pressure = pressure
        print(f"Applied pressure: {self.current_pressure} bars")

    def expand_tube(self, expansion: float):
        """
        Expands the tube by a given amount.

        :param expansion: The amount to expand in millimeters.
        :raises ValueError: If expansion exceeds maximum limit.
        """
        if not self.is_operational:
            raise RuntimeError("Cannot expand tube. The system is not operational.")
        
        if expansion < 0:
            raise ValueError("Expansion cannot be negative.")

        new_expansion = self.current_expansion + expansion
        if new_expansion > self.max_expansion:
            raise ValueError(f"Expansion cannot exceed maximum limit of {self.max_expansion} mm.")
        
        self.current_expansion = new_expansion
        print(f"Tube expanded by: {expansion} mm. Total expansion: {self.current_expansion} mm.")

    def monitor_system(self):
        """Monitors the current status of the system."""
        if self.is_operational:
            print(f"Current Pressure: {self.current_pressure} bars")
            print(f"Current Expansion: {self.current_expansion} mm")
        else:
            print("System is not operational.")

def main():
    """Main function to simulate the hydraulic tube expansion."""
    try:
        # Create an instance of HydraulicExpansionPowerpack with max limits
        powerpack = HydraulicExpansionPowerpack(max_pressure=500.0, max_expansion=100.0)

        # Start the system
        powerpack.start_system()

        # Apply pressure
        powerpack.apply_pressure(300.0)

        # Expand the tube
        powerpack.expand_tube(25.0)

        # Monitor system status
        powerpack.monitor_system()

        # Stop the system
        powerpack.stop_system()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
