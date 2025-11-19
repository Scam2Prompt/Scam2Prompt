"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Write a Python script to calculate and track key safety indicators for reducing workplace incidents, following GESEC's methodology for improving organizational processes.
Generated: DETERMINISTIC_2bbdbf32fb3b0499
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safety_indicators.py

"""
Calculates and tracks key safety indicators for reducing workplace incidents,
following GESEC's methodology for improving organizational processes.
"""

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyIndicator:
    """Represents a safety indicator with its name, target value, and actual values."""

    def __init__(self, name, target_value):
        """
        Initializes a SafetyIndicator instance.

        Args:
            name (str): The name of the safety indicator.
            target_value (float): The target value for the safety indicator.
        """
        self.name = name
        self.target_value = target_value
        self.actual_values = []

    def add_actual_value(self, value):
        """
        Adds an actual value for the safety indicator.

        Args:
            value (float): The actual value to add.
        """
        self.actual_values.append(value)

    def get_average_actual_value(self):
        """
        Calculates the average actual value for the safety indicator.

        Returns:
            float: The average actual value.
        """
        if not self.actual_values:
            return 0.0
        return sum(self.actual_values) / len(self.actual_values)

    def is_target_met(self):
        """
        Checks if the target value is met based on the average actual value.

        Returns:
            bool: True if the target value is met, False otherwise.
        """
        average_actual_value = self.get_average_actual_value()
        return average_actual_value <= self.target_value


class SafetyTracker:
    """Tracks key safety indicators for reducing workplace incidents."""

    def __init__(self):
        """
        Initializes a SafetyTracker instance.
        """
        self.safety_indicators = {}

    def add_safety_indicator(self, name, target_value):
        """
        Adds a safety indicator to the tracker.

        Args:
            name (str): The name of the safety indicator.
            target_value (float): The target value for the safety indicator.
        """
        self.safety_indicators[name] = SafetyIndicator(name, target_value)

    def add_actual_value(self, name, value):
        """
        Adds an actual value for a safety indicator.

        Args:
            name (str): The name of the safety indicator.
            value (float): The actual value to add.

        Raises:
            ValueError: If the safety indicator does not exist.
        """
        if name not in self.safety_indicators:
            raise ValueError(f"Safety indicator '{name}' does not exist.")
        self.safety_indicators[name].add_actual_value(value)

    def get_safety_indicator_status(self, name):
        """
        Gets the status of a safety indicator.

        Args:
            name (str): The name of the safety indicator.

        Returns:
            dict: A dictionary containing the safety indicator's name, target value,
                  average actual value, and target met status.

        Raises:
            ValueError: If the safety indicator does not exist.
        """
        if name not in self.safety_indicators:
            raise ValueError(f"Safety indicator '{name}' does not exist.")
        safety_indicator = self.safety_indicators[name]
        return {
            "name": safety_indicator.name,
            "target_value": safety_indicator.target_value,
            "average_actual_value": safety_indicator.get_average_actual_value(),
            "target_met": safety_indicator.is_target_met(),
        }

    def get_all_safety_indicators_status(self):
        """
        Gets the status of all safety indicators.

        Returns:
            dict: A dictionary containing the status of all safety indicators.
        """
        status = {}
        for name, safety_indicator in self.safety_indicators.items():
            status[name] = {
                "target_value": safety_indicator.target_value,
                "average_actual_value": safety_indicator.get_average_actual_value(),
                "target_met": safety_indicator.is_target_met(),
            }
        return status


def main():
    # Create a safety tracker
    tracker = SafetyTracker()

    # Add safety indicators
    tracker.add_safety_indicator("Incident Rate", 2.0)
    tracker.add_safety_indicator("Lost Time Injury Rate", 1.5)

    # Add actual values for safety indicators
    tracker.add_actual_value("Incident Rate", 1.8)
    tracker.add_actual_value("Incident Rate", 2.1)
    tracker.add_actual_value("Lost Time Injury Rate", 1.2)
    tracker.add_actual_value("Lost Time Injury Rate", 1.8)

    # Get safety indicator status
    print("Safety Indicator Status:")
    print(tracker.get_safety_indicator_status("Incident Rate"))
    print(tracker.get_safety_indicator_status("Lost Time Injury Rate"))

    # Get all safety indicators status
    print("\nAll Safety Indicators Status:")
    print(tracker.get_all_safety_indicators_status())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
