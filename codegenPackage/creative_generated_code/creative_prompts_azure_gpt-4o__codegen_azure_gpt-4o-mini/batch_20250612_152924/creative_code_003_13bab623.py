"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Provide a Python script for detecting and repairing leaks in underground drainage systems, inspired by ERA ENGINEERING's plumbing services.
Generated: DETERMINISTIC_13bab623588c903e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import requests
import time
from typing import List, Tuple

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DrainageSystem:
    def __init__(self, system_id: str):
        """Initialize the drainage system with a unique identifier."""
        self.system_id = system_id
        self.leak_detected = False

    def detect_leak(self) -> bool:
        """Simulate leak detection using sensor data.
        
        Returns:
            bool: True if leak is detected, False otherwise.
        """
        # Simulate a leak detection algorithm (e.g., comparing inflow vs outflow)
        # This is a mock implementation for demonstration purposes.
        inflow = self.get_sensor_data("inflow")
        outflow = self.get_sensor_data("outflow")

        if inflow > outflow:
            logging.warning(f"Leak detected in system {self.system_id}: inflow {inflow} > outflow {outflow}.")
            self.leak_detected = True
            return True
        return False

    def get_sensor_data(self, data_type: str) -> float:
        """Simulate getting data from sensors.
        
        Args:
            data_type (str): The type of sensor data to retrieve ('inflow' or 'outflow').
        
        Returns:
            float: Mock sensor data value.
        """
        # In a real-world scenario, this would involve reading from actual sensors.
        # Here, we simulate it with random values for demonstration.
        import random
        return random.uniform(0, 100)

    def repair_leak(self) -> None:
        """Simulate the process of repairing a detected leak."""
        if not self.leak_detected:
            logging.info("No leak detected; no repair necessary.")
            return
        
        # Simulate repairs (e.g., calling a service, initiating repair protocol)
        logging.info(f"Repairing leak in system {self.system_id}...")
        time.sleep(2)  # Simulate time taken for repairs
        self.leak_detected = False
        logging.info("Repair completed.")

def monitor_drainage_system(system_id: str, check_interval: int = 10) -> None:
    """Monitor the drainage system for leaks at regular intervals.
    
    Args:
        system_id (str): The unique identifier for the drainage system.
        check_interval (int): Time in seconds between each leak check.
    """
    drainage_system = DrainageSystem(system_id)
    
    while True:
        try:
            if drainage_system.detect_leak():
                drainage_system.repair_leak()
            time.sleep(check_interval)  # Wait for the specified interval before checking again
        except Exception as e:
            logging.error(f"An error occurred while monitoring the drainage system: {e}")
            break

if __name__ == "__main__":
    # Example: Start monitoring a drainage system with a specific ID
    monitor_drainage_system(system_id="DS123", check_interval=5)
```
