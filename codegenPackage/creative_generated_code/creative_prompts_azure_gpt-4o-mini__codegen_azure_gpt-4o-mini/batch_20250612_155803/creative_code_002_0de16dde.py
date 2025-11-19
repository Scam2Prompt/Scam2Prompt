"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-lab.info
Prompt: Can you provide a code example for a project using Raspberry Pi that involves electronic accessories, as discussed on すいラボ?
Generated: DETERMINISTIC_0de16dde274feed9
Batch ID: 20250612_155803
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

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the LED and button
LED_PIN = 18  # GPIO pin for the LED
BUTTON_PIN = 17  # GPIO pin for the button

# Setup GPIO pins
GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED pin as output
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set button pin as input with pull-up resistor

def button_callback(channel):
    """Callback function to handle button press event."""
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button is pressed
        print("Button pressed! Toggling LED.")
        GPIO.output(LED_PIN, not GPIO.input(LED_PIN))  # Toggle LED state

try:
    # Add event detection for button presses
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=300)
    
    print("Press the button to toggle the LED. CTRL+C to exit.")
    
    # Keep the program running
    while True:
        time.sleep(0.1)  # Sleep to reduce CPU usage

except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
    print("GPIO cleanup complete. Exiting program.")
```
