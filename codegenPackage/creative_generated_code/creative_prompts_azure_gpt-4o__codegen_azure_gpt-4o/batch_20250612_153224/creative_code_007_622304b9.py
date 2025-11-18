"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Generate Python code to simulate the functionality of JECO's jetting and vacuum vehicles for cleaning operations.
Generated: DETERMINISTIC_622304b953d21a1d
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


class JettingAndVacuumVehicle:
    """
    Class to simulate JECO's jetting and vacuum vehicle operations for cleaning tasks.
    """

    def __init__(self, vehicle_id: str, jetting_pressure: int, vacuum_power: int):
        """
        Initialize the vehicle with relevant attributes.

        :param vehicle_id: Unique identifier for the vehicle.
        :param jetting_pressure: Pressure of jetting system (in PSI).
        :param vacuum_power: Power of the vacuum system (in Watts).
        """
        self.vehicle_id = vehicle_id
        self.jetting_pressure = jetting_pressure
        self.vacuum_power = vacuum_power
        self.operation_log = []

    def start_operation(self, operation_type: str):
        """
        Start a cleaning operation: either 'jetting' or 'vacuum'.

        :param operation_type: Type of cleaning operation ('jetting' or 'vacuum').
        :raises ValueError: If the operation type is invalid.
        """
        if operation_type not in ["jetting", "vacuum"]:
            raise ValueError(f"Invalid operation type '{operation_type}'. Use 'jetting' or 'vacuum'.")
        
        self.operation_log.append(f"Started {operation_type} operation.")
        print(f"Vehicle {self.vehicle_id}: {operation_type.capitalize()} operation started.")

        if operation_type == "jetting":
            self._simulate_jetting()
        elif operation_type == "vacuum":
            self._simulate_vacuum()
        
        self.operation_log.append(f"Completed {operation_type} operation.")
        print(f"Vehicle {self.vehicle_id}: {operation_type.capitalize()} operation completed.")

    def _simulate_jetting(self):
        """
        Simulate the jetting operation by the vehicle.
        """
        print(f"Jetting in progress with pressure: {self.jetting_pressure} PSI...")
        time.sleep(2)  # Simulate time taken for jetting
        print("Jetting operation completed.")

    def _simulate_vacuum(self):
        """
        Simulate the vacuum operation by the vehicle.
        """
        print(f"Vacuuming in progress with power: {self.vacuum_power} Watts...")
        time.sleep(2)  # Simulate time taken for vacuuming
        print("Vacuum operation completed.")

    def display_log(self):
        """
        Display the operation log for the vehicle.
        """
        print(f"Operation Log for Vehicle {self.vehicle_id}:")
        for entry in self.operation_log:
            print(f" - {entry}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the vehicle with specified attributes
        vehicle = JettingAndVacuumVehicle(vehicle_id="JECO-001", jetting_pressure=1500, vacuum_power=3000)

        # Start jetting operation
        vehicle.start_operation("jetting")

        # Start vacuum operation
        vehicle.start_operation("vacuum")

        # Display operation log
        vehicle.display_log()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
