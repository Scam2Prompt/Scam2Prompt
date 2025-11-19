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
import time
import logging

# Configuring logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EVOCarController:
    """A class to control the EVO electric flat car using the KP series low-voltage power supply system."""

    def __init__(self, power_supply):
        """
        Initialize the EVOCarController with a power supply instance.
        
        Args:
            power_supply (PowerSupply): An instance of the low-voltage power supply system.
        """
        self.power_supply = power_supply
        self.is_powered = False

    def power_on(self):
        """Power on the car."""
        try:
            if not self.is_powered:
                self.power_supply.turn_on()
                self.is_powered = True
                logging.info("EVO car powered on.")
            else:
                logging.warning("EVO car is already powered on.")
        except Exception as e:
            logging.error(f"Failed to power on the EVO car: {e}")

    def power_off(self):
        """Power off the car."""
        try:
            if self.is_powered:
                self.power_supply.turn_off()
                self.is_powered = False
                logging.info("EVO car powered off.")
            else:
                logging.warning("EVO car is already powered off.")
        except Exception as e:
            logging.error(f"Failed to power off the EVO car: {e}")

    def move(self, direction, speed):
        """
        Move the car in a specified direction at a given speed.
        
        Args:
            direction (str): The direction to move ('forward', 'backward', 'left', 'right').
            speed (float): The speed at which to move (in m/s).
        """
        try:
            if not self.is_powered:
                logging.error("Cannot move the EVO car because it is powered off.")
                return
            
            if direction not in ['forward', 'backward', 'left', 'right']:
                logging.error("Invalid direction. Please choose from 'forward', 'backward', 'left', 'right'.")
                return
            
            logging.info(f"Moving {direction} at {speed} m/s.")
            # Simulating movement (In a real scenario, you'd send commands to the hardware)
            time.sleep(1)  # Simulate time taken to move

            logging.info("Movement completed.")
        except Exception as e:
            logging.error(f"Failed to move the EVO car: {e}")

class PowerSupply:
    """A mock class representing a power supply system for the EVO car."""

    def turn_on(self):
        """Simulate turning on the power supply."""
        logging.info("Power supply turned on.")

    def turn_off(self):
        """Simulate turning off the power supply."""
        logging.info("Power supply turned off.")

# Example usage
if __name__ == "__main__":
    try:
        power_supply = PowerSupply()
        evo_car = EVOCarController(power_supply)

        evo_car.power_on()
        evo_car.move('forward', 5.0)
        evo_car.power_off()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
