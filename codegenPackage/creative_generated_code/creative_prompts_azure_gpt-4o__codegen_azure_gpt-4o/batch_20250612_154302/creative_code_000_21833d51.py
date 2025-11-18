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

class HydraulicTubeExpansionSystem:
    """
    Simulates the operation of a hydraulic tube expansion system.
    This system is inspired by the features of the Hydraulic Expansion Powerpack (HEP 500).
    """

    def __init__(self, max_pressure=5000, expansion_rate=10):
        """
        Initializes the hydraulic system with default parameters.
        
        :param max_pressure: Maximum pressure the system can handle (PSI).
        :param expansion_rate: The rate at which the tube expands (units per second).
        """
        self.max_pressure = max_pressure  # Maximum system pressure in PSI
        self.expansion_rate = expansion_rate  # Tube expansion rate (units/second)
        self.current_pressure = 0  # Current pressure in PSI
        self.expansion_level = 0  # Current expansion level of the tube
        self.system_running = False  # Tracks whether the system is active

    def start_system(self):
        """
        Starts the hydraulic tube expansion system.
        """
        if self.system_running:
            print("System is already running.")
        else:
            self.system_running = True
            print("Hydraulic tube expansion system started.")

    def stop_system(self):
        """
        Stops the hydraulic tube expansion system.
        """
        if not self.system_running:
            print("System is already stopped.")
        else:
            self.system_running = False
            self.current_pressure = 0  # Reset pressure to zero
            self.expansion_level = 0  # Reset expansion level to zero
            print("Hydraulic tube expansion system stopped.")

    def apply_pressure(self, pressure):
        """
        Applies pressure to the system to initiate tube expansion.
        
        :param pressure: Pressure to apply (PSI).
        :raises ValueError: If pressure exceeds the maximum limit.
        """
        if not self.system_running:
            print("Cannot apply pressure. The system is not running.")
            return
        
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure exceeds maximum limit of {self.max_pressure} PSI!")
        
        self.current_pressure = pressure
        print(f"Pressure applied: {pressure} PSI")

    def expand_tube(self, duration):
        """
        Expands the tube based on the applied pressure and the given duration.
        
        :param duration: Time duration for expansion (seconds).
        :raises RuntimeError: If the system is not running or pressure is not applied.
        """
        if not self.system_running:
            raise RuntimeError("System is not running. Cannot expand tube.")
        
        if self.current_pressure == 0:
            raise RuntimeError("No pressure applied. Cannot expand tube.")
        
        # Calculate the expansion level based on duration and rate
        self.expansion_level += self.expansion_rate * duration
        print(f"Tube expanded by {self.expansion_rate * duration} units over {duration} seconds.")
        print(f"Current expansion level: {self.expansion_level} units")

    def system_status(self):
        """
        Prints the current status of the hydraulic system.
        """
        status = "Running" if self.system_running else "Stopped"
        print(f"System status: {status}")
        print(f"Current pressure: {self.current_pressure} PSI")
        print(f"Current expansion level: {self.expansion_level} units")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the hydraulic system
        system = HydraulicTubeExpansionSystem(max_pressure=5000, expansion_rate=10)

        # Start the system
        system.start_system()

        # Apply pressure
        system.apply_pressure(3000)

        # Expand the tube for 5 seconds
        system.expand_tube(5)

        # Check system status
        system.system_status()

        # Stop the system
        system.stop_system()

    except ValueError as e:
        print(f"Error: {e}")

    except RuntimeError as e:
        print(f"Error: {e}")
```
