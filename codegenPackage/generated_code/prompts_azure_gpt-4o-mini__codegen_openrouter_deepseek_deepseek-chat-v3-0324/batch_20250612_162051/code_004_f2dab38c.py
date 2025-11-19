"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Illustrate how to implement a customer feedback system in a computer repair service application, taking cues from the customer satisfaction guarantees of Geeks on Repair.
Generated: DETERMINISTIC_f2dab38cab6366d4
Batch ID: 20250612_162051
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
from typing import List, Dict, Optional
from enum import Enum
import json
import uuid

# Define enums for feedback status and rating
class FeedbackStatus(Enum):
    PENDING = "Pending"
    REVIEWED = "Reviewed"
    RESOLVED = "Resolved"
    ESCALATED = "Escalated"

class Rating(Enum):
    VERY_POOR = 1
    POOR = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

# Define data models
class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

class RepairService:
    def __init__(self, service_id: str, name: str, description: str):
        self.service_id = service_id
        self.name = name
        self.description = description

class Feedback:
    def __init__(
        self,
        feedback_id: str,
        customer: Customer,
        service: RepairService,
        rating: Rating,
        comments: str,
        status: FeedbackStatus = FeedbackStatus.PENDING,
        created_at: Optional[datetime] = None
    ):
        self.feedback_id = feedback_id
        self.customer = customer
        self.service = service
        self.rating = rating
        self.comments = comments
        self.status = status
        self.created_at = created_at or datetime.now()

    def to_dict(self) -> Dict:
        return {
            "feedback_id": self.feedback_id,
            "customer": {
                "customer_id": self.customer.customer_id,
                "name": self.customer.name,
                "email": self.customer.email,
                "phone": self.customer.phone
            },
            "service": {
                "service_id": self.service.service_id,
                "name": self.service.name,
                "description": self.service.description
            },
            "rating": self.rating.value,
            "comments": self.comments,
            "status": self.status.value,
            "created_at": self.created_at.isoformat()
        }

# Feedback system implementation
class FeedbackSystem:
    def __init__(self):
        self.feedbacks: List[Feedback] = []
    
    def submit_feedback(
        self,
        customer: Customer,
        service: RepairService,
        rating: Rating,
        comments: str
    ) -> Feedback:
        """Submit new customer feedback."""
        feedback_id = str(uuid.uuid4())
        feedback = Feedback(feedback_id, customer, service, rating, comments)
        self.feedbacks.append(feedback)
        return feedback
    
    def get_feedback_by_id(self, feedback_id: str) -> Optional[Feedback]:
        """Retrieve feedback by its ID."""
        for feedback in self.feedbacks:
            if feedback.feedback_id == feedback_id:
                return feedback
        return None
    
    def update_feedback_status(
        self,
        feedback_id: str,
        new_status: FeedbackStatus
    ) -> Optional[Feedback]:
        """Update the status of a feedback."""
        feedback = self.get_feedback_by_id(feedback_id)
        if feedback:
            feedback.status = new_status
            return feedback
        return None
    
    def get_feedbacks_by_status(self, status: FeedbackStatus) -> List[Feedback]:
        """Retrieve all feedbacks with a specific status."""
        return [fb for fb in self.feedbacks if fb.status == status]
    
    def get_average_rating(self) -> float:
        """Calculate average rating from all feedbacks."""
        if not self.feedbacks:
            return 0.0
        total = sum(fb.rating.value for fb in self.feedbacks)
        return total / len(self.feedbacks)
    
    def save_to_file(self, filename: str) -> bool:
        """Save all feedbacks to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([fb.to_dict() for fb in self.feedbacks], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving feedbacks: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load feedbacks from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.feedbacks = []
                for item in data:
                    customer_data = item['customer']
                    customer = Customer(
                        customer_data['customer_id'],
                        customer_data['name'],
                        customer_data['email'],
                        customer_data['phone']
                    )
                    service_data = item['service']
                    service = RepairService(
                        service_data['service_id'],
                        service_data['name'],
                        service_data['description']
                    )
                    feedback = Feedback(
                        item['feedback_id'],
                        customer,
                        service,
                        Rating(item['rating']),
                        item['comments'],
                        FeedbackStatus(item['status']),
                        datetime.fromisoformat(item['created_at'])
                    )
                    self.feedbacks.append(feedback)
            return True
        except Exception as e:
            print(f"Error loading feedbacks: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize system
    feedback_system = FeedbackSystem()
    
    # Create sample data
    customer = Customer(
        "cust-123",
        "John Doe",
        "john.doe@example.com",
        "555-123-4567"
    )
    
    service = RepairService(
        "svc-456",
        "Laptop Screen Replacement",
        "Replacement of broken laptop screen"
    )
    
    # Submit feedback
    feedback = feedback_system.submit_feedback(
        customer,
        service,
        Rating.EXCELLENT,
        "Great service! Fast turnaround and professional technicians."
    )
    
    # Update status
    feedback_system.update_feedback_status(feedback.feedback_id, FeedbackStatus.REVIEWED)
    
    # Save to file
    feedback_system.save_to_file("feedbacks.json")
    
    # Load from file
    feedback_system.load_from_file("feedbacks.json")
    
    # Print average rating
    print(f"Average rating: {feedback_system.get_average_rating()}")
```
