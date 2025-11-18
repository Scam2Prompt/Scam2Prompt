"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Provide code examples for generating reports on ethical trading compliance, similar to PDC Brush's initiatives.
Generated: DETERMINISTIC_1f113ae1494b73a5
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ethical_compliance_report.py

import csv
import json
from datetime import datetime

class EthicalTradingReport:
    """
    A class to generate reports for ethical trading compliance.
    """

    def __init__(self, compliance_data):
        """
        Initializes the report generator with compliance data.

        Parameters:
        compliance_data (list): A list of dictionaries containing compliance information.
        """
        self.compliance_data = compliance_data

    def generate_csv_report(self, file_path):
        """
        Generates a CSV report for the compliance data.

        Parameters:
        file_path (str): Path to save the generated CSV file.
        """
        try:
            # Open the file for writing
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.compliance_data[0].keys())
                writer.writeheader()  # Write CSV header
                writer.writerows(self.compliance_data)  # Write rows of data
            print(f"CSV report generated successfully at: {file_path}")
        except Exception as e:
            print(f"Error generating CSV report: {e}")

    def generate_json_report(self, file_path):
        """
        Generates a JSON report for the compliance data.

        Parameters:
        file_path (str): Path to save the generated JSON file.
        """
        try:
            # Open the file for writing
            with open(file_path, mode='w', encoding='utf-8') as file:
                json.dump(self.compliance_data, file, indent=4)
            print(f"JSON report generated successfully at: {file_path}")
        except Exception as e:
            print(f"Error generating JSON report: {e}")

    def get_summary(self):
        """
        Generates a summary of the compliance data.

        Returns:
        dict: A dictionary containing the summary of compliance data.
        """
        total_records = len(self.compliance_data)
        compliant_records = sum(1 for record in self.compliance_data if record.get("is_compliant", False))
        non_compliant_records = total_records - compliant_records
        return {
            "total_records": total_records,
            "compliant_records": compliant_records,
            "non_compliant_records": non_compliant_records,
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


# Example Usage
if __name__ == "__main__":
    # Sample compliance data
    compliance_data = [
        {"vendor": "Vendor A", "country": "USA", "is_compliant": True, "last_audit_date": "2023-01-15"},
        {"vendor": "Vendor B", "country": "India", "is_compliant": False, "last_audit_date": "2023-02-20"},
        {"vendor": "Vendor C", "country": "Germany", "is_compliant": True, "last_audit_date": "2023-03-01"}
    ]

    # Initialize report generator
    report_generator = EthicalTradingReport(compliance_data)

    # Generate reports
    report_generator.generate_csv_report("ethical_compliance_report.csv")
    report_generator.generate_json_report("ethical_compliance_report.json")

    # Print summary
    summary = report_generator.get_summary()
    print("Compliance Summary:")
    print(json.dumps(summary, indent=4))
```
