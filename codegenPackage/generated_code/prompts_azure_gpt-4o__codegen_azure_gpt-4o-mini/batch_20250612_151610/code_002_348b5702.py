"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: Generate code to simulate the operation of a Cummins 6.7L Turbo Diesel engine, focusing on reliability metrics mentioned on the Indusur webpage.
Generated: DETERMINISTIC_348b57028b332856
Batch ID: 20250612_151610
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
import logging

# Configure logging for the simulation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cummins67LTurboDieselEngine:
    """
    A class to simulate the operation of a Cummins 6.7L Turbo Diesel engine.
    This simulation focuses on reliability metrics such as engine temperature,
    oil pressure, and fuel efficiency.
    """

    def __init__(self):
        self.engine_temperature = 70  # Initial temperature in Celsius
        self.oil_pressure = 40         # Initial oil pressure in PSI
        self.fuel_efficiency = 15      # Initial fuel efficiency in MPG
        self.running = False

    def start_engine(self):
        """Starts the engine and begins the simulation."""
        self.running = True
        logging.info("Engine started.")
        self.simulate_operation()

    def stop_engine(self):
        """Stops the engine simulation."""
        self.running = False
        logging.info("Engine stopped.")

    def simulate_operation(self):
        """Simulates the engine operation, updating metrics periodically."""
        try:
            while self.running:
                self.update_metrics()
                self.log_metrics()
                time.sleep(1)  # Simulate time delay for each operation cycle
        except Exception as e:
            logging.error(f"An error occurred during simulation: {e}")
            self.stop_engine()

    def update_metrics(self):
        """Updates the engine metrics based on simulated conditions."""
        # Simulate temperature increase
        self.engine_temperature += random.uniform(0.1, 0.5)
        # Simulate oil pressure fluctuation
        self.oil_pressure += random.uniform(-0.5, 0.5)
        # Simulate fuel efficiency changes
        self.fuel_efficiency += random.uniform(-0.1, 0.1)

        # Ensure metrics stay within realistic bounds
        self.engine_temperature = min(max(self.engine_temperature, 70), 120)  # Safe operating range
        self.oil_pressure = min(max(self.oil_pressure, 20), 60)               # Safe operating range
        self.fuel_efficiency = max(self.fuel_efficiency, 0)                   # Cannot be negative

    def log_metrics(self):
        """Logs the current engine metrics."""
        logging.info(f"Engine Temperature: {self.engine_temperature:.2f} °C")
        logging.info(f"Oil Pressure: {self.oil_pressure:.2f} PSI")
        logging.info(f"Fuel Efficiency: {self.fuel_efficiency:.2f} MPG")

if __name__ == "__main__":
    engine = Cummins67LTurboDieselEngine()
    try:
        engine.start_engine()
        time.sleep(10)  # Let the engine run for 10 seconds
    finally:
        engine.stop_engine()
```
