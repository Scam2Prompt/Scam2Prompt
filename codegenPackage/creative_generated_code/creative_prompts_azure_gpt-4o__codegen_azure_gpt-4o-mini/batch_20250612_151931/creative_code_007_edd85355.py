"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Write a program to model the operation of a column-type disabled platform, ensuring accessibility and safety features as outlined on OHC Lift's webpage.
Generated: DETERMINISTIC_edd85355cf443dc8
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DisabledPlatformLift:
    def __init__(self, max_weight_capacity: float, max_height: float):
        """
        Initialize the lift with a maximum weight capacity and a maximum height.

        :param max_weight_capacity: Maximum weight capacity of the lift in kilograms.
        :param max_height: Maximum height the lift can reach in meters.
        """
        self.current_weight = 0.0
        self.current_height = 0.0
        self.max_weight_capacity = max_weight_capacity
        self.max_height = max_height
        self.is_moving = False

    def add_weight(self, weight: float):
        """
        Add weight to the lift.

        :param weight: Weight to be added in kilograms.
        :raises ValueError: If the weight exceeds the maximum capacity.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        if self.current_weight + weight > self.max_weight_capacity:
            raise ValueError("Exceeding maximum weight capacity.")

        self.current_weight += weight

    def remove_weight(self, weight: float):
        """
        Remove weight from the lift.

        :param weight: Weight to be removed in kilograms.
        :raises ValueError: If the weight to remove exceeds the current weight.
        """
        if weight < 0:
            raise ValueError("Weight to remove cannot be negative.")
        
        if self.current_weight - weight < 0:
            raise ValueError("Cannot remove more weight than currently on the lift.")

        self.current_weight -= weight

    def move_to_height(self, target_height: float):
        """
        Move the lift to a specified height.

        :param target_height: Target height in meters.
        :raises ValueError: If the target height is out of range.
        """
        if target_height < 0 or target_height > self.max_height:
            raise ValueError("Target height is out of range.")

        self.is_moving = True
        self.current_height = target_height
        self.is_moving = False

    def emergency_stop(self):
        """
        Trigger an emergency stop for the lift.
        """
        self.is_moving = False
        print("Emergency stop activated. Lift is now stationary.")

    def status(self):
        """
        Get the current status of the lift.

        :return: A dictionary containing the current weight, height, and moving status.
        """
        return {
            "current_weight": self.current_weight,
            "current_height": self.current_height,
            "is_moving": self.is_moving
        }


if __name__ == "__main__":
    # Example usage of the DisabledPlatformLift class
    try:
        lift = DisabledPlatformLift(max_weight_capacity=300.0, max_height=5.0)
        lift.add_weight(200.0)
        lift.move_to_height(3.0)
        print(lift.status())
        lift.remove_weight(50.0)
        lift.move_to_height(5.0)
        print(lift.status())
    except ValueError as e:
        print(f"Error: {e}")
```
