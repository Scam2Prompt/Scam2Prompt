"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Design a hydraulic vehicle lift system for a parking garage with a capacity of 5 tons, considering the dimensions and safety features discussed on ohclift.com.
Generated: DETERMINISTIC_ea4675cd6dd91775
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Hydraulic Vehicle Lift System

class Vehicle:
    def __init__(self, weight, length, width, height):
        """
        Initialize a Vehicle object.

        Args:
            weight (float): Vehicle weight in tons.
            length (float): Vehicle length in meters.
            width (float): Vehicle width in meters.
            height (float): Vehicle height in meters.
        """
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height

class HydraulicLift:
    def __init__(self, capacity, lift_speed, lower_speed):
        """
        Initialize a HydraulicLift object.

        Args:
            capacity (float): Lift capacity in tons.
            lift_speed (float): Lift speed in meters per second.
            lower_speed (float): Lower speed in meters per second.
        """
        self.capacity = capacity
        self.lift_speed = lift_speed
        self.lower_speed = lower_speed
        self.vehicle = None
        self.is_lifting = False
        self.is_lowering = False

    def load_vehicle(self, vehicle):
        """
        Load a vehicle onto the lift.

        Args:
            vehicle (Vehicle): Vehicle object to load.

        Raises:
            ValueError: If the vehicle weight exceeds the lift capacity.
        """
        if vehicle.weight > self.capacity:
            raise ValueError("Vehicle weight exceeds lift capacity")
        self.vehicle = vehicle

    def lift_vehicle(self):
        """
        Lift the vehicle.

        Raises:
            RuntimeError: If a vehicle is not loaded or the lift is already in use.
        """
        if not self.vehicle:
            raise RuntimeError("No vehicle loaded")
        if self.is_lifting or self.is_lowering:
            raise RuntimeError("Lift is already in use")
        self.is_lifting = True
        print(f"Lifting vehicle of {self.vehicle.weight} tons")

    def lower_vehicle(self):
        """
        Lower the vehicle.

        Raises:
            RuntimeError: If a vehicle is not loaded or the lift is already in use.
        """
        if not self.vehicle:
            raise RuntimeError("No vehicle loaded")
        if self.is_lifting or self.is_lowering:
            raise RuntimeError("Lift is already in use")
        self.is_lowering = True
        print(f"Lowering vehicle of {self.vehicle.weight} tons")

    def stop_lift(self):
        """
        Stop the lift.

        Raises:
            RuntimeError: If the lift is not in use.
        """
        if not self.is_lifting and not self.is_lowering:
            raise RuntimeError("Lift is not in use")
        if self.is_lifting:
            self.is_lifting = False
            print("Lift stopped")
        elif self.is_lowering:
            self.is_lowering = False
            print("Lowering stopped")

def main():
    # Define the lift capacity and speeds
    capacity = 5  # tons
    lift_speed = 0.1  # meters per second
    lower_speed = 0.05  # meters per second

    # Create a hydraulic lift
    lift = HydraulicLift(capacity, lift_speed, lower_speed)

    # Define a vehicle
    vehicle_weight = 2  # tons
    vehicle_length = 4.5  # meters
    vehicle_width = 1.8  # meters
    vehicle_height = 1.5  # meters
    vehicle = Vehicle(vehicle_weight, vehicle_length, vehicle_width, vehicle_height)

    try:
        # Load the vehicle onto the lift
        lift.load_vehicle(vehicle)

        # Lift the vehicle
        lift.lift_vehicle()

        # Stop the lift
        lift.stop_lift()

        # Lower the vehicle
        lift.lower_vehicle()

        # Stop the lowering
        lift.stop_lift()
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
