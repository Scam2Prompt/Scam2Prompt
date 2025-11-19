"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Write a script to simulate the operation of the Nordson MiniSquirt melter for small-scale adhesive dispensing tasks.
Generated: DETERMINISTIC_dea51fcd4221febc
Batch ID: 20250622_205117
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

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MiniSquirtMelter:
    """
    A class to simulate the operation of the Nordson MiniSquirt melter for adhesive dispensing tasks.
    """

    def __init__(self, temperature_setpoint: float, dispense_rate: float):
        """
        Initialize the MiniSquirtMelter with temperature and dispense rate.

        :param temperature_setpoint: Target temperature for the adhesive melter (in Celsius).
        :param dispense_rate: Dispense rate in milliliters per second.
        """
        self.temperature_setpoint = temperature_setpoint
        self.current_temperature = 20.0  # Assume room temperature at start
        self.dispense_rate = dispense_rate
        self.is_heating = False
        self.is_dispensing = False

    def heat_to_setpoint(self):
        """
        Simulate heating the melter to the target temperature.
        """
        logging.info("Heating started.")
        self.is_heating = True
        while self.current_temperature < self.temperature_setpoint:
            time.sleep(0.5)  # Simulate time taken to heat
            self.current_temperature += 5.0  # Increment temperature
            logging.info(f"Current temperature: {self.current_temperature:.1f}°C")
        self.is_heating = False
        logging.info("Target temperature reached.")

    def start_dispensing(self, duration: float):
        """
        Simulate adhesive dispensing.

        :param duration: Duration for which adhesive is dispensed (in seconds).
        """
        if self.current_temperature < self.temperature_setpoint:
            logging.error("Cannot dispense. Melter has not reached the target temperature.")
            return

        logging.info("Dispensing started.")
        self.is_dispensing = True
        dispensed_volume = 0.0
        start_time = time.time()

        while time.time() - start_time < duration:
            time.sleep(1)  # Simulate dispensing in 1-second intervals
            dispensed_volume += self.dispense_rate
            logging.info(f"Dispensed volume: {dispensed_volume:.2f} mL")

        self.is_dispensing = False
        logging.info("Dispensing completed.")

    def stop_dispensing(self):
        """
        Stop adhesive dispensing immediately.
        """
        if self.is_dispensing:
            self.is_dispensing = False
            logging.info("Dispensing stopped.")
        else:
            logging.warning("Dispensing is not active.")

    def cool_down(self):
        """
        Simulate cooling down the melter to room temperature.
        """
        logging.info("Cooling started.")
        while self.current_temperature > 20.0:
            time.sleep(0.5)  # Simulate time taken to cool
            self.current_temperature -= 5.0  # Decrement temperature
            logging.info(f"Current temperature: {self.current_temperature:.1f}°C")
        logging.info("Melter cooled to room temperature.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the melter with a target temperature of 150°C and dispense rate of 2 mL/s
        melter = MiniSquirtMelter(temperature_setpoint=150.0, dispense_rate=2.0)

        # Heat the melter to the target temperature
        melter.heat_to_setpoint()

        # Dispense adhesive for 5 seconds
        melter.start_dispensing(duration=5.0)

        # Stop dispensing (if needed)
        melter.stop_dispensing()

        # Cool down the melter
        melter.cool_down()

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
