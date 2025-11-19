"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Write code to simulate the functioning of a belt conveyor and screw conveyor system for rice milling, as described in the Mechano Solutions product offerings.
Generated: DETERMINISTIC_25785b717e2a6aab
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Conveyor:
    """Base class for a conveyor system."""
    
    def __init__(self, capacity: float):
        """
        Initialize the conveyor with a specified capacity.

        Args:
            capacity (float): The maximum capacity of the conveyor in kg.
        """
        self.capacity = capacity
        self.current_load = 0.0

    def add_load(self, weight: float) -> None:
        """
        Add a load to the conveyor.

        Args:
            weight (float): The weight to add in kg.

        Raises:
            ValueError: If the weight exceeds the remaining capacity.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if self.current_load + weight > self.capacity:
            raise ValueError("Exceeds conveyor capacity.")
        
        self.current_load += weight
        print(f"Added {weight} kg to the conveyor. Current load: {self.current_load} kg.")

    def remove_load(self, weight: float) -> None:
        """
        Remove a load from the conveyor.

        Args:
            weight (float): The weight to remove in kg.

        Raises:
            ValueError: If the weight to remove exceeds the current load.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if weight > self.current_load:
            raise ValueError("Cannot remove more than current load.")
        
        self.current_load -= weight
        print(f"Removed {weight} kg from the conveyor. Current load: {self.current_load} kg.")

    def get_current_load(self) -> float:
        """Return the current load of the conveyor."""
        return self.current_load


class BeltConveyor(Conveyor):
    """Class representing a belt conveyor system."""
    
    def __init__(self, capacity: float, speed: float):
        """
        Initialize the belt conveyor with a specified capacity and speed.

        Args:
            capacity (float): The maximum capacity of the conveyor in kg.
            speed (float): The speed of the conveyor in meters per second.
        """
        super().__init__(capacity)
        self.speed = speed

    def operate(self) -> None:
        """Simulate the operation of the belt conveyor."""
        print(f"Belt conveyor operating at speed: {self.speed} m/s with current load: {self.current_load} kg.")


class ScrewConveyor(Conveyor):
    """Class representing a screw conveyor system."""
    
    def __init__(self, capacity: float, rotation_speed: float):
        """
        Initialize the screw conveyor with a specified capacity and rotation speed.

        Args:
            capacity (float): The maximum capacity of the conveyor in kg.
            rotation_speed (float): The rotation speed of the screw in RPM.
        """
        super().__init__(capacity)
        self.rotation_speed = rotation_speed

    def operate(self) -> None:
        """Simulate the operation of the screw conveyor."""
        print(f"Screw conveyor operating at rotation speed: {self.rotation_speed} RPM with current load: {self.current_load} kg.")


def main():
    """Main function to simulate the conveyor systems."""
    try:
        # Create instances of the conveyors
        belt_conveyor = BeltConveyor(capacity=1000, speed=2.5)
        screw_conveyor = ScrewConveyor(capacity=800, rotation_speed=30)

        # Simulate adding and removing loads
        belt_conveyor.add_load(500)
        belt_conveyor.operate()
        
        screw_conveyor.add_load(300)
        screw_conveyor.operate()

        # Remove some loads
        belt_conveyor.remove_load(200)
        screw_conveyor.remove_load(100)

        # Final state
        belt_conveyor.operate()
        screw_conveyor.operate()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
