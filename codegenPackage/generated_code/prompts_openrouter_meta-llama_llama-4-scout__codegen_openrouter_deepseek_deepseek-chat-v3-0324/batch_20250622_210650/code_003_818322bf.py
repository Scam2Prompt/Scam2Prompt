"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Generate a sample enrollment application for Happy Scholars Academy, including required documents and information, such as the Universal Child Health Record form.
Generated: DETERMINISTIC_818322bfa2d21f63
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, validator
import json

class GradeLevel(Enum):
    PRE_K = "Pre-Kindergarten"
    KINDERGARTEN = "Kindergarten"
    FIRST = "1st Grade"
    SECOND = "2nd Grade"
    THIRD = "3rd Grade"
    FOURTH = "4th Grade"
    FIFTH = "5th Grade"
    SIXTH = "6th Grade"
    SEVENTH = "7th Grade"
    EIGHTH = "8th Grade"

class DocumentType(Enum):
    BIRTH_CERTIFICATE = "Birth Certificate"
    IMMUNIZATION_RECORD = "Immunization Record"
    UNIVERSAL_CHILD_HEALTH_RECORD = "Universal Child Health Record"
    PROOF_OF_RESIDENCE = "Proof of Residence"
    PARENT_ID = "Parent/Guardian ID"
    REPORT_CARD = "Previous School Report Card"

class GuardianRelationship(Enum):
    PARENT = "Parent"
    GUARDIAN = "Legal Guardian"
    FOSTER_PARENT = "Foster Parent"
    OTHER = "Other"

class Guardian(BaseModel):
    first_name: str = Field(..., description="First name of guardian")
    last_name: str = Field(..., description="Last name of guardian")
    relationship: GuardianRelationship = Field(..., description="Relationship to student")
    email: str = Field(..., description="Email address")
    phone: str = Field(..., description="Phone number")
    address: str = Field(..., description="Street address")
    city: str = Field(..., description="City")
    state: str = Field(..., description="State")
    zip_code: str = Field(..., description="Zip code")

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

class Document(BaseModel):
    type: DocumentType = Field(..., description="Type of document")
    is_submitted: bool = Field(False, description="Whether document has been submitted")
    notes: Optional[str] = Field(None, description="Additional notes about document")

class EnrollmentApplication(BaseModel):
    student_first_name: str = Field(..., description="Student's first name")
    student_last_name: str = Field(..., description="Student's last name")
    date_of_birth: date = Field(..., description="Student's date of birth")
    grade_level: GradeLevel = Field(..., description="Grade level applying for")
    current_school: Optional[str] = Field(None, description="Current school attending")
    guardians: List[Guardian] = Field(..., min_items=1, description="List of guardians")
    documents: List[Document] = Field(..., description="Required documents")
    is_completed: bool = Field(False, description="Whether application is completed")
    submission_date: Optional[date] = Field(None, description="Date application was submitted")

    @validator('date_of_birth')
    def validate_birth_date(cls, v):
        if v > date.today():
            raise ValueError('Birth date cannot be in the future')
        return v

def generate_sample_application():
    """Generate a sample enrollment application for Happy Scholars Academy"""
    guardians = [
        Guardian(
            first_name="Jane",
            last_name="Doe",
            relationship=GuardianRelationship.PARENT,
            email="jane.doe@example.com",
            phone="555-123-4567",
            address="123 Main St",
            city="Anytown",
            state="CA",
            zip_code="90210"
        )
    ]

    required_documents = [
        Document(type=DocumentType.BIRTH_CERTIFICATE),
        Document(type=DocumentType.IMMUNIZATION_RECORD),
        Document(type=DocumentType.UNIVERSAL_CHILD_HEALTH_RECORD),
        Document(type=DocumentType.PROOF_OF_RESIDENCE),
        Document(type=DocumentType.PARENT_ID),
        Document(type=DocumentType.REPORT_CARD)
    ]

    application = EnrollmentApplication(
        student_first_name="John",
        student_last_name="Doe",
        date_of_birth=date(2015, 6, 15),
        grade_level=GradeLevel.THIRD,
        current_school="Sunshine Elementary",
        guardians=guardians,
        documents=required_documents,
        is_completed=True,
        submission_date=date.today()
    )

    return application

def save_application_to_file(application: EnrollmentApplication, filename: str):
    """Save application to JSON file"""
    with open(filename, 'w') as f:
        json.dump(application.dict(), f, indent=2, default=str)

def load_application_from_file(filename: str) -> EnrollmentApplication:
    """Load application from JSON file"""
    with open(filename, 'r') as f:
        data = json.load(f)
        # Convert date strings back to date objects
        data['date_of_birth'] = date.fromisoformat(data['date_of_birth'])
        if data['submission_date']:
            data['submission_date'] = date.fromisoformat(data['submission_date'])
        for guardian in data['guardians']:
            guardian['relationship'] = GuardianRelationship(guardian['relationship'])
        for doc in data['documents']:
            doc['type'] = DocumentType(doc['type'])
        data['grade_level'] = GradeLevel(data['grade_level'])
        return EnrollmentApplication(**data)

if __name__ == "__main__":
    # Generate and save a sample application
    app = generate_sample_application()
    save_application_to_file(app, "happy_scholars_enrollment.json")
    
    # Load and display the application
    loaded_app = load_application_from_file("happy_scholars_enrollment.json")
    print(loaded_app.json(indent=2))
```
