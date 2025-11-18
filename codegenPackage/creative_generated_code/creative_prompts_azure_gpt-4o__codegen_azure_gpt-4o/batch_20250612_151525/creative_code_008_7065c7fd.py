"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Provide code to manage adhesive foam systems using Nordson's FoamMelt or SureFoam machines.
Generated: DETERMINISTIC_7065c7fd56987e87
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Adhesive Foam Management System for Nordson FoamMelt or SureFoam Machines
This Python script manages and monitors adhesive foam systems. It includes control
over machine actions, configuration parameters, and system diagnostics.
"""

import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("adhesive_foam_system.log"), logging.StreamHandler()]
)

class AdhesiveFoamSystem:
    """
    Class to manage Nordson FoamMelt or SureFoam adhesive foam systems.
    """

    def __init__(self, machine_type: str):
        """
        Initialize the adhesive foam system.

        :param machine_type: Type of machine ('FoamMelt' or 'SureFoam')
        """
        if machine_type not in ['FoamMelt', 'SureFoam']:
            raise ValueError("Invalid machine type. Please choose 'FoamMelt' or 'SureFoam'.")
        
        self.machine_type = machine_type
        self.is_running = False
        self.temperature = 25.0  # Default temperature (in Celsius)
        self.pressure = 0.0  # Default pressure (in Bar)
        logging.info(f"{self.machine_type} system initialized.")

    def start_system(self):
        """
        Start the adhesive foam system.
        """
        if self.is_running:
            logging.warning("System is already running.")
            return
        
        self.is_running = True
        logging.info(f"{self.machine_type} system started.")

    def stop_system(self):
        """
        Stop the adhesive foam system.
        """
        if not self.is_running:
            logging.warning("System is not running.")
            return

        self.is_running = False
        logging.info(f"{self.machine_type} system stopped.")

    def set_temperature(self, temperature: float):
        """
        Set the system temperature.

        :param temperature: Desired temperature in Celsius
        """
        if temperature < 0 or temperature > 100:  # Example temperature range
            logging.error("Temperature out of range. Must be between 0°C and 100°C.")
            return
        
        self.temperature = temperature
        logging.info(f"Temperature set to {temperature}°C.")

    def set_pressure(self, pressure: float):
        """
        Set the system pressure.

        :param pressure: Desired pressure in Bar
        """
        if pressure < 0 or pressure > 10:  # Example pressure range
            logging.error("Pressure out of range. Must be between 0 Bar and 10 Bar.")
            return

        self.pressure = pressure
        logging.info(f"Pressure set to {pressure} Bar.")

    def get_status(self):
        """
        Get the current status of the adhesive foam system.

        :return: Dictionary with system status
        """
        status = {
            "machine_type": self.machine_type,
            "is_running": self.is_running,
            "temperature": self.temperature,
            "pressure": self.pressure,
        }
        logging.info("System status retrieved.")
        return status

    def run_diagnostics(self):
        """
        Run diagnostics on the adhesive foam system.
        """
        logging.info("Running diagnostics...")
        
        # Perform basic diagnostics
        issues = []
        if self.temperature < 15 or self.temperature > 85:  # Example safe temperature range
            issues.append("Temperature out of safe range.")
        if self.pressure < 1 or self.pressure > 8:  # Example safe pressure range
            issues.append("Pressure out of safe range.")
        if not self.is_running:
            issues.append("System is not running.")

        if issues:
            logging.error(f"Diagnostics found issues: {issues}")
            return {"status": "FAILED", "issues": issues}
        
        logging.info("Diagnostics completed successfully. No issues found.")
        return {"status": "PASSED", "issues": []}

# Example usage
if __name__ == "__main__":
    try:
        # Initialize system
        system = AdhesiveFoamSystem(machine_type="FoamMelt")

        # Start system
        system.start_system()

        # Configure parameters
        system.set_temperature(50)
        system.set_pressure(5)

        # Get status
        status = system.get_status()
        logging.info(f"System Status: {status}")

        # Run diagnostics
        diagnostics = system.run_diagnostics()
        logging.info(f"Diagnostics Result: {diagnostics}")

        # Stop system
        system.stop_system()

    except Exception as e:
        logging.exception("An error occurred during operation.")
```
