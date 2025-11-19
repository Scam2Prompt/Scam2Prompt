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
# Import necessary libraries
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

# Define the data model for a safety and health incident report
class IncidentReport(BaseModel):
    """
    Data model for capturing and analyzing safety and health incident reports
    in construction projects using AFCO's risk management framework.
    """
    incident_id: str = Field(..., description="Unique identifier for the incident report")
    project_name: str = Field(..., description="Name of the construction project")
    location: str = Field(..., description="Location where the incident occurred")
    date_time: datetime = Field(..., description="Date and time of the incident")
    reported_by: str = Field(..., description="Name of the person who reported the incident")
    description: str = Field(..., description="Detailed description of the incident")
    severity_level: str = Field(..., description="Severity level of the incident (e.g., Low, Medium, High)")
    risk_category: str = Field(..., description="Risk category based on AFCO's framework (e.g., Safety, Health, Environmental)")
    corrective_actions: Optional[List[str]] = Field(None, description="List of corrective actions taken or proposed")
    witnesses: Optional[List[str]] = Field(None, description="List of witnesses to the incident")
    attachments: Optional[List[str]] = Field(None, description="List of file paths or URLs to attachments related to the incident")

    class Config:
        """
        Configuration for the IncidentReport model.
        """
        schema_extra = {
            "example": {
                "incident_id": "INC12345",
                "project_name": "Downtown Office Tower",
                "location": "Site A - Floor 3",
                "date_time": "2023-10-01T14:30:00",
                "reported_by": "John Doe",
                "description": "Worker slipped on wet floor and sustained minor injuries.",
                "severity_level": "Medium",
                "risk_category": "Safety",
                "corrective_actions": ["Clean wet areas immediately", "Install warning signs"],
                "witnesses": ["Jane Smith", "Michael Brown"],
                "attachments": ["incident_photo.jpg", "medical_report.pdf"]
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create an example incident report
        example_report = IncidentReport(
            incident_id="INC12345",
            project_name="Downtown Office Tower",
            location="Site A - Floor 3",
            date_time=datetime(2023, 10, 1, 14, 30),
            reported_by="John Doe",
            description="Worker slipped on wet floor and sustained minor injuries.",
            severity_level="Medium",
            risk_category="Safety",
            corrective_actions=["Clean wet areas immediately", "Install warning signs"],
            witnesses=["Jane Smith", "Michael Brown"],
            attachments=["incident_photo.jpg", "medical_report.pdf"]
        )
        print(example_report.json(indent=4))
    except ValidationError as e:
        # Handle validation errors
        print("Error creating incident report:", e.json())
```
