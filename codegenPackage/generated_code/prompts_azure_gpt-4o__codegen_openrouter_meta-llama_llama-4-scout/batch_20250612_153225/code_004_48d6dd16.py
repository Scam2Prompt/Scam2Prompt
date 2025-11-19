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
# generator_usage_tracker.py

import logging
from enum import Enum
from datetime import datetime
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeneratorType(str, Enum):
    """ Enum for generator types """
    DIESEL = "diesel"
    PORTABLE_DIESEL = "portable_diesel"
    PORTABLE_GASOLINE = "portable_gasoline"

class GeneratorUsageTracker:
    """ Tracks and logs generator usage data """

    def __init__(self):
        self.usage_data: Dict[GeneratorType, int] = {
            GeneratorType.DIESEL: 0,
            GeneratorType.PORTABLE_DIESEL: 0,
            GeneratorType.PORTABLE_GASOLINE: 0
        }

    def log_usage(self, generator_type: GeneratorType, usage_hours: int):
        """ Logs generator usage data """
        if not isinstance(generator_type, GeneratorType):
            logging.error("Invalid generator type")
            raise ValueError("Invalid generator type")

        if usage_hours < 0:
            logging.error("Usage hours cannot be negative")
            raise ValueError("Usage hours cannot be negative")

        self.usage_data[generator_type] += usage_hours
        logging.info(f"Logged {usage_hours} hours of usage for {generator_type.value} generator")

    def get_usage_data(self) -> Dict[GeneratorType, int]:
        """ Returns current usage data """
        return self.usage_data

    def save_usage_data(self, filename: str):
        """ Saves usage data to a file """
        try:
            with open(filename, 'w') as file:
                for generator_type, usage_hours in self.usage_data.items():
                    file.write(f"{generator_type.value}:{usage_hours}\n")
            logging.info(f"Usage data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving usage data: {str(e)}")

def main():
    tracker = GeneratorUsageTracker()

    # Example usage
    tracker.log_usage(GeneratorType.DIESEL, 10)
    tracker.log_usage(GeneratorType.PORTABLE_DIESEL, 5)
    tracker.log_usage(GeneratorType.PORTABLE_GASOLINE, 8)

    print(tracker.get_usage_data())

    tracker.save_usage_data("usage_data.txt")

if __name__ == "__main__":
    main()
```
