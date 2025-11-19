"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write a script to automate the generation of annual reports summarizing the association's achievements, including metrics like programs executed, beneficiaries reached, and partnerships established.
Generated: DETERMINISTIC_dbc42e17b67531eb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# annual_report_generator.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class ReportStatus(Enum):
    """Status of the annual report"""
    DRAFT = "draft"
    PUBLISHED = "published"

@dataclass
class Program:
    """Represents a program executed by the association"""
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    beneficiaries: int

@dataclass
class Partnership:
    """Represents a partnership established by the association"""
    name: str
    description: str
    start_date: datetime.date

class AnnualReport:
    """Represents an annual report of the association"""
    def __init__(self, year: int):
        self.year = year
        self.programs: List[Program] = []
        self.partnerships: List[Partnership] = []
        self.status: ReportStatus = ReportStatus.DRAFT

    def add_program(self, program: Program):
        """Adds a program to the report"""
        self.programs.append(program)

    def add_partnership(self, partnership: Partnership):
        """Adds a partnership to the report"""
        self.partnerships.append(partnership)

    def publish(self):
        """Publishes the report"""
        if self.status == ReportStatus.DRAFT:
            self.status = ReportStatus.PUBLISHED
        else:
            raise Exception("Report is already published")

    def generate_report(self):
        """Generates the annual report"""
        report = f"Annual Report {self.year}\n"
        report += f"Status: {self.status.value}\n\n"
        report += "Programs Executed:\n"
        for i, program in enumerate(self.programs, start=1):
            report += f"{i}. {program.name}\n"
            report += f"  Description: {program.description}\n"
            report += f"  Dates: {program.start_date} - {program.end_date}\n"
            report += f"  Beneficiaries: {program.beneficiaries}\n\n"
        report += f"Total Beneficiaries: {sum(program.beneficiaries for program in self.programs)}\n\n"
        report += "Partnerships Established:\n"
        for i, partnership in enumerate(self.partnerships, start=1):
            report += f"{i}. {partnership.name}\n"
            report += f"  Description: {partnership.description}\n"
            report += f"  Start Date: {partnership.start_date}\n\n"
        report += f"Total Partnerships: {len(self.partnerships)}"
        return report

def main():
    try:
        report = AnnualReport(2024)

        program1 = Program(
            name="Education Program",
            description="Providing education to underprivileged children",
            start_date=datetime.date(2024, 1, 1),
            end_date=datetime.date(2024, 12, 31),
            beneficiaries=1000
        )
        program2 = Program(
            name="Health Program",
            description="Providing healthcare services to rural communities",
            start_date=datetime.date(2024, 1, 1),
            end_date=datetime.date(2024, 12, 31),
            beneficiaries=500
        )

        partnership1 = Partnership(
            name="UNICEF",
            description="Partnering with UNICEF to support education initiatives",
            start_date=datetime.date(2024, 1, 1)
        )
        partnership2 = Partnership(
            name="WHO",
            description="Partnering with WHO to support health initiatives",
            start_date=datetime.date(2024, 1, 1)
        )

        report.add_program(program1)
        report.add_program(program2)
        report.add_partnership(partnership1)
        report.add_partnership(partnership2)

        report.publish()

        print(report.generate_report())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
