"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Recommend tools and write code for embedded systems development, referencing APTRON Gurgaon’s Embedded Systems training.
Generated: DETERMINISTIC_f3fa3f2a2e094498
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for embedded systems development
import time       # For time-related functions
import RPi.GPIO as GPIO  # Raspberry Pi GPIO library

# Constants for GPIO pins
LED_PIN = 18      # Define the GPIO pin for the LED
BUTTON_PIN = 17   # Define the GPIO pin for the button

def setup():
    """Configure the GPIO pins and initial settings."""
    GPIO.setmode(GPIO.BCM)        # Use BCM pin numbering
    GPIO.setup(LED_PIN, GPIO.OUT) # Set LED pin as output
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set button pin as input with pull-up resistor

def blink_led(duration):
    """Blink the LED for a specified duration.

    Args:
        duration (float): Time in seconds for which the LED should blink.
    """
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
    time.sleep(duration)               # Keep it on for the specified duration
    GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off

def button_pressed_callback(channel):
    """Callback function to handle button press events.

    Args:
        channel (int): The pin number that triggered the callback.
    """
    print("Button pressed! Blinking LED.")
    blink_led(1)  # Blink the LED for 1 second

def main():
    """Main function to set up the environment and run the loop."""
    try:
        setup()  # Set up GPIO pins
        # Add event detection for button press
        GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed_callback, bouncetime=300)

        print("Press the button to blink the LED. Ctrl+C to exit.")
        # Main program loop
        while True:
            time.sleep(0.1)  # Sleep to reduce CPU usage

    except KeyboardInterrupt:
        print("Exiting program.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings on exit

if __name__ == "__main__":
    main()  # Run the main function
```
