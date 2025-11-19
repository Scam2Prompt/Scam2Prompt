"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a data model for capturing and analyzing safety and health incident reports in construction projects, using AFCO's risk management framework as a reference.
Generated: DETERMINISTIC_324f2a9fd1a02bdf
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safety_incident_report.py

from enum import Enum
from datetime import datetime
from typing import List

class IncidentType(str, Enum):
    """Types of safety and health incidents"""
    ACCIDENT = "Accident"
    NEAR_MISS = "Near Miss"
    INJURY = "Injury"
    ILLNESS = "Illness"

class RiskCategory(str, Enum):
    """AFCO's risk management framework categories"""
    HAZARD = "Hazard"
    EXPOSURE = "Exposure"
    CONTROL = "Control"

class SafetyIncidentReport:
    """Data model for capturing and analyzing safety and health incident reports"""

    def __init__(self, 
                 incident_id: str, 
                 incident_type: IncidentType, 
                 date: datetime, 
                 location: str, 
                 description: str, 
                 risk_category: RiskCategory, 
                 risk_assessment: str, 
                 actions_taken: str, 
                 reporter: str):
        """
        Initialize a SafetyIncidentReport object.

        Args:
        - incident_id (str): Unique identifier for the incident report
        - incident_type (IncidentType): Type of safety and health incident
        - date (datetime): Date and time of the incident
        - location (str): Location where the incident occurred
        - description (str): Detailed description of the incident
        - risk_category (RiskCategory): AFCO's risk management framework category
        - risk_assessment (str): Risk assessment of the incident
        - actions_taken (str): Actions taken in response to the incident
        - reporter (str): Person reporting the incident
        """
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.date = date
        self.location = location
        self.description = description
        self.risk_category = risk_category
        self.risk_assessment = risk_assessment
        self.actions_taken = actions_taken
        self.reporter = reporter

    def __str__(self):
        return f"Incident ID: {self.incident_id}"

    def to_dict(self):
        """Convert the SafetyIncidentReport object to a dictionary"""
        return {
            "incident_id": self.incident_id,
            "incident_type": self.incident_type.value,
            "date": self.date.isoformat(),
            "location": self.location,
            "description": self.description,
            "risk_category": self.risk_category.value,
            "risk_assessment": self.risk_assessment,
            "actions_taken": self.actions_taken,
            "reporter": self.reporter
        }

class SafetyIncidentReportRepository:
    """Repository for storing and retrieving safety and health incident reports"""

    def __init__(self):
        self.reports = []

    def add_report(self, report: SafetyIncidentReport):
        """Add a safety and health incident report to the repository"""
        self.reports.append(report)

    def get_reports(self) -> List[SafetyIncidentReport]:
        """Retrieve all safety and health incident reports from the repository"""
        return self.reports

    def get_report(self, incident_id: str) -> SafetyIncidentReport:
        """Retrieve a safety and health incident report by incident ID"""
        for report in self.reports:
            if report.incident_id == incident_id:
                return report
        raise ValueError(f"No report found with incident ID {incident_id}")

def main():
    # Example usage
    repository = SafetyIncidentReportRepository()

    report1 = SafetyIncidentReport(
        incident_id="INC001",
        incident_type=IncidentType.ACCIDENT,
        date=datetime(2022, 9, 1, 10, 0, 0),
        location="Construction Site A",
        description="Worker fell from scaffolding",
        risk_category=RiskCategory.HAZARD,
        risk_assessment="High risk",
        actions_taken="Worker received medical attention",
        reporter="John Doe"
    )

    repository.add_report(report1)

    print(report1.to_dict())

    try:
        report = repository.get_report("INC001")
        print(report.to_dict())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
