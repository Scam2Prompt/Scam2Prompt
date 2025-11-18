"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Write Python code to simulate real-time data collection from industrial sewing machines using a device similar to OpenSeam's hardware, and process the data to calculate machine utilization metrics.
Generated: DETERMINISTIC_d591da3779c4047a
Batch ID: 20250612_150323
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
import logging
from typing import List, Dict

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SewingMachine:
    """Class representing an industrial sewing machine."""

    def __init__(self, machine_id: str):
        """Initialize a new sewing machine with a unique ID."""
        self.machine_id = machine_id
        self.total_operating_time = 0.0
        self.total_downtime = 0.0
        self.is_operational = True

    def run(self) -> None:
        """Simulate the sewing machine's operation."""
        if self.is_operational:
            operating_time = random.uniform(1, 5)  # Simulate operating time in seconds
            downtime = random.uniform(0, 2)        # Simulate downtime in seconds
            time.sleep(operating_time)
            self.total_operating_time += operating_time
            time.sleep(downtime)
            self.total_downtime += downtime
            logging.info(f"Machine {self.machine_id} operated for {operating_time:.2f} seconds and was down for {downtime:.2f} seconds.")

    def get_utilization(self) -> float:
        """Calculate and return machine utilization as a percentage."""
        total_time = self.total_operating_time + self.total_downtime
        if total_time == 0:
            return 0.0
        utilization = (self.total_operating_time / total_time) * 100
        logging.info(f"Machine {self.machine_id} utilization: {utilization:.2f}%")
        return utilization

class DataCollector:
    """Class for collecting and processing data from sewing machines."""

    def __init__(self, machines: List[SewingMachine]):
        """Initialize the data collector with a list of sewing machines."""
        self.machines = machines

    def collect_data(self, duration: int) -> None:
        """Collect data for a specified duration in seconds."""
        start_time = time.time()
        while time.time() - start_time < duration:
            for machine in self.machines:
                machine.run()

    def generate_report(self) -> Dict[str, float]:
        """Generate a utilization report for all machines."""
        report = {}
        for machine in self.machines:
            report[machine.machine_id] = machine.get_utilization()
        return report

if __name__ == "__main__":
    try:
        # Create a list of sewing machines
        machines = [SewingMachine(f"Machine_{i}") for i in range(1, 6)]
        
        # Create the data collector
        collector = DataCollector(machines)

        # Collect data for 20 seconds
        collector.collect_data(duration=20)

        # Generate and log the utilization report
        utilization_report = collector.generate_report()
        logging.info("Utilization Report: {}".format(utilization_report))

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
