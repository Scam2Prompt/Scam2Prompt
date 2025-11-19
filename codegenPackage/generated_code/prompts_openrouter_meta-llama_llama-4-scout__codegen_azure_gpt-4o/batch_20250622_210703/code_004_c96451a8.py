"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: "Design a data model for tracking project progress and performance metrics in a business intelligence system similar to what Jau Consulting provides."
Generated: DETERMINISTIC_c96451a87d9918c3
Batch ID: 20250622_210703
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

# Define the data model for a project
class Project(BaseModel):
    project_id: int = Field(..., description="Unique identifier for the project")
    name: str = Field(..., description="Name of the project")
    description: Optional[str] = Field(None, description="Brief description of the project")
    start_date: datetime = Field(..., description="Start date of the project")
    end_date: Optional[datetime] = Field(None, description="End date of the project")
    status: str = Field(..., description="Current status of the project (e.g., 'In Progress', 'Completed')")
    owner: str = Field(..., description="Name of the person responsible for the project")

# Define the data model for performance metrics
class PerformanceMetric(BaseModel):
    metric_id: int = Field(..., description="Unique identifier for the metric")
    project_id: int = Field(..., description="ID of the project this metric is associated with")
    name: str = Field(..., description="Name of the performance metric")
    value: float = Field(..., description="Value of the metric")
    target_value: Optional[float] = Field(None, description="Target value for the metric")
    timestamp: datetime = Field(..., description="Timestamp when the metric was recorded")

# Define the data model for tracking project progress
class ProjectProgress(BaseModel):
    progress_id: int = Field(..., description="Unique identifier for the progress entry")
    project_id: int = Field(..., description="ID of the project this progress is associated with")
    milestone: str = Field(..., description="Name of the milestone achieved")
    completion_percentage: float = Field(..., ge=0, le=100, description="Percentage of project completion")
    timestamp: datetime = Field(..., description="Timestamp when the progress was recorded")

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample project
        project = Project(
            project_id=1,
            name="Business Intelligence System",
            description="A system to track project progress and performance metrics",
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31),
            status="In Progress",
            owner="John Doe"
        )
        
        # Create a sample performance metric
        metric = PerformanceMetric(
            metric_id=101,
            project_id=1,
            name="Revenue Growth",
            value=15.5,
            target_value=20.0,
            timestamp=datetime.now()
        )
        
        # Create a sample project progress entry
        progress = ProjectProgress(
            progress_id=201,
            project_id=1,
            milestone="Phase 1 Completion",
            completion_percentage=50.0,
            timestamp=datetime.now()
        )
        
        # Print the created objects
        print(project)
        print(metric)
        print(progress)
    
    except ValidationError as e:
        # Handle validation errors
        print("Validation Error:", e)
```
