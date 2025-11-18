"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Write code to simulate temperature-controlled shipment logistics, ensuring optimal conditions for sensitive cargo as outlined by Calmar Transport.
Generated: DETERMINISTIC_c9854324ebd5757b
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time


class TemperatureControlledShipment:
    """
    A class to simulate temperature-controlled shipment logistics for sensitive cargo.
    """

    def __init__(self, min_temp, max_temp):
        """
        Initialize the shipment with temperature range.

        :param min_temp: Minimum allowable temperature (in Celsius).
        :param max_temp: Maximum allowable temperature (in Celsius).
        """
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.current_temp = random.uniform(min_temp, max_temp)  # Set a random initial temperature
        self.status = "OK"

    def monitor_temperature(self):
        """
        Monitors the current temperature of the shipment and ensures it stays within the allowable range.
        """
        try:
            if self.current_temp < self.min_temp:
                self.status = "ALERT: Temperature too low!"
            elif self.current_temp > self.max_temp:
                self.status = "ALERT: Temperature too high!"
            else:
                self.status = "OK"
        except Exception as e:
            self.status = f"ERROR: {str(e)}"

    def adjust_temperature(self):
        """
        Adjusts the shipment temperature to ensure it remains within the acceptable range.
        """
        try:
            if self.current_temp < self.min_temp:
                # Simulate heating the cargo to bring it within range
                self.current_temp += random.uniform(0.5, 1.5)
            elif self.current_temp > self.max_temp:
                # Simulate cooling the cargo to bring it within range
                self.current_temp -= random.uniform(0.5, 1.5)
        except Exception as e:
            self.status = f"ERROR: {str(e)}"

    def simulate(self, duration=10, interval=2):
        """
        Simulates the shipment logistics process over a given duration.

        :param duration: Total simulation time in seconds.
        :param interval: Interval between temperature checks in seconds.
        """
        print("Starting temperature-controlled shipment simulation...")
        try:
            for _ in range(duration // interval):
                # Simulate random temperature fluctuation
                self.current_temp += random.uniform(-1.0, 1.0)

                # Monitor and adjust temperature
                self.monitor_temperature()
                print(f"Current Temp: {self.current_temp:.2f}°C | Status: {self.status}")
                self.adjust_temperature()

                # Sleep for the given interval
                time.sleep(interval)

            print("Simulation complete.")
        except KeyboardInterrupt:
            print("Simulation interrupted by user.")
        except Exception as e:
            print(f"ERROR: {str(e)}")


# Main script execution
if __name__ == "__main__":
    # Define temperature limits based on Calmar Transport guidelines
    MIN_TEMP = 2.0  # Minimum temperature in Celsius
    MAX_TEMP = 8.0  # Maximum temperature in Celsius

    # Create shipment instance
    shipment = TemperatureControlledShipment(MIN_TEMP, MAX_TEMP)

    # Run the simulation
    shipment.simulate(duration=20, interval=5)
```
