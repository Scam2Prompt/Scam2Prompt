"""
Generated Code Metadata:
========================
Original URL: https://medurex.com
Prompt: Write code to simulate a clinical trial workflow, including study design, data management, and regulatory compliance, based on Medurex's three-step streamlined process.
Generated: DETERMINISTIC_2ba111e67861c8a7
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import json
import csv
from pathlib import Path
from enum import Enum, auto


class StudyPhase(Enum):
    PHASE_I = auto()
    PHASE_II = auto()
    PHASE_III = auto()
    PHASE_IV = auto()


class RegulatoryStatus(Enum):
    DRAFT = auto()
    SUBMITTED = auto()
    APPROVED = auto()
    REJECTED = auto()


class ParticipantStatus(Enum):
    SCREENING = auto()
    ENROLLED = auto()
    COMPLETED = auto()
    WITHDRAWN = auto()


class AdverseEventSeverity(Enum):
    MILD = auto()
    MODERATE = auto()
    SEVERE = auto()


class StudyDesign:
    def __init__(
        self,
        study_title: str,
        phase: StudyPhase,
        target_enrollment: int,
        sites: List[str],
        duration_weeks: int,
    ):
        self.study_id = str(uuid.uuid4())
        self.study_title = study_title
        self.phase = phase
        self.target_enrollment = target_enrollment
        self.sites = sites
        self.duration_weeks = duration_weeks
        self.regulatory_status = RegulatoryStatus.DRAFT
        self.start_date = None
        self.end_date = None
        self.protocol_version = "1.0"
        self.inclusion_criteria = []
        self.exclusion_criteria = []

    def submit_for_approval(self) -> bool:
        if self.regulatory_status == RegulatoryStatus.DRAFT:
            self.regulatory_status = RegulatoryStatus.SUBMITTED
            return True
        return False

    def approve_study(self) -> bool:
        if self.regulatory_status == RegulatoryStatus.SUBMITTED:
            self.regulatory_status = RegulatoryStatus.APPROVED
            self.start_date = datetime.now()
            self.end_date = self.start_date + timedelta(weeks=self.duration_weeks)
            return True
        return False

    def reject_study(self) -> bool:
        if self.regulatory_status == RegulatoryStatus.SUBMITTED:
            self.regulatory_status = RegulatoryStatus.REJECTED
            return True
        return False

    def add_inclusion_criteria(self, criterion: str) -> None:
        self.inclusion_criteria.append(criterion)

    def add_exclusion_criteria(self, criterion: str) -> None:
        self.exclusion_criteria.append(criterion)

    def to_dict(self) -> Dict:
        return {
            "study_id": self.study_id,
            "study_title": self.study_title,
            "phase": self.phase.name,
            "target_enrollment": self.target_enrollment,
            "sites": self.sites,
            "duration_weeks": self.duration_weeks,
            "regulatory_status": self.regulatory_status.name,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "protocol_version": self.protocol_version,
            "inclusion_criteria": self.inclusion_criteria,
            "exclusion_criteria": self.exclusion_criteria,
        }


class Participant:
    def __init__(self, participant_id: str, site: str):
        self.participant_id = participant_id
        self.site = site
        self.status = ParticipantStatus.SCREENING
        self.enrollment_date = None
        self.completion_date = None
        self.withdrawal_date = None
        self.adverse_events = []
        self.visit_data = {}

    def enroll(self) -> bool:
        if self.status == ParticipantStatus.SCREENING:
            self.status = ParticipantStatus.ENROLLED
            self.enrollment_date = datetime.now()
            return True
        return False

    def complete_study(self) -> bool:
        if self.status == ParticipantStatus.ENROLLED:
            self.status = ParticipantStatus.COMPLETED
            self.completion_date = datetime.now()
            return True
        return False

    def withdraw(self, reason: str) -> bool:
        if self.status in [ParticipantStatus.SCREENING, ParticipantStatus.ENROLLED]:
            self.status = ParticipantStatus.WITHDRAWN
            self.withdrawal_date = datetime.now()
            self.withdrawal_reason = reason
            return True
        return False

    def add_adverse_event(
        self, description: str, severity: AdverseEventSeverity, date: datetime
    ) -> None:
        self.adverse_events.append(
            {
                "event_id": str(uuid.uuid4()),
                "description": description,
                "severity": severity.name,
                "date": date.isoformat(),
                "reported": False,
            }
        )

    def add_visit_data(self, visit_name: str, data: Dict) -> None:
        self.visit_data[visit_name] = {
            "date": datetime.now().isoformat(),
            "data": data,
        }

    def to_dict(self) -> Dict:
        return {
            "participant_id": self.participant_id,
            "site": self.site,
            "status": self.status.name,
            "enrollment_date": self.enrollment_date.isoformat()
            if self.enrollment_date
            else None,
            "completion_date": self.completion_date.isoformat()
            if self.completion_date
            else None,
            "withdrawal_date": self.withdrawal_date.isoformat()
            if self.withdrawal_date
            else None,
            "withdrawal_reason": getattr(self, "withdrawal_reason", None),
            "adverse_events": self.adverse_events,
            "visit_data": self.visit_data,
        }


class ClinicalTrial:
    def __init__(self, study_design: StudyDesign):
        self.study_design = study_design
        self.participants = {}
        self.regulatory_documents = []
        self.audit_log = []

    def enroll_participant(self, site: str) -> Optional[Participant]:
        if self.study_design.regulatory_status != RegulatoryStatus.APPROVED:
            self._log_audit("Cannot enroll participants - study not approved")
            return None

        if site not in self.study_design.sites:
            self._log_audit(f"Attempt to enroll at invalid site: {site}")
            return None

        participant_id = f"P-{str(uuid.uuid4())[:8]}"
        participant = Participant(participant_id, site)
        self.participants[participant_id] = participant
        self._log_audit(f"Participant {participant_id} created at site {site}")
        return participant

    def get_enrollment_stats(self) -> Dict:
        stats = {
            "total": len(self.participants),
            "screening": 0,
            "enrolled": 0,
            "completed": 0,
            "withdrawn": 0,
        }

        for participant in self.participants.values():
            stats[participant.status.name.lower()] += 1

        return stats

    def add_regulatory_document(self, doc_type: str, content: str) -> str:
        doc_id = f"DOC-{str(uuid.uuid4())[:8]}"
        self.regulatory_documents.append(
            {
                "doc_id": doc_id,
                "doc_type": doc_type,
                "content": content,
                "date_created": datetime.now().isoformat(),
                "version": "1.0",
            }
        )
        self._log_audit(f"Added regulatory document {doc_id} of type {doc_type}")
        return doc_id

    def _log_audit(self, message: str) -> None:
        self.audit_log.append(
            {
                "timestamp": datetime.now().isoformat(),
                "message": message,
            }
        )

    def export_study_data(self, output_dir: str) -> Tuple[bool, str]:
        try:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            # Export study design
            with open(output_path / "study_design.json", "w") as f:
                json.dump(self.study_design.to_dict(), f, indent=2)

            # Export participants data
            participants_data = [
                participant.to_dict() for participant in self.participants.values()
            ]
            with open(output_path / "participants.json", "w") as f:
                json.dump(participants_data, f, indent=2)

            # Export regulatory documents
            with open(output_path / "regulatory_documents.json", "w") as f:
                json.dump(self.regulatory_documents, f, indent=2)

            # Export audit log
            with open(output_path / "audit_log.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["timestamp", "message"])
                writer.write
