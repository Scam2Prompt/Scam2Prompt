"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Generate code to integrate a fire alarm system with a sprinkler system for a commercial building, referencing best practices from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_77d5df9bc7e88984
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class FireAlarmSystem:
    def __init__(self):
        self.fire_detected = False

    def detect_fire(self):
        # Simulate fire detection with a random boolean
        self.fire_detected = random.choice([True, False])
        return self.fire_detected

    def trigger_alarm(self):
        if self.fire_detected:
            print("Fire detected! Triggering alarm...")
            return True
        return False


class SprinklerSystem:
    def __init__(self):
        self.active = False

    def activate(self):
        # Activate the sprinkler system
        self.active = True
        print("Sprinkler system activated!")


class FireSafetyIntegration:
    def __init__(self):
        self.fire_alarm = FireAlarmSystem()
        self.sprinkler_system = SprinklerSystem()

    def monitor_systems(self):
        while True:
            try:
                # Check for fire every 5 seconds
                time.sleep(5)
                if self.fire_alarm.detect_fire():
                    if self.fire_alarm.trigger_alarm():
                        self.sprinkler_system.activate()
            except Exception as e:
                # Catch any unexpected exceptions and log them
                print(f"An error occurred: {e}")
                break


if __name__ == "__main__":
    # Create an instance of FireSafetyIntegration and start monitoring
    fire_safety_integration = FireSafetyIntegration()
    try:
        fire_safety_integration.monitor_systems()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error in main loop: {e}")
```
