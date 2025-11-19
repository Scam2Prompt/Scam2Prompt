"""
Generated Code Metadata:
========================
Original URL: https://tracingiallc.com
Prompt: Design a workflow for a fund recovery process, including stages like assessment, case fact-finding, and investigation, based on Tracingia LLC's approach to recovering lost or stolen financial assets.
Generated: DETERMINISTIC_60872ba77d3e58df
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
import uuid

class CaseStatus(Enum):
    """Enum representing the possible statuses of a recovery case."""
    NEW = auto()
    ASSESSMENT = auto()
    FACT_FINDING = auto()
    INVESTIGATION = auto()
    RESOLVED = auto()
    CLOSED = auto()

@dataclass
class RecoveryCase:
    """Dataclass representing a fund recovery case."""
    case_id: str
    client_name: str
    amount_lost: float
    currency: str
    date_reported: datetime
    status: CaseStatus = CaseStatus.NEW
    assessment_notes: Optional[str] = None
    fact_findings: Optional[List[str]] = None
    investigation_results: Optional[str] = None
    resolution: Optional[str] = None

class RecoveryWorkflow:
    """Class representing the fund recovery workflow."""
    
    def __init__(self):
        self.cases = {}
        
    def create_case(self, client_name: str, amount_lost: float, currency: str) -> RecoveryCase:
        """Create a new recovery case."""
        if amount_lost <= 0:
            raise ValueError("Amount lost must be positive")
            
        case_id = str(uuid.uuid4())
        new_case = RecoveryCase(
            case_id=case_id,
            client_name=client_name,
            amount_lost=amount_lost,
            currency=currency,
            date_reported=datetime.now()
        )
        self.cases[case_id] = new_case
        return new_case
    
    def start_assessment(self, case_id: str, notes: str) -> RecoveryCase:
        """Begin the assessment stage of a case."""
        case = self._get_case(case_id)
        if case.status != CaseStatus.NEW:
            raise ValueError("Assessment can only be started for new cases")
            
        case.status = CaseStatus.ASSESSMENT
        case.assessment_notes = notes
        return case
    
    def complete_assessment(self, case_id: str) -> RecoveryCase:
        """Complete the assessment stage."""
        case = self._get_case(case_id)
        if case.status != CaseStatus.ASSESSMENT:
            raise ValueError("Assessment must be in progress to complete")
            
        case.status = CaseStatus.FACT_FINDING
        return case
    
    def add_fact_finding(self, case_id: str, finding: str) -> RecoveryCase:
        """Add a fact finding to the case."""
        case = self._get_case(case_id)
        if case.status != CaseStatus.FACT_FINDING:
            raise ValueError("Case must be in fact-finding stage")
            
        if case.fact_findings is None:
            case.fact_findings = []
        case.fact_findings.append(finding)
        return case
    
    def complete_fact_finding(self, case_id: str) -> RecoveryCase:
        """Complete the fact-finding stage."""
        case = self._get_case(case_id)
        if case.status != CaseStatus.FACT_FINDING:
            raise ValueError("Fact-finding must be in progress to complete")
            
        case.status = CaseStatus.INVESTIGATION
        return case
    
    def complete_investigation(self, case_id: str, results: str) -> RecoveryCase:
        """Complete the investigation with results."""
        case = self._get_case(case_id)
        if case.status != CaseStatus.INVESTIGATION:
            raise ValueError("Investigation must be in progress to complete")
            
        case.status = CaseStatus.RESOLVED
        case.investigation_results = results
        return case
    
    def resolve_case(self, case_id: str, resolution: str) -> RecoveryCase:
        """Mark a case as resolved with a resolution."""
        case = self._get_case(case_id)
        if case.status != CaseStatus.RESOLVED:
            raise ValueError("Case must be resolved before closing")
            
        case.status = CaseStatus.CLOSED
        case.resolution = resolution
        return case
    
    def _get_case(self, case_id: str) -> RecoveryCase:
        """Internal method to get a case by ID with error handling."""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError(f"Case with ID {case_id} not found")
        return case
    
    def get_case_status(self, case_id: str) -> CaseStatus:
        """Get the current status of a case."""
        case = self._get_case(case_id)
        return case.status
    
    def get_case_details(self, case_id: str) -> RecoveryCase:
        """Get all details of a case."""
        return self._get_case(case_id)
```
