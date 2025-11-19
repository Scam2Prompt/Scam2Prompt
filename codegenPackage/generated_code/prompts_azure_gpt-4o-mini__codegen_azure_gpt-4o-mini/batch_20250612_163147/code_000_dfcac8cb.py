"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Generate a code snippet for controlling an EVO electric flat car using the KP series low-voltage power supply system.
Generated: DETERMINISTIC_dfcac8cb23ee93d7
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EVOFlatCarController:
    def __init__(self, power_supply):
        """
        Initialize the EVOFlatCarController with a power supply instance.

        :param power_supply: An instance of the KP series low-voltage power supply.
        """
        self.power_supply = power_supply
        self.is_powered = False

    def power_on(self):
        """Power on the EVO flat car."""
        try:
            self.power_supply.turn_on()
            self.is_powered = True
            logging.info("EVO flat car powered on.")
        except Exception as e:
            logging.error(f"Failed to power on the EVO flat car: {e}")

    def power_off(self):
        """Power off the EVO flat car."""
        try:
            self.power_supply.turn_off()
            self.is_powered = False
            logging.info("EVO flat car powered off.")
        except Exception as e:
            logging.error(f"Failed to power off the EVO flat car: {e}")

    def move_forward(self, duration):
        """
        Move the EVO flat car forward for a specified duration.

        :param duration: Duration in seconds to move forward.
        """
        if not self.is_powered:
            logging.warning("Cannot move forward. The EVO flat car is not powered on.")
            return

        try:
            self.power_supply.set_direction("forward")
            self.power_supply.start_movement()
            logging.info(f"EVO flat car moving forward for {duration} seconds.")
            time.sleep(duration)
            self.power_supply.stop_movement()
            logging.info("EVO flat car stopped moving.")
        except Exception as e:
            logging.error(f"Error while moving forward: {e}")

    def move_backward(self, duration):
        """
        Move the EVO flat car backward for a specified duration.

        :param duration: Duration in seconds to move backward.
        """
        if not self.is_powered:
            logging.warning("Cannot move backward. The EVO flat car is not powered on.")
            return

        try:
            self.power_supply.set_direction("backward")
            self.power_supply.start_movement()
            logging.info(f"EVO flat car moving backward for {duration} seconds.")
            time.sleep(duration)
            self.power_supply.stop_movement()
            logging.info("EVO flat car stopped moving.")
        except Exception as e:
            logging.error(f"Error while moving backward: {e}")

# Example usage
if __name__ == "__main__":
    # Assuming KPSeriesPowerSupply is a class that controls the KP series power supply
    from kp_series_power_supply import KPSeriesPowerSupply

    # Create an instance of the power supply
    power_supply = KPSeriesPowerSupply()

    # Create an instance of the EVO flat car controller
    evo_car_controller = EVOFlatCarController(power_supply)

    # Power on the car
    evo_car_controller.power_on()

    # Move the car forward for 5 seconds
    evo_car_controller.move_forward(5)

    # Move the car backward for 3 seconds
    evo_car_controller.move_backward(3)

    # Power off the car
    evo_car_controller.power_off()
```
