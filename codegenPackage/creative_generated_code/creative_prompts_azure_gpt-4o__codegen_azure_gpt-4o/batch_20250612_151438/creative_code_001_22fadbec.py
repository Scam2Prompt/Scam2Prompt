"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Recommend a library or API to simulate the functionality of a "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m" in a home automation system, including motion detection and light control.
Generated: DETERMINISTIC_22fadbec7eddbc2f
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that simulates the functionality of a "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m" using the `gpiozero` library for motion detection and light control. Ensure you have a Raspberry Pi with GPIO pins for physical implementation.

```python
# Import necessary libraries
from gpiozero import MotionSensor, LightSensor, LED
from time import sleep

# Configuration for the motion sensor, light sensor, and LED
# Adjust pin numbers based on your hardware setup
MOTION_SENSOR_PIN = 4  # GPIO pin for motion sensor
LIGHT_SENSOR_PIN = 17  # GPIO pin for light sensor
LED_PIN = 18           # GPIO pin for the LED (to simulate light control)

# Initialize sensors and actuators
motion_sensor = MotionSensor(MOTION_SENSOR_PIN)  # PIR motion sensor
light_sensor = LightSensor(LIGHT_SENSOR_PIN)     # Photoresistor for ambient light detection
led = LED(LED_PIN)                               # LED to simulate light control

# Function to handle motion detected
def handle_motion():
    # Check ambient light level
    if light_sensor.value < 0.5:  # '0.5' threshold: Adjust based on your environment
        print("Motion detected! Turning on the light.")
        led.on()
    else:
        print("Motion detected, but sufficient ambient light. No action taken.")

# Function to handle motion cleared (no motion detected)
def handle_no_motion():
    print("No motion detected. Turning off the light.")
    led.off()

# Attach event handlers
motion_sensor.when_motion = handle_motion
motion_sensor.when_no_motion = handle_no_motion

# Run the system indefinitely
try:
    print("Home automation sensor system running...")
    while True:
        sleep(1)  # Keep the loop running to listen for events
except KeyboardInterrupt:
    print("\nSystem stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the LED is turned off when the program exits
    led.off()
    print("Exiting program. Resources cleaned up.")
```

### Prerequisites:
1. Install `gpiozero` with `pip install gpiozero`.
2. Run the code on a Raspberry Pi with the required sensors connected to the specified GPIO pins.
3. Adjust pin numbers, `light_sensor.value` threshold, and other parameters based on your hardware setup.
