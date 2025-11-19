"""
Generated Code Metadata:
========================
Original URL: https://xanade.com
Prompt: Write a Python code snippet using the Raspberry Pi 5 single-board computer (8GB) to control an XL6019 5A DC-DC adjustable voltage boost power supply module.
Generated: DETERMINISTIC_f9b22ef63e47f94e
Batch ID: 20250622_205514
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

# Constants
PWM_PIN = 18  # GPIO pin connected to the XL6019's EN pin
PWM_FREQUENCY = 1000  # PWM frequency in Hz
VOLTAGE_MIN = 3.3  # Minimum output voltage (V)
VOLTAGE_MAX = 35.0  # Maximum output voltage (V)
DUTY_CYCLE_MIN = 0.0  # Minimum duty cycle (0%)
DUTY_CYCLE_MAX = 100.0  # Maximum duty cycle (100%)

class XL6019Controller:
    def __init__(self):
        """Initialize the XL6019 controller."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PWM_PIN, GPIO.OUT)
        self.pwm = GPIO.PWM(PWM_PIN, PWM_FREQUENCY)
        self.pwm.start(0)  # Start PWM with 0% duty cycle

    def set_voltage(self, target_voltage):
        """
        Set the output voltage of the XL6019 module.
        
        Args:
            target_voltage (float): Desired output voltage (3.3V to 35V)
        
        Raises:
            ValueError: If target voltage is out of range
        """
        if not VOLTAGE_MIN <= target_voltage <= VOLTAGE_MAX:
            raise ValueError(f"Voltage must be between {VOLTAGE_MIN}V and {VOLTAGE_MAX}V")
        
        # Calculate duty cycle (simplified linear approximation)
        duty_cycle = ((target_voltage - VOLTAGE_MIN) / (VOLTAGE_MAX - VOLTAGE_MIN)) * 100
        duty_cycle = max(DUTY_CYCLE_MIN, min(DUTY_CYCLE_MAX, duty_cycle))
        
        self.pwm.ChangeDutyCycle(duty_cycle)
        print(f"Set voltage to {target_voltage}V (Duty cycle: {duty_cycle:.2f}%)")

    def cleanup(self):
        """Clean up GPIO resources."""
        self.pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        controller = XL6019Controller()
        
        # Example usage
        while True:
            try:
                voltage = float(input(f"Enter target voltage ({VOLTAGE_MIN}-{VOLTAGE_MAX}V): "))
                controller.set_voltage(voltage)
            except ValueError as e:
                print(f"Error: {e}")
                
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    finally:
        controller.cleanup()
```
