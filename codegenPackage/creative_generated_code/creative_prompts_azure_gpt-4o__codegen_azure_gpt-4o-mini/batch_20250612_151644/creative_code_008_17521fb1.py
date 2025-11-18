"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://complyaml.com
Prompt: Create a script to track and report AML compliance progress across multiple departments, based on ComplyAML's training breakdown.
Generated: DETERMINISTIC_17521fb167bc06aa
Batch ID: 20250612_151644
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
from typing import Dict, List

# Set up logging for tracking progress and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for compliance status
COMPLIANCE_STATUS = {
    'COMPLIANT': 'Compliant',
    'NON_COMPLIANT': 'Non-Compliant',
    'IN_PROGRESS': 'In Progress',
}

class DepartmentComplianceTracker:
    def __init__(self):
        # Initialize the compliance data as a dictionary
        self.compliance_data: Dict[str, Dict[str, str]] = {}

    def load_compliance_data(self, file_path: str) -> None:
        """Load compliance data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                self.compliance_data = json.load(file)
                logging.info("Compliance data loaded successfully from %s", file_path)
        except FileNotFoundError:
            logging.error("The specified file was not found: %s", file_path)
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the file: %s", file_path)
            raise

    def track_progress(self) -> Dict[str, str]:
        """Track and report AML compliance progress across departments."""
        progress_report = {}
        for department, training_info in self.compliance_data.items():
            # Determine compliance status based on training completion
            total_training = len(training_info.get('training_sessions', []))
            completed_training = sum(1 for status in training_info.get('training_sessions', []) if status == COMPLIANCE_STATUS['COMPLIANT'])

            # Calculate compliance percentage
            if total_training > 0:
                compliance_percentage = (completed_training / total_training) * 100
                progress_report[department] = f"{compliance_percentage:.2f}% compliant"
            else:
                progress_report[department] = "No training sessions available"

        return progress_report

    def report_progress(self, progress_report: Dict[str, str]) -> None:
        """Print the compliance progress report to the console."""
        logging.info("AML Compliance Progress Report:")
        for department, status in progress_report.items():
            print(f"Department: {department}, Compliance Status: {status}")

def main():
    # Create an instance of the tracker
    tracker = DepartmentComplianceTracker()
    
    # Load compliance data
    try:
        tracker.load_compliance_data('compliance_data.json')
    except Exception as e:
        logging.critical("Failed to load compliance data: %s", e)
        return

    # Track progress and generate report
    progress_report = tracker.track_progress()
    tracker.report_progress(progress_report)

if __name__ == "__main__":
    main()
```

To create a JSON file named `compliance_data.json`, the structure should look like this:

```json
{
    "Department A": {
        "training_sessions": ["Compliant", "Non-Compliant", "Compliant"]
    },
    "Department B": {
        "training_sessions": ["Compliant", "In Progress"]
    },
    "Department C": {
        "training_sessions": []
    }
}
```
