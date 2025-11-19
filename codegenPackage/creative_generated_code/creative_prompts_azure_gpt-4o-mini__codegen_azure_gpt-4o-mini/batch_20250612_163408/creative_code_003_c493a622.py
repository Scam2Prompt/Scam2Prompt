"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Can you demonstrate how to create a plant watering monitoring system using Raspberry Pi, based on the instructions from tubone BOYAKI?
Generated: DETERMINISTIC_c493a62287bc1fb0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import RPi.GPIO as GPIO
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
SOIL_MOISTURE_PIN = 17  # Pin for soil moisture sensor
WATER_PUMP_PIN = 27      # Pin for water pump relay

# Set up GPIO pins
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)  # Soil moisture sensor as input
GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)    # Water pump as output

def read_soil_moisture():
    """Read the soil moisture level."""
    try:
        moisture_level = GPIO.input(SOIL_MOISTURE_PIN)
        logging.info("Soil Moisture Level: %s", moisture_level)
        return moisture_level
    except Exception as e:
        logging.error("Error reading soil moisture: %s", e)
        return None

def activate_water_pump(duration):
    """Activate the water pump for a specified duration."""
    try:
        logging.info("Activating water pump for %d seconds", duration)
        GPIO.output(WATER_PUMP_PIN, GPIO.HIGH)  # Turn on the pump
        time.sleep(duration)                     # Keep it on for the specified duration
        GPIO.output(WATER_PUMP_PIN, GPIO.LOW)   # Turn off the pump
        logging.info("Water pump deactivated")
    except Exception as e:
        logging.error("Error activating water pump: %s", e)

def main():
    """Main function to monitor soil moisture and water the plant."""
    try:
        logging.info("Plant Watering Monitoring System Started")
        while True:
            moisture_level = read_soil_moisture()
            if moisture_level is not None:
                # If soil is dry (assuming 0 means dry)
                if moisture_level == 0:
                    activate_water_pump(5)  # Activate pump for 5 seconds
                else:
                    logging.info("Soil is moist, no need to water.")
            time.sleep(60)  # Wait for 1 minute before next reading
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    except Exception as e:
        logging.error("An error occurred: %s", e)
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
        logging.info("GPIO cleanup completed. Exiting program.")

if __name__ == "__main__":
    main()
```
