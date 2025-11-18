"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write Python code to simulate the activation of a fire sprinkler system based on temperature thresholds, as described by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_c23fe847ad249b3f
Batch ID: 20250612_153224
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

class FireSprinklerSystem:
    def __init__(self, activation_temperature=68.0):
        """
        Initializes the Fire Sprinkler System.
        
        :param activation_temperature: Temperature threshold (in Celsius) to activate the sprinklers.
        """
        self.activation_temperature = activation_temperature
        self.is_activated = False

    def monitor_temperature(self):
        """
        Monitors the temperature and activates the sprinklers if the threshold is exceeded.
        Simulates temperature readings for demonstration purposes.
        """
        try:
            print("Fire Sprinkler System is monitoring temperature...")

            while not self.is_activated:
                # Simulate temperature reading (random value between 20°C and 100°C)
                current_temperature = random.uniform(20.0, 100.0)
                print(f"Current temperature: {current_temperature:.2f}°C")

                if current_temperature >= self.activation_temperature:
                    self.activate_sprinklers(current_temperature)
                else:
                    print("Temperature is within safe limits.")

                # Pause for a short duration to simulate real-time temperature monitoring
                time.sleep(2)

        except KeyboardInterrupt:
            print("\nMonitoring interrupted. Fire Sprinkler System shutting down...")
        except Exception as e:
            print(f"An error occurred: {e}")

    def activate_sprinklers(self, temperature):
        """
        Activates the fire sprinklers when the temperature exceeds the threshold.
        
        :param temperature: The temperature that triggered sprinkler activation.
        """
        self.is_activated = True
        print(f"ALERT! Fire sprinklers activated at {temperature:.2f}°C!")
        print("Sprinklers are now releasing water to suppress fire.")

# Entry point for the application
if __name__ == "__main__":
    # Define the activation temperature (default is 68°C)
    activation_temperature = 68.0

    # Create an instance of FireSprinklerSystem
    sprinkler_system = FireSprinklerSystem(activation_temperature)

    # Start monitoring temperature
    sprinkler_system.monitor_temperature()
```
