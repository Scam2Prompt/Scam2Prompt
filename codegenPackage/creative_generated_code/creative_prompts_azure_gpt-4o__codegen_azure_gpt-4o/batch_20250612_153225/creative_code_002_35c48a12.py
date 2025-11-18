"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Provide code to design a monitoring system for micro-inverters in a solar panel setup, following the installation standards (NEN 1010 and NEN 3140) mentioned on Technische Installatiebedrijf van Boxtel's webpage.
Generated: DETERMINISTIC_35c48a1293539ad7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Monitoring System for Micro-Inverters in a Solar Panel Setup

This code is designed to monitor and log the performance of micro-inverters 
installed in a solar panel array. It adheres to best practices for error handling, 
documentation, and clean code design.

Note: The monitoring system assumes compliance with installation standards 
like NEN 1010 and NEN 3140. Proper implementation of grid connection safety and 
electrical standards is the responsibility of the installation team.
"""

import time
import logging
import random

# Configure logging for the monitoring system
logging.basicConfig(
    filename="micro_inverter_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MicroInverter:
    """
    Represents a micro-inverter in the solar panel monitoring system.

    Attributes:
        id (int): Unique identifier for the micro-inverter.
        status (str): Current operational status ("OK", "FAILURE", etc.).
        power_output (float): Current power output in watts.
    """
    def __init__(self, inverter_id):
        self.id = inverter_id
        self.status = "OK"
        self.power_output = 0.0

    def simulate_power_output(self):
        """
        Simulates the power output for the micro-inverter.
        Randomly generates a power output value and randomly simulates failures.
        """
        if random.random() < 0.05:  # 5% chance of failure
            self.status = "FAILURE"
            self.power_output = 0.0
        else:
            self.status = "OK"
            self.power_output = random.uniform(50.0, 300.0)  # Simulate power output in watts

    def get_status(self):
        """
        Retrieves the current status and power output of the micro-inverter.

        Returns:
            dict: Status and power output details.
        """
        return {
            "id": self.id,
            "status": self.status,
            "power_output": self.power_output
        }

class MonitoringSystem:
    """
    Represents the monitoring system for a collection of micro-inverters.

    Attributes:
        inverters (list): List of MicroInverter objects being monitored.
    """
    def __init__(self, num_inverters):
        self.inverters = [MicroInverter(inverter_id=i) for i in range(1, num_inverters + 1)]

    def monitor_inverters(self):
        """
        Monitors the status and power output of all micro-inverters.
        Logs their information and handles any failures.
        """
        for inverter in self.inverters:
            inverter.simulate_power_output()
            status_info = inverter.get_status()

            if status_info["status"] == "FAILURE":
                logging.error(f"Inverter ID {status_info['id']} has FAILED.")
            else:
                logging.info(f"Inverter ID {status_info['id']} is OK. Power Output: {status_info['power_output']}W")
    
    def run_monitoring_loop(self, interval_seconds=60):
        """
        Runs the monitoring loop to periodically check the status of all inverters.

        Args:
            interval_seconds (int): Interval between monitoring checks (in seconds).
        """
        try:
            while True:
                self.monitor_inverters()
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            logging.info("Monitoring system stopped by user.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Initialize the monitoring system with 10 micro-inverters
    num_inverters = 10
    monitoring_system = MonitoringSystem(num_inverters=num_inverters)

    # Start the monitoring loop (interval: 60 seconds)
    monitoring_system.run_monitoring_loop(interval_seconds=60)
```
