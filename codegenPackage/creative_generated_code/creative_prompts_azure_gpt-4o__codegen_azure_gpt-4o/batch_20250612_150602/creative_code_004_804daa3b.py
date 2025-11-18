"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Write code to automate the tracking of FSC audit results for a company specializing in cleaning products, referencing PDC Brush's audit success.
Generated: DETERMINISTIC_804daa3b5fe3be99
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
import os

class FSCAuditTracker:
    """
    A class to automate the tracking of FSC audit results for a company.
    This system tracks audit results and generates reports for compliance monitoring.
    """

    def __init__(self, file_path="fsc_audit_results.csv"):
        """
        Initialize the FSCAuditTracker with a path to the CSV file for storing data.

        :param file_path: Path to the CSV file containing audit results.
        """
        self.file_path = file_path

        # Ensure the CSV file exists with correct headers
        if not os.path.exists(self.file_path):
            self._initialize_csv()

    def _initialize_csv(self):
        """
        Initialize the CSV file with headers if it doesn't exist.
        """
        headers = ["Date", "Branch", "AuditResult", "Comments"]
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    def record_audit_result(self, branch, audit_result, comments=""):
        """
        Record an audit result for a specific branch.

        :param branch: Name of the branch audited.
        :param audit_result: Result of the audit (e.g., "Pass", "Fail").
        :param comments: Optional comments about the audit.
        :raises ValueError: If audit_result is not valid.
        """
        valid_results = ["Pass", "Fail"]
        if audit_result not in valid_results:
            raise ValueError(f"Invalid audit result. Must be one of {valid_results}.")

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, branch, audit_result, comments])

    def generate_summary_report(self):
        """
        Generate a summary report of audit results.

        :return: A dictionary summarizing the audit results (e.g., counts of Pass and Fail).
        """
        summary = {"Pass": 0, "Fail": 0}
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["AuditResult"] in summary:
                        summary[row["AuditResult"]] += 1
        except Exception as e:
            print(f"Error reading audit results: {e}")
        return summary

    def display_summary_report(self):
        """
        Display the summary report in a user-friendly format.
        """
        summary = self.generate_summary_report()
        print("FSC Audit Summary Report:")
        for result, count in summary.items():
            print(f"{result}: {count}")

# Example usage (uncomment to run):
# tracker = FSCAuditTracker()
# tracker.record_audit_result(branch="PDC Brush HQ", audit_result="Pass", comments="Met all compliance standards.")
# tracker.record_audit_result(branch="Regional Office", audit_result="Fail", comments="Several non-compliance issues found.")
# tracker.display_summary_report()
```
