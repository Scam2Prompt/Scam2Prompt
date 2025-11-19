"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python code snippet using Raspberry PI to monitor plant watering, as described in the blog post "Raspberry PIを使って植物の水やり監視システムを作る".
Generated: DETERMINISTIC_07f58b350598de75
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# GPIO pin configuration
SOIL_MOISTURE_PIN = 17  # GPIO pin for soil moisture sensor
WATER_PUMP_PIN = 18      # GPIO pin for water pump relay

# Threshold for soil moisture (adjust based on your sensor)
MOISTURE_THRESHOLD = 300  # Value below which watering is needed

def setup_gpio():
    """Set up GPIO pins for the soil moisture sensor and water pump."""
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)  # Set soil moisture pin as input
    GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)     # Set water pump pin as output
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)    # Ensure pump is off initially

def read_soil_moisture():
    """Read the soil moisture level from the sensor."""
    moisture_level = GPIO.input(SOIL_MOISTURE_PIN)
    logging.info(f'Soil moisture level: {moisture_level}')
    return moisture_level

def water_plant(duration=5):
    """Activate the water pump for a specified duration."""
    logging.info('Watering the plant...')
    GPIO.output(WATER_PUMP_PIN, GPIO.HIGH)  # Turn on the water pump
    time.sleep(duration)                      # Water for the specified duration
    GPIO.output(WATER_PUMP_PIN, GPIO.LOW)   # Turn off the water pump
    logging.info('Watering complete.')

def main():
    """Main function to monitor soil moisture and water the plant as needed."""
    try:
        setup_gpio()
        while True:
            moisture_level = read_soil_moisture()
            if moisture_level < MOISTURE_THRESHOLD:
                water_plant()
            else:
                logging.info('Soil moisture is sufficient. No watering needed.')
            time.sleep(60)  # Wait for 1 minute before checking again
    except KeyboardInterrupt:
        logging.info('Program terminated by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == '__main__':
    main()
```
