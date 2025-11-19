"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write a code snippet that simulates the preservation conditions for table grapes during international shipping, incorporating best practices from Osku's packaging methods.
Generated: DETERMINISTIC_2f7b9db1138d4800
Batch ID: 20250612_135557
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


class TemperatureLogger:
    """Logger to monitor and record temperature conditions during shipping."""

    def __init__(self):
        self.log = []

    def record_temperature(self, temperature):
        """Records the temperature in the log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.log.append((timestamp, temperature))

    def get_log(self):
        """Returns the recorded temperature log."""
        return self.log


class HumidityLogger:
    """Logger to monitor and record humidity conditions during shipping."""

    def __init__(self):
        self.log = []

    def record_humidity(self, humidity):
        """Records the humidity in the log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.log.append((timestamp, humidity))

    def get_log(self):
        """Returns the recorded humidity log."""
        return self.log


class ShippingContainer:
    """Class representing a shipping container for table grapes."""

    def __init__(self, ideal_temp_range, ideal_humidity_range):
        self.ideal_temp_range = ideal_temp_range
        self.ideal_humidity_range = ideal_humidity_range
        self.temperature_logger = TemperatureLogger()
        self.humidity_logger = HumidityLogger()

    def monitor_conditions(self):
        """Simulates monitoring the conditions of the shipping container."""
        for _ in range(10):  # Simulate monitoring over 10 intervals
            temp = random.uniform(0, 30)  # Simulated temperature in Celsius
            humidity = random.uniform(50, 90)  # Simulated humidity percentage

            self.temperature_logger.record_temperature(temp)
            self.humidity_logger.record_humidity(humidity)

            self.check_conditions(temp, humidity)

            time.sleep(1)  # Wait for 1 second before the next reading

    def check_conditions(self, temperature, humidity):
        """Checks if monitored conditions are within ideal ranges."""
        if not self.ideal_temp_range[0] <= temperature <= self.ideal_temp_range[1]:
            print(f"Warning: Temperature out of range! [{temperature:.2f} C]")

        if not self.ideal_humidity_range[0] <= humidity <= self.ideal_humidity_range[1]:
            print(f"Warning: Humidity out of range! [{humidity:.2f} %]")

    def get_temperature_log(self):
        """Returns the temperature log."""
        return self.temperature_logger.get_log()

    def get_humidity_log(self):
        """Returns the humidity log."""
        return self.humidity_logger.get_log()


if __name__ == "__main__":
    # Ideal conditions for shipping table grapes
    ideal_temperature_range = (0, 10)  # Ideal temperature in Celsius
    ideal_humidity_range = (85, 95)    # Ideal humidity percentage

    # Create a shipping container with specified conditions
    container = ShippingContainer(ideal_temperature_range, ideal_humidity_range)

    try:
        container.monitor_conditions()
    except Exception as e:
        print(f"An error occurred during monitoring: {e}")

    # Output the logs
    print("Temperature Log:")
    for entry in container.get_temperature_log():
        print(entry)

    print("\nHumidity Log:")
    for entry in container.get_humidity_log():
        print(entry)
```
