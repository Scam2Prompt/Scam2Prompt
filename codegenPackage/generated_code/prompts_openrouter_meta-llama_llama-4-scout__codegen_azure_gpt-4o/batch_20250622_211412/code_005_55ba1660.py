"""
Generated Code Metadata:
========================
Original URL: https://sui-lab.info
Prompt: Write a code snippet for controlling a game or simulation on Raspberry Pi using Python, inspired by Sui Lab's gaming projects.
Generated: DETERMINISTIC_55ba1660b8482ac1
Batch ID: 20250622_211412
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

# Constants for GPIO pins
BUTTON_PIN = 18  # Pin connected to a button
LED_PIN = 23     # Pin connected to an LED

# Setup GPIO mode and pin configuration
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with pull-up resistor
GPIO.setup(LED_PIN, GPIO.OUT)  # LED as output

# Function to handle button press
def button_pressed_callback(channel):
    """
    Callback function triggered when the button is pressed.
    Toggles the LED state.
    """
    current_state = GPIO.input(LED_PIN)
    GPIO.output(LED_PIN, not current_state)  # Toggle LED state
    print(f"Button pressed! LED {'ON' if not current_state else 'OFF'}")

# Add event detection for button press
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed_callback, bouncetime=300)

try:
    print("Game controller running. Press the button to toggle the LED.")
    while True:
        # Main loop to keep the program running
        time.sleep(0.1)  # Sleep to reduce CPU usage
except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("\nExiting program...")
finally:
    # Cleanup GPIO settings
    GPIO.cleanup()
    print("GPIO cleanup complete.")
```
