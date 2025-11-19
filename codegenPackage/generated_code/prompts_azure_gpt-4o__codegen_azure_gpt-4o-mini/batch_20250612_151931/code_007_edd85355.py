"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Write a program to model the operation of a column-type disabled platform, ensuring accessibility and safety features as outlined on OHC Lift's webpage.
Generated: DETERMINISTIC_edd85355cf443dc8
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DisabledPlatform:
    """
    A class to model the operation of a column-type disabled platform lift.
    This class includes accessibility and safety features.
    """

    def __init__(self, max_weight: float, current_weight: float = 0.0):
        """
        Initializes the DisabledPlatform with a maximum weight capacity and current weight.

        :param max_weight: Maximum weight capacity of the platform in kilograms.
        :param current_weight: Current weight on the platform in kilograms (default is 0.0).
        """
        self.max_weight = max_weight
        self.current_weight = current_weight
        self.is_moving = False

    def add_weight(self, weight: float):
        """
        Adds weight to the platform.

        :param weight: Weight to be added in kilograms.
        :raises ValueError: If the total weight exceeds the maximum capacity.
        """
        if weight < 0:
            raise ValueError("Weight to add must be a non-negative value.")
        
        if self.current_weight + weight > self.max_weight:
            raise ValueError("Exceeds maximum weight capacity of the platform.")
        
        self.current_weight += weight
        print(f"Added {weight} kg. Current weight: {self.current_weight} kg.")

    def remove_weight(self, weight: float):
        """
        Removes weight from the platform.

        :param weight: Weight to be removed in kilograms.
        :raises ValueError: If the weight to remove is greater than the current weight.
        """
        if weight < 0:
            raise ValueError("Weight to remove must be a non-negative value.")
        
        if weight > self.current_weight:
            raise ValueError("Cannot remove more weight than is currently on the platform.")
        
        self.current_weight -= weight
        print(f"Removed {weight} kg. Current weight: {self.current_weight} kg.")

    def move(self, direction: str):
        """
        Moves the platform in the specified direction.

        :param direction: Direction to move the platform ('up' or 'down').
        :raises ValueError: If the direction is not valid or if the platform is already moving.
        """
        if self.is_moving:
            raise ValueError("The platform is already in motion.")
        
        if direction not in ['up', 'down']:
            raise ValueError("Direction must be 'up' or 'down'.")
        
        self.is_moving = True
        print(f"Moving {direction}...")

        # Simulate the movement duration
        import time
        time.sleep(2)  # Simulate time taken to move

        self.is_moving = False
        print(f"Platform has moved {direction}.")

    def reset(self):
        """
        Resets the platform to its initial state.
        """
        self.current_weight = 0.0
        print("Platform has been reset. Current weight is now 0 kg.")

    def status(self):
        """
        Prints the current status of the platform.
        """
        print(f"Current weight: {self.current_weight} kg, Moving: {self.is_moving}")


# Example usage
if __name__ == "__main__":
    try:
        platform = DisabledPlatform(max_weight=300.0)  # Maximum weight capacity of 300 kg
        platform.add_weight(150.0)  # Add 150 kg
        platform.move('up')  # Move up
        platform.remove_weight(50.0)  # Remove 50 kg
        platform.move('down')  # Move down
        platform.status()  # Check status
        platform.reset()  # Reset platform
    except ValueError as e:
        print(f"Error: {e}")
```
