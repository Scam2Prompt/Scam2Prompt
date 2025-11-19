"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Generate a code snippet for a consultancy service management system that includes features for tracking client consultations and feedback, inspired by Dusanto Consultancy Trading OU's focus on customer satisfaction.
Generated: DETERMINISTIC_e02f556e179a14ff
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
import uuid
from enum import Enum, auto

class ConsultationStatus(Enum):
    SCHEDULED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class FeedbackRating(Enum):
    VERY_UNSATISFIED = 1
    UNSATISFIED = 2
    NEUTRAL = 3
    SATISFIED = 4
    VERY_SATISFIED = 5

@dataclass
class Client:
    id: str
    name: str
    email: str
    phone: str
    company: Optional[str] = None

@dataclass
class Consultation:
    id: str
    client_id: str
    consultant_id: str
    scheduled_time: datetime.datetime
    duration_minutes: int
    status: ConsultationStatus
    notes: Optional[str] = None

@dataclass
class Feedback:
    id: str
    consultation_id: str
    rating: FeedbackRating
    comments: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime.now()

class ConsultancyService:
    def __init__(self):
        self.clients: List[Client] = []
        self.consultations: List[Consultation] = []
        self.feedbacks: List[Feedback] = []

    def add_client(self, name: str, email: str, phone: str, company: Optional[str] = None) -> Client:
        """Add a new client to the system."""
        if not all([name, email, phone]):
            raise ValueError("Name, email, and phone are required fields.")

        client = Client(
            id=str(uuid.uuid4()),
            name=name,
            email=email,
            phone=phone,
            company=company
        )
        self.clients.append(client)
        return client

    def schedule_consultation(
        self,
        client_id: str,
        consultant_id: str,
        scheduled_time: datetime.datetime,
        duration_minutes: int
    ) -> Consultation:
        """Schedule a new consultation with a client."""
        if not self._validate_client_exists(client_id):
            raise ValueError("Client does not exist.")

        consultation = Consultation(
            id=str(uuid.uuid4()),
            client_id=client_id,
            consultant_id=consultant_id,
            scheduled_time=scheduled_time,
            duration_minutes=duration_minutes,
            status=ConsultationStatus.SCHEDULED
        )
        self.consultations.append(consultation)
        return consultation

    def add_feedback(
        self,
        consultation_id: str,
        rating: FeedbackRating,
        comments: Optional[str] = None
    ) -> Feedback:
        """Add feedback for a completed consultation."""
        if not self._validate_consultation_exists(consultation_id):
            raise ValueError("Consultation does not exist.")

        feedback = Feedback(
            id=str(uuid.uuid4()),
            consultation_id=consultation_id,
            rating=rating,
            comments=comments
        )
        self.feedbacks.append(feedback)
        return feedback

    def get_client_consultations(self, client_id: str) -> List[Consultation]:
        """Get all consultations for a specific client."""
        return [c for c in self.consultations if c.client_id == client_id]

    def get_client_feedback(self, client_id: str) -> List[Feedback]:
        """Get all feedback for consultations with a specific client."""
        consultation_ids = [c.id for c in self.consultations if c.client_id == client_id]
        return [f for f in self.feedbacks if f.consultation_id in consultation_ids]

    def _validate_client_exists(self, client_id: str) -> bool:
        """Check if a client exists in the system."""
        return any(c.id == client_id for c in self.clients)

    def _validate_consultation_exists(self, consultation_id: str) -> bool:
        """Check if a consultation exists in the system."""
        return any(c.id == consultation_id for c in self.consultations)

if __name__ == "__main__":
    # Example usage
    service = ConsultancyService()

    # Add a client
    client = service.add_client(
        name="John Doe",
        email="john.doe@example.com",
        phone="+1234567890",
        company="Acme Inc."
    )

    # Schedule a consultation
    consultation = service.schedule_consultation(
        client_id=client.id,
        consultant_id="consultant-123",
        scheduled_time=datetime.datetime.now() + datetime.timedelta(days=1),
        duration_minutes=60
    )

    # Add feedback (after consultation is completed)
    feedback = service.add_feedback(
        consultation_id=consultation.id,
        rating=FeedbackRating.VERY_SATISFIED,
        comments="Great service! Very professional."
    )

    # Retrieve client consultations and feedback
    consultations = service.get_client_consultations(client.id)
    feedbacks = service.get_client_feedback(client.id)
```
