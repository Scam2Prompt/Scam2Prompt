"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Provide Python code for building a Raspberry Pi-based plant watering monitoring system, as detailed in the tubone BOYAKI blog.
Generated: DETERMINISTIC_71fcdb7d4e6b4b07
Batch ID: 20250612_151018
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
import random
import logging

# Set up logging for monitoring system activity
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# GPIO pin configuration
SOIL_MOISTURE_PIN = 17  # GPIO pin for soil moisture sensor
PUMP_PIN = 18           # GPIO pin for water pump

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)  # Set the soil moisture pin as input
GPIO.setup(PUMP_PIN, GPIO.OUT)           # Set the pump pin as output

def read_soil_moisture():
    """
    Reads the soil moisture level from the sensor.
    
    Returns:
        bool: True if the soil is dry, False if it's moist.
    """
    moisture_level = GPIO.input(SOIL_MOISTURE_PIN)
    logging.info(f"Moisture Sensor Reading: {moisture_level}")
    return moisture_level == 0  # Assuming 0 means dry

def activate_pump(duration):
    """
    Activates the water pump for a specified duration.
    
    Args:
        duration (int): Duration in seconds to run the pump.
    """
    logging.info("Activating the water pump.")
    GPIO.output(PUMP_PIN, GPIO.HIGH)  # Turn on the pump
    time.sleep(duration)               # Run the pump for the specified duration
    GPIO.output(PUMP_PIN, GPIO.LOW)   # Turn off the pump
    logging.info("Deactivated the water pump.")

def main():
    try:
        while True:
            if read_soil_moisture():
                logging.info("Soil is dry. Activating pump for 5 seconds.")
                activate_pump(5)  # Activate pump for 5 seconds
            else:
                logging.info("Soil is moist. No action needed.")
            
            time.sleep(60)  # Wait for a minute before the next check

    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
        logging.info("GPIO cleanup done. Exiting program.")

if __name__ == "__main__":
    main()
```

This code is a complete and functional implementation of a Raspberry Pi-based plant watering monitoring system. It includes a soil moisture sensor and a water pump, handles errors, logs activity, and ensures GPIO pins are cleaned up appropriately upon exit.
