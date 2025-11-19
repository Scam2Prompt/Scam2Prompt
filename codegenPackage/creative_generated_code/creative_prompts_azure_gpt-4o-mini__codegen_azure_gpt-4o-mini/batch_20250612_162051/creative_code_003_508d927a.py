"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Develop a sample application that showcases the use of VinaRoy's air blower FB200 in cement industry processes.
Generated: DETERMINISTIC_508d927a3465d28b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time

# Configuring logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AirBlowerFB200:
    """
    A class to represent the VinaRoy FB200 air blower used in cement industry processes.
    """

    def __init__(self, blower_id: str):
        """
        Initializes the air blower with a unique ID.
        
        Parameters:
        blower_id (str): Unique identifier for the air blower.
        """
        self.blower_id = blower_id
        self.is_on = False  # State to track if the blower is on
        logging.info(f'AirBlowerFB200 initialized with ID: {self.blower_id}')

    def turn_on(self):
        """Turns on the air blower."""
        if not self.is_on:
            self.is_on = True
            logging.info(f'AirBlower {self.blower_id} turned ON.')
        else:
            logging.warning(f'AirBlower {self.blower_id} is already ON.')

    def turn_off(self):
        """Turns off the air blower."""
        if self.is_on:
            self.is_on = False
            logging.info(f'AirBlower {self.blower_id} turned OFF.')
        else:
            logging.warning(f'AirBlower {self.blower_id} is already OFF.')

    def blow_air(self, duration: float):
        """
        Simulates blowing air for a specified duration.

        Parameters:
        duration (float): Duration in seconds for which the air blower should operate.
        
        Raises:
        ValueError: If the blower is not turned on or if the duration is negative.
        """
        if not self.is_on:
            logging.error(f'Cannot blow air. AirBlower {self.blower_id} is OFF.')
            raise ValueError(f'AirBlower {self.blower_id} is OFF. Please turn it ON before blowing air.')

        if duration < 0:
            logging.error('Duration must be a non-negative value.')
            raise ValueError('Duration must be a non-negative value.')

        logging.info(f'AirBlower {self.blower_id} is blowing air for {duration} seconds.')
        time.sleep(duration)  # Simulating the air blowing process
        logging.info(f'AirBlower {self.blower_id} finished blowing air.')

# Sample usage of the AirBlowerFB200 class
if __name__ == "__main__":
    try:
        # Create an instance of the air blower
        air_blower = AirBlowerFB200(blower_id="Blower-001")

        # Turn on the air blower
        air_blower.turn_on()

        # Blow air for 5 seconds
        air_blower.blow_air(duration=5)

        # Turn off the air blower
        air_blower.turn_off()
        
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
