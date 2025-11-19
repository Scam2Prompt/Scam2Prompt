"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Generate code to simulate the temperature and humidity testing process for golf grips, using parameters like those mentioned in Longhui Golf’s factory testing procedures.
Generated: DETERMINISTIC_f1a413cb768dd148
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import random
import time
from dataclasses import dataclass

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class GolfGrip:
    """Represents a golf grip with its properties."""
    material: str
    size: str
    weight: float

class TemperatureHumidityTest:
    """Simulates temperature and humidity testing process for golf grips."""

    def __init__(self, grip: GolfGrip):
        self.grip = grip
        self.test_conditions = {
            "temperature": [-20, 50],  # Temperature range in Celsius
            "humidity": [30, 90]  # Humidity range in percentage
        }

    def simulate_test(self):
        """Simulates the temperature and humidity testing process."""
        try:
            logging.info(f"Starting test for {self.grip.material} golf grip.")
            for condition in ["temperature", "humidity"]:
                test_value = random.uniform(self.test_conditions[condition][0], self.test_conditions[condition][1])
                logging.info(f"Setting {condition} to {test_value} {self.get_unit(condition)}")
                time.sleep(1)  # Simulate test duration
                if not self.is_within_tolerance(test_value, condition):
                    logging.warning(f"{condition.capitalize()} {test_value} {self.get_unit(condition)} is outside tolerance.")
            logging.info("Test completed successfully.")
        except Exception as e:
            logging.error(f"Error during test: {e}")

    def get_unit(self, condition: str) -> str:
        """Returns the unit for the given condition."""
        if condition == "temperature":
            return "°C"
        elif condition == "humidity":
            return "%"

    def is_within_tolerance(self, test_value: float, condition: str) -> bool:
        """Checks if the test value is within tolerance."""
        if condition == "temperature":
            return -15 <= test_value <= 45
        elif condition == "humidity":
            return 40 <= test_value <= 80

def main():
    # Create a golf grip instance
    grip = GolfGrip("Rubber", "Standard", 50.0)

    # Create and run a temperature and humidity test
    test = TemperatureHumidityTest(grip)
    test.simulate_test()

if __name__ == "__main__":
    main()
```
