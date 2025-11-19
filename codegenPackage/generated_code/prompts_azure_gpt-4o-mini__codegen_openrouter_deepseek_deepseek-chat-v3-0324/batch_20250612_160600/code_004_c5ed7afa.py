"""
Generated Code Metadata:
========================
Original URL: https://medurex.com
Prompt: Outline a workflow for a clinical trial that includes study design, data management, and regulatory support, reflecting the streamlined processes described by Medurex.
Generated: DETERMINISTIC_c5ed7afa7ab5d67d
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Clinical Trial Workflow System for Medurex

This module outlines a streamlined workflow for clinical trials including:
- Study Design
- Data Management
- Regulatory Support
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
from datetime import date
import uuid

class TrialPhase(Enum):
    """Enum representing clinical trial phases"""
    PHASE_I = auto()
    PHASE_II = auto()
    PHASE_III = auto()
    PHASE_IV = auto()

class RegulatoryStatus(Enum):
    """Enum representing regulatory approval status"""
    DRAFT = auto()
    SUBMITTED = auto()
    APPROVED = auto()
    REJECTED = auto()
    AMENDMENT_REQUESTED = auto()

class DataCollectionMethod(Enum):
    """Enum representing data collection methods"""
    ELECTRONIC = auto()
    PAPER = auto()
    HYBRID = auto()

@dataclass
class StudySite:
    """Class representing a clinical trial site"""
    site_id: str
    name: str
    location: str
    principal_investigator: str
    is_active: bool = True

@dataclass
class Participant:
    """Class representing a trial participant"""
    participant_id: str
    site_id: str
    enrollment_date: date
    demographic_data: dict
    is_active: bool = True

@dataclass
class Protocol:
    """Class representing the study protocol"""
    protocol_id: str
    title: str
    version: str
    phase: TrialPhase
    objectives: List[str]
    inclusion_criteria: List[str]
    exclusion_criteria: List[str]
    approval_status: RegulatoryStatus = RegulatoryStatus.DRAFT

@dataclass
class CaseReportForm:
    """Class representing a Case Report Form (CRF)"""
    crf_id: str
    name: str
    version: str
    fields: List[dict]
    collection_method: DataCollectionMethod

@dataclass
class RegulatoryDocument:
    """Class representing regulatory documents"""
    doc_id: str
    name: str
    type: str
    version: str
    submission_date: Optional[date] = None
    approval_date: Optional[date] = None
    status: RegulatoryStatus = RegulatoryStatus.DRAFT

class ClinicalTrialWorkflow:
    """Main class representing the clinical trial workflow"""
    
    def __init__(self):
        self.protocol = None
        self.sites = []
        self.participants = []
        self.crfs = []
        self.regulatory_docs = []
    
    def create_protocol(self, title: str, phase: TrialPhase, objectives: List[str],
                       inclusion_criteria: List[str], exclusion_criteria: List[str]) -> Protocol:
        """Create a new study protocol"""
        protocol = Protocol(
            protocol_id=str(uuid.uuid4()),
            title=title,
            version="1.0",
            phase=phase,
            objectives=objectives,
            inclusion_criteria=inclusion_criteria,
            exclusion_criteria=exclusion_criteria
        )
        self.protocol = protocol
        return protocol
    
    def add_site(self, name: str, location: str, principal_investigator: str) -> StudySite:
        """Add a new study site"""
        site = StudySite(
            site_id=str(uuid.uuid4()),
            name=name,
            location=location,
            principal_investigator=principal_investigator
        )
        self.sites.append(site)
        return site
    
    def enroll_participant(self, site_id: str, demographic_data: dict) -> Participant:
        """Enroll a new participant"""
        participant = Participant(
            participant_id=str(uuid.uuid4()),
            site_id=site_id,
            enrollment_date=date.today(),
            demographic_data=demographic_data
        )
        self.participants.append(participant)
        return participant
    
    def create_crf(self, name: str, fields: List[dict], 
                   collection_method: DataCollectionMethod) -> CaseReportForm:
        """Create a new Case Report Form"""
        crf = CaseReportForm(
            crf_id=str(uuid.uuid4()),
            name=name,
            version="1.0",
            fields=fields,
            collection_method=collection_method
        )
        self.crfs.append(crf)
        return crf
    
    def submit_regulatory_document(self, name: str, type: str) -> RegulatoryDocument:
        """Submit a regulatory document for approval"""
        doc = RegulatoryDocument(
            doc_id=str(uuid.uuid4()),
            name=name,
            type=type,
            version="1.0",
            submission_date=date.today(),
            status=RegulatoryStatus.SUBMITTED
        )
        self.regulatory_docs.append(doc)
        return doc
    
    def update_regulatory_status(self, doc_id: str, status: RegulatoryStatus) -> bool:
        """Update the status of a regulatory document"""
        for doc in self.regulatory_docs:
            if doc.doc_id == doc_id:
                doc.status = status
                if status == RegulatoryStatus.APPROVED:
                    doc.approval_date = date.today()
                return True
        return False
    
    def get_active_participants(self) -> List[Participant]:
        """Get all active participants"""
        return [p for p in self.participants if p.is_active]
    
    def get_active_sites(self) -> List[StudySite]:
        """Get all active sites"""
        return [s for s in self.sites if s.is_active]

# Example usage
if __name__ == "__main__":
    workflow = ClinicalTrialWorkflow()
    
    # Study Design
    protocol = workflow.create_protocol(
        title="Efficacy of New Drug X",
        phase=TrialPhase.PHASE_III,
        objectives=["Assess efficacy", "Evaluate safety"],
        inclusion_criteria=["Age 18-65", "Diagnosed with condition Y"],
        exclusion_criteria=["Pregnant women", "Prior treatment with Z"]
    )
    
    # Site Management
    site1 = workflow.add_site(
        name="Main Medical Center",
        location="New York",
        principal_investigator="Dr. Smith"
    )
    
    # Participant Enrollment
    participant1 = workflow.enroll_participant(
        site_id=site1.site_id,
        demographic_data={"age": 45, "gender": "F"}
    )
    
    # Data Management
    crf = workflow.create_crf(
        name="Baseline Assessment",
        fields=[
            {"name": "blood_pressure", "type": "number"},
            {"name": "symptoms", "type": "text"}
        ],
        collection_method=DataCollectionMethod.ELECTRONIC
    )
    
    # Regulatory Support
    ind = workflow.submit_regulatory_document(
        name="Investigational New Drug Application",
        type="IND"
    )
    workflow.update_regulatory_status(ind.doc_id, RegulatoryStatus.APPROVED)
```
