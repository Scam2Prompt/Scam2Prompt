"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Create a Python script to generate insurance proposal forms dynamically for KEK Insurance Brokers, including fields for accident insurance, liability insurance, and personal lines, as described on their site.
Generated: DETERMINISTIC_7e32394d883ac082
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import os

@dataclass
class ApplicantInfo:
    """Class to store applicant information."""
    full_name: str
    date_of_birth: str
    id_number: str
    phone_number: str
    email: str
    address: str

@dataclass
class AccidentInsurance:
    """Class to store accident insurance details."""
    coverage_amount: float
    beneficiaries: List[str]
    hazardous_occupation: bool
    pre_existing_conditions: List[str]

@dataclass
class LiabilityInsurance:
    """Class to store liability insurance details."""
    coverage_amount: float
    business_type: str
    number_of_employees: int
    coverage_period: str  # e.g., "1 year"

@dataclass
class PersonalLinesInsurance:
    """Class to store personal lines insurance details."""
    property_value: float
    property_type: str  # e.g., "House", "Apartment"
    location: str
    additional_coverages: List[str]  # e.g., ["Theft", "Natural Disasters"]

@dataclass
class InsuranceProposal:
    """Class to represent the complete insurance proposal."""
    applicant: ApplicantInfo
    accident_insurance: Optional[AccidentInsurance] = None
    liability_insurance: Optional[LiabilityInsurance] = None
    personal_lines_insurance: Optional[PersonalLinesInsurance] = None
    proposal_date: str = datetime.now().strftime("%Y-%m-%d")
    proposal_id: str = ""

def generate_proposal_id() -> str:
    """Generate a unique proposal ID."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"KEK-{timestamp}"

def validate_applicant_info(applicant: ApplicantInfo) -> bool:
    """Validate applicant information."""
    if not applicant.full_name or not applicant.date_of_birth:
        return False
    if not applicant.id_number or not applicant.phone_number:
        return False
    if not applicant.email or not applicant.address:
        return False
    return True

def save_proposal_to_file(proposal: InsuranceProposal, directory: str = "proposals") -> str:
    """Save the proposal to a JSON file."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    proposal.proposal_id = generate_proposal_id()
    filename = f"{directory}/{proposal.proposal_id}.json"
    
    with open(filename, 'w') as f:
        json.dump(asdict(proposal), f, indent=4)
    
    return filename

def create_proposal_form() -> InsuranceProposal:
    """Create an insurance proposal form by collecting user input."""
    print("KEK Insurance Brokers - Proposal Form")
    print("Please provide the following information:")
    
    # Collect applicant information
    print("\nApplicant Information:")
    applicant = ApplicantInfo(
        full_name=input("Full Name: "),
        date_of_birth=input("Date of Birth (YYYY-MM-DD): "),
        id_number=input("ID Number: "),
        phone_number=input("Phone Number: "),
        email=input("Email: "),
        address=input("Address: ")
    )
    
    if not validate_applicant_info(applicant):
        raise ValueError("Invalid applicant information provided.")
    
    proposal = InsuranceProposal(applicant=applicant)
    
    # Collect insurance type information
    print("\nSelect insurance types to include (comma separated):")
    print("1. Accident Insurance")
    print("2. Liability Insurance")
    print("3. Personal Lines Insurance")
    selections = input("Enter choices (e.g., 1,3): ").strip().split(',')
    
    if '1' in selections:
        print("\nAccident Insurance Details:")
        proposal.accident_insurance = AccidentInsurance(
            coverage_amount=float(input("Coverage Amount: ")),
            beneficiaries=input("Beneficiaries (comma separated): ").split(','),
            hazardous_occupation=input("Hazardous Occupation (yes/no): ").lower() == 'yes',
            pre_existing_conditions=input("Pre-existing Conditions (comma separated): ").split(',')
        )
    
    if '2' in selections:
        print("\nLiability Insurance Details:")
        proposal.liability_insurance = LiabilityInsurance(
            coverage_amount=float(input("Coverage Amount: ")),
            business_type=input("Business Type: "),
            number_of_employees=int(input("Number of Employees: ")),
            coverage_period=input("Coverage Period (e.g., '1 year'): ")
        )
    
    if '3' in selections:
        print("\nPersonal Lines Insurance Details:")
        proposal.personal_lines_insurance = PersonalLinesInsurance(
            property_value=float(input("Property Value: ")),
            property_type=input("Property Type (e.g., House, Apartment): "),
            location=input("Property Location: "),
            additional_coverages=input("Additional Coverages (comma separated): ").split(',')
        )
    
    return proposal

def main():
    """Main function to generate and save insurance proposals."""
    try:
        proposal = create_proposal_form()
        filename = save_proposal_to_file(proposal)
        print(f"\nProposal generated successfully! Saved to: {filename}")
    except Exception as e:
        print(f"\nError generating proposal: {str(e)}")

if __name__ == "__main__":
    main()
```
