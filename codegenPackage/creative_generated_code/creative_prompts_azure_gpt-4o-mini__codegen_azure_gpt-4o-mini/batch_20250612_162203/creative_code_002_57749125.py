"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Write a Python script to automate the generation of educational credit reports based on the data management practices described on the Cooprometa website.
Generated: DETERMINISTIC_57749125f73cf33e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os
from datetime import datetime

class CreditReportGenerator:
    """A class to generate educational credit reports from CSV data."""

    def __init__(self, input_file, output_file):
        """
        Initialize the CreditReportGenerator.

        :param input_file: Path to the CSV file containing data.
        :param output_file: Path to the output JSON file for the credit report.
        """
        self.input_file = input_file
        self.output_file = output_file

    def read_csv(self):
        """Reads data from the CSV file and returns a list of dictionaries."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")

        data = []
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except Exception as e:
            raise RuntimeError(f"Error reading CSV file: {str(e)}")
        
        return data

    def generate_report(self, data):
        """
        Generates a credit report based on the provided data.

        :param data: A list of dictionaries containing educational data.
        :return: A report in the form of a dictionary.
        """
        report = {
            'generated_at': datetime.now().isoformat(),
            'total_students': len(data),
            'student_details': []
        }

        for student in data:
            student_info = {
                'name': student.get('Name'),
                'credits_earned': int(student.get('Credits Earned', 0)),
                'gpa': float(student.get('GPA', 0.0)),
            }
            report['student_details'].append(student_info)

        return report

    def write_json(self, report):
        """Writes the generated report to a JSON file."""
        try:
            with open(self.output_file, mode='w', encoding='utf-8') as file:
                json.dump(report, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error writing JSON file: {str(e)}")

    def run(self):
        """Executes the report generation process."""
        try:
            data = self.read_csv()
            report = self.generate_report(data)
            self.write_json(report)
            print(f"Credit report generated successfully: {self.output_file}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Define input and output file paths
    input_csv_file = 'educational_data.csv'  # Path to the input CSV file
    output_json_file = 'credit_report.json'   # Path to the output JSON file

    # Create a CreditReportGenerator instance and run the report generation
    report_generator = CreditReportGenerator(input_csv_file, output_json_file)
    report_generator.run()
```
