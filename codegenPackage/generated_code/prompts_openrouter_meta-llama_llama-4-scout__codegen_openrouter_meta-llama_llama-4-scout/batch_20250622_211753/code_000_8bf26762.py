"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Write a Python code snippet to control an ozone generator using a Raspberry Pi, including a timer for automatic shutdown after a specified duration.
Generated: DETERMINISTIC_8bf267623a1ad640
Batch ID: 20250622_211753
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
import argparse

# Define constants
OZONE_GENERATOR_PIN = 17  # GPIO pin connected to ozone generator
DEFAULT_DURATION = 60  # default duration in minutes

def setup_gpio():
    """Setup GPIO pin as output"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OZONE_GENERATOR_PIN, GPIO.OUT)

def turn_on_ozone_generator():
    """Turn on ozone generator"""
    GPIO.output(OZONE_GENERATOR_PIN, GPIO.HIGH)

def turn_off_ozone_generator():
    """Turn off ozone generator"""
    GPIO.output(OZONE_GENERATOR_PIN, GPIO.LOW)

def main():
    parser = argparse.ArgumentParser(description='Control ozone generator with timer')
    parser.add_argument('-d', '--duration', type=int, default=DEFAULT_DURATION, help='Duration in minutes')
    args = parser.parse_args()

    try:
        setup_gpio()
        turn_on_ozone_generator()
        print(f"Ozone generator turned on for {args.duration} minutes")

        # Convert duration to seconds
        duration_seconds = args.duration * 60
        time.sleep(duration_seconds)
        turn_off_ozone_generator()
        print("Ozone generator turned off")
    except KeyboardInterrupt:
        turn_off_ozone_generator()
        print("\nOzone generator turned off due to interrupt")
    except Exception as e:
        turn_off_ozone_generator()
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```
