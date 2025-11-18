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
from datetime import datetime, timedelta

class TemperatureControlledShipment:
    """
    A class to manage temperature-controlled shipment logistics.
    """

    def __init__(self, cargo_name, optimal_temp_range, check_interval=5):
        """
        Initializes the shipment with the cargo details and temperature settings.

        :param cargo_name: Name of the cargo being transported.
        :param optimal_temp_range: A tuple defining the optimal temperature range (min, max) in Celsius.
        :param check_interval: Time interval in seconds to check the temperature.
        """
        self.cargo_name = cargo_name
        self.optimal_temp_range = optimal_temp_range
        self.current_temperature = self.simulate_initial_temperature()
        self.check_interval = check_interval
        self.is_shipment_active = True
        self.log = []

    def simulate_initial_temperature(self):
        """Simulate an initial starting temperature within the optimal range."""
        return random.uniform(self.optimal_temp_range[0], self.optimal_temp_range[1])

    def check_temperature(self):
        """
        Check the current temperature of the shipment and log the status.
        If the temperature falls outside the optimal range, raise an alert.
        """
        if not self.is_shipment_active:
            raise RuntimeError("Shipment is no longer active.")

        # Simulate temperature fluctuations
        self.current_temperature += random.uniform(-2, 2)

        # Log the current status
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "Normal"
        if self.current_temperature < self.optimal_temp_range[0] or self.current_temperature > self.optimal_temp_range[1]:
            status = "ALERT! Temperature out of range!"
        
        log_entry = {
            "timestamp": timestamp,
            "temperature": self.current_temperature,
            "status": status
        }
        self.log.append(log_entry)

        # Print the log entry for monitoring
        print(f"[{log_entry['timestamp']}] Current Temp: {log_entry['temperature']:.2f}°C - Status: {log_entry['status']}")

        if status == "ALERT! Temperature out of range!":
            self.handle_temperature_alert()

    def handle_temperature_alert(self):
        """Handles the alert when the temperature is out of the optimal range."""
        print("Taking necessary actions to restore optimal conditions...")
        # Here you would implement the necessary logic, e.g., activate heating or cooling systems

    def start_shipment(self):
        """Starts monitoring the shipment temperature at defined intervals."""
        try:
            print(f"Starting shipment of '{self.cargo_name}'...")
            while self.is_shipment_active:
                self.check_temperature()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            print("Shipment monitoring interrupted by user.")
        finally:
            self.end_shipment()

    def end_shipment(self):
        """Ends the temperature monitoring and logs the final status."""
        self.is_shipment_active = False
        print("Shipment ended. Final log:")
        for entry in self.log:
            print(entry)

# Example usage
if __name__ == "__main__":
    try:
        shipment = TemperatureControlledShipment(cargo_name="Vaccines", optimal_temp_range=(2, 8))
        shipment.start_shipment()
    except Exception as e:
        print(f"An error occurred: {e}")
```
