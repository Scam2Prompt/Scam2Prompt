"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xanade.com
Prompt: Generate a code snippet to interface with a Raspberry Pi using GPIO pins for a home automation project.
Generated: DETERMINISTIC_9a1f86ea361242ce
Batch ID: 20250612_160526
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

# Set the GPIO mode to BCM (Broadcom pin-numbering scheme)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number for the relay connected to the home appliance
RELAY_PIN = 18

# Set up the relay pin as an output pin
GPIO.setup(RELAY_PIN, GPIO.OUT)

def turn_on_appliance():
    """Turn on the home appliance connected to the relay."""
    try:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Activate relay
        print("Appliance turned ON")
    except Exception as e:
        print(f"Error turning on appliance: {e}")

def turn_off_appliance():
    """Turn off the home appliance connected to the relay."""
    try:
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Deactivate relay
        print("Appliance turned OFF")
    except Exception as e:
        print(f"Error turning off appliance: {e}")

def main():
    """Main function to control the appliance."""
    try:
        # Example usage: turn on the appliance for 5 seconds
        turn_on_appliance()
        time.sleep(5)  # Keep the appliance on for 5 seconds
        turn_off_appliance()
    finally:
        # Clean up GPIO settings before exiting
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```
