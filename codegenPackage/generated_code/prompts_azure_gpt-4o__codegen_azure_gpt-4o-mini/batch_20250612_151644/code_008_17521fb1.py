"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Create a script to track and report AML compliance progress across multiple departments, based on ComplyAML's training breakdown.
Generated: DETERMINISTIC_17521fb167bc06aa
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AMLComplianceTracker:
    def __init__(self, departments: List[str]):
        """
        Initialize the AMLComplianceTracker with a list of departments.

        :param departments: List of department names to track compliance for.
        """
        self.departments = {dept: {'training_completed': 0, 'total_training': 0} for dept in departments}

    def add_training(self, department: str, total_training: int):
        """
        Add training information for a specific department.

        :param department: The name of the department.
        :param total_training: The total number of training sessions for the department.
        """
        if department not in self.departments:
            logging.error(f"Department '{department}' not found.")
            raise ValueError(f"Department '{department}' not found.")
        
        self.departments[department]['total_training'] += total_training
        logging.info(f"Added {total_training} training sessions for department '{department}'.")

    def complete_training(self, department: str, completed: int):
        """
        Mark training sessions as completed for a specific department.

        :param department: The name of the department.
        :param completed: The number of training sessions completed.
        """
        if department not in self.departments:
            logging.error(f"Department '{department}' not found.")
            raise ValueError(f"Department '{department}' not found.")
        
        if completed < 0:
            logging.error("Completed training sessions cannot be negative.")
            raise ValueError("Completed training sessions cannot be negative.")
        
        if completed > self.departments[department]['total_training']:
            logging.error("Completed training sessions exceed total training sessions.")
            raise ValueError("Completed training sessions exceed total training sessions.")
        
        self.departments[department]['training_completed'] += completed
        logging.info(f"Marked {completed} training sessions as completed for department '{department}'.")

    def get_compliance_report(self) -> Dict[str, float]:
        """
        Generate a compliance report showing the progress of each department.

        :return: A dictionary with department names as keys and compliance percentages as values.
        """
        report = {}
        for dept, data in self.departments.items():
            if data['total_training'] > 0:
                compliance_percentage = (data['training_completed'] / data['total_training']) * 100
            else:
                compliance_percentage = 0.0
            report[dept] = compliance_percentage
            logging.info(f"Compliance for department '{dept}': {compliance_percentage:.2f}%")
        return report

    def save_report_to_file(self, filename: str):
        """
        Save the compliance report to a JSON file.

        :param filename: The name of the file to save the report to.
        """
        report = self.get_compliance_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            logging.info(f"Compliance report saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Failed to save report to file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        departments = ['Finance', 'Operations', 'Compliance', 'HR']
        tracker = AMLComplianceTracker(departments)

        # Add training sessions
        tracker.add_training('Finance', 10)
        tracker.add_training('Operations', 8)

        # Complete training sessions
        tracker.complete_training('Finance', 5)
        tracker.complete_training('Operations', 3)

        # Generate and save report
        tracker.save_report_to_file('aml_compliance_report.json')

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
