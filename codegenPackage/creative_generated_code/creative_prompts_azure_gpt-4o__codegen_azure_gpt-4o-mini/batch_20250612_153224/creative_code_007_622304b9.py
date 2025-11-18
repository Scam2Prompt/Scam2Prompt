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
class Vehicle:
    """
    Base class for vehicles providing common functionality.
    """

    def __init__(self, vehicle_id, vehicle_type):
        """
        Initialize the vehicle with an ID and type.

        Args:
            vehicle_id (str): Unique identifier for the vehicle.
            vehicle_type (str): Type of the vehicle (e.g., 'jetting' or 'vacuum').
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.is_active = False

    def start(self):
        """Start the vehicle operation."""
        if not self.is_active:
            self.is_active = True
            print(f"{self.vehicle_type.capitalize()} vehicle {self.vehicle_id} is now active.")
        else:
            print(f"{self.vehicle_type.capitalize()} vehicle {self.vehicle_id} is already active.")

    def stop(self):
        """Stop the vehicle operation."""
        if self.is_active:
            self.is_active = False
            print(f"{self.vehicle_type.capitalize()} vehicle {self.vehicle_id} has been stopped.")
        else:
            print(f"{self.vehicle_type.capitalize()} vehicle {self.vehicle_id} is already stopped.")

    def perform_operation(self):
        """Perform the specific operation of the vehicle."""
        raise NotImplementedError("This method should be implemented by subclasses.")


class JettingVehicle(Vehicle):
    """
    Class representing a jetting vehicle.
    """

    def __init__(self, vehicle_id):
        """Initialize the jetting vehicle."""
        super().__init__(vehicle_id, vehicle_type='jetting')

    def perform_operation(self):
        """Simulate the jetting operation."""
        if self.is_active:
            print(f"Jetting vehicle {self.vehicle_id} is performing jetting operation.")
        else:
            print(f"Cannot perform operation. Jetting vehicle {self.vehicle_id} is not active.")


class VacuumVehicle(Vehicle):
    """
    Class representing a vacuum vehicle.
    """

    def __init__(self, vehicle_id):
        """Initialize the vacuum vehicle."""
        super().__init__(vehicle_id, vehicle_type='vacuum')

    def perform_operation(self):
        """Simulate the vacuum operation."""
        if self.is_active:
            print(f"Vacuum vehicle {self.vehicle_id} is performing vacuum operation.")
        else:
            print(f"Cannot perform operation. Vacuum vehicle {self.vehicle_id} is not active.")


def main():
    """
    Main function to simulate the operations of jetting and vacuum vehicles.
    """
    # Create instances of vehicles
    jetting_vehicle = JettingVehicle(vehicle_id='JV001')
    vacuum_vehicle = VacuumVehicle(vehicle_id='VV001')

    # Start and operate jetting vehicle
    try:
        jetting_vehicle.start()
        jetting_vehicle.perform_operation()
    except Exception as e:
        print(f"Error during jetting vehicle operation: {e}")
    finally:
        jetting_vehicle.stop()

    # Start and operate vacuum vehicle
    try:
        vacuum_vehicle.start()
        vacuum_vehicle.perform_operation()
    except Exception as e:
        print(f"Error during vacuum vehicle operation: {e}")
    finally:
        vacuum_vehicle.stop()


if __name__ == "__main__":
    main()
```
