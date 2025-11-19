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
# Raspberry Pi LED Control Project
# This code uses GPIO pins on a Raspberry Pi to control an LED.
# A button is also used to toggle the LED's state.
# Ensure you have the `RPi.GPIO` library installed before running this code.

import RPi.GPIO as GPIO  # Import the GPIO library
import time  # Import the time library for delays

# Pin configuration
LED_PIN = 18  # Pin connected to the LED
BUTTON_PIN = 17  # Pin connected to the button

def setup():
    """
    Set up the GPIO pins.
    """
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED_PIN as an output
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set BUTTON_PIN as an input with an internal pull-up resistor

def toggle_led():
    """
    Toggles the LED state when the button is pressed.
    """
    led_state = False  # Initial LED state
    try:
        print("Press the button to toggle the LED. Press Ctrl+C to exit.")
        while True:
            button_pressed = not GPIO.input(BUTTON_PIN)  # Check if the button is pressed
            if button_pressed:
                led_state = not led_state  # Toggle the LED state
                GPIO.output(LED_PIN, led_state)  # Set the LED state
                print(f"LED {'ON' if led_state else 'OFF'}")
                time.sleep(0.2)  # Debounce delay
            time.sleep(0.01)  # Small delay to prevent high CPU usage
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        cleanup()

def cleanup():
    """
    Clean up GPIO pins.
    """
    GPIO.output(LED_PIN, False)  # Turn off the LED
    GPIO.cleanup()  # Reset all GPIO pins
    print("GPIO cleanup complete.")

if __name__ == "__main__":
    setup()  # Initialize GPIO pins
    toggle_led()  # Start toggling LED
```

### Requirements:
1. Connect an LED to the Raspberry Pi GPIO pin (e.g., GPIO 18) with a current-limiting resistor.
2. Connect a button to a GPIO pin (e.g., GPIO 17), ensuring the pin is pulled high or low appropriately.
3. Run the code using Python 3 on your Raspberry Pi.
