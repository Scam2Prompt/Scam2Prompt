"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Create a script to track screen time usage across multiple apps on a smartphone using Android or iOS APIs. Include recommendations for libraries to visualize the data.
Generated: DETERMINISTIC_9c5bb229092f3cbd
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# screen_time_tracker.py

import datetime
import json
import logging
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ScreenTimeTracker:
    def __init__(self):
        """Initialize the screen time tracker with an empty usage record."""
        self.usage_data: Dict[str, List[Dict[str, datetime.timedelta]]] = {}

    def log_app_usage(self, app_name: str, duration: datetime.timedelta):
        """Log the screen time usage for a specific app.

        Args:
            app_name (str): Name of the app.
            duration (datetime.timedelta): Duration of usage.

        Raises:
            ValueError: If duration is negative or app_name is empty.
        """
        if duration < datetime.timedelta(0):
            raise ValueError("Duration must be a non-negative timedelta.")
        if not app_name:
            raise ValueError("App name cannot be empty.")

        if app_name not in self.usage_data:
            self.usage_data[app_name] = []

        self.usage_data[app_name].append({
            'timestamp': datetime.datetime.now(),
            'duration': duration
        })
        logging.info(f"Logged {duration} for app {app_name}")

    def generate_report(self) -> Dict[str, datetime.timedelta]:
        """Generate a report of total screen time used per app.

        Returns:
            Dict[str, datetime.timedelta]: A dictionary with app names as keys and total usage durations as values.
        """
        report = {}
        for app, usages in self.usage_data.items():
            total_duration = sum((usage['duration'] for usage in usages), datetime.timedelta())
            report[app] = total_duration
        logging.info("Generated report.")
        return report

    def save_report_to_file(self, filename: str):
        """Save the usage report to a JSON file.

        Args:
            filename (str): The name of the file to save the report.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_report(), file, default=str)
            logging.info(f"Report saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving report to file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    tracker = ScreenTimeTracker()
    
    # Simulate logging app usage
    try:
        tracker.log_app_usage("App1", datetime.timedelta(minutes=30))
        tracker.log_app_usage("App2", datetime.timedelta(hours=1))
        tracker.log_app_usage("App1", datetime.timedelta(minutes=45))
        
        # Generate and save report
        tracker.save_report_to_file("screen_time_report.json")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Recommendations for libraries to visualize data:
# - Matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python.
# - Plotly: An interactive graphing library that supports a wide range of complex visualizations.
# - Seaborn: A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive statistical graphics.
```
