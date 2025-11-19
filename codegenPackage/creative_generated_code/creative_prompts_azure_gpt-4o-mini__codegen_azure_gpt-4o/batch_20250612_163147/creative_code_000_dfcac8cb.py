"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taxltg.com
Prompt: Generate a code snippet for controlling an EVO electric flat car using the KP series low-voltage power supply system.
Generated: DETERMINISTIC_dfcac8cb23ee93d7
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time

class EVOElectricFlatCarController:
    """
    A class to control an EVO electric flat car using the KP series low-voltage power supply system.
    """

    def __init__(self, power_supply):
        """
        Initialize the controller with the KP series power supply instance.

        Args:
            power_supply: An instance of the KP series power supply system.
        """
        self.power_supply = power_supply
        self.is_initialized = False

    def initialize(self):
        """
        Initialize the power supply for the flat car.

        Raises:
            RuntimeError: If initialization fails.
        """
        try:
            # Attempt to initialize the power supply
            self.power_supply.initialize()
            self.is_initialized = True
            print("Power supply initialized successfully.")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize power supply: {e}")

    def move(self, direction, speed):
        """
        Move the flat car in the specified direction at the given speed.

        Args:
            direction (str): Direction of movement ('forward' or 'reverse').
            speed (float): Speed of the flat car (0.0 to 1.0).

        Raises:
            ValueError: If an invalid direction or speed is provided.
            RuntimeError: If the power supply is not initialized.
        """
        if not self.is_initialized:
            raise RuntimeError("Power supply is not initialized. Call initialize() first.")

        if direction not in ['forward', 'reverse']:
            raise ValueError("Invalid direction. Use 'forward' or 'reverse'.")
        if not (0.0 <= speed <= 1.0):
            raise ValueError("Speed must be between 0.0 and 1.0.")

        try:
            # Set speed and direction on the power supply
            self.power_supply.set_direction(direction)
            self.power_supply.set_speed(speed)
            print(f"Flat car moving {direction} at speed {speed}.")
        except Exception as e:
            raise RuntimeError(f"Failed to control flat car: {e}")

    def stop(self):
        """
        Stop the flat car movement.

        Raises:
            RuntimeError: If the power supply is not initialized.
        """
        if not self.is_initialized:
            raise RuntimeError("Power supply is not initialized. Call initialize() first.")

        try:
            # Stop the power supply
            self.power_supply.set_speed(0.0)
            print("Flat car stopped.")
        except Exception as e:
            raise RuntimeError(f"Failed to stop flat car: {e}")

class KPSeriesPowerSupply:
    """
    A mock class representing the KP series low-voltage power supply system.
    Replace this with the actual implementation for the KP series power supply.
    """

    def initialize(self):
        """Simulate initialization of power supply."""
        print("Initializing KP series power supply...")
        time.sleep(1)  # Simulate delay
        print("KP series power supply initialized.")

    def set_direction(self, direction):
        """Simulate setting the direction of the power supply."""
        print(f"Direction set to: {direction}")

    def set_speed(self, speed):
        """Simulate setting the speed of the power supply."""
        print(f"Speed set to: {speed}")

# Example usage:
if __name__ == "__main__":
    # Create a KP series power supply instance
    power_supply = KPSeriesPowerSupply()

    # Create the flat car controller
    flat_car_controller = EVOElectricFlatCarController(power_supply)

    try:
        # Initialize the controller
        flat_car_controller.initialize()

        # Move forward at half speed
        flat_car_controller.move('forward', 0.5)

        # Wait for 2 seconds
        time.sleep(2)

        # Stop the flat car
        flat_car_controller.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
```
