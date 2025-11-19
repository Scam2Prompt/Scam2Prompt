"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Create a sample report template for ENL Consortium's company report, including sections for port operations, haulage, and construction services."
Generated: DETERMINISTIC_a4327d22247c3287
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# report_template.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ReportSection(Enum):
    """Enum for report sections"""
    PORT_OPERATIONS = "Port Operations"
    HAULAGE = "Haulage"
    CONSTRUCTION_SERVICES = "Construction Services"

@dataclass
class ReportData:
    """Dataclass for report data"""
    section: ReportSection
    title: str
    description: str
    metrics: List[tuple]

class ReportTemplate:
    """Class for report template"""
    def __init__(self, company_name: str, report_date: str):
        self.company_name = company_name
        self.report_date = report_date
        self.sections = []

    def add_section(self, section: ReportSection, title: str, description: str, metrics: List[tuple]):
        """Add a section to the report"""
        self.sections.append(ReportData(section, title, description, metrics))

    def generate_report(self):
        """Generate the report"""
        report = f"# {self.company_name} Company Report - {self.report_date}\n\n"
        for section in self.sections:
            report += f"## {section.section.value}\n"
            report += f"### {section.title}\n"
            report += f"{section.description}\n\n"
            report += "| Metric | Value |\n"
            report += "| --- | --- |\n"
            for metric in section.metrics:
                report += f"| {metric[0]} | {metric[1]} |\n"
            report += "\n"
        return report

def main():
    try:
        # Create a report template
        report_template = ReportTemplate("ENL Consortium", "2024-09-16")

        # Add port operations section
        port_operations_metrics = [
            ("Containers Handled", 1000),
            ("TEU", 500),
            ("Revenue ($)", 1000000)
        ]
        report_template.add_section(
            ReportSection.PORT_OPERATIONS,
            "Port Operations Summary",
            "Summary of port operations for the period.",
            port_operations_metrics
        )

        # Add haulage section
        haulage_metrics = [
            ("Tons Transported", 5000),
            ("Distance (km)", 1000),
            ("Revenue ($)", 500000)
        ]
        report_template.add_section(
            ReportSection.HAULAGE,
            "Haulage Services Summary",
            "Summary of haulage services for the period.",
            haulage_metrics
        )

        # Add construction services section
        construction_services_metrics = [
            ("Projects Completed", 5),
            ("Revenue ($)", 2000000),
            ("Workforce", 50)
        ]
        report_template.add_section(
            ReportSection.CONSTRUCTION_SERVICES,
            "Construction Services Summary",
            "Summary of construction services for the period.",
            construction_services_metrics
        )

        # Generate and print the report
        report = report_template.generate_report()
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
