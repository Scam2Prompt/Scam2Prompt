"""
Generated Code Metadata:
========================
Original URL: https://pepedao.org
Prompt: Describe the process for submitting a request for a new feature on the WIKIWIKI platform.
Generated: DETERMINISTIC_0a80c176b06133f6
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Optional
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, validator, Field

class FeaturePriority(Enum):
    """Enum representing the priority levels for feature requests."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class FeatureStatus(Enum):
    """Enum representing the status of feature requests."""
    SUBMITTED = "Submitted"
    UNDER_REVIEW = "Under Review"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    IN_DEVELOPMENT = "In Development"
    COMPLETED = "Completed"

class FeatureRequest(BaseModel):
    """Model representing a feature request submission."""
    title: str = Field(..., min_length=5, max_length=100, description="Title of the feature request")
    description: str = Field(..., min_length=20, max_length=1000, description="Detailed description of the feature")
    requester_name: str = Field(..., min_length=2, max_length=50, description="Name of the person requesting the feature")
    requester_email: str = Field(..., description="Email of the requester")
    priority: FeaturePriority = Field(default=FeaturePriority.MEDIUM, description="Priority level of the feature")
    status: FeatureStatus = Field(default=FeatureStatus.SUBMITTED, description="Current status of the request")
    submission_date: datetime = Field(default_factory=datetime.now, description="Date when request was submitted")
    additional_notes: Optional[str] = Field(default=None, max_length=500, description="Optional additional notes")

    @validator('requester_email')
    def validate_email(cls, v):
        """Validate that the email contains an @ symbol and a domain."""
        if '@' not in v or '.' not in v.split('@')[-1]:
            raise ValueError('Invalid email format')
        return v

class FeatureRequestSystem:
    """System for managing feature requests on WIKIWIKI platform."""
    
    def __init__(self):
        self.feature_requests: Dict[int, FeatureRequest] = {}
        self.next_id = 1

    def submit_feature_request(self, request: FeatureRequest) -> int:
        """Submit a new feature request and return its ID."""
        request_id = self.next_id
        self.feature_requests[request_id] = request
        self.next_id += 1
        return request_id

    def get_feature_request(self, request_id: int) -> Optional[FeatureRequest]:
        """Retrieve a feature request by its ID."""
        return self.feature_requests.get(request_id)

    def update_feature_request_status(self, request_id: int, new_status: FeatureStatus) -> bool:
        """Update the status of a feature request."""
        if request_id not in self.feature_requests:
            return False
        self.feature_requests[request_id].status = new_status
        return True

    def get_all_feature_requests(self) -> Dict[int, FeatureRequest]:
        """Get all feature requests."""
        return self.feature_requests.copy()

# Example usage
if __name__ == "__main__":
    system = FeatureRequestSystem()
    
    # Create a new feature request
    new_request = FeatureRequest(
        title="Dark Mode Support",
        description="Add a dark mode option to reduce eye strain during nighttime usage.",
        requester_name="John Doe",
        requester_email="john.doe@example.com",
        priority=FeaturePriority.HIGH
    )
    
    # Submit the request
    request_id = system.submit_feature_request(new_request)
    print(f"Feature request submitted with ID: {request_id}")
    
    # Retrieve the request
    retrieved_request = system.get_feature_request(request_id)
    if retrieved_request:
        print(f"Retrieved request: {retrieved_request.title}")
```
