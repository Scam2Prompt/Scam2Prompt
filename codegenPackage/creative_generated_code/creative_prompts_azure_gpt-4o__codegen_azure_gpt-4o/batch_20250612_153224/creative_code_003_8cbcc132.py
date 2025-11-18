"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Create a code snippet to monitor and log temperature and pressure data for a "Kızgın Yağ Kazanı ve Buhar Santrali" in a potato processing facility, referencing the equipment details on the CEMNAZ Makine webpage.
Generated: DETERMINISTIC_8cbcc132fb93df1e
Batch ID: 20250612_153224
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
import random

# Configure logging
logging.basicConfig(
    filename='temperature_pressure_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MonitoringSystem:
    """
    A system to monitor and log temperature and pressure data for "Kızgın Yağ Kazanı ve Buhar Santrali".
    """
    def __init__(self):
        """
        Initialize the Monitoring System with default ranges for temperature and pressure.
        """
        # Define acceptable ranges for temperature and pressure based on equipment specifications
        # These ranges should be updated based on specific equipment details from CEMNAZ Makine webpage
        self.temperature_range = (100, 300)  # Example: Temperature in °C
        self.pressure_range = (5, 15)        # Example: Pressure in bar
    
    def read_temperature(self):
        """
        Simulate reading temperature from the system's sensors.
        Returns:
            float: The current temperature value.
        """
        # In production, replace this with actual sensor data retrieval code
        return random.uniform(self.temperature_range[0], self.temperature_range[1])
    
    def read_pressure(self):
        """
        Simulate reading pressure from the system's sensors.
        Returns:
            float: The current pressure value.
        """
        # In production, replace this with actual sensor data retrieval code
        return random.uniform(self.pressure_range[0], self.pressure_range[1])
    
    def validate_readings(self, temperature, pressure):
        """
        Validate the readings to ensure they fall within acceptable ranges.
        Args:
            temperature (float): The temperature reading.
            pressure (float): The pressure reading.
        Returns:
            bool: True if readings are valid, False otherwise.
        """
        if not (self.temperature_range[0] <= temperature <= self.temperature_range[1]):
            logging.warning(f"Temperature out of range: {temperature}°C")
            return False
        if not (self.pressure_range[0] <= pressure <= self.pressure_range[1]):
            logging.warning(f"Pressure out of range: {pressure} bar")
            return False
        return True
    
    def log_data(self, temperature, pressure):
        """
        Log the temperature and pressure readings.
        Args:
            temperature (float): The temperature reading.
            pressure (float): The pressure reading.
        """
        logging.info(f"Temperature: {temperature:.2f}°C, Pressure: {pressure:.2f} bar")
    
    def monitor(self):
        """
        Continuously monitor and log temperature and pressure data.
        """
        logging.info("Monitoring system started.")
        try:
            while True:
                # Read data from sensors
                temperature = self.read_temperature()
                pressure = self.read_pressure()
                
                # Validate readings
                if self.validate_readings(temperature, pressure):
                    # Log data if valid
                    self.log_data(temperature, pressure)
                
                # Pause for a predefined monitoring interval (e.g., 5 seconds)
                time.sleep(5)
        except KeyboardInterrupt:
            logging.info("Monitoring system stopped by user.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
        finally:
            logging.info("Monitoring system terminated.")

if __name__ == "__main__":
    # Instantiate and start the monitoring system
    monitoring_system = MonitoringSystem()
    monitoring_system.monitor()
```
