"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: Write code to generate customized recovery strategies for unpaid claims, including denial resolution and appeal management, inspired by My Healthcare Billing's A/R recovery services.
Generated: DETERMINISTIC_3fac55a2cf3c573c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional, Union

class ClaimStatus(Enum):
    UNPAID = "Unpaid"
    DENIED = "Denied"
    UNDER_REVIEW = "Under Review"
    APPEALED = "Appealed"
    PAID = "Paid"

class DenialReason(Enum):
    CODING_ERROR = "Coding Error"
    MISSING_INFO = "Missing Information"
    ELIGIBILITY = "Eligibility Issue"
    TIMELY_FILING = "Timely Filing"
    MEDICAL_NECESSITY = "Medical Necessity"
    OTHER = "Other"

class AppealStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    SUBMITTED = "Submitted"
    APPROVED = "Approved"
    DENIED = "Denied"

class Claim:
    def __init__(
        self,
        claim_id: str,
        patient_id: str,
        provider_id: str,
        amount: float,
        date_of_service: str,
        status: ClaimStatus = ClaimStatus.UNPAID,
        denial_reason: Optional[DenialReason] = None,
        appeal_status: Optional[AppealStatus] = None
    ):
        self.claim_id = claim_id
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.amount = amount
        self.date_of_service = date_of_service
        self.status = status
        self.denial_reason = denial_reason
        self.appeal_status = appeal_status
        self.history = []

    def add_history_entry(self, action: str, details: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "action": action,
            "details": details
        })

    def to_dict(self) -> Dict:
        return {
            "claim_id": self.claim_id,
            "patient_id": self.patient_id,
            "provider_id": self.provider_id,
            "amount": self.amount,
            "date_of_service": self.date_of_service,
            "status": self.status.value,
            "denial_reason": self.denial_reason.value if self.denial_reason else None,
            "appeal_status": self.appeal_status.value if self.appeal_status else None,
            "history": self.history
        }

class RecoveryStrategy:
    def __init__(self):
        self.strategies = {
            DenialReason.CODING_ERROR: self._handle_coding_error,
            DenialReason.MISSING_INFO: self._handle_missing_info,
            DenialReason.ELIGIBILITY: self._handle_eligibility,
            DenialReason.TIMELY_FILING: self._handle_timely_filing,
            DenialReason.MEDICAL_NECESSITY: self._handle_medical_necessity,
            DenialReason.OTHER: self._handle_other
        }

    def generate_strategy(self, claim: Claim) -> Dict:
        if claim.status != ClaimStatus.DENIED:
            raise ValueError("Strategy can only be generated for denied claims")
        
        if not claim.denial_reason:
            raise ValueError("Denial reason must be specified")
        
        strategy = self.strategies[claim.denial_reason](claim)
        claim.add_history_entry(
            "Recovery Strategy Generated",
            f"Strategy created for denial reason: {claim.denial_reason.value}"
        )
        return strategy

    def _handle_coding_error(self, claim: Claim) -> Dict:
        return {
            "action": "Review and correct coding",
            "steps": [
                "Obtain original medical records",
                "Review diagnosis and procedure codes",
                "Correct any coding errors",
                "Resubmit claim with corrected codes",
                "Follow up in 14 days"
            ],
            "timeline": "7-10 business days",
            "success_rate": "85%"
        }

    def _handle_missing_info(self, claim: Claim) -> Dict:
        return {
            "action": "Gather missing information",
            "steps": [
                "Identify missing documentation",
                "Contact provider for required information",
                "Submit supplemental documentation",
                "Follow up in 10 days"
            ],
            "timeline": "5-7 business days",
            "success_rate": "75%"
        }

    def _handle_eligibility(self, claim: Claim) -> Dict:
        return {
            "action": "Verify eligibility and resubmit",
            "steps": [
                "Verify patient eligibility at time of service",
                "Check for retroactive coverage",
                "If eligible, resubmit claim with proof",
                "If ineligible, explore patient responsibility"
            ],
            "timeline": "10-14 business days",
            "success_rate": "60%"
        }

    def _handle_timely_filing(self, claim: Claim) -> Dict:
        return {
            "action": "Appeal timely filing denial",
            "steps": [
                "Verify actual date of service",
                "Check payer's timely filing requirements",
                "Gather proof of timely submission",
                "Submit appeal with documentation",
                "Request exception if applicable"
            ],
            "timeline": "14-21 business days",
            "success_rate": "50%"
        }

    def _handle_medical_necessity(self, claim: Claim) -> Dict:
        return {
            "action": "Appeal medical necessity denial",
            "steps": [
                "Obtain detailed medical records",
                "Review payer's medical policy",
                "Prepare letter of medical necessity from provider",
                "Submit appeal with supporting documentation",
                "Request peer-to-peer review if needed"
            ],
            "timeline": "21-30 business days",
            "success_rate": "65%"
        }

    def _handle_other(self, claim: Claim) -> Dict:
        return {
            "action": "Investigate and resolve",
            "steps": [
                "Contact payer for specific denial reason",
                "Gather additional information as needed",
                "Determine appropriate corrective action",
                "Resubmit or appeal as appropriate"
            ],
            "timeline": "Varies",
            "success_rate": "40%"
        }

class AppealManager:
    def __init__(self):
        self.appeal_templates = {
            DenialReason.CODING_ERROR: self._coding_error_appeal_template,
            DenialReason.MISSING_INFO: self._missing_info_appeal_template,
            DenialReason.ELIGIBILITY: self._eligibility_appeal_template,
            DenialReason.TIMELY_FILING: self._timely_filing_appeal_template,
            DenialReason.MEDICAL_NECESSITY: self._medical_necessity_appeal_template,
            DenialReason.OTHER: self._other_appeal_template
        }

    def initiate_appeal(self, claim: Claim) -> Dict:
        if claim.status != ClaimStatus.DENIED:
            raise ValueError("Appeal can only be initiated for denied claims")
        
        if not claim.denial_reason:
            raise ValueError("Denial reason must be specified for appeal")
        
        claim.appeal_status = AppealStatus.IN_PROGRESS
        appeal_details = self.appeal_templates[claim.denial_reason](claim)
        
        claim.add_history_entry(
            "Appeal Initiated",
            f"Appeal started for denial reason: {claim.denial_reason.value}"
        )
        
        return appeal_details

    def _coding_error_appeal_template(self, claim: Claim) -> Dict:
        return {
            "type": "Coding Correction Appeal",
            "template": f"""
            [Provider Letterhead]
            [Date]
            
            Appeals Department
            [Payer Name]
            [Payer Address]
            
            Re: Appeal of Claim Denial - Coding Error
            Claim ID: {claim.claim_id}
            Patient: {claim.patient_id}
            DOS: {claim.date_of_service}
            
            Dear Appeals Reviewer,
            
            We are appealing the denial of the above-referenced claim due to alleged coding errors.
            After careful review, we have identified the correct codes to be:
            
            Original Codes: [List original codes]
            Corrected Codes: [List corrected codes]
            
            Supporting documentation is attached, including:
            - Medical records supporting the corrected codes
            - Documentation of medical necessity
            
            We request that you reprocess this claim with the corrected codes.
            
            Sincerely,
            [Provider Name]
            [Contact Information]
            """
        }

    def _missing_info_appeal_template(self, claim: Claim) -> Dict:
        return {
            "type": "Missing Information Appeal",
            "template": f"""
            [Provider Letterhead]
            [Date]
            
            Appeals Department
            [Payer Name]
            [Payer Address]
            
            Re: Appeal of Claim Denial - Missing Information
            Claim ID: {claim.claim_id}
            Patient: {claim.patient_id}
            DOS: {claim.date_of_service}
            
            Dear Appeals Reviewer,
            
            We are appealing the denial of the above-referenced claim due to missing information.
            Please find attached the requested documentation:
            
            -
