"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Write a code snippet to simulate the activation of fire sprinklers based on temperature thresholds."
Generated: DETERMINISTIC_aecc4e761440a374
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class FireSprinklerSystem:
    def __init__(self, activation_temperature=60):
        """
        Initialize the fire sprinkler system.

        :param activation_temperature: Temperature threshold (in Celsius) to activate sprinklers.
        """
        self.activation_temperature = activation_temperature
        self.is_activated = False

    def check_temperature(self, current_temperature):
        """
        Check the current temperature and activate sprinklers if the threshold is exceeded.

        :param current_temperature: The current temperature reading (in Celsius).
        """
        if current_temperature >= self.activation_temperature:
            self.activate_sprinklers()
        else:
            print(f"Temperature {current_temperature}°C is below the threshold. Sprinklers are inactive.")

    def activate_sprinklers(self):
        """
        Activate the fire sprinklers.
        """
        if not self.is_activated:
            self.is_activated = True
            print("ALERT: Temperature threshold exceeded! Activating fire sprinklers...")
        else:
            print("Sprinklers are already activated.")

    def reset_sprinklers(self):
        """
        Reset the fire sprinklers to inactive state.
        """
        if self.is_activated:
            self.is_activated = False
            print("Sprinklers have been reset to inactive state.")
        else:
            print("Sprinklers are already inactive.")

def simulate_temperature_readings(sprinkler_system, duration=10, interval=1):
    """
    Simulate temperature readings over a period of time.

    :param sprinkler_system: Instance of FireSprinklerSystem to monitor temperature.
    :param duration: Total duration of the simulation in seconds.
    :param interval: Time interval (in seconds) between temperature readings.
    """
    print("Starting temperature simulation...")
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            # Simulate a random temperature reading between 30°C and 80°C
            current_temperature = random.uniform(30, 80)
            print(f"Current temperature: {current_temperature:.2f}°C")
            sprinkler_system.check_temperature(current_temperature)
            time.sleep(interval)
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred during simulation: {e}")
            break
    print("Temperature simulation ended.")

if __name__ == "__main__":
    # Create an instance of FireSprinklerSystem with a threshold of 60°C
    sprinkler_system = FireSprinklerSystem(activation_temperature=60)

    # Simulate temperature readings for 10 seconds with 1-second intervals
    simulate_temperature_readings(sprinkler_system, duration=10, interval=1)

    # Reset sprinklers after simulation
    sprinkler_system.reset_sprinklers()
```
