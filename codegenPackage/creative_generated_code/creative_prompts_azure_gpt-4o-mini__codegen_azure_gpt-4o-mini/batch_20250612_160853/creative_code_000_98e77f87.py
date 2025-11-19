"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Generate a code snippet for creating a custom LED sign using the specifications and materials mentioned on the Nova Forma website.
Generated: DETERMINISTIC_98e77f876a19a8d2
Batch ID: 20250612_160853
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

# Define the GPIO pins for the LED sign
LED_PINS = [17, 18, 27, 22, 23, 24, 25, 4]  # Example GPIO pins for an 8-LED sign

# Function to initialize GPIO settings
def setup_gpio():
    """Set up the GPIO pins for output."""
    GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)  # Set each pin as output

# Function to light up the LEDs in a sequence
def light_up_sequence():
    """Light up the LEDs in a sequence."""
    try:
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)  # Turn on the LED
            time.sleep(0.5)               # Wait for half a second
            GPIO.output(pin, GPIO.LOW)   # Turn off the LED
    except Exception as e:
        print(f"An error occurred while lighting up LEDs: {e}")

# Function to clean up GPIO settings
def cleanup_gpio():
    """Clean up GPIO settings before exiting."""
    GPIO.cleanup()  # Reset all GPIO pins used in this program

if __name__ == "__main__":
    setup_gpio()  # Initialize GPIO settings
    try:
        while True:
            light_up_sequence()  # Continuously light up LEDs
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        cleanup_gpio()  # Ensure GPIO cleanup on exit
```

### Note:
- To run this code, you need a Raspberry Pi with the RPi.GPIO library installed.
- Make sure you have connected the LEDs to the specified GPIO pins properly.
- Adjust the `LED_PINS` list according to your actual GPIO pin connections.
