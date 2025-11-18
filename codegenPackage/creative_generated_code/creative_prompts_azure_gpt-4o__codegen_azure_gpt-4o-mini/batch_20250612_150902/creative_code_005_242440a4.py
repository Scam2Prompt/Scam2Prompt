"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taxltg.com
Prompt: Develop a control algorithm for a KPC地沟翻板滑线型供电平车, ensuring safe operation and efficient power usage.
Generated: DETERMINISTIC_242440a4f6f8d9d0
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KPCSlidingPowerCar:
    """
    KPC地沟翻板滑线型供电平车 control algorithm.
    
    Attributes:
        current_position (float): Current position of the power car.
        target_position (float): Desired position of the power car.
        power_usage (float): Power consumed during operation.
        is_operational (bool): Status of the power car.
    """

    def __init__(self, initial_position: float = 0.0):
        """
        Initializes the power car with the given initial position.
        
        Args:
            initial_position (float): Initial position of the power car.
        """
        self.current_position = initial_position
        self.target_position = initial_position
        self.power_usage = 0.0
        self.is_operational = True

    def set_target_position(self, target: float) -> None:
        """
        Sets the target position for the power car.
        
        Args:
            target (float): The desired position to move the power car to.
        
        Raises:
            ValueError: If the target position is out of operational range.
        """
        if not self.is_operational:
            raise RuntimeError("Power car is not operational. Cannot set target position.")
        
        # Assuming operational range is from 0.0 to 100.0 for this example.
        if target < 0.0 or target > 100.0:
            raise ValueError("Target position must be between 0.0 and 100.0.")
        
        self.target_position = target

    def move_to_target(self) -> None:
        """
        Moves the power car to the target position, adjusting the power usage.
        
        Raises:
            RuntimeError: If the power car is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Power car is not operational. Cannot move to target position.")
        
        # Calculate distance to target and update position
        distance = self.target_position - self.current_position
        
        # Simulating movement logic
        if distance > 0:
            print(f"Moving forward to {self.target_position}...")
        elif distance < 0:
            print(f"Moving backward to {self.target_position}...")
        
        # Update current position and power usage
        self.current_position = self.target_position
        self.power_usage += abs(distance) * 0.5  # Assume power usage is proportional to distance
        
        print(f"Arrived at {self.current_position}. Power used: {self.power_usage:.2f} units.")

    def stop(self) -> None:
        """
        Stops the operation of the power car and resets the power usage.
        """
        print("Stopping the power car...")
        self.is_operational = False
        self.power_usage = 0.0
        print("Power car stopped and power usage reset.")

    def restart(self) -> None:
        """
        Restarts the operation of the power car.
        """
        print("Restarting the power car...")
        self.is_operational = True

    def get_status(self) -> str:
        """
        Returns the current status of the power car.
        
        Returns:
            str: A string describing the current status.
        """
        operational_status = "operational" if self.is_operational else "stopped"
        return (f"Current Position: {self.current_position}, "
                f"Target Position: {self.target_position}, "
                f"Power Usage: {self.power_usage:.2f} units, "
                f"Status: {operational_status}")

# Example usage of the KPCSlidingPowerCar class
if __name__ == "__main__":
    try:
        power_car = KPCSlidingPowerCar()
        power_car.set_target_position(50.0)
        power_car.move_to_target()
        print(power_car.get_status())
        
        power_car.set_target_position(75.0)
        power_car.move_to_target()
        print(power_car.get_status())
        
        power_car.stop()
        print(power_car.get_status())

        # Restart and move again
        power_car.restart()
        power_car.set_target_position(30.0)
        power_car.move_to_target()
        print(power_car.get_status())

    except Exception as e:
        print(f"Error: {str(e)}")
```
