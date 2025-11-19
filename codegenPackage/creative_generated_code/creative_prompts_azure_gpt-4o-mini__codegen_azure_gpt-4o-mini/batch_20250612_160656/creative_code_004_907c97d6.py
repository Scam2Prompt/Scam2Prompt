"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://forestx.se
Prompt: Illustrate how to implement a digital tool for sustainable forest usage, incorporating the innovative approaches highlighted by ForestX.
Generated: DETERMINISTIC_907c97d692c67ea1
Batch ID: 20250612_160656
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ForestUsageTracker:
    """
    A class to track sustainable forest usage through logging and data analysis.
    """

    def __init__(self, forest_id: str):
        """
        Initializes the ForestUsageTracker with a specific forest ID.

        :param forest_id: Unique identifier for the forest.
        """
        self.forest_id = forest_id
        self.usage_data = []

    def log_usage(self, usage_entry: Dict):
        """
        Logs a new usage entry for the forest.

        :param usage_entry: A dictionary containing usage information.
        """
        try:
            if not self.validate_usage_entry(usage_entry):
                raise ValueError("Invalid usage entry format.")
                
            usage_entry['timestamp'] = datetime.now().isoformat()
            self.usage_data.append(usage_entry)
            logging.info(f"Logged usage: {usage_entry}")
        except Exception as e:
            logging.error(f"Error logging usage: {str(e)}")

    def validate_usage_entry(self, entry: Dict) -> bool:
        """
        Validates the format of a usage entry.

        :param entry: The usage entry to validate.
        :return: True if valid, False otherwise.
        """
        required_keys = {'user_id', 'activity', 'amount'}
        return required_keys.issubset(entry.keys())

    def generate_report(self) -> Dict:
        """
        Generates a report of the logged usage in the forest.

        :return: A dictionary summary of the usage data.
        """
        report = {
            'forest_id': self.forest_id,
            'total_entries': len(self.usage_data),
            'usage_summary': {}
        }

        for entry in self.usage_data:
            activity = entry['activity']
            report['usage_summary'][activity] = report['usage_summary'].get(activity, 0) + entry['amount']

        logging.info(f"Generated report: {json.dumps(report, indent=2)}")
        return report

    def save_to_file(self, filename: str):
        """
        Saves the logged usage data to a JSON file.

        :param filename: The name of the file to save the usage data to.
        """
        try:
            with open(filename, 'w') as outfile:
                json.dump(self.usage_data, outfile, indent=2)
            logging.info(f"Usage data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save file {filename}: {str(e)}")


# Example usage
if __name__ == '__main__':
    tracker = ForestUsageTracker("F123")

    # Log some usage entries
    tracker.log_usage({'user_id': 'U001', 'activity': 'logging', 'amount': 10})
    tracker.log_usage({'user_id': 'U002', 'activity': 'planting', 'amount': 20})

    # Generate report
    report = tracker.generate_report()

    # Save report to file
    tracker.save_to_file("forest_usage_report.json")
```
