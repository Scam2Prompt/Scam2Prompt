"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: Generate code for a vocational education partnership management system that facilitates collaboration between schools and international organizations, inspired by AVEA's joint education programs.
Generated: DETERMINISTIC_d1a898b7ab869762
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Vocational Education Partnership Management System (VEPMS)
A system to manage collaborations between schools and international organizations.
"""

from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum, auto
import uuid
import logging
from dataclasses import dataclass, field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PartnershipStatus(Enum):
    """Enum representing partnership statuses."""
    PROPOSED = auto()
    ACTIVE = auto()
    SUSPENDED = auto()
    COMPLETED = auto()
    TERMINATED = auto()

class ProgramType(Enum):
    """Enum representing program types."""
    DUAL_STUDY = auto()
    APPRENTICESHIP = auto()
    CERTIFICATION = auto()
    WORK_BASED_LEARNING = auto()
    EXCHANGE = auto()

@dataclass
class Organization:
    """Represents an organization participating in partnerships."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    country: str
    contact_email: str
    website: Optional[str] = None
    description: Optional[str] = None
    is_school: bool = False

    def __post_init__(self):
        if not self.name:
            raise ValueError("Organization name cannot be empty")
        if not self.contact_email or "@" not in self.contact_email:
            raise ValueError("Invalid contact email")

@dataclass
class Program:
    """Represents an educational program offered through a partnership."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    program_type: ProgramType
    description: str
    duration_months: int
    required_qualifications: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=lambda: ["English"])

    def __post_init__(self):
        if self.duration_months <= 0:
            raise ValueError("Duration must be positive")
        if not self.name:
            raise ValueError("Program name cannot be empty")

@dataclass
class Partnership:
    """Represents a partnership between organizations."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    organizations: List[Organization]
    programs: List[Program]
    start_date: datetime
    end_date: Optional[datetime] = None
    status: PartnershipStatus = PartnershipStatus.PROPOSED
    documents: List[str] = field(default_factory=list)
    notes: Optional[str] = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("Partnership name cannot be empty")
        if len(self.organizations) < 2:
            raise ValueError("Partnership must involve at least two organizations")
        if self.end_date and self.end_date < self.start_date:
            raise ValueError("End date cannot be before start date")

class PartnershipManager:
    """Manages partnerships between schools and organizations."""
    
    def __init__(self):
        self.partnerships: Dict[str, Partnership] = {}
        self.organizations: Dict[str, Organization] = {}
        self.programs: Dict[str, Program] = {}

    def add_organization(self, organization: Organization) -> str:
        """Add an organization to the system."""
        if organization.id in self.organizations:
            raise ValueError("Organization already exists")
        self.organizations[organization.id] = organization
        logger.info(f"Added organization: {organization.name}")
        return organization.id

    def add_program(self, program: Program) -> str:
        """Add a program to the system."""
        if program.id in self.programs:
            raise ValueError("Program already exists")
        self.programs[program.id] = program
        logger.info(f"Added program: {program.name}")
        return program.id

    def create_partnership(
        self,
        name: str,
        organization_ids: List[str],
        program_ids: List[str],
        start_date: datetime,
        end_date: Optional[datetime] = None,
        status: PartnershipStatus = PartnershipStatus.PROPOSED
    ) -> str:
        """Create a new partnership."""
        organizations = []
        for org_id in organization_ids:
            if org_id not in self.organizations:
                raise ValueError(f"Organization {org_id} not found")
            organizations.append(self.organizations[org_id])

        programs = []
        for prog_id in program_ids:
            if prog_id not in self.programs:
                raise ValueError(f"Program {prog_id} not found")
            programs.append(self.programs[prog_id])

        partnership = Partnership(
            name=name,
            organizations=organizations,
            programs=programs,
            start_date=start_date,
            end_date=end_date,
            status=status
        )

        self.partnerships[partnership.id] = partnership
        logger.info(f"Created partnership: {name}")
        return partnership.id

    def update_partnership_status(
        self,
        partnership_id: str,
        new_status: PartnershipStatus
    ) -> None:
        """Update the status of a partnership."""
        if partnership_id not in self.partnerships:
            raise ValueError("Partnership not found")
        
        self.partnerships[partnership_id].status = new_status
        logger.info(f"Updated partnership {partnership_id} status to {new_status}")

    def get_partnerships_by_organization(
        self,
        organization_id: str
    ) -> List[Partnership]:
        """Get all partnerships for a specific organization."""
        if organization_id not in self.organizations:
            raise ValueError("Organization not found")
        
        return [
            p for p in self.partnerships.values()
            if any(org.id == organization_id for org in p.organizations)
        ]

    def get_active_partnerships(self) -> List[Partnership]:
        """Get all active partnerships."""
        return [
            p for p in self.partnerships.values()
            if p.status == PartnershipStatus.ACTIVE
        ]

    def add_document_to_partnership(
        self,
        partnership_id: str,
        document_path: str
    ) -> None:
        """Add a document reference to a partnership."""
        if partnership_id not in self.partnerships:
            raise ValueError("Partnership not found")
        
        self.partnerships[partnership_id].documents.append(document_path)
        logger.info(f"Added document to partnership {partnership_id}")

    def search_programs(
        self,
        program_type: Optional[ProgramType] = None,
        language: Optional[str] = None,
        min_duration: Optional[int] = None
    ) -> List[Program]:
        """Search programs based on criteria."""
        results = list(self.programs.values())
        
        if program_type:
            results = [p for p in results if p.program_type == program_type]
        if language:
            results = [p for p in results if language in p.languages]
        if min_duration:
            results = [p for p in results if p.duration_months >= min_duration]
            
        return results

# Example usage
if __name__ == "__main__":
    try:
        manager = PartnershipManager()
        
        # Create organizations
        school = Organization(
            name="Tech Vocational School",
            country="Germany",
            contact_email="contact@techschool.de",
            is_school=True
        )
        company = Organization(
            name="Global Tech Inc.",
            country="USA",
            contact_email="partnerships@globaltech.com"
        )
        
        school_id = manager.add_organization(school)
        company_id = manager.add_organization(company)
        
        # Create programs
        dual_program = Program(
            name="Dual Study in Software Engineering",
            program_type=ProgramType.DUAL_STUDY,
            description="Combination of academic study and practical work",
            duration_months=36
        )
        cert_program = Program(
            name="Cloud Certification Program",
            program_type=ProgramType.CERTIFICATION,
            description="Professional certification in cloud technologies",
            duration_months=6
        )
        
        dual_program_id = manager.add_program(dual_program)
        cert_program_id = manager.add_program(cert_program)
        
        # Create partnership
        partnership_id = manager.create_partnership(
            name="Tech Education Initiative 2023",
            organization_ids=[school_id, company_id],
            program_ids=[dual_program_id, cert_program_id],
            start_date=datetime(2023, 9, 1),
            end_date=datetime(2026, 8, 31)
        )
        
        # Update status
        manager.update_partnership_status(partnership_id, PartnershipStatus.ACTIVE)
        
        # Search programs
        found_programs = manager.search_programs(
            program_type=ProgramType.DUAL_STUDY,
            min_duration=24
        )
        print(f"Found {len(found_programs)} matching programs")
        
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
