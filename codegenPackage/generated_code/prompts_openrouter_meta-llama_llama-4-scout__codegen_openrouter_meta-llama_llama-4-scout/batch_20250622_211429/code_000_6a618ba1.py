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
# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime

# Set up GPIO pin numbering
GPIO.setmode(GPIO.BCM)

# Define constants for sensor and relay pins
SOIL_MOISTURE_PIN = 17  # Replace with actual pin number
RELAY_PIN = 23  # Replace with actual pin number

# Set up GPIO pins
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def get_soil_moisture_level():
    """
    Reads the soil moisture level from the sensor.

    Returns:
        int: Soil moisture level (0-100%)
    """
    try:
        # Read soil moisture level (assuming analog output)
        soil_moisture_level = GPIO.input(SOIL_MOISTURE_PIN)
        # Convert to percentage (assuming 0-100% range)
        return int((soil_moisture_level / 1023) * 100)
    except Exception as e:
        print(f"Error reading soil moisture level: {e}")
        return None

def water_plant():
    """
    Activates the relay to water the plant.
    """
    try:
        # Turn on relay to water the plant
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(10)  # Water for 10 seconds
        # Turn off relay
        GPIO.output(RELAY_PIN, GPIO.LOW)
    except Exception as e:
        print(f"Error watering plant: {e}")

def monitor_soil_moisture():
    """
    Monitors soil moisture level and waters the plant if necessary.
    """
    try:
        soil_moisture_level = get_soil_moisture_level()
        if soil_moisture_level is not None and soil_moisture_level < 20:
            print(f"Soil moisture level low ({soil_moisture_level}%): watering plant")
            water_plant()
        else:
            print(f"Soil moisture level OK ({soil_moisture_level}%)")
    except Exception as e:
        print(f"Error monitoring soil moisture: {e}")

def main():
    try:
        while True:
            monitor_soil_moisture()
            time.sleep(60)  # Monitor every 1 minute
    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        # Clean up GPIO pins
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```
