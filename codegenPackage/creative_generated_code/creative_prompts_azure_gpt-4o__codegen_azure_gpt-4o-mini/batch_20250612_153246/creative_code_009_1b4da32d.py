"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.projectortechnology.gr
Prompt: Create a program to track and log the usage of interactive kits in an educational setting, referencing the interactive education products offered by Projector Technology.
Generated: DETERMINISTIC_1b4da32dd5c136c7
Batch ID: 20250612_153246
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
from typing import List, Dict, Any


# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class KitUsageTracker:
    """
    A class to track and log the usage of interactive kits in an educational setting.
    """

    def __init__(self, logfile: str):
        """
        Initializes the KitUsageTracker with a specified logfile.

        Args:
            logfile (str): The filename where usage logs will be stored.
        """
        self.logfile = logfile
        self.usage_data: List[Dict[str, Any]] = []
        logging.info(f"Initialized KitUsageTracker with logfile: {logfile}")

    def log_usage(self, kit_name: str, user_id: str, duration: float):
        """
        Logs the usage of a specific interactive kit.

        Args:
            kit_name (str): The name of the interactive kit being used.
            user_id (str): The ID of the user utilizing the kit.
            duration (float): Duration of usage in minutes.
        """
        timestamp = datetime.now().isoformat()
        usage_entry = {
            'timestamp': timestamp,
            'kit_name': kit_name,
            'user_id': user_id,
            'duration': duration
        }
        
        self.usage_data.append(usage_entry)
        logging.info(f"Logged usage: {usage_entry}")
        self._save_to_file()

    def _save_to_file(self):
        """
        Saves the usage data to the specified logfile in JSON format.
        """
        try:
            with open(self.logfile, 'w') as file:
                json.dump(self.usage_data, file, indent=4)
            logging.info(f"Usage data saved to {self.logfile}")
        except IOError as e:
            logging.error(f"Failed to save usage data to {self.logfile}: {e}")

    def generate_report(self) -> List[Dict[str, Any]]:
        """
        Generates a usage report.

        Returns:
            List[Dict[str, Any]]: List of logged usage entries.
        """
        logging.info("Generating usage report")
        return self.usage_data

# Example usage
if __name__ == "__main__":
    # Create an instance of KitUsageTracker with a specified log file
    tracker = KitUsageTracker('kit_usage_log.json')

    # Log some usage (these would typically come from user interactions in a real application)
    tracker.log_usage(kit_name='Interactive Whiteboard', user_id='user123', duration=45.0)
    tracker.log_usage(kit_name='Science Experiment Kit', user_id='user456', duration=30.0)

    # Generate and print a report of usage
    report = tracker.generate_report()
    print(json.dumps(report, indent=4))
```
