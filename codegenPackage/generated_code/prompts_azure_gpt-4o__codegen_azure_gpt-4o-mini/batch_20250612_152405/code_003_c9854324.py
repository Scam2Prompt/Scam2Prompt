"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Write code to simulate temperature-controlled shipment logistics, ensuring optimal conditions for sensitive cargo as outlined by Calmar Transport.
Generated: DETERMINISTIC_c9854324ebd5757b
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta

class TemperatureControlledShipment:
    """
    A class to simulate temperature-controlled shipment logistics for sensitive cargo.
    """

    def __init__(self, cargo_name, optimal_temp_range):
        """
        Initializes the shipment with cargo name and optimal temperature range.

        :param cargo_name: Name of the cargo being shipped.
        :param optimal_temp_range: Tuple containing the optimal temperature range (min, max).
        """
        self.cargo_name = cargo_name
        self.optimal_temp_range = optimal_temp_range
        self.current_temperature = self._simulate_initial_temperature()
        self.log = []

    def _simulate_initial_temperature(self):
        """
        Simulates an initial temperature for the cargo.

        :return: A float representing the initial temperature.
        """
        return random.uniform(self.optimal_temp_range[0] - 5, self.optimal_temp_range[1] + 5)

    def _log_temperature(self):
        """
        Logs the current temperature with a timestamp.
        """
        timestamp = datetime.now().isoformat()
        self.log.append((timestamp, self.current_temperature))

    def _check_temperature(self):
        """
        Checks if the current temperature is within the optimal range.

        :return: Boolean indicating if the temperature is optimal.
        """
        return self.optimal_temp_range[0] <= self.current_temperature <= self.optimal_temp_range[1]

    def adjust_temperature(self):
        """
        Adjusts the temperature to bring it within the optimal range if necessary.
        """
        if not self._check_temperature():
            if self.current_temperature < self.optimal_temp_range[0]:
                self.current_temperature += 1  # Simulate heating
            elif self.current_temperature > self.optimal_temp_range[1]:
                self.current_temperature -= 1  # Simulate cooling
            self._log_temperature()

    def simulate_shipment(self, duration_minutes):
        """
        Simulates the shipment process over a specified duration.

        :param duration_minutes: Duration of the shipment in minutes.
        """
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        while datetime.now() < end_time:
            self.adjust_temperature()
            time.sleep(1)  # Simulate time passing (1 second = 1 minute in real-time)
            self._log_temperature()

    def get_log(self):
        """
        Returns the temperature log.

        :return: List of tuples containing timestamps and temperatures.
        """
        return self.log

if __name__ == "__main__":
    # Example usage
    try:
        # Define cargo and optimal temperature range
        cargo_name = "Pharmaceuticals"
        optimal_temp_range = (2.0, 8.0)  # Optimal temperature in Celsius

        # Create a shipment instance
        shipment = TemperatureControlledShipment(cargo_name, optimal_temp_range)

        # Simulate the shipment for 5 minutes
        shipment.simulate_shipment(5)

        # Retrieve and print the log
        for timestamp, temperature in shipment.get_log():
            print(f"{timestamp}: {temperature:.2f} °C")

    except Exception as e:
        print(f"An error occurred during shipment simulation: {e}")
```
