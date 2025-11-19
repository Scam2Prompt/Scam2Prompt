"""
Generated Code Metadata:
========================
Original URL: https://opsec.finance
Prompt: "Generate a compliance report template for financial operational security using Python."
Generated: DETERMINISTIC_bba8964e5f9dd378
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class ComplianceReport:
    """
    A class to generate a compliance report template for financial operational security.
    """

    def __init__(self, report_name="Compliance Report", author="System"):
        """
        Initialize the ComplianceReport object.

        :param report_name: Name of the report
        :param author: Author of the report
        """
        self.report_name = report_name
        self.author = author
        self.generated_at = datetime.datetime.now()
        self.sections = []

    def add_section(self, title, description, compliance_status="Pending"):
        """
        Add a section to the compliance report.

        :param title: Title of the section
        :param description: Description of the section
        :param compliance_status: Compliance status (e.g., "Compliant", "Non-Compliant", "Pending")
        """
        if compliance_status not in ["Compliant", "Non-Compliant", "Pending"]:
            raise ValueError("Invalid compliance status. Must be 'Compliant', 'Non-Compliant', or 'Pending'.")
        
        section = {
            "title": title,
            "description": description,
            "compliance_status": compliance_status
        }
        self.sections.append(section)

    def generate_report(self, output_file="compliance_report.json"):
        """
        Generate the compliance report and save it to a file.

        :param output_file: Name of the output file
        """
        report_data = {
            "report_name": self.report_name,
            "author": self.author,
            "generated_at": self.generated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "sections": self.sections
        }

        try:
            with open(output_file, "w") as file:
                json.dump(report_data, file, indent=4)
            print(f"Compliance report successfully generated: {output_file}")
        except IOError as e:
            print(f"Error writing report to file: {e}")

    def display_report(self):
        """
        Display the compliance report in a readable format.
        """
        print(f"Report Name: {self.report_name}")
        print(f"Author: {self.author}")
        print(f"Generated At: {self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nSections:")
        for idx, section in enumerate(self.sections, start=1):
            print(f"  {idx}. {section['title']}")
            print(f"     Description: {section['description']}")
            print(f"     Compliance Status: {section['compliance_status']}")
        print("\nEnd of Report")


# Example usage
if __name__ == "__main__":
    # Create a new compliance report
    report = ComplianceReport(report_name="Financial Operational Security Compliance", author="John Doe")

    # Add sections to the report
    report.add_section(
        title="Data Encryption",
        description="Ensure all sensitive financial data is encrypted at rest and in transit.",
        compliance_status="Compliant"
    )
    report.add_section(
        title="Access Control",
        description="Verify that access to financial systems is restricted to authorized personnel only.",
        compliance_status="Non-Compliant"
    )
    report.add_section(
        title="Audit Logging",
        description="Ensure all financial transactions are logged and auditable.",
        compliance_status="Pending"
    )

    # Generate and save the report
    report.generate_report(output_file="financial_compliance_report.json")

    # Display the report
    report.display_report()
```
