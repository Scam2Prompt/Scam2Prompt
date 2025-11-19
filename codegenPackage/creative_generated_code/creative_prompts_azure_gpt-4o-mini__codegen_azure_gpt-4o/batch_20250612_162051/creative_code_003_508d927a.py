"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Develop a sample application that showcases the use of VinaRoy's air blower FB200 in cement industry processes.
Generated: DETERMINISTIC_508d927a3465d28b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sample Application to Showcase the Use of VinaRoy's Air Blower FB200 in Cement Industry Processes.

This application simulates the integration of the FB200 air blower in processes such as:
1. Material drying
2. Dust control
3. Pneumatic conveying

The application demonstrates how to use the air blower in a controlled environment, 
including monitoring and error handling.

Author: Expert Developer
"""

import time
import logging

# Configure logging to track events and errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)


class AirBlowerFB200:
    """
    Class representing the VinaRoy Air Blower FB200.
    Provides methods to interact with the blower, such as start, stop, and monitor.
    """

    def __init__(self, max_pressure: float, max_runtime: float):
        """
        Initialize the air blower with given specifications.

        :param max_pressure: Maximum pressure in PSI
        :param max_runtime: Maximum runtime in hours before cooldown is required
        """
        self.max_pressure = max_pressure
        self.max_runtime = max_runtime
        self.is_running = False
        self.runtime_hours = 0.0
        logging.info("Air Blower FB200 initialized with max pressure: %s PSI and max runtime: %s hours.",
                     self.max_pressure, self.max_runtime)

    def start(self):
        """
        Start the air blower. Checks for any issues before starting.
        """
        if self.is_running:
            logging.warning("Air Blower is already running.")
            return

        if self.runtime_hours >= self.max_runtime:
            logging.error("Air Blower requires cooldown. Maximum runtime reached!")
            raise RuntimeError("Cooldown required before starting the blower.")

        self.is_running = True
        logging.info("Air Blower has been started.")

    def stop(self):
        """
        Stop the air blower and reset runtime tracking.
        """
        if not self.is_running:
            logging.warning("Air Blower is not currently running.")
            return

        self.is_running = False
        self.runtime_hours = 0.0  # Reset runtime hours for demonstration purposes
        logging.info("Air Blower has been stopped.")

    def simulate_operation(self, duration_hours: float, pressure: float):
        """
        Simulates the operation of the air blower.

        :param duration_hours: Duration in hours for which the blower runs
        :param pressure: Pressure in PSI during operation
        """
        if not self.is_running:
            logging.error("Cannot simulate operation. Air Blower is not running.")
            raise RuntimeError("Air Blower must be started before operation simulation.")

        if pressure > self.max_pressure:
            logging.error("Pressure exceeds maximum limit! Operation aborted.")
            raise ValueError("Pressure exceeds maximum limit.")

        if self.runtime_hours + duration_hours > self.max_runtime:
            logging.error("Operation duration exceeds maximum runtime. Cooldown required.")
            raise RuntimeError("Cooldown required before extended operation.")

        # Simulate the operation
        logging.info("Air Blower is running for %.2f hours at %.2f PSI.", duration_hours, pressure)
        time.sleep(duration_hours)  # A placeholder for actual operation
        self.runtime_hours += duration_hours
        logging.info("Operation completed. Total runtime hours: %.2f.", self.runtime_hours)

    def monitor(self):
        """
        Monitor the status and runtime of the air blower.
        """
        status = "Running" if self.is_running else "Stopped"
        logging.info("Air Blower Status: %s | Runtime Hours: %.2f | Max Runtime: %.2f",
                     status, self.runtime_hours, self.max_runtime)


def main():
    """
    Main function to demonstrate the use of Air Blower FB200 in the cement industry.
    """
    try:
        # Initialize the air blower with specifications
        blower = AirBlowerFB200(max_pressure=120.0, max_runtime=10.0)

        # Start the blower
        blower.start()

        # Simulate operations
        blower.simulate_operation(duration_hours=3.0, pressure=100.0)
        blower.monitor()

        blower.simulate_operation(duration_hours=2.0, pressure=90.0)
        blower.monitor()

        # Stop the blower
        blower.stop()

    except (RuntimeError, ValueError) as e:
        logging.error("An error occurred: %s", str(e))
    finally:
        logging.info("Application has exited.")


if __name__ == "__main__":
    main()
```
