"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Create a program to model the operation of a stair lift system, referencing the product offerings from ICON Elevator.
Generated: DETERMINISTIC_1facec941e5f1e5f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List

class LiftStatus(Enum):
    """Enum for lift status"""
    IDLE = 1
    MOVING_UP = 2
    MOVING_DOWN = 3
    STOPPED = 4
    ERROR = 5

class StairLift:
    """Class representing a stair lift system"""
    def __init__(self, model: str, max_weight: int, max_speed: float):
        """
        Initialize a stair lift object

        Args:
        model (str): Model of the stair lift
        max_weight (int): Maximum weight capacity
        max_speed (float): Maximum speed of the lift
        """
        self.model = model
        self.max_weight = max_weight
        self.max_speed = max_speed
        self.status = LiftStatus.IDLE
        self.current_floor = 1
        self.destination_floor = 1

    def move_up(self, destination_floor: int):
        """
        Move the lift up to the destination floor

        Args:
        destination_floor (int): Destination floor

        Raises:
        ValueError: If destination floor is less than or equal to current floor
        """
        if destination_floor <= self.current_floor:
            raise ValueError("Destination floor must be greater than current floor")
        self.destination_floor = destination_floor
        self.status = LiftStatus.MOVING_UP

    def move_down(self, destination_floor: int):
        """
        Move the lift down to the destination floor

        Args:
        destination_floor (int): Destination floor

        Raises:
        ValueError: If destination floor is greater than or equal to current floor
        """
        if destination_floor >= self.current_floor:
            raise ValueError("Destination floor must be less than current floor")
        self.destination_floor = destination_floor
        self.status = LiftStatus.MOVING_DOWN

    def stop(self):
        """Stop the lift"""
        self.status = LiftStatus.STOPPED

    def update_status(self):
        """Update the status of the lift"""
        if self.status == LiftStatus.MOVING_UP and self.current_floor < self.destination_floor:
            self.current_floor += 1
            if self.current_floor == self.destination_floor:
                self.status = LiftStatus.IDLE
        elif self.status == LiftStatus.MOVING_DOWN and self.current_floor > self.destination_floor:
            self.current_floor -= 1
            if self.current_floor == self.destination_floor:
                self.status = LiftStatus.IDLE

    def __str__(self):
        return f"Stair Lift {self.model} - Status: {self.status.name}, Current Floor: {self.current_floor}, Destination Floor: {self.destination_floor}"

class ICONElevator:
    """Class representing an ICON Elevator system"""
    def __init__(self):
        self.lifts: List[StairLift] = []

    def add_lift(self, lift: StairLift):
        """
        Add a stair lift to the system

        Args:
        lift (StairLift): Stair lift to add
        """
        self.lifts.append(lift)

    def remove_lift(self, lift: StairLift):
        """
        Remove a stair lift from the system

        Args:
        lift (StairLift): Stair lift to remove

        Raises:
        ValueError: If lift is not in the system
        """
        if lift not in self.lifts:
            raise ValueError("Lift not found in the system")
        self.lifts.remove(lift)

    def __str__(self):
        system_info = "ICON Elevator System:\n"
        for i, lift in enumerate(self.lifts):
            system_info += f"Lift {i+1}: {lift}\n"
        return system_info

def main():
    # Create an ICON Elevator system
    icon_system = ICONElevator()

    # Create stair lifts
    lift1 = StairLift("SlimLine", 400, 0.5)
    lift2 = StairLift("Curved", 300, 0.3)

    # Add lifts to the system
    icon_system.add_lift(lift1)
    icon_system.add_lift(lift2)

    # Print initial system info
    print(icon_system)

    # Move lifts
    lift1.move_up(5)
    lift2.move_down(2)

    # Update and print lift status
    for _ in range(5):
        lift1.update_status()
        lift2.update_status()
        print(icon_system)

if __name__ == "__main__":
    main()
```
