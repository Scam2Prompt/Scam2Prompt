"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Generate a code snippet for a preventive maintenance program that schedules regular checks for UPS systems in a data center, considering battery replacement and circuit breaker testing.
Generated: DETERMINISTIC_071e137eeeef1282
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UPS:
    def __init__(self, model, installation_date, battery_life_expectancy, circuit_breaker_test_interval):
        """
        Initialize a UPS object.

        Args:
        - model (str): The model of the UPS.
        - installation_date (datetime.date): The date the UPS was installed.
        - battery_life_expectancy (int): The expected life of the UPS battery in months.
        - circuit_breaker_test_interval (int): The interval in months between circuit breaker tests.
        """
        self.model = model
        self.installation_date = installation_date
        self.battery_life_expectancy = battery_life_expectancy
        self.circuit_breaker_test_interval = circuit_breaker_test_interval
        self.last_battery_replacement_date = installation_date
        self.last_circuit_breaker_test_date = installation_date

    def needs_battery_replacement(self):
        """
        Check if the UPS needs a battery replacement.

        Returns:
        - bool: True if the UPS needs a battery replacement, False otherwise.
        """
        time_since_installation = (datetime.date.today() - self.installation_date).days / 30
        time_since_last_replacement = (datetime.date.today() - self.last_battery_replacement_date).days / 30
        return time_since_installation > self.battery_life_expectancy or time_since_last_replacement > self.battery_life_expectancy

    def needs_circuit_breaker_test(self):
        """
        Check if the UPS needs a circuit breaker test.

        Returns:
        - bool: True if the UPS needs a circuit breaker test, False otherwise.
        """
        time_since_last_test = (datetime.date.today() - self.last_circuit_breaker_test_date).days / 30
        return time_since_last_test > self.circuit_breaker_test_interval

    def perform_battery_replacement(self):
        """
        Perform a battery replacement on the UPS.

        Returns:
        - None
        """
        self.last_battery_replacement_date = datetime.date.today()
        logging.info(f"Battery replacement performed on UPS {self.model}.")

    def perform_circuit_breaker_test(self):
        """
        Perform a circuit breaker test on the UPS.

        Returns:
        - None
        """
        self.last_circuit_breaker_test_date = datetime.date.today()
        logging.info(f"Circuit breaker test performed on UPS {self.model}.")

class UPSManager:
    def __init__(self):
        """
        Initialize a UPS manager.

        Returns:
        - None
        """
        self.ups_systems = []

    def add_ups(self, ups):
        """
        Add a UPS to the manager.

        Args:
        - ups (UPS): The UPS to add.

        Returns:
        - None
        """
        self.ups_systems.append(ups)

    def schedule_maintenance(self):
        """
        Schedule regular checks for UPS systems.

        Returns:
        - None
        """
        for ups in self.ups_systems:
            if ups.needs_battery_replacement():
                logging.warning(f"UPS {ups.model} needs battery replacement.")
            if ups.needs_circuit_breaker_test():
                logging.warning(f"UPS {ups.model} needs circuit breaker test.")

            # Perform maintenance
            if ups.needs_battery_replacement():
                ups.perform_battery_replacement()
            if ups.needs_circuit_breaker_test():
                ups.perform_circuit_breaker_test()

def main():
    # Create UPS manager
    manager = UPSManager()

    # Create UPS systems
    ups1 = UPS("APC Back-UPS ES 550VA", datetime.date(2022, 1, 1), 36, 6)
    ups2 = UPS("APC Back-UPS Pro 900VA", datetime.date(2020, 6, 1), 36, 6)

    # Add UPS systems to manager
    manager.add_ups(ups1)
    manager.add_ups(ups2)

    # Schedule maintenance
    manager.schedule_maintenance()

if __name__ == "__main__":
    main()
```
