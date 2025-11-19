"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Write a Python script to control an ozone generator, setting the timer based on room size and humidity levels for effective air purification.
Generated: DETERMINISTIC_95e24f50973ae11b
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ozone_generator_controller.py

import logging
import time

# Define logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OzoneGenerator:
    def __init__(self, room_size, humidity_level):
        """
        Initialize the ozone generator controller.

        Args:
            room_size (float): Room size in square meters.
            humidity_level (float): Humidity level as a percentage.
        """
        self.room_size = room_size
        self.humidity_level = humidity_level
        self.timer = 0

    def calculate_timer(self):
        """
        Calculate the timer based on room size and humidity levels.

        Returns:
            int: Timer in minutes.
        """
        # Adjust timer based on room size (larger rooms require longer timers)
        if self.room_size < 100:
            base_timer = 30
        elif self.room_size < 200:
            base_timer = 45
        else:
            base_timer = 60

        # Adjust timer based on humidity levels (higher humidity requires longer timers)
        if self.humidity_level < 40:
            humidity_factor = 1
        elif self.humidity_level < 60:
            humidity_factor = 1.5
        else:
            humidity_factor = 2

        self.timer = int(base_timer * humidity_factor)
        return self.timer

    def start_purification(self):
        """
        Start the air purification process.
        """
        try:
            timer = self.calculate_timer()
            logging.info(f"Starting air purification for {timer} minutes.")
            for minute in range(timer):
                logging.info(f"Purification in progress: {minute+1}/{timer} minutes.")
                time.sleep(60)  # Wait for 1 minute
            logging.info("Air purification complete.")
        except Exception as e:
            logging.error(f"Error during purification: {str(e)}")

    def stop_purification(self):
        """
        Stop the air purification process.
        """
        logging.info("Stopping air purification.")
        # Add code to stop the ozone generator here

def main():
    try:
        room_size = float(input("Enter room size in square meters: "))
        humidity_level = float(input("Enter humidity level as a percentage: "))
        ozone_generator = OzoneGenerator(room_size, humidity_level)
        ozone_generator.start_purification()
    except ValueError:
        logging.error("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
