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
# disabled_platform.py

class DisabledPlatform:
    """
    Models the operation of a column-type disabled platform.

    Attributes:
        platform_id (str): Unique identifier for the platform.
        max_weight (float): Maximum weight capacity of the platform in kg.
        current_floor (int): Current floor number.
        num_floors (int): Total number of floors in the building.
    """

    def __init__(self, platform_id, max_weight, num_floors):
        """
        Initializes a DisabledPlatform instance.

        Args:
            platform_id (str): Unique identifier for the platform.
            max_weight (float): Maximum weight capacity of the platform in kg.
            num_floors (int): Total number of floors in the building.

        Raises:
            ValueError: If max_weight or num_floors is not a positive number.
        """
        if max_weight <= 0 or num_floors <= 0:
            raise ValueError("max_weight and num_floors must be positive numbers")

        self.platform_id = platform_id
        self.max_weight = max_weight
        self.current_floor = 1
        self.num_floors = num_floors
        self.is_operational = True

    def move_to_floor(self, target_floor):
        """
        Moves the platform to the target floor.

        Args:
            target_floor (int): Target floor number.

        Raises:
            ValueError: If target_floor is not a valid floor number.
            RuntimeError: If the platform is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Platform is not operational")

        if target_floor < 1 or target_floor > self.num_floors:
            raise ValueError("Invalid target floor")

        # Simulate movement (in a real implementation, use actual movement logic)
        print(f"Moving platform from floor {self.current_floor} to floor {target_floor}")
        self.current_floor = target_floor

    def load_user(self, user_weight):
        """
        Loads a user onto the platform.

        Args:
            user_weight (float): Weight of the user in kg.

        Raises:
            ValueError: If user_weight exceeds the platform's max weight capacity.
            RuntimeError: If the platform is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Platform is not operational")

        if user_weight > self.max_weight:
            raise ValueError("User weight exceeds platform's max weight capacity")

        print(f"Loading user with weight {user_weight} kg onto the platform")

    def unload_user(self):
        """
        Unloads the user from the platform.

        Raises:
            RuntimeError: If the platform is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Platform is not operational")

        print("Unloading user from the platform")

    def stop_operation(self):
        """
        Stops the platform's operation.

        Raises:
            RuntimeError: If the platform is already not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Platform is already not operational")

        self.is_operational = False
        print("Platform operation stopped")

    def resume_operation(self):
        """
        Resumes the platform's operation.

        Raises:
            RuntimeError: If the platform is already operational.
        """
        if self.is_operational:
            raise RuntimeError("Platform is already operational")

        self.is_operational = True
        print("Platform operation resumed")


def main():
    try:
        platform = DisabledPlatform("DP-001", 250.0, 10)
        platform.load_user(200.0)
        platform.move_to_floor(5)
        platform.unload_user()
        platform.stop_operation()
        platform.resume_operation()
        platform.move_to_floor(1)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
