"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Generate code to interface with a paddy dryer system, incorporating features like heat exchangers and blowers as described on Mechano Solutions' website.
Generated: DETERMINISTIC_fbd0120ac6990aed
Batch ID: 20250612_162106
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaddyDryerSystem:
    def __init__(self):
        """Initialize the Paddy Dryer System with default states."""
        self.heat_exchanger_status = False
        self.blower_status = False
        self.temperature = 25  # Default temperature in Celsius
        self.humidity = 60     # Default humidity in percentage

    def turn_on_heat_exchanger(self):
        """Turn on the heat exchanger."""
        if not self.heat_exchanger_status:
            self.heat_exchanger_status = True
            logging.info("Heat exchanger turned ON.")
        else:
            logging.warning("Heat exchanger is already ON.")

    def turn_off_heat_exchanger(self):
        """Turn off the heat exchanger."""
        if self.heat_exchanger_status:
            self.heat_exchanger_status = False
            logging.info("Heat exchanger turned OFF.")
        else:
            logging.warning("Heat exchanger is already OFF.")

    def turn_on_blower(self):
        """Turn on the blower."""
        if not self.blower_status:
            self.blower_status = True
            logging.info("Blower turned ON.")
        else:
            logging.warning("Blower is already ON.")

    def turn_off_blower(self):
        """Turn off the blower."""
        if self.blower_status:
            self.blower_status = False
            logging.info("Blower turned OFF.")
        else:
            logging.warning("Blower is already OFF.")

    def set_temperature(self, temp):
        """Set the desired temperature for the drying process.
        
        Args:
            temp (float): Desired temperature in Celsius.
        
        Raises:
            ValueError: If the temperature is out of the acceptable range.
        """
        if 20 <= temp <= 80:  # Acceptable temperature range
            self.temperature = temp
            logging.info(f"Temperature set to {self.temperature}°C.")
        else:
            logging.error("Temperature out of range. Must be between 20°C and 80°C.")
            raise ValueError("Temperature must be between 20°C and 80°C.")

    def set_humidity(self, humidity):
        """Set the desired humidity level for the drying process.
        
        Args:
            humidity (float): Desired humidity in percentage.
        
        Raises:
            ValueError: If the humidity is out of the acceptable range.
        """
        if 30 <= humidity <= 70:  # Acceptable humidity range
            self.humidity = humidity
            logging.info(f"Humidity set to {self.humidity}%.")
        else:
            logging.error("Humidity out of range. Must be between 30% and 70%.")
            raise ValueError("Humidity must be between 30% and 70%.")

    def monitor_system(self):
        """Monitor the system status and log the current settings."""
        logging.info(f"System Status: Heat Exchanger: {'ON' if self.heat_exchanger_status else 'OFF'}, "
                     f"Blower: {'ON' if self.blower_status else 'OFF'}, "
                     f"Temperature: {self.temperature}°C, "
                     f"Humidity: {self.humidity}%.")

    def run_drying_cycle(self, duration):
        """Run the drying cycle for a specified duration.
        
        Args:
            duration (int): Duration of the drying cycle in seconds.
        
        Raises:
            ValueError: If the duration is not positive.
        """
        if duration <= 0:
            logging.error("Duration must be a positive integer.")
            raise ValueError("Duration must be a positive integer.")
        
        self.turn_on_heat_exchanger()
        self.turn_on_blower()
        logging.info(f"Starting drying cycle for {duration} seconds.")
        
        time.sleep(duration)  # Simulate the drying process
        
        self.turn_off_blower()
        self.turn_off_heat_exchanger()
        logging.info("Drying cycle completed.")

# Example usage
if __name__ == "__main__":
    try:
        dryer = PaddyDryerSystem()
        dryer.set_temperature(60)
        dryer.set_humidity(50)
        dryer.monitor_system()
        dryer.run_drying_cycle(10)  # Run for 10 seconds
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
