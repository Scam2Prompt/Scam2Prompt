"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Develop a Raspberry Pi project to monitor plant watering systems, referencing the tutorial from the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_0cd14442de269042
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Raspberry Pi Plant Watering System Monitor
Author: [Your Name]
Description: This project monitors soil moisture levels and provides real-time feedback via LED indicators.
Requirements:
- Raspberry Pi (any model)
- Soil moisture sensor
- LEDs (Red, Green)
- Resistors for LEDs (220Ω recommended)
- Breadboard and jumper wires
- Python 3
"""

import RPi.GPIO as GPIO
import time

# Pin configuration
SOIL_SENSOR_PIN = 18  # GPIO pin for soil moisture sensor
RED_LED_PIN = 23      # GPIO pin for red LED
GREEN_LED_PIN = 24    # GPIO pin for green LED

# Threshold value for dry/wet soil (adjust based on sensor sensitivity)
MOISTURE_THRESHOLD = 400

def setup_pins():
    """
    Sets up GPIO pins for the soil moisture sensor and LEDs.
    """
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)  # Soil moisture sensor pin (input)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)    # Red LED pin (output)
    GPIO.setup(GREEN_LED_PIN, GPIO.OUT)  # Green LED pin (output)

def read_soil_moisture():
    """
    Reads the soil moisture level from the sensor.
    Returns True if moisture is above the threshold (wet soil), otherwise False.
    """
    try:
        moisture_level = GPIO.input(SOIL_SENSOR_PIN)
        return moisture_level
    except Exception as e:
        print(f"Error reading soil moisture sensor: {e}")
        return None

def update_leds(is_soil_wet):
    """
    Updates the LEDs based on the moisture level.
    - Green LED turns on if soil is wet.
    - Red LED turns on if soil is dry.
    """
    try:
        if is_soil_wet:
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            GPIO.output(RED_LED_PIN, GPIO.LOW)
        else:
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
    except Exception as e:
        print(f"Error updating LEDs: {e}")

def cleanup():
    """
    Cleans up GPIO settings after program termination.
    """
    GPIO.cleanup()

def main():
    """
    Main function to monitor soil moisture levels and update LEDs in real time.
    """
    print("Starting Plant Watering System Monitor...")
    setup_pins()

    try:
        while True:
            moisture_level = read_soil_moisture()
            if moisture_level is None:
                print("Skipping due to sensor read error.")
                continue

            print(f"Moisture Level: {'Wet' if moisture_level else 'Dry'}")
            update_leds(moisture_level)

            time.sleep(2)  # Pause for 2 seconds before the next reading
    except KeyboardInterrupt:
        print("\nProgram interrupted. Cleaning up...")
    finally:
        cleanup()
        print("Program terminated.")

if __name__ == "__main__":
    main()
```
