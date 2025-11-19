"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Provide a step-by-step guide to implement Star-Delta motor starting using GE contactors, including capacitor protection, as described in the webpage.
Generated: DETERMINISTIC_1c5754e8e6d35f2d
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import RPi.GPIO as GPIO  # Assuming Raspberry Pi for GPIO control

# Constants for GPIO pins (adjust based on your setup)
STAR_CONTACTOR_PIN = 17
DELTA_CONTACTOR_PIN = 27
MAIN_CONTACTOR_PIN = 22
OVERLOAD_PIN = 23  # Input pin for overload detection
CAPACITOR_PROTECTION_PIN = 24  # Input pin for capacitor protection

# Timing constants (in seconds)
STAR_TIME = 5  # Time to stay in star configuration
TRANSITION_DELAY = 1  # Delay between star and delta transition

def setup_gpio():
    """Initialize GPIO pins"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Setup output pins
    GPIO.setup(STAR_CONTACTOR_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(DELTA_CONTACTOR_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MAIN_CONTACTOR_PIN, GPIO.OUT, initial=GPIO.LOW)
    
    # Setup input pins with pull-down resistors
    GPIO.setup(OVERLOAD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(CAPACITOR_PROTECTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def check_protections():
    """Check for overload and capacitor protection faults"""
    if GPIO.input(OVERLOAD_PIN) == GPIO.HIGH:
        raise RuntimeError("Motor overload detected!")
    if GPIO.input(CAPACITOR_PROTECTION_PIN) == GPIO.HIGH:
        raise RuntimeError("Capacitor protection triggered!")

def star_delta_start():
    """Perform star-delta motor starting sequence"""
    try:
        # Step 1: Check protections before starting
        check_protections()
        
        # Step 2: Engage main contactor
        GPIO.output(MAIN_CONTACTOR_PIN, GPIO.HIGH)
        print("Main contactor engaged")
        
        # Step 3: Engage star contactor
        GPIO.output(STAR_CONTACTOR_PIN, GPIO.HIGH)
        print("Star configuration activated")
        
        # Step 4: Run in star configuration for predefined time
        start_time = time.time()
        while time.time() - start_time < STAR_TIME:
            check_protections()  # Continuous protection monitoring
            time.sleep(0.1)
        
        # Step 5: Transition to delta configuration
        GPIO.output(STAR_CONTACTOR_PIN, GPIO.LOW)
        print("Star contactor disengaged")
        time.sleep(TRANSITION_DELAY)  # Brief delay to prevent short-circuit
        
        GPIO.output(DELTA_CONTACTOR_PIN, GPIO.HIGH)
        print("Delta configuration activated")
        
        print("Motor successfully started in delta configuration")
        
    except RuntimeError as e:
        print(f"Error during motor start: {e}")
        emergency_stop()
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        emergency_stop()
        raise

def emergency_stop():
    """Immediately stop all contactors"""
    GPIO.output(STAR_CONTACTOR_PIN, GPIO.LOW)
    GPIO.output(DELTA_CONTACTOR_PIN, GPIO.LOW)
    GPIO.output(MAIN_CONTACTOR_PIN, GPIO.LOW)
    print("Emergency stop activated - all contactors disengaged")

def cleanup():
    """Cleanup GPIO resources"""
    emergency_stop()
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup_gpio()
        star_delta_start()
    finally:
        cleanup()
```
