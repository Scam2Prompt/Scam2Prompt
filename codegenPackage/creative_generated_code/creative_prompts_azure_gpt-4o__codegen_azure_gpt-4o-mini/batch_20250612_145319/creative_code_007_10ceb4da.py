"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Create a data model for tracking client feedback and satisfaction for interior design projects, referencing Zirciulit Design Firm's commitment to customer collaboration.
Generated: DETERMINISTIC_10ceb4da035e4d0e
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, validator

class ClientFeedback(BaseModel):
    """Model to represent client feedback for interior design projects."""
    
    feedback_id: int = Field(..., description="Unique identifier for the feedback entry")
    client_name: str = Field(..., description="Name of the client providing the feedback")
    client_email: EmailStr = Field(..., description="Email address of the client")
    project_id: int = Field(..., description="Identifier of the associated interior design project")
    satisfaction_rating: int = Field(..., ge=1, le=5, description="Satisfaction rating from 1 to 5")
    comments: Optional[str] = Field(None, description="Additional comments from the client")
    feedback_date: datetime = Field(default_factory=datetime.now, description="Date when the feedback was provided")

    @validator('satisfaction_rating')
    def check_satisfaction_rating(cls, value):
        """Ensure that the satisfaction rating is between 1 and 5."""
        if value < 1 or value > 5:
            raise ValueError('Satisfaction rating must be between 1 and 5.')
        return value

class InteriorDesignProject(BaseModel):
    """Model to represent an interior design project."""
    
    project_id: int = Field(..., description="Unique identifier for the project")
    project_name: str = Field(..., description="Name of the interior design project")
    client_name: str = Field(..., description="Name of the client")
    feedback_list: List[ClientFeedback] = Field(default_factory=list, description="List of feedback entries for this project")

    def add_feedback(self, feedback: ClientFeedback):
        """Add new feedback to the project."""
        if feedback.project_id != self.project_id:
            raise ValueError("Feedback's project_id must match the project's ID.")
        self.feedback_list.append(feedback)

    def average_satisfaction(self) -> float:
        """Calculate the average satisfaction rating from the feedback."""
        if not self.feedback_list:
            return 0.0
        total_rating = sum(feedback.satisfaction_rating for feedback in self.feedback_list)
        return total_rating / len(self.feedback_list)

# Example usage
if __name__ == "__main__":
    try:
        project = InteriorDesignProject(project_id=1, project_name="Modern Living Room", client_name="John Doe")
        
        # Creating a feedback entry
        feedback1 = ClientFeedback(feedback_id=1, client_name="John Doe", client_email="john.doe@example.com",
                                   project_id=1, satisfaction_rating=4, comments="Great design!")
        
        # Adding feedback to the project
        project.add_feedback(feedback1)
        
        # Adding another feedback entry
        feedback2 = ClientFeedback(feedback_id=2, client_name="Jane Smith", client_email="jane.smith@example.com",
                                   project_id=1, satisfaction_rating=5, comments="Absolutely loved it!")
        project.add_feedback(feedback2)

        # Calculate average satisfaction rating
        average_rating = project.average_satisfaction()
        print(f"Average Satisfaction Rating: {average_rating:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
