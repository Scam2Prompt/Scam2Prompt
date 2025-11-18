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
class StairLift:
    """
    A class to model the operation of a stair lift system.
    Attributes:
        capacity (int): Maximum weight capacity of the stair lift in pounds.
        current_weight (int): Current weight on the stair lift.
        current_floor (int): The current floor of the stair lift.
    """
    
    def __init__(self, capacity=300):
        """
        Initializes the StairLift with a given weight capacity.
        :param capacity: Maximum weight capacity, defaults to 300 pounds.
        """
        self.capacity = capacity
        self.current_weight = 0
        self.current_floor = 0

    def add_weight(self, weight):
        """
        Adds weight to the stair lift.
        :param weight: Weight to be added in pounds.
        :raises ValueError: If the weight exceeds capacity.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if self.current_weight + weight > self.capacity:
            raise ValueError("Exceeded weight capacity.")
        self.current_weight += weight

    def remove_weight(self, weight):
        """
        Removes weight from the stair lift.
        :param weight: Weight to be removed in pounds.
        :raises ValueError: If the weight to remove is greater than current weight.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if self.current_weight - weight < 0:
            raise ValueError("Cannot remove more weight than currently present.")
        self.current_weight -= weight

    def move_to_floor(self, target_floor):
        """
        Moves the stair lift to a specified floor.
        :param target_floor: The floor to move to.
        :raises ValueError: If the target floor is invalid.
        """
        if target_floor < 0:
            raise ValueError("Floor number cannot be negative.")
        
        print(f"Moving from floor {self.current_floor} to floor {target_floor}.")
        self.current_floor = target_floor
        print(f"Arrived at floor {self.current_floor}.")

    def status(self):
        """
        Provides the current status of the stair lift.
        :return: A string representing the current status.
        """
        return (f"Current Floor: {self.current_floor}, "
                f"Current Weight: {self.current_weight} lbs, "
                f"Weight Capacity: {self.capacity} lbs")

def main():
    """
    Main function to demonstrate the operation of the stair lift system.
    """
    stair_lift = StairLift()

    try:
        stair_lift.add_weight(150)
        stair_lift.move_to_floor(1)
        print(stair_lift.status())
        
        stair_lift.add_weight(200)  # This should raise an exception
    except ValueError as e:
        print(f"Error: {e}")

    try:
        stair_lift.remove_weight(50)
        stair_lift.move_to_floor(2)
        print(stair_lift.status())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
