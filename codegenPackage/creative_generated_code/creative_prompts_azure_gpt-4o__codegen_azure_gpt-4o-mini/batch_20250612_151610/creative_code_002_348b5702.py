"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Generate code to simulate the operation of a Cummins 6.7L Turbo Diesel engine, focusing on reliability metrics mentioned on the Indusur webpage.
Generated: DETERMINISTIC_348b57028b332856
Batch ID: 20250612_151610
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

class Cummins67LTurboDieselEngine:
    """
    A class to simulate the operation of a Cummins 6.7L Turbo Diesel engine.

    Attributes:
        temperature (float): The current engine temperature in degrees Celsius.
        oil_pressure (float): The current oil pressure in psi.
        fuel_efficiency (float): The current fuel efficiency in miles per gallon.
        total_runtime (float): The total runtime of the engine in hours.
        reliability_score (float): A score representing engine reliability.
    """

    def __init__(self):
        """
        Initializes the engine with default parameters.
        """
        self.temperature = 70.0  # Initial temperature in Celsius
        self.oil_pressure = 30.0  # Initial oil pressure in psi
        self.fuel_efficiency = 20.0  # Initial fuel efficiency in mpg
        self.total_runtime = 0.0  # Total runtime in hours
        self.reliability_score = 100.0  # Initial reliability score

    def simulate_operation(self, hours):
        """
        Simulates the engine operation for a given number of hours.

        Args:
            hours (float): Number of hours to simulate the engine operation.

        Raises:
            ValueError: If hours is negative.
        """
        if hours < 0:
            raise ValueError("Simulation hours must be non-negative.")

        for hour in range(int(hours)):
            self.update_engine_metrics()
            self.total_runtime += 1
            time.sleep(1)  # Simulate time passing in a real scenario
            self.log_engine_status()

    def update_engine_metrics(self):
        """
        Updates the engine metrics based on simulated conditions.
        """
        # Simulate temperature increase
        self.temperature += random.uniform(0.5, 2.0)
        
        # Simulate oil pressure fluctuation
        self.oil_pressure += random.uniform(-1.0, 1.0)
        if self.oil_pressure < 20.0:
            self.oil_pressure = 20.0  # Minimum oil pressure threshold

        # Simulate fuel efficiency variation
        self.fuel_efficiency += random.uniform(-0.5, 0.5)
        if self.fuel_efficiency < 10.0:
            self.fuel_efficiency = 10.0  # Minimum fuel efficiency threshold

        # Simulate reliability degradation over time
        self.reliability_score -= random.uniform(0.01, 0.05)
        if self.reliability_score < 0.0:
            self.reliability_score = 0.0  # Minimum reliability score

    def log_engine_status(self):
        """
        Logs the current status of the engine metrics.
        """
        print(f"Runtime: {self.total_runtime} hours")
        print(f"Temperature: {self.temperature:.2f} °C")
        print(f"Oil Pressure: {self.oil_pressure:.2f} psi")
        print(f"Fuel Efficiency: {self.fuel_efficiency:.2f} mpg")
        print(f"Reliability Score: {self.reliability_score:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    try:
        engine = Cummins67LTurboDieselEngine()
        engine.simulate_operation(5)  # Simulate operation for 5 hours
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
