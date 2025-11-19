"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write a Python script that simulates the monitoring of electrical conductors and alerts for variations, inspired by the automation and control solutions from Miraya Electric S.A.C.
Generated: DETERMINISTIC_dc64b563085f53c8
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_conductor_monitor.py

"""
Simulates the monitoring of electrical conductors and alerts for variations.

Inspired by the automation and control solutions from Miraya Electric S.A.C.
"""

import logging
import random
import time
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricalConductor:
    def __init__(self, name: str, normal_current_range: tuple):
        """
        Initializes an ElectricalConductor instance.

        Args:
        - name (str): The name of the conductor.
        - normal_current_range (tuple): The normal current range (min, max) for the conductor.
        """
        self.name = name
        self.normal_current_range = normal_current_range
        self.current_value = None

    def update_current_value(self, value: float):
        """
        Updates the current value of the conductor.

        Args:
        - value (float): The new current value.
        """
        self.current_value = value

    def is_within_normal_range(self) -> bool:
        """
        Checks if the current value is within the normal current range.

        Returns:
        - bool: True if the current value is within the normal range, False otherwise.
        """
        if self.current_value is None:
            return False
        return self.normal_current_range[0] <= self.current_value <= self.normal_current_range[1]

class ConductorMonitor:
    def __init__(self):
        """
        Initializes a ConductorMonitor instance.
        """
        self.conductors: Dict[str, ElectricalConductor] = {}

    def add_conductor(self, conductor: ElectricalConductor):
        """
        Adds a conductor to the monitor.

        Args:
        - conductor (ElectricalConductor): The conductor to add.
        """
        self.conductors[conductor.name] = conductor

    def monitor_conductors(self):
        """
        Simulates monitoring the conductors and alerts for variations.
        """
        for conductor in self.conductors.values():
            if not conductor.is_within_normal_range():
                logging.warning(f"Conductor {conductor.name} is outside normal current range: {conductor.current_value}")
            else:
                logging.info(f"Conductor {conductor.name} is within normal current range: {conductor.current_value}")

def simulate_conductor_data(conductor: ElectricalConductor):
    """
    Simulates current data for a conductor.

    Args:
    - conductor (ElectricalConductor): The conductor to simulate data for.
    """
    # Simulate a random current value
    current_value = random.uniform(0, 100)
    conductor.update_current_value(current_value)

def main():
    # Create a conductor monitor
    monitor = ConductorMonitor()

    # Create conductors
    conductor1 = ElectricalConductor("Conductor 1", (10, 20))
    conductor2 = ElectricalConductor("Conductor 2", (5, 15))

    # Add conductors to the monitor
    monitor.add_conductor(conductor1)
    monitor.add_conductor(conductor2)

    try:
        while True:
            # Simulate conductor data
            simulate_conductor_data(conductor1)
            simulate_conductor_data(conductor2)

            # Monitor conductors
            monitor.monitor_conductors()

            # Wait for 1 second
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped.")

if __name__ == "__main__":
    main()
```
