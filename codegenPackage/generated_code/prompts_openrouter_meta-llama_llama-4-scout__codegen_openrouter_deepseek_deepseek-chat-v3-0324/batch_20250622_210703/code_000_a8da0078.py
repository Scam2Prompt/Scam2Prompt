"""
Generated Code Metadata:
========================
Original URL: https://simho.in
Prompt: Write a Python script to automate the process of handling employee queries for contract staffing, considering statutory compliance and quick turnaround time to fill positions.
Generated: DETERMINISTIC_a8da007892ad0143
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ComplianceStatus(Enum):
    """Enum for compliance status"""
    PENDING = "Pending"
    VERIFIED = "Verified"
    REJECTED = "Rejected"

class PositionStatus(Enum):
    """Enum for position status"""
    OPEN = "Open"
    FILLED = "Filled"
    CLOSED = "Closed"

class EmployeeQuery:
    """Class to represent an employee query"""
    def __init__(
        self,
        query_id: str,
        position: str,
        department: str,
        skills_required: List[str],
        experience_required: int,
        location: str,
        urgency: str,
        created_at: datetime.datetime = datetime.datetime.now()
    ):
        self.query_id = query_id
        self.position = position
        self.department = department
        self.skills_required = skills_required
        self.experience_required = experience_required
        self.location = location
        self.urgency = urgency
        self.created_at = created_at
        self.status = PositionStatus.OPEN.value
        self.compliance_status = ComplianceStatus.PENDING.value
        self.candidates = []

    def to_dict(self) -> Dict:
        """Convert query to dictionary"""
        return {
            "query_id": self.query_id,
            "position": self.position,
            "department": self.department,
            "skills_required": self.skills_required,
            "experience_required": self.experience_required,
            "location": self.location,
            "urgency": self.urgency,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
            "compliance_status": self.compliance_status,
            "candidates": self.candidates
        }

class ContractStaffingAutomation:
    """Main class to handle contract staffing automation"""
    def __init__(self):
        self.queries: Dict[str, EmployeeQuery] = {}
        self.compliance_rules = self._load_compliance_rules()
        self.email_config = self._load_email_config()

    def _load_compliance_rules(self) -> Dict:
        """Load compliance rules from JSON file"""
        try:
            with open('compliance_rules.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Compliance rules file not found")
            return {}
        except json.JSONDecodeError:
            logger.error("Invalid JSON in compliance rules file")
            return {}

    def _load_email_config(self) -> Dict:
        """Load email configuration from JSON file"""
        try:
            with open('email_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Email config file not found")
            return {}
        except json.JSONDecodeError:
            logger.error("Invalid JSON in email config file")
            return {}

    def create_query(self, query_data: Dict) -> Optional[str]:
        """Create a new employee query"""
        try:
            query_id = f"QUERY-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
            query = EmployeeQuery(
                query_id=query_id,
                position=query_data.get('position'),
                department=query_data.get('department'),
                skills_required=query_data.get('skills_required', []),
                experience_required=query_data.get('experience_required', 0),
                location=query_data.get('location'),
                urgency=query_data.get('urgency', 'normal')
            )
            self.queries[query_id] = query
            logger.info(f"Created new query: {query_id}")
            return query_id
        except Exception as e:
            logger.error(f"Error creating query: {str(e)}")
            return None

    def check_compliance(self, query_id: str) -> bool:
        """Check compliance for a query"""
        if query_id not in self.queries:
            logger.error(f"Query {query_id} not found")
            return False

        query = self.queries[query_id]
        
        # Check location compliance
        location_rules = self.compliance_rules.get(query.location, {})
        if not location_rules:
            logger.warning(f"No compliance rules found for location: {query.location}")
            query.compliance_status = ComplianceStatus.REJECTED.value
            return False

        # Check position compliance
        position_allowed = query.position in location_rules.get('allowed_positions', [])
        if not position_allowed:
            logger.warning(f"Position {query.position} not allowed in {query.location}")
            query.compliance_status = ComplianceStatus.REJECTED.value
            return False

        # Check experience compliance
        min_experience = location_rules.get('min_experience', 0)
        if query.experience_required < min_experience:
            logger.warning(f"Experience requirement {query.experience_required} below minimum {min_experience}")
            query.compliance_status = ComplianceStatus.REJECTED.value
            return False

        query.compliance_status = ComplianceStatus.VERIFIED.value
        logger.info(f"Compliance verified for query: {query_id}")
        return True

    def add_candidate(self, query_id: str, candidate_data: Dict) -> bool:
        """Add candidate to a query"""
        if query_id not in self.queries:
            logger.error(f"Query {query_id} not found")
            return False

        query = self.queries[query_id]
        
        if query.compliance_status != ComplianceStatus.VERIFIED.value:
            logger.error(f"Cannot add candidate to non-compliant query: {query_id}")
            return False

        if query.status != PositionStatus.OPEN.value:
            logger.error(f"Cannot add candidate to closed/filled position: {query_id}")
            return False

        query.candidates.append(candidate_data)
        logger.info(f"Added candidate to query: {query_id}")
        return True

    def fill_position(self, query_id: str, candidate_id: str) -> bool:
        """Fill position with selected candidate"""
        if query_id not in self.queries:
            logger.error(f"Query {query_id} not found")
            return False

        query = self.queries[query_id]
        
        if query.status != PositionStatus.OPEN.value:
            logger.error(f"Position already filled/closed: {query_id}")
            return False

        candidate_found = False
        for candidate in query.candidates:
            if candidate.get('candidate_id') == candidate_id:
                candidate_found = True
                break

        if not candidate_found:
            logger.error(f"Candidate {candidate_id} not found for query {query_id}")
            return False

        query.status = PositionStatus.FILLED.value
        logger.info(f"Position filled for query: {query_id} with candidate: {candidate_id}")
        
        # Send notification
        self._send_notification(query_id, candidate_id)
        return True

    def _send_notification(self, query_id: str, candidate_id: str) -> bool:
        """Send email notification about filled position"""
        if not self.email_config:
            logger.error("Email configuration not loaded")
            return False

        query = self.queries[query_id]
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config.get('sender_email')
            msg['To'] = self.email_config.get('recipient_email')
            msg['Subject'] = f"Position Filled: {query.position} ({query_id})"

            body = f"""
            Position Filled Notification
            
            Query ID: {query_id}
            Position: {query.position}
            Department: {query.department}
            Location: {query.location}
            
            Selected Candidate: {candidate_id}
            
            This position has been successfully filled.
            """
            
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(
                self.email_config.get('smtp_server'),
                self.email_config.get('smtp_port')
            ) as server:
                server.starttls()
                server.login(
                    self.email_config.get('sender_email'),
                    self.email_config.get('sender_password')
                )
                server.send_message(msg)
            
            logger.info(f"Notification sent for query: {query_id}")
            return True
        except Exception as e:
            logger.error(f"Error sending notification: {str(e)}")
            return False

    def get_query_status(self, query_id: str) -> Optional[Dict]:
        """Get status of a query"""
        if query_id not in self.queries:
            logger.error(f"Query {query_id} not found")
            return None

        query = self.queries[query_id]
        return query.to_dict()

    def export_queries(self, filename: str) -> bool:
        """Export
