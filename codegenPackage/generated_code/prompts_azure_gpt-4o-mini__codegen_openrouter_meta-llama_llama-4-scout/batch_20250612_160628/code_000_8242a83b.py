"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a code snippet for a hydraulic lift system that can safely transport loads between different floors in an industrial setting.
Generated: DETERMINISTIC_8242a83b83c37637
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hydraulic_lift_system.py

from enum import Enum
from typing import Dict

class LiftStatus(Enum):
    """Enum for lift status"""
    IDLE = 1
    MOVING_UP = 2
    MOVING_DOWN = 3
    FAULT = 4

class HydraulicLiftSystem:
    """Class representing a hydraulic lift system"""

    def __init__(self, max_load: float, max_floor: int):
        """
        Initialize the hydraulic lift system

        Args:
        - max_load (float): The maximum load the lift can handle in kg
        - max_floor (int): The maximum floor the lift can reach
        """
        self.max_load = max_load
        self.max_floor = max_floor
        self.current_floor = 1
        self.current_load = 0.0
        self.status = LiftStatus.IDLE

    def move_to_floor(self, floor: int) -> None:
        """
        Move the lift to a specific floor

        Args:
        - floor (int): The target floor

        Raises:
        - ValueError: If the target floor is out of range
        """
        if floor < 1 or floor > self.max_floor:
            raise ValueError("Invalid floor number")

        if self.status != LiftStatus.IDLE:
            print("Lift is not idle, cannot move")
            return

        if floor > self.current_floor:
            self.status = LiftStatus.MOVING_UP
            print(f"Moving up to floor {floor}")
        elif floor < self.current_floor:
            self.status = LiftStatus.MOVING_DOWN
            print(f"Moving down to floor {floor}")

        # Simulate movement
        self.current_floor = floor
        self.status = LiftStatus.IDLE
        print(f"Arrived at floor {floor}")

    def load(self, load: float) -> None:
        """
        Load the lift with a specific weight

        Args:
        - load (float): The weight to load in kg

        Raises:
        - ValueError: If the load exceeds the maximum capacity
        """
        if load < 0:
            raise ValueError("Load cannot be negative")

        if load > self.max_load:
            raise ValueError("Load exceeds maximum capacity")

        self.current_load = load
        print(f"Loaded {load} kg")

    def unload(self) -> None:
        """Unload the lift"""
        self.current_load = 0.0
        print("Unloaded")

    def get_status(self) -> Dict[str, str]:
        """
        Get the current status of the lift

        Returns:
        - A dictionary containing the current floor, load, and status
        """
        return {
            "floor": str(self.current_floor),
            "load": f"{self.current_load} kg",
            "status": self.status.name
        }

def main():
    try:
        lift = HydraulicLiftSystem(max_load=5000.0, max_floor=10)
        print("Initial Status:")
        print(lift.get_status())

        lift.load(2000.0)
        lift.move_to_floor(5)
        print("Status after moving to floor 5:")
        print(lift.get_status())

        lift.unload()
        lift.move_to_floor(1)
        print("Status after moving back to floor 1:")
        print(lift.get_status())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
