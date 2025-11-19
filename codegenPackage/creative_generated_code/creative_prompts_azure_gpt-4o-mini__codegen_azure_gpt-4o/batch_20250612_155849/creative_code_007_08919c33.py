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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Mock sensor and ventilation system interaction
class AirQualitySensor:
    """
    Simulates an air quality sensor that provides readings for CO2, VOCs, and PM2.5 levels.
    """
    def get_readings(self):
        """
        Randomly generates air quality readings for simulation purposes.
        
        Returns:
            dict: Air quality readings including CO2, VOC, and PM2.5 levels.
        """
        return {
            "CO2": random.randint(400, 1500),  # Parts per million (ppm)
            "VOC": random.randint(0, 300),    # Parts per billion (ppb)
            "PM2.5": random.uniform(0, 50)   # Micrograms per cubic meter (µg/m³)
        }

class VentilationSystem:
    """
    Simulates a ventilation system that can adjust its operation based on air quality.
    """
    def __init__(self):
        self.state = "OFF"  # State can be "OFF", "LOW", "MEDIUM", "HIGH"

    def adjust(self, state):
        """
        Adjusts the ventilation system to the specified state.
        
        Args:
            state (str): Desired ventilation state ("OFF", "LOW", "MEDIUM", or "HIGH").
        """
        self.state = state
        logging.info(f"Ventilation system adjusted to: {self.state}")

def calculate_ventilation_level(readings):
    """
    Determines the appropriate ventilation level based on air quality readings.
    
    Args:
        readings (dict): Air quality readings (CO2, VOC, PM2.5).
        
    Returns:
        str: Ventilation level ("OFF", "LOW", "MEDIUM", "HIGH").
    """
    co2 = readings["CO2"]
    voc = readings["VOC"]
    pm25 = readings["PM2.5"]

    # Determine ventilation level based on thresholds
    if co2 > 1000 or voc > 150 or pm25 > 35:
        return "HIGH"
    elif co2 > 800 or voc > 100 or pm25 > 25:
        return "MEDIUM"
    elif co2 > 600 or voc > 50 or pm25 > 15:
        return "LOW"
    else:
        return "OFF"

def main():
    """
    Main function to monitor air quality and control ventilation system.
    """
    sensor = AirQualitySensor()
    ventilation_system = VentilationSystem()

    try:
        while True:
            # Get air quality readings
            readings = sensor.get_readings()
            logging.info(f"Air quality readings: {readings}")

            # Determine ventilation level
            ventilation_level = calculate_ventilation_level(readings)

            # Adjust ventilation system
            ventilation_system.adjust(ventilation_level)

            # Wait before the next reading (e.g., 5 seconds)
            time.sleep(5)

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
