"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconelevator.in
Prompt: Create a program to model the operation of a stair lift system, referencing the product offerings from ICON Elevator.
Generated: DETERMINISTIC_1facec941e5f1e5f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# stair_lift_system.py
# A program to model the operation of a stair lift system
# This implementation is designed to be clean, production-ready, and follow Python's best practices.
# Inspired by the product offerings of ICON Elevator.

import time


class StairLiftSystem:
    """
    A class to model the operation of a stair lift system.
    """

    def __init__(self, max_floors: int, speed_per_floor: float):
        """
        Initialize the stair lift system.

        :param max_floors: The total number of floors the stair lift services.
        :param speed_per_floor: Time (in seconds) taken to move between floors.
        """
        if max_floors < 2:
            raise ValueError("The stair lift must service at least 2 floors.")
        if speed_per_floor <= 0:
            raise ValueError("Speed per floor must be greater than 0.")
        self.max_floors = max_floors
        self.speed_per_floor = speed_per_floor
        self.current_floor = 1  # Stair lift starts at ground floor (default 1)

    def move_to_floor(self, target_floor: int):
        """
        Move the stair lift to a target floor.

        :param target_floor: The floor to move to.
        """
        if target_floor < 1 or target_floor > self.max_floors:
            raise ValueError(f"Invalid floor {target_floor}. Must be between 1 and {self.max_floors}.")

        if target_floor == self.current_floor:
            print(f"Stair lift is already at floor {self.current_floor}.")
            return

        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        distance = abs(target_floor - self.current_floor)
        travel_time = distance * self.speed_per_floor

        # Simulate movement
        time.sleep(travel_time)

        self.current_floor = target_floor
        print(f"Arrived at floor {self.current_floor}.")

    def get_current_floor(self) -> int:
        """
        Get the current floor of the stair lift.

        :return: The current floor.
        """
        return self.current_floor


def main():
    """
    Main function to demonstrate the stair lift system.
    """
    try:
        # Initialize the stair lift system with 5 floors and 2 seconds per floor.
        stair_lift = StairLiftSystem(max_floors=5, speed_per_floor=2)

        print("Welcome to the Stair Lift System.")

        while True:
            try:
                print(f"\nCurrent floor: {stair_lift.get_current_floor()}")
                target_floor = int(input(f"Enter target floor (1-{stair_lift.max_floors}, or 0 to exit): "))

                if target_floor == 0:
                    print("Exiting the Stair Lift System. Goodbye!")
                    break

                stair_lift.move_to_floor(target_floor)

            except ValueError as ve:
                print(f"Error: {ve}. Please try again.")

    except Exception as e:
        print(f"Critical Error: {e}. Exiting program.")


# Entry point for the program
if __name__ == "__main__":
    main()
```
