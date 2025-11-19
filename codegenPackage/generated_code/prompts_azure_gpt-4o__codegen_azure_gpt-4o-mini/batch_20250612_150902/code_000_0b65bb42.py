"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write Python code to automate the generation of medical examination reports for occupational health services, including fields for "Examen Médico de Ingreso," "Examen Médico Periódico," and "Examen Médico de Retiro," as described on Medicid IPS's website.
Generated: DETERMINISTIC_0b65bb4238a9f051
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class MedicalExaminationReport:
    """
    A class to represent a medical examination report for occupational health services.
    """

    def __init__(self, employee_name, employee_id, examination_type, examination_date, findings):
        """
        Initializes a new medical examination report.

        :param employee_name: Name of the employee
        :param employee_id: Unique identifier for the employee
        :param examination_type: Type of examination (Ingreso, Periódico, Retiro)
        :param examination_date: Date of the examination
        :param findings: Findings from the examination
        """
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.examination_type = examination_type
        self.examination_date = examination_date
        self.findings = findings

    def generate_report(self):
        """
        Generates a formatted report for the medical examination.

        :return: A string representation of the medical examination report
        """
        report = (
            f"Medical Examination Report\n"
            f"Employee Name: {self.employee_name}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Examination Type: {self.examination_type}\n"
            f"Examination Date: {self.examination_date.strftime('%Y-%m-%d')}\n"
            f"Findings:\n{self.findings}\n"
        )
        return report

    def save_report(self, filename):
        """
        Saves the report to a JSON file.

        :param filename: The name of the file to save the report
        """
        report_data = {
            "employee_name": self.employee_name,
            "employee_id": self.employee_id,
            "examination_type": self.examination_type,
            "examination_date": self.examination_date.isoformat(),
            "findings": self.findings
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(report_data, json_file, indent=4)
            print(f"Report saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving report: {e}")

def main():
    """
    Main function to create and save a medical examination report.
    """
    # Example data for the report
    employee_name = "John Doe"
    employee_id = "123456"
    examination_type = "Examen Médico de Ingreso"
    examination_date = datetime.now()
    findings = "No significant health issues detected."

    # Create a medical examination report
    report = MedicalExaminationReport(employee_name, employee_id, examination_type, examination_date, findings)

    # Generate and print the report
    print(report.generate_report())

    # Save the report to a file
    report.save_report("medical_examination_report.json")

if __name__ == "__main__":
    main()
```
