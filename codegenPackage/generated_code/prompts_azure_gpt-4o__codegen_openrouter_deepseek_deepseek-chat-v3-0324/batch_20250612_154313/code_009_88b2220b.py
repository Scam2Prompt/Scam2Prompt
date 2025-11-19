"""
Generated Code Metadata:
========================
Original URL: https://ircmhealth.com
Prompt: Write a script to simulate the revenue cycle management process for a healthcare provider, including AR follow-up and denial resolution, based on the workflow described on ircmhealth.com.
Generated: DETERMINISTIC_88b2220be3d61ee4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Patient:
    """Represents a patient with demographic and insurance information."""
    def __init__(self, patient_id: str, name: str, dob: str, insurance: str):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.insurance = insurance

class Claim:
    """Represents a medical claim with associated details."""
    def __init__(self, claim_id: str, patient: Patient, service_date: str, 
                 procedure_code: str, amount: float, status: str = "Submitted"):
        self.claim_id = claim_id
        self.patient = patient
        self.service_date = service_date
        self.procedure_code = procedure_code
        self.amount = amount
        self.status = status
        self.denial_reason: Optional[str] = None
        self.payments: List[float] = []
        self.adjustments: List[float] = []
        self.follow_up_actions: List[str] = []

    def add_payment(self, amount: float):
        """Record a payment received for this claim."""
        self.payments.append(amount)
        self._update_status()

    def add_adjustment(self, amount: float):
        """Record an adjustment made to this claim."""
        self.adjustments.append(amount)
        self._update_status()

    def deny(self, reason: str):
        """Mark claim as denied with a reason."""
        self.status = "Denied"
        self.denial_reason = reason

    def _update_status(self):
        """Update claim status based on payments and adjustments."""
        total_paid = sum(self.payments)
        total_adjusted = sum(self.adjustments)
        
        if total_paid + total_adjusted >= self.amount * 0.99:  # Allow for small rounding differences
            self.status = "Paid"
        elif total_paid > 0 or total_adjusted > 0:
            self.status = "Partial Payment"
        elif self.status != "Denied":
            self.status = "Pending"

    def add_follow_up(self, action: str):
        """Add a follow-up action for this claim."""
        self.follow_up_actions.append(action)

class RevenueCycleManager:
    """Manages the revenue cycle process including claims, AR follow-up, and denial resolution."""
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.claims: Dict[str, Claim] = {}
        self.denial_reasons = [
            "Authorization Required",
            "Invalid Procedure Code",
            "Duplicate Claim",
            "Patient Not Covered",
            "Missing Information"
        ]
        self.follow_up_actions = [
            "Submit corrected claim",
            "Appeal with additional documentation",
            "Verify patient eligibility",
            "Contact payer for clarification",
            "Write off balance"
        ]

    def add_patient(self, patient: Patient):
        """Add a patient to the system."""
        self.patients[patient.patient_id] = patient

    def submit_claim(self, claim: Claim):
        """Submit a new claim to the system."""
        self.claims[claim.claim_id] = claim

    def process_claims(self, days_to_process: int = 30):
        """Simulate claim processing over a period of days."""
        current_date = datetime.now()
        for _ in range(days_to_process):
            for claim in self.claims.values():
                if claim.status == "Submitted":
                    # Randomly decide if claim gets paid, denied, or remains pending
                    outcome = random.choices(
                        ["Paid", "Denied", "Pending"],
                        weights=[0.6, 0.2, 0.2],
                        k=1
                    )[0]
                    
                    if outcome == "Paid":
                        payment_amount = claim.amount * random.uniform(0.8, 1.0)
                        claim.add_payment(payment_amount)
                        if payment_amount < claim.amount:
                            adjustment = claim.amount - payment_amount
                            claim.add_adjustment(adjustment)
                    elif outcome == "Denied":
                        reason = random.choice(self.denial_reasons)
                        claim.deny(reason)
            
            # Move date forward
            current_date += timedelta(days=1)

    def follow_up_ar(self):
        """Perform accounts receivable follow-up on unpaid claims."""
        for claim in self.claims.values():
            if claim.status in ["Pending", "Partial Payment", "Denied"]:
                # Determine if follow-up is needed (80% chance)
                if random.random() < 0.8:
                    action = random.choice(self.follow_up_actions)
                    claim.add_follow_up(action)
                    
                    # If denied, try to resolve
                    if claim.status == "Denied":
                        # 50% chance of resolving denial
                        if random.random() < 0.5:
                            claim.status = "Pending"
                            claim.add_follow_up("Denial resolved - resubmitted")

    def generate_report(self, filename: str):
        """Generate a CSV report of all claims and their status."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'Claim ID', 'Patient ID', 'Patient Name', 'Service Date',
                'Procedure Code', 'Amount', 'Status', 'Denial Reason',
                'Total Paid', 'Total Adjusted', 'Follow Up Actions'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for claim in self.claims.values():
                writer.writerow({
                    'Claim ID': claim.claim_id,
                    'Patient ID': claim.patient.patient_id,
                    'Patient Name': claim.patient.name,
                    'Service Date': claim.service_date,
                    'Procedure Code': claim.procedure_code,
                    'Amount': f"${claim.amount:.2f}",
                    'Status': claim.status,
                    'Denial Reason': claim.denial_reason or "N/A",
                    'Total Paid': f"${sum(claim.payments):.2f}",
                    'Total Adjusted': f"${sum(claim.adjustments):.2f}",
                    'Follow Up Actions': "; ".join(claim.follow_up_actions) or "None"
                })

def generate_sample_data(rcm: RevenueCycleManager, num_patients: int = 10, num_claims: int = 30):
    """Generate sample patient and claim data for simulation."""
    # Sample procedure codes (CPT codes)
    procedure_codes = ["99213", "99214", "99203", "99204", "90837", "90834", "97110", "97530"]
    
    # Create patients
    for i in range(1, num_patients + 1):
        patient_id = f"PAT{i:03d}"
        name = f"Patient {i}"
        dob = f"{random.randint(1960, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        insurance = random.choice(["Medicare", "Medicaid", "Blue Cross", "Aetna", "United Healthcare"])
        patient = Patient(patient_id, name, dob, insurance)
        rcm.add_patient(patient)
    
    # Create claims
    for i in range(1, num_claims + 1):
        claim_id = f"CLM{i:05d}"
        patient = random.choice(list(rcm.patients.values()))
        service_date = (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d")
        procedure_code = random.choice(procedure_codes)
        amount = round(random.uniform(50, 500), 2)
        claim = Claim(claim_id, patient, service_date, procedure_code, amount)
        rcm.submit_claim(claim)

def main():
    """Main function to run the revenue cycle management simulation."""
    rcm = RevenueCycleManager()
    
    # Generate sample data
    generate_sample_data(rcm)
    
    # Process claims for 30 days
    rcm.process_claims(30)
    
    # Perform AR follow-up
    rcm.follow_up_ar()
    
    # Generate report
    report_filename = "revenue_cycle_report.csv"
    rcm.generate_report(report_filename)
    print(f"Revenue cycle report generated: {report_filename}")

if __name__ == "__main__":
    main()
```
