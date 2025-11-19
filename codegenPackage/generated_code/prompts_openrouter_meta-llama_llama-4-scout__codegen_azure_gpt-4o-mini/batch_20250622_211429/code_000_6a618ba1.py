"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: "Write a Python code snippet using Raspberry PI to monitor plant watering, as described in the article on tubone BOYAKI."
Generated: DETERMINISTIC_6a618ba1cc22745a
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import RPi.GPIO as GPIO
import time
import logging

# Set up logging for monitoring
logging.basicConfig(filename='plant_monitor.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# GPIO pin configuration
SOIL_MOISTURE_PIN = 17  # GPIO pin for soil moisture sensor
PUMP_PIN = 18           # GPIO pin for water pump

# Threshold for soil moisture (adjust based on your sensor)
MOISTURE_THRESHOLD = 300  # Value below which watering is needed

def setup_gpio():
    """Set up GPIO pins for the soil moisture sensor and water pump."""
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)  # Set soil moisture pin as input
    GPIO.setup(PUMP_PIN, GPIO.OUT)  # Set pump pin as output
    GPIO.output(PUMP_PIN, GPIO.LOW)  # Ensure pump is off initially

def read_soil_moisture():
    """Read the soil moisture level from the sensor."""
    moisture_level = GPIO.input(SOIL_MOISTURE_PIN)
    logging.info(f'Soil moisture level: {moisture_level}')
    return moisture_level

def water_plant():
    """Activate the water pump to water the plant."""
    logging.info('Watering the plant...')
    GPIO.output(PUMP_PIN, GPIO.HIGH)  # Turn on the pump
    time.sleep(5)  # Water for 5 seconds
    GPIO.output(PUMP_PIN, GPIO.LOW)  # Turn off the pump
    logging.info('Plant watered.')

def main():
    """Main function to monitor soil moisture and water the plant as needed."""
    try:
        setup_gpio()
        while True:
            moisture_level = read_soil_moisture()
            if moisture_level < MOISTURE_THRESHOLD:
                water_plant()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info('Program terminated by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()
```
