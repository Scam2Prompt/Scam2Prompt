"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evinblue.com
Prompt: Write a code snippet that integrates a DEF monitoring system for BS-VI diesel engines, ensuring compliance with ISO 22241-1 standards.
Generated: DETERMINISTIC_f48906081c5e5301
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging for the DEF monitoring system
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DEFMonitoringSystem:
    """A class to monitor Diesel Exhaust Fluid (DEF) levels for BS-VI diesel engines."""

    def __init__(self, max_def_level=100.0):
        """
        Initialize the DEF monitoring system.

        Parameters:
        max_def_level (float): The maximum acceptable DEF level in liters.
        """
        self.max_def_level = max_def_level
        self.current_def_level = 0.0

    def update_def_level(self, def_level):
        """
        Update the current DEF level.

        Parameters:
        def_level (float): The current DEF level in liters.

        Raises:
        ValueError: If def_level is negative or exceeds the maximum level.
        """
        if def_level < 0:
            logging.error("Attempted to set a negative DEF level.")
            raise ValueError("DEF level cannot be negative.")
        if def_level > self.max_def_level:
            logging.error("Attempted to set DEF level above maximum limit.")
            raise ValueError(f"DEF level cannot exceed {self.max_def_level} liters.")
        
        self.current_def_level = def_level
        logging.info(f"DEF level updated to {self.current_def_level} liters.")

    def get_def_status(self):
        """
        Get the current status of the DEF level.

        Returns:
        dict: A dictionary containing the current DEF level and status.
        """
        status = {
            "current_def_level": self.current_def_level,
            "status": "Normal" if self.current_def_level >= 10.0 else "Low"
        }
        return status

    def log_def_data(self, log_file='def_monitor.log'):
        """
        Log the current DEF level and status to a file.

        Parameters:
        log_file (str): The file where DEF data will be logged.
        """
        status = self.get_def_status()
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "current_def_level": status["current_def_level"],
            "status": status["status"]
        }
        
        try:
            with open(log_file, 'a') as file:
                file.write(json.dumps(log_entry) + '\n')
            logging.info("DEF data logged successfully.")
        except IOError as e:
            logging.error(f"Failed to write to log file: {e}")

# Example usage of the DEFMonitoringSystem class
if __name__ == "__main__":
    def_monitor = DEFMonitoringSystem()
    
    try:
        # Update DEF level for testing
        def_monitor.update_def_level(50.0)  # Valid update
        def_monitor.log_def_data()            # Log current status

        def_monitor.update_def_level(5.0)    # Low level warning
        def_monitor.log_def_data()            # Log current status

        def_monitor.update_def_level(150.0)  # Invalid update to trigger error
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
