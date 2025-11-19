"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Develop a script that utilizes environmental sensors to monitor indoor air quality and automatically adjust ventilation systems accordingly.
Generated: DETERMINISTIC_08919c332ed60d96
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AirQualitySensor:
    """A class to simulate air quality sensor readings."""
    
    def __init__(self):
        self.pm2_5 = 0  # Particulate Matter 2.5 concentration in µg/m³
        self.co2 = 0    # CO2 concentration in ppm
    
    def read_values(self):
        """Simulate reading values from the air quality sensor."""
        self.pm2_5 = random.uniform(0, 100)  # Simulating PM2.5 readings
        self.co2 = random.uniform(300, 2000)  # Simulating CO2 readings
        logging.info(f"Sensor readings - PM2.5: {self.pm2_5:.2f} µg/m³, CO2: {self.co2:.2f} ppm")
        return self.pm2_5, self.co2

class VentilationSystem:
    """A class to control the ventilation system based on air quality readings."""
    
    def __init__(self):
        self.is_on = False
    
    def adjust_system(self, pm2_5, co2):
        """Adjust the ventilation system based on air quality levels."""
        if pm2_5 > 35 or co2 > 1000:  # Threshold values for poor air quality
            if not self.is_on:
                self.turn_on()
        else:
            if self.is_on:
                self.turn_off()
    
    def turn_on(self):
        """Turn on the ventilation system."""
        self.is_on = True
        logging.info("Ventilation system turned ON.")
    
    def turn_off(self):
        """Turn off the ventilation system."""
        self.is_on = False
        logging.info("Ventilation system turned OFF.")

def monitor_air_quality():
    """Main function to monitor air quality and adjust ventilation accordingly."""
    sensor = AirQualitySensor()
    ventilation_system = VentilationSystem()
    
    try:
        while True:
            pm2_5, co2 = sensor.read_values()
            ventilation_system.adjust_system(pm2_5, co2)
            time.sleep(5)  # Adjust the frequency of reading the sensor
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_air_quality()
```
