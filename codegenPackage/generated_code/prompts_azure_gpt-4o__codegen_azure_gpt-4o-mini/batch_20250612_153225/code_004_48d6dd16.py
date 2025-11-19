"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Provide code examples for tracking and logging generator usage data, focusing on the types of generators listed on Birlik Jeneratör's website (diesel, portable diesel, and portable gasoline).
Generated: DETERMINISTIC_48d6dd16d2c263a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    filename='generator_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GeneratorUsageTracker:
    """
    A class to track and log generator usage data.
    Supported generator types: diesel, portable diesel, portable gasoline.
    """

    def __init__(self):
        self.usage_data: Dict[str, Any] = {
            'diesel': [],
            'portable_diesel': [],
            'portable_gasoline': []
        }

    def log_usage(self, generator_type: str, hours_used: float, fuel_consumed: float) -> None:
        """
        Log the usage of a generator.

        :param generator_type: Type of the generator (diesel, portable_diesel, portable_gasoline)
        :param hours_used: Number of hours the generator was used
        :param fuel_consumed: Amount of fuel consumed in liters
        :raises ValueError: If the generator type is invalid or if hours_used or fuel_consumed are negative
        """
        if generator_type not in self.usage_data:
            raise ValueError(f"Invalid generator type: {generator_type}. Must be one of {list(self.usage_data.keys())}.")
        
        if hours_used < 0 or fuel_consumed < 0:
            raise ValueError("Hours used and fuel consumed must be non-negative.")

        # Create a log entry
        entry = {
            'timestamp': datetime.now(),
            'hours_used': hours_used,
            'fuel_consumed': fuel_consumed
        }

        # Append the entry to the appropriate generator type
        self.usage_data[generator_type].append(entry)

        # Log the usage
        logging.info(f"Logged usage for {generator_type}: {entry}")

    def get_usage_report(self) -> Dict[str, Any]:
        """
        Generate a report of the usage data.

        :return: A dictionary containing the usage data for each generator type
        """
        return self.usage_data

# Example usage
if __name__ == "__main__":
    tracker = GeneratorUsageTracker()
    
    try:
        tracker.log_usage('diesel', 5.0, 20.0)
        tracker.log_usage('portable_diesel', 3.5, 15.0)
        tracker.log_usage('portable_gasoline', 2.0, 10.0)

        # Print the usage report
        report = tracker.get_usage_report()
        print(report)

    except ValueError as e:
        logging.error(f"Error logging generator usage: {e}")
```
