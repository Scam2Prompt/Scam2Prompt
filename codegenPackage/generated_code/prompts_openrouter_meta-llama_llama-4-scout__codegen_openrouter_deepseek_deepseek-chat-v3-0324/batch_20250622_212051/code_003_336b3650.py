"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Design a data model for a mentorship platform that includes features such as mentor directories, opportunity databases, and scholarship listings.
Generated: DETERMINISTIC_336b36501600c83e
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MENTOR = "mentor"
    MENTEE = "mentee"

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    first_name: str
    last_name: str
    role: UserRole
    bio: Optional[str] = None
    skills: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

    @validator('skills')
    def validate_skills(cls, v):
        if len(v) > 20:
            raise ValueError("Cannot have more than 20 skills")
        return v

class MentorProfile(BaseModel):
    user_id: str
    expertise: List[str]
    years_of_experience: int
    availability: str
    linkedin_url: Optional[str] = None
    twitter_handle: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    mentee_capacity: int = Field(default=5, ge=1, le=20)

class MenteeProfile(BaseModel):
    user_id: str
    learning_goals: List[str]
    current_level: str
    desired_mentor_qualities: List[str] = []

class OpportunityType(str, Enum):
    INTERNSHIP = "internship"
    JOB = "job"
    VOLUNTEER = "volunteer"
    RESEARCH = "research"

class Opportunity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    organization: str
    opportunity_type: OpportunityType
    posted_by: str  # user_id of the poster
    posted_at: datetime = Field(default_factory=datetime.utcnow)
    deadline: Optional[datetime] = None
    is_active: bool = True
    tags: List[str] = []
    location: Optional[str] = None
    is_remote: bool = False

class Scholarship(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    amount: Optional[float] = None
    deadline: datetime
    eligibility_criteria: str
    application_url: str
    posted_by: str  # user_id of the poster
    posted_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    tags: List[str] = []

class MentorshipRequestStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "completed"

class MentorshipRequest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    mentee_id: str
    mentor_id: str
    message: Optional[str] = None
    status: MentorshipRequestStatus = MentorshipRequestStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    goals: List[str] = []

class MeetingPlatform(str, Enum):
    ZOOM = "zoom"
    GOOGLE_MEET = "google_meet"
    MICROSOFT_TEAMS = "microsoft_teams"
    OTHER = "other"

class MentorshipSession(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    request_id: str
    scheduled_time: datetime
    duration_minutes: int = Field(60, ge=15, le=240)
    platform: MeetingPlatform
    meeting_link: str
    notes: Optional[str] = None
    is_completed: bool = False
    feedback_from_mentor: Optional[str] = None
    feedback_from_mentee: Optional[str] = None
```
