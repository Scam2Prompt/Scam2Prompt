"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Provide an example of code to manage nitrogen generation for adhesive systems, inspired by Nordson's nitrogen generation machines.
Generated: DETERMINISTIC_ae39ba7411a88eab
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# nitrogen_generator.py

import time
import logging
from typing import Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class NitrogenGenerator:
    """
    Class to manage nitrogen generation for adhesive systems.
    Inspired by Nordson's nitrogen generation machines.
    """
    def __init__(self, target_purity: float, max_pressure: float, min_pressure: float):
        """
        Initialize the nitrogen generator system.

        :param target_purity: Desired nitrogen purity percentage (0-100).
        :param max_pressure: Maximum pressure threshold (in PSI).
        :param min_pressure: Minimum pressure threshold (in PSI).
        """
        self.target_purity = target_purity
        self.max_pressure = max_pressure
        self.min_pressure = min_pressure
        self.current_pressure = 0
        self.current_purity = 0
        self.is_running = False
        logging.info("Nitrogen Generator initialized.")

    def start(self):
        """
        Start the nitrogen generation process.
        """
        if self.is_running:
            logging.warning("Nitrogen Generator is already running.")
            return

        self.is_running = True
        logging.info("Nitrogen Generation started.")
        self._simulate_nitrogen_generation()

    def stop(self):
        """
        Stop the nitrogen generation process.
        """
        if not self.is_running:
            logging.warning("Nitrogen Generator is not running.")
            return

        self.is_running = False
        logging.info("Nitrogen Generation stopped.")

    def _simulate_nitrogen_generation(self):
        """
        Simulate the nitrogen generation process.
        Adjusts purity and pressure levels incrementally.
        """
        try:
            while self.is_running:
                # Simulate purity adjustment
                if self.current_purity < self.target_purity:
                    self.current_purity += 0.5  # Increment purity
                elif self.current_purity > self.target_purity:
                    self.current_purity -= 0.5  # Decrement purity

                # Simulate pressure adjustment
                if self.current_pressure < self.max_pressure:
                    self.current_pressure += 1  # Increment pressure
                elif self.current_pressure > self.max_pressure:
                    logging.warning("Pressure exceeds maximum threshold. Reducing pressure.")
                    self.current_pressure -= 1  # Reduce pressure

                # Ensure pressure doesn't fall below minimum
                if self.current_pressure < self.min_pressure:
                    logging.warning("Pressure below minimum threshold. Increasing pressure.")
                    self.current_pressure += 1  # Increase pressure

                logging.info(f"Current Purity: {self.current_purity:.2f}%, Current Pressure: {self.current_pressure} PSI")

                # Simulate time delay for the generation process
                time.sleep(1)
        except Exception as e:
            logging.error(f"An error occurred during nitrogen generation: {e}")
            self.stop()

    def get_status(self) -> dict:
        """
        Get the current status of the nitrogen generator.

        :return: A dictionary containing the current purity, pressure, and running status.
        """
        return {
            "is_running": self.is_running,
            "current_purity": self.current_purity,
            "current_pressure": self.current_pressure,
            "target_purity": self.target_purity,
            "max_pressure": self.max_pressure,
            "min_pressure": self.min_pressure
        }

    def adjust_target_purity(self, new_purity: Union[int, float]):
        """
        Adjust the target nitrogen purity level.

        :param new_purity: New desired nitrogen purity percentage (0-100).
        """
        if not 0 <= new_purity <= 100:
            logging.error("Invalid purity level. Must be between 0 and 100.")
            return
        self.target_purity = new_purity
        logging.info(f"Target purity adjusted to {new_purity}%.")

    def adjust_pressure_thresholds(self, new_min_pressure: Union[int, float], new_max_pressure: Union[int, float]):
        """
        Adjust the pressure thresholds.

        :param new_min_pressure: New minimum pressure threshold.
        :param new_max_pressure: New maximum pressure threshold.
        """
        if new_min_pressure < 0 or new_max_pressure < 0 or new_min_pressure >= new_max_pressure:
            logging.error("Invalid pressure thresholds. Ensure min < max and values are non-negative.")
            return
        self.min_pressure = new_min_pressure
        self.max_pressure = new_max_pressure
        logging.info(f"Pressure thresholds adjusted: Min = {new_min_pressure} PSI, Max = {new_max_pressure} PSI.")


# Example usage
if __name__ == "__main__":
    generator = NitrogenGenerator(target_purity=99.9, max_pressure=120, min_pressure=80)
    generator.start()
    time.sleep(10)  # Run for 10 seconds
    generator.stop()
    print(generator.get_status())
```
