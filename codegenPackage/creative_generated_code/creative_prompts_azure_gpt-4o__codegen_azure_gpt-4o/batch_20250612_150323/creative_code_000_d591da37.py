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
import random
import time
import logging
from datetime import datetime, timedelta

# Configure logging for debugging and production readiness
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("machine_utilization.log"),
        logging.StreamHandler()
    ]
)

class SewingMachineSimulator:
    """
    Simulates real-time data collection from an industrial sewing machine.
    """
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.status = "OFF"  # Possible states: "ON", "OFF"
        self.last_status_change = datetime.now()

    def update_status(self):
        """
        Simulates a random status update for the machine.
        """
        current_time = datetime.now()
        elapsed_seconds = (current_time - self.last_status_change).total_seconds()

        # Randomly decide whether to change status or maintain the current state
        if random.random() < 0.1:  # 10% chance of status change
            self.status = "ON" if self.status == "OFF" else "OFF"
            self.last_status_change = current_time

        return {
            "timestamp": current_time,
            "machine_id": self.machine_id,
            "status": self.status,
            "elapsed_time": elapsed_seconds if self.status == "ON" else 0
        }


class UtilizationProcessor:
    """
    Processes real-time machine data to calculate utilization metrics.
    """
    def __init__(self):
        self.data = {}

    def process_data(self, machine_data):
        """
        Processes incoming machine data and updates utilization metrics.
        """
        machine_id = machine_data["machine_id"]
        elapsed_time = machine_data["elapsed_time"]

        # Initialize data structure for the machine if not already present
        if machine_id not in self.data:
            self.data[machine_id] = {
                "total_on_time": timedelta(seconds=0),
                "last_timestamp": machine_data["timestamp"]
            }

        # Update utilization metrics if the machine is "ON"
        if machine_data["status"] == "ON":
            self.data[machine_id]["total_on_time"] += timedelta(seconds=elapsed_time)

        # Update the last timestamp
        self.data[machine_id]["last_timestamp"] = machine_data["timestamp"]

    def calculate_utilization(self, machine_id):
        """
        Returns the utilization percentage for the given machine.
        """
        if machine_id not in self.data:
            raise ValueError(f"No data found for machine ID: {machine_id}")

        utilization_time = self.data[machine_id]["total_on_time"]
        total_runtime = datetime.now() - self.data[machine_id]["last_timestamp"]

        if total_runtime.total_seconds() == 0:
            return 0.0

        return (utilization_time.total_seconds() / total_runtime.total_seconds()) * 100


def simulate_real_time_data_collection():
    """
    Simulates real-time data collection and utilization processing.
    """
    # Initialize machine simulators and processor
    machine_ids = ["SM-1001", "SM-1002", "SM-1003"]
    machines = [SewingMachineSimulator(machine_id) for machine_id in machine_ids]
    processor = UtilizationProcessor()

    try:
        while True:
            for machine in machines:
                # Simulate machine status update
                machine_data = machine.update_status()
                logging.info(f"Collected data: {machine_data}")

                # Process the collected data
                processor.process_data(machine_data)

                # Calculate and log utilization metrics
                utilization = processor.calculate_utilization(machine.machine_id)
                logging.info(
                    f"Machine {machine.machine_id} utilization: {utilization:.2f}%"
                )
            
            # Simulate real-time by sleeping for 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Simulation interrupted by user. Exiting...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    simulate_real_time_data_collection()
```
