"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Write a program to simulate digital visa application workflows, incorporating visapwr's focus on balancing security and customer expectations.
Generated: DETERMINISTIC_253d0980f8b4e072
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import random
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class VisaType(Enum):
    TOURIST = auto()
    BUSINESS = auto()
    STUDENT = auto()
    WORK = auto()
    TRANSIT = auto()

class ApplicationStatus(Enum):
    DRAFT = auto()
    SUBMITTED = auto()
    UNDER_REVIEW = auto()
    APPROVED = auto()
    REJECTED = auto()
    ADDITIONAL_DOCUMENTS_REQUIRED = auto()
    SCHEDULE_INTERVIEW = auto()

class SecurityRiskLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

@dataclass
class Applicant:
    id: str
    name: str
    email: str
    nationality: str
    passport_number: str
    date_of_birth: str
    risk_level: SecurityRiskLevel = SecurityRiskLevel.LOW

@dataclass
class Document:
    id: str
    type: str
    url: str
    verified: bool = False

@dataclass
class VisaApplication:
    id: str
    applicant: Applicant
    visa_type: VisaType
    status: ApplicationStatus
    documents: List[Document]
    submission_date: datetime
    last_updated: datetime
    processing_time_days: int
    notes: str = ""

class VisaWorkflowSimulator:
    def __init__(self):
        self.applications: Dict[str, VisaApplication] = {}
        self.security_checks = {
            SecurityRiskLevel.LOW: self._low_risk_check,
            SecurityRiskLevel.MEDIUM: self._medium_risk_check,
            SecurityRiskLevel.HIGH: self._high_risk_check
        }
    
    def create_application(
        self,
        applicant: Applicant,
        visa_type: VisaType,
        documents: List[Document]
    ) -> VisaApplication:
        """Create a new visa application."""
        app_id = str(uuid.uuid4())
        now = datetime.now()
        
        application = VisaApplication(
            id=app_id,
            applicant=applicant,
            visa_type=visa_type,
            status=ApplicationStatus.DRAFT,
            documents=documents,
            submission_date=now,
            last_updated=now,
            processing_time_days=self._estimate_processing_time(visa_type, applicant.risk_level)
        )
        
        self.applications[app_id] = application
        logger.info(f"Created new application {app_id} for {applicant.name}")
        return application
    
    def submit_application(self, application_id: str) -> VisaApplication:
        """Submit an application for processing."""
        if application_id not in self.applications:
            raise ValueError("Application not found")
        
        app = self.applications[application_id]
        app.status = ApplicationStatus.SUBMITTED
        app.last_updated = datetime.now()
        
        logger.info(f"Application {application_id} submitted")
        return app
    
    def process_application(self, application_id: str) -> VisaApplication:
        """Process an application through the workflow."""
        if application_id not in self.applications:
            raise ValueError("Application not found")
        
        app = self.applications[application_id]
        
        if app.status != ApplicationStatus.SUBMITTED:
            raise ValueError("Application must be in SUBMITTED status")
        
        # Perform security check based on risk level
        security_check = self.security_checks.get(app.applicant.risk_level)
        security_check(app)
        
        # Update status based on security check
        if app.status == ApplicationStatus.SUBMITTED:
            if random.random() < 0.7:  # 70% chance to move to under review
                app.status = ApplicationStatus.UNDER_REVIEW
            else:
                app.status = ApplicationStatus.ADDITIONAL_DOCUMENTS_REQUIRED
        
        app.last_updated = datetime.now()
        logger.info(f"Processed application {application_id}, new status: {app.status}")
        return app
    
    def review_application(self, application_id: str) -> VisaApplication:
        """Review an application and make a decision."""
        if application_id not in self.applications:
            raise ValueError("Application not found")
        
        app = self.applications[application_id]
        
        if app.status != ApplicationStatus.UNDER_REVIEW:
            raise ValueError("Application must be in UNDER_REVIEW status")
        
        # Simulate review process
        if app.applicant.risk_level == SecurityRiskLevel.HIGH:
            if random.random() < 0.3:  # 30% approval for high risk
                app.status = ApplicationStatus.APPROVED
            else:
                app.status = ApplicationStatus.REJECTED
        else:
            if random.random() < 0.85:  # 85% approval for low/medium risk
                app.status = ApplicationStatus.APPROVED
            else:
                app.status = ApplicationStatus.REJECTED
        
        app.last_updated = datetime.now()
        logger.info(f"Reviewed application {application_id}, decision: {app.status}")
        return app
    
    def request_additional_documents(self, application_id: str, document_types: List[str]) -> VisaApplication:
        """Request additional documents from applicant."""
        if application_id not in self.applications:
            raise ValueError("Application not found")
        
        app = self.applications[application_id]
        app.status = ApplicationStatus.ADDITIONAL_DOCUMENTS_REQUIRED
        app.notes = f"Requested additional documents: {', '.join(document_types)}"
        app.last_updated = datetime.now()
        
        logger.info(f"Requested additional documents for application {application_id}")
        return app
    
    def schedule_interview(self, application_id: str) -> VisaApplication:
        """Schedule an interview for the applicant."""
        if application_id not in self.applications:
            raise ValueError("Application not found")
        
        app = self.applications[application_id]
        app.status = ApplicationStatus.SCHEDULE_INTERVIEW
        app.last_updated = datetime.now()
        
        logger.info(f"Scheduled interview for application {application_id}")
        return app
    
    def _estimate_processing_time(self, visa_type: VisaType, risk_level: SecurityRiskLevel) -> int:
        """Estimate processing time based on visa type and risk level."""
        base_times = {
            VisaType.TOURIST: 15,
            VisaType.BUSINESS: 10,
            VisaType.STUDENT: 20,
            VisaType.WORK: 30,
            VisaType.TRANSIT: 5
        }
        
        risk_multipliers = {
            SecurityRiskLevel.LOW: 1.0,
            SecurityRiskLevel.MEDIUM: 1.5,
            SecurityRiskLevel.HIGH: 2.5
        }
        
        return int(base_times[visa_type] * risk_multipliers[risk_level])
    
    def _low_risk_check(self, application: VisaApplication):
        """Perform low risk security checks."""
        # Basic document verification
        for doc in application.documents:
            if not doc.verified:
                doc.verified = random.random() < 0.9  # 90% verification success
    
    def _medium_risk_check(self, application: VisaApplication):
        """Perform medium risk security checks."""
        self._low_risk_check(application)
        
        # Additional checks for medium risk
        if random.random() < 0.3:  # 30% chance to request interview
            application.status = ApplicationStatus.SCHEDULE_INTERVIEW
    
    def _high_risk_check(self, application: VisaApplication):
        """Perform high risk security checks."""
        self._medium_risk_check(application)
        
        # Additional checks for high risk
        if random.random() < 0.7:  # 70% chance to request additional documents
            application.status = ApplicationStatus.ADDITIONAL_DOCUMENTS_REQUIRED
    
    def get_application_status(self, application_id: str) -> Tuple[ApplicationStatus, str]:
        """Get current status of an application."""
        if application_id not in self.applications:
            raise ValueError("Application not found")
        
        app = self.applications[application_id]
        return (app.status, f"Last updated: {app.last_updated}")

def generate_sample_applicant(risk_level: SecurityRiskLevel = SecurityRiskLevel.LOW) -> Applicant:
    """Generate a sample applicant for testing."""
    nationalities = ["US", "UK", "CA", "AU", "IN", "CN", "JP", "BR", "FR", "DE"]
    return Applicant(
        id=str(uuid.uuid4()),
        name=f"Applicant-{random.randint(1000, 9999)}",
        email=f"user{random.randint(100, 999)}@example.com",
        nationality=random.choice(nationalities),
