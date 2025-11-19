"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: How can I ensure that my electrical system design meets the requirements of the ISO 9001:2015 certification, and what documentation is needed to support the design?
Generated: DETERMINISTIC_baee062235078129
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_system_design.py

"""
Module to ensure electrical system design meets ISO9001:2015 certification requirements.

Provides a class to manage documentation and design verification.
"""

import datetime

class ElectricalSystemDesign:
    def __init__(self, design_name, description):
        """
        Initialize an electrical system design.

        Args:
            design_name (str): Name of the electrical system design.
            description (str): Brief description of the design.

        Raises:
            ValueError: If design_name or description is empty.
        """
        if not design_name or not description:
            raise ValueError("Design name and description are required")

        self.design_name = design_name
        self.description = description
        self.documentation = []
        self.verification_records = []

    def add_documentation(self, document_name, document_content):
        """
        Add documentation to support the design.

        Args:
            document_name (str): Name of the document.
            document_content (str): Content of the document.

        Raises:
            ValueError: If document_name or document_content is empty.
        """
        if not document_name or not document_content:
            raise ValueError("Document name and content are required")

        self.documentation.append({
            "name": document_name,
            "content": document_content,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def verify_design(self, verification_method, verification_result):
        """
        Record design verification.

        Args:
            verification_method (str): Method used for verification.
            verification_result (bool): Result of the verification.

        Raises:
            ValueError: If verification_method is empty.
        """
        if not verification_method:
            raise ValueError("Verification method is required")

        self.verification_records.append({
            "method": verification_method,
            "result": verification_result,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def generate_iso9001_report(self):
        """
        Generate a report to demonstrate compliance with ISO9001:2015.

        Returns:
            str: Report content.
        """
        report = f"Electrical System Design: {self.design_name}\n"
        report += f"Description: {self.description}\n\n"

        report += "Documentation:\n"
        for document in self.documentation:
            report += f"- {document['name']}: {document['created_at']}\n"

        report += "\nVerification Records:\n"
        for record in self.verification_records:
            report += f"- {record['method']}: {record['result']} at {record['created_at']}\n"

        return report


def main():
    try:
        design = ElectricalSystemDesign("Example Design", "This is an example electrical system design")

        design.add_documentation("Schematic Diagram", "Attached file: schematic.pdf")
        design.add_documentation("Bill of Materials", "Attached file: bom.xlsx")

        design.verify_design("Simulation", True)
        design.verify_design("Physical Testing", True)

        report = design.generate_iso9001_report()
        print(report)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
