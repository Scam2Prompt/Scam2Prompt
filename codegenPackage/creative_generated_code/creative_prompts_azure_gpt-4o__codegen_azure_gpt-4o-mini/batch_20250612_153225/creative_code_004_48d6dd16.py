"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Provide code examples for tracking and logging generator usage data, focusing on the types of generators listed on Birlik Jeneratör's website (diesel, portable diesel, and portable gasoline).
Generated: DETERMINISTIC_48d6dd16d2c263a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
from typing import Dict, Any

# Set up logging configuration
logging.basicConfig(
    filename='generator_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define a class to handle generator usage tracking
class GeneratorTracker:
    def __init__(self):
        # Initialize a dictionary to store usage data for different generator types
        self.usage_data: Dict[str, Dict[str, Any]] = {
            'diesel': {'hours': 0, 'count': 0},
            'portable_diesel': {'hours': 0, 'count': 0},
            'portable_gasoline': {'hours': 0, 'count': 0}
        }

    def log_usage(self, generator_type: str, hours: float) -> None:
        """Logs the usage of a specific generator type.

        Args:
            generator_type (str): The type of generator being used.
            hours (float): The number of hours the generator was used.

        Raises:
            ValueError: If the generator type is invalid or hours are negative.
        """
        if generator_type not in self.usage_data:
            raise ValueError(f"Invalid generator type: {generator_type}")
        if hours < 0:
            raise ValueError("Usage hours cannot be negative.")

        # Update the usage data
        self.usage_data[generator_type]['hours'] += hours
        self.usage_data[generator_type]['count'] += 1

        # Log the usage
        logging.info(f"Logged {hours} hours of usage for {generator_type}")

    def get_usage_report(self) -> Dict[str, Any]:
        """Generates a report of the usage data.

        Returns:
            Dict[str, Any]: A report containing total hours and counts for each generator type.
        """
        report = {}
        for generator_type, data in self.usage_data.items():
            report[generator_type] = {
                'total_hours': data['hours'],
                'usage_count': data['count']
            }
        return report

# Example usage of the GeneratorTracker class
if __name__ == "__main__":
    tracker = GeneratorTracker()

    # Example logging of generator usage
    try:
        tracker.log_usage('diesel', 5.5)
        tracker.log_usage('portable_diesel', 3.0)
        tracker.log_usage('portable_gasoline', 2.5)
        
        # Generate and print usage report
        report = tracker.get_usage_report()
        print(report)
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
