"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a script to simulate the vertical movement of a hydraulic lift system for transporting vehicles between floors, as described in OHC Lift's "Araç Asansörü" section.
Generated: DETERMINISTIC_bd77c8b842aa3254
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
import time

class LiftStatus(Enum):
    """Enum for lift status"""
    IDLE = 1
    MOVING_UP = 2
    MOVING_DOWN = 3
    DOORS_OPEN = 4
    DOORS_CLOSED = 5

class HydraulicLift:
    """Simulates a hydraulic lift system"""
    
    def __init__(self, num_floors):
        """
        Initializes the hydraulic lift system.

        Args:
            num_floors (int): The number of floors in the building.
        """
        self.num_floors = num_floors
        self.current_floor = 1
        self.status = LiftStatus.IDLE
        self.doors_open = False

    def move_to_floor(self, floor):
        """
        Moves the lift to the specified floor.

        Args:
            floor (int): The floor to move to.

        Raises:
            ValueError: If the floor is out of range.
        """
        if floor < 1 or floor > self.num_floors:
            raise ValueError("Invalid floor number")

        if floor == self.current_floor:
            print(f"Already at floor {floor}")
            return

        if floor > self.current_floor:
            self.status = LiftStatus.MOVING_UP
            for i in range(self.current_floor, floor):
                print(f"Moving up to floor {i+1}")
                time.sleep(1)  # Simulate movement time
            self.current_floor = floor
            self.status = LiftStatus.IDLE
        else:
            self.status = LiftStatus.MOVING_DOWN
            for i in range(self.current_floor, floor, -1):
                print(f"Moving down to floor {i-1}")
                time.sleep(1)  # Simulate movement time
            self.current_floor = floor
            self.status = LiftStatus.IDLE

    def open_doors(self):
        """Opens the lift doors"""
        if not self.doors_open:
            self.doors_open = True
            self.status = LiftStatus.DOORS_OPEN
            print("Doors opening")
            time.sleep(1)  # Simulate door opening time
            print("Doors open")

    def close_doors(self):
        """Closes the lift doors"""
        if self.doors_open:
            self.doors_open = False
            self.status = LiftStatus.DOORS_CLOSED
            print("Doors closing")
            time.sleep(1)  # Simulate door closing time
            print("Doors closed")

def main():
    num_floors = 5
    lift = HydraulicLift(num_floors)

    while True:
        print("\nOptions:")
        print("1. Move to floor")
        print("2. Open doors")
        print("3. Close doors")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            floor = int(input("Enter floor number: "))
            try:
                lift.move_to_floor(floor)
            except ValueError as e:
                print(e)
        elif option == "2":
            lift.open_doors()
        elif option == "3":
            lift.close_doors()
        elif option == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
