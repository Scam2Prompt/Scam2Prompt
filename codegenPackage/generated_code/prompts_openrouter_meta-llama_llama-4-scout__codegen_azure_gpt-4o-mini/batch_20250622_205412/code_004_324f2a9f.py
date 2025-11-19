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
import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, constr, condecimal, validator

class IncidentReport(BaseModel):
    """Model for capturing a safety and health incident report in construction projects."""
    
    incident_id: int = Field(..., description="Unique identifier for the incident report.")
    project_id: int = Field(..., description="Identifier for the construction project.")
    incident_date: datetime.date = Field(..., description="Date when the incident occurred.")
    description: constr(min_length=1, max_length=500) = Field(..., description="Detailed description of the incident.")
    severity: str = Field(..., description="Severity level of the incident (e.g., Low, Medium, High).")
    reported_by: str = Field(..., description="Name of the person reporting the incident.")
    corrective_actions: Optional[List[str]] = Field(default_factory=list, description="List of corrective actions taken.")
    cost_estimate: Optional[condecimal(gt=0)] = Field(None, description="Estimated cost associated with the incident.")
    
    @validator('incident_date')
    def validate_incident_date(cls, v):
        """Ensure the incident date is not in the future."""
        if v > datetime.date.today():
            raise ValueError("Incident date cannot be in the future.")
        return v

    @validator('severity')
    def validate_severity(cls, v):
        """Ensure severity is one of the predefined levels."""
        valid_severities = ['Low', 'Medium', 'High']
        if v not in valid_severities:
            raise ValueError(f"Severity must be one of {valid_severities}.")
        return v

class IncidentReportManager:
    """Manager class for handling incident reports."""
    
    def __init__(self):
        self.reports: List[IncidentReport] = []
    
    def add_report(self, report: IncidentReport) -> None:
        """Add a new incident report to the manager."""
        self.reports.append(report)
    
    def get_report(self, incident_id: int) -> Optional[IncidentReport]:
        """Retrieve an incident report by its ID."""
        for report in self.reports:
            if report.incident_id == incident_id:
                return report
        return None
    
    def analyze_reports(self) -> dict:
        """Analyze incident reports and return summary statistics."""
        severity_count = {}
        total_cost = 0
        
        for report in self.reports:
            severity_count[report.severity] = severity_count.get(report.severity, 0) + 1
            if report.cost_estimate:
                total_cost += report.cost_estimate
        
        return {
            "total_reports": len(self.reports),
            "severity_distribution": severity_count,
            "total_cost": total_cost
        }

# Example usage
if __name__ == "__main__":
    manager = IncidentReportManager()
    
    # Create a sample incident report
    try:
        report = IncidentReport(
            incident_id=1,
            project_id=101,
            incident_date=datetime.date(2023, 10, 1),
            description="A worker slipped and fell on the site.",
            severity="Medium",
            reported_by="John Doe",
            corrective_actions=["Improved signage", "Safety training"],
            cost_estimate=1500.00
        )
        manager.add_report(report)
        
        # Analyze reports
        analysis = manager.analyze_reports()
        print(analysis)
        
    except Exception as e:
        print(f"Error occurred: {e}")
```
