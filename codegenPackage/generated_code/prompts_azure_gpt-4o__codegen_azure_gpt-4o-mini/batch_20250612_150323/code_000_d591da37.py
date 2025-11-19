"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write Python code to simulate real-time data collection from industrial sewing machines using a device similar to OpenSeam's hardware, and process the data to calculate machine utilization metrics.
Generated: DETERMINISTIC_d591da3779c4047a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SewingMachine:
    """Class to represent an industrial sewing machine."""
    
    def __init__(self, machine_id: str):
        self.machine_id = machine_id
        self.is_operational = True
        self.start_time = None
        self.end_time = None
        self.total_runtime = 0.0

    def start(self):
        """Start the sewing machine and record the start time."""
        if not self.is_operational:
            logging.warning(f"Machine {self.machine_id} is not operational.")
            return
        self.start_time = time.time()
        logging.info(f"Machine {self.machine_id} started at {self.start_time}.")

    def stop(self):
        """Stop the sewing machine and calculate the runtime."""
        if not self.is_operational:
            logging.warning(f"Machine {self.machine_id} is not operational.")
            return
        if self.start_time is None:
            logging.warning(f"Machine {self.machine_id} was not started.")
            return
        self.end_time = time.time()
        self.total_runtime += self.end_time - self.start_time
        logging.info(f"Machine {self.machine_id} stopped at {self.end_time}. Total runtime: {self.total_runtime:.2f} seconds.")
        self.start_time = None

    def get_utilization(self) -> float:
        """Calculate the utilization percentage based on total runtime."""
        # Assuming a fixed operational period of 8 hours (28800 seconds) for utilization calculation
        operational_period = 28800.0
        utilization = (self.total_runtime / operational_period) * 100
        return utilization

class DataCollector:
    """Class to simulate real-time data collection from sewing machines."""
    
    def __init__(self, machines: List[SewingMachine]):
        self.machines = machines

    def collect_data(self):
        """Simulate data collection from each sewing machine."""
        while True:
            for machine in self.machines:
                if machine.is_operational:
                    # Randomly decide to start or stop the machine for simulation
                    if random.choice([True, False]):
                        machine.start()
                    else:
                        machine.stop()
                    # Log the utilization metric
                    utilization = machine.get_utilization()
                    logging.info(f"Machine {machine.machine_id} utilization: {utilization:.2f}%")
            time.sleep(5)  # Simulate a delay between data collection intervals

def main():
    """Main function to run the data collection simulation."""
    try:
        # Create a list of sewing machines
        machines = [SewingMachine(machine_id=f"SM-{i}") for i in range(1, 6)]
        
        # Initialize the data collector with the machines
        collector = DataCollector(machines)
        
        # Start data collection
        collector.collect_data()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
