"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Write a Python script to operate a microwave digestion system, focusing on the specific steps and parameters outlined for the MD6T microwave digestion instrument.
Generated: DETERMINISTIC_d1431188effbcdc1
Batch ID: 20250612_155449
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MicrowaveDigestionSystem:
    def __init__(self):
        """Initialize the microwave digestion system."""
        self.temperature = 0
        self.pressure = 0
        self.time = 0
        self.is_running = False

    def set_parameters(self, temperature, pressure, time):
        """Set the digestion parameters.

        Args:
            temperature (float): The temperature in degrees Celsius.
            pressure (float): The pressure in bar.
            time (int): The digestion time in minutes.

        Raises:
            ValueError: If any parameter is out of range.
        """
        if not (0 <= temperature <= 300):
            raise ValueError("Temperature must be between 0 and 300 degrees Celsius.")
        if not (0 <= pressure <= 10):
            raise ValueError("Pressure must be between 0 and 10 bar.")
        if time <= 0:
            raise ValueError("Time must be greater than 0 minutes.")

        self.temperature = temperature
        self.pressure = pressure
        self.time = time
        logging.info("Parameters set: Temp=%s, Pressure=%s, Time=%s", temperature, pressure, time)

    def start_digestion(self):
        """Start the digestion process."""
        if self.is_running:
            logging.warning("Digestion already in progress.")
            return
        
        logging.info("Starting digestion process...")
        self.is_running = True

        try:
            # Simulate the digestion process
            self._heat_up()
            self._maintain_conditions()
        except Exception as e:
            logging.error("An error occurred during digestion: %s", e)
            self.is_running = False
            return
        
        self.is_running = False
        logging.info("Digestion completed successfully.")

    def _heat_up(self):
        """Simulate the heating process."""
        logging.info("Heating up to %s degrees Celsius...", self.temperature)
        time.sleep(2)  # Simulate time delay
        logging.info("Reached target temperature.")

    def _maintain_conditions(self):
        """Simulate maintaining temperature and pressure conditions."""
        logging.info("Maintaining temperature at %s degrees Celsius and pressure at %s bar for %s minutes...",
                     self.temperature, self.pressure, self.time)
        time.sleep(self.time * 60)  # Simulate duration of the digestion process
        logging.info("Conditions maintained for %s minutes.", self.time)

    def stop_digestion(self):
        """Stop the digestion process."""
        if not self.is_running:
            logging.warning("No digestion process is currently running.")
            return
        
        logging.info("Stopping the digestion process...")
        self.is_running = False
        logging.info("Digestion process stopped.")

if __name__ == "__main__":
    try:
        # Example usage
        digestion_system = MicrowaveDigestionSystem()
        digestion_system.set_parameters(temperature=200, pressure=5, time=10)
        digestion_system.start_digestion()
    except ValueError as ve:
        logging.error("Invalid parameters: %s", ve)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
