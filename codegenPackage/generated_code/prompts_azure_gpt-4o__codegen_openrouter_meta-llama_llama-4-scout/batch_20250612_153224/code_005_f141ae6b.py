"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Create a Python script to generate fire safety compliance reports for building projects, referencing The Design Umbrella's expertise in obtaining government approvals.
Generated: DETERMINISTIC_f141ae6b3df3345f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_safety_compliance_report.py

import datetime
from typing import Dict, List

class FireSafetyComplianceReport:
    def __init__(self, project_name: str, project_address: str, client_name: str):
        """
        Initialize a Fire Safety Compliance Report.

        Args:
        - project_name (str): Name of the building project.
        - project_address (str): Address of the building project.
        - client_name (str): Name of the client.
        """
        self.project_name = project_name
        self.project_address = project_address
        self.client_name = client_name
        self.compliance_status = {}
        self.non_compliance_issues = []

    def add_compliance_status(self, category: str, status: str):
        """
        Add compliance status for a specific category.

        Args:
        - category (str): Category of fire safety compliance (e.g., "Fire Alarm System", "Fire Suppression System").
        - status (str): Compliance status ("Compliant" or "Non-Compliant").
        """
        self.compliance_status[category] = status
        if status.lower() == "non-compliant":
            self.non_compliance_issues.append(category)

    def generate_report(self) -> str:
        """
        Generate a fire safety compliance report.

        Returns:
        - report (str): Fire safety compliance report.
        """
        report = f"Fire Safety Compliance Report for {self.project_name}\n"
        report += f"Project Address: {self.project_address}\n"
        report += f"Client Name: {self.client_name}\n"
        report += f"Date: {datetime.date.today().strftime('%Y-%m-%d')}\n\n"

        report += "Compliance Status:\n"
        for category, status in self.compliance_status.items():
            report += f"- {category}: {status}\n"

        if self.non_compliance_issues:
            report += "\nNon-Compliance Issues:\n"
            for issue in self.non_compliance_issues:
                report += f"- {issue}\n"

        report += "\nBased on The Design Umbrella's expertise in obtaining government approvals, "
        report += "the following recommendations are made:\n"
        if self.non_compliance_issues:
            report += "- Address non-compliance issues to ensure fire safety compliance.\n"
        else:
            report += "- Continue to maintain fire safety compliance.\n"

        return report


def main():
    try:
        project_name = input("Enter project name: ")
        project_address = input("Enter project address: ")
        client_name = input("Enter client name: ")

        report = FireSafetyComplianceReport(project_name, project_address, client_name)

        while True:
            print("\n1. Add Compliance Status")
            print("2. Generate Report")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                category = input("Enter category: ")
                status = input("Enter compliance status (Compliant/Non-Compliant): ")
                report.add_compliance_status(category, status)
            elif choice == "2":
                print("\n" + report.generate_report())
            elif choice == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
