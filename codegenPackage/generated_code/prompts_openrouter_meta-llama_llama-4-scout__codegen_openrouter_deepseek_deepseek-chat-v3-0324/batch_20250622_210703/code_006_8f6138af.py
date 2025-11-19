"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Write a code snippet to track and manage therapy referrals for children, including progress monitoring and communication with parents and therapists.
Generated: DETERMINISTIC_8f6138aff1855e2d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum

class TherapyType(Enum):
    SPEECH = "Speech Therapy"
    OCCUPATIONAL = "Occupational Therapy"
    PHYSICAL = "Physical Therapy"
    BEHAVIORAL = "Behavioral Therapy"

class ReferralStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DENIED = "Denied"

class TherapySession:
    def __init__(self, date: datetime.date, duration_minutes: int, notes: str):
        self.date = date
        self.duration_minutes = duration_minutes
        self.notes = notes

class TherapyReferral:
    def __init__(
        self,
        child_id: str,
        child_name: str,
        therapy_type: TherapyType,
        referring_doctor: str,
        date_referred: datetime.date,
        parent_contact: str,
        therapist_contact: str
    ):
        self.child_id = child_id
        self.child_name = child_name
        self.therapy_type = therapy_type
        self.referring_doctor = referring_doctor
        self.date_referred = date_referred
        self.parent_contact = parent_contact
        self.therapist_contact = therapist_contact
        self.status = ReferralStatus.PENDING
        self.sessions: List[TherapySession] = []
        self.progress_notes: List[str] = []
        self.last_updated = datetime.date.today()

    def add_session(self, session: TherapySession) -> None:
        self.sessions.append(session)
        self.last_updated = datetime.date.today()

    def add_progress_note(self, note: str) -> None:
        self.progress_notes.append(note)
        self.last_updated = datetime.date.today()

    def update_status(self, new_status: ReferralStatus) -> None:
        self.status = new_status
        self.last_updated = datetime.date.today()

class ReferralManager:
    def __init__(self):
        self.referrals: Dict[str, TherapyReferral] = {}

    def add_referral(self, referral: TherapyReferral) -> None:
        if referral.child_id in self.referrals:
            raise ValueError(f"Referral already exists for child {referral.child_id}")
        self.referrals[referral.child_id] = referral

    def get_referral(self, child_id: str) -> Optional[TherapyReferral]:
        return self.referrals.get(child_id)

    def update_referral_status(self, child_id: str, new_status: ReferralStatus) -> None:
        referral = self.referrals.get(child_id)
        if not referral:
            raise ValueError(f"No referral found for child {child_id}")
        referral.update_status(new_status)

    def get_all_referrals_by_status(self, status: ReferralStatus) -> List[TherapyReferral]:
        return [r for r in self.referrals.values() if r.status == status]

    def send_parent_update(self, child_id: str, message: str) -> None:
        referral = self.referrals.get(child_id)
        if not referral:
            raise ValueError(f"No referral found for child {child_id}")
        # In a real implementation, this would send an email/SMS
        print(f"Message sent to parent {referral.parent_contact}: {message}")

    def send_therapist_update(self, child_id: str, message: str) -> None:
        referral = self.referrals.get(child_id)
        if not referral:
            raise ValueError(f"No referral found for child {child_id}")
        # In a real implementation, this would send an email/SMS
        print(f"Message sent to therapist {referral.therapist_contact}: {message}")

    def generate_progress_report(self, child_id: str) -> Dict:
        referral = self.referrals.get(child_id)
        if not referral:
            raise ValueError(f"No referral found for child {child_id}")
        
        return {
            "child_name": referral.child_name,
            "therapy_type": referral.therapy_type.value,
            "status": referral.status.value,
            "total_sessions": len(referral.sessions),
            "total_hours": sum(s.duration_minutes for s in referral.sessions) / 60,
            "last_session": max(s.date for s in referral.sessions) if referral.sessions else None,
            "progress_notes": referral.progress_notes,
            "last_updated": referral.last_updated
        }
```
