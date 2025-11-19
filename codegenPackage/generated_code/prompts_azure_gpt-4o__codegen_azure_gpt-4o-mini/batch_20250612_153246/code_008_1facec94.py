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
class StairLift:
    """
    A class to model a stair lift system.
    """

    def __init__(self, lift_id, max_weight, current_floor=0):
        """
        Initializes the stair lift with an ID, maximum weight capacity, and current floor.

        :param lift_id: Unique identifier for the stair lift
        :param max_weight: Maximum weight capacity of the stair lift in kilograms
        :param current_floor: The current floor where the stair lift is located (default is ground floor)
        """
        self.lift_id = lift_id
        self.max_weight = max_weight
        self.current_floor = current_floor
        self.is_moving = False

    def move_to_floor(self, target_floor, weight):
        """
        Moves the stair lift to the specified floor if the weight is within the limit.

        :param target_floor: The floor to which the lift should move
        :param weight: The weight of the passenger(s) in kilograms
        :raises ValueError: If the weight exceeds the maximum capacity
        :raises ValueError: If the target floor is invalid
        """
        if weight > self.max_weight:
            raise ValueError("Weight exceeds maximum capacity of the stair lift.")
        
        if target_floor < 0:
            raise ValueError("Invalid floor: Floor number cannot be negative.")

        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        self.is_moving = True
        self.current_floor = target_floor
        self.is_moving = False
        print(f"Arrived at floor {self.current_floor}.")

    def get_current_floor(self):
        """
        Returns the current floor of the stair lift.

        :return: Current floor number
        """
        return self.current_floor

    def get_status(self):
        """
        Returns the operational status of the stair lift.

        :return: A string indicating whether the lift is moving or stationary
        """
        return "Moving" if self.is_moving else "Stationary"


def main():
    """
    Main function to demonstrate the operation of the stair lift system.
    """
    try:
        # Create a stair lift instance
        stair_lift = StairLift(lift_id="SL001", max_weight=300)

        # Display initial status
        print(f"Stair Lift ID: {stair_lift.lift_id}")
        print(f"Current Floor: {stair_lift.get_current_floor()}")
        print(f"Status: {stair_lift.get_status()}")

        # Move the stair lift to a new floor
        stair_lift.move_to_floor(target_floor=2, weight=250)

        # Display final status
        print(f"Final Floor: {stair_lift.get_current_floor()}")
        print(f"Status: {stair_lift.get_status()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
