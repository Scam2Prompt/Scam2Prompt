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
# insurance_proposal_form.py

from dataclasses import dataclass
from enum import Enum
from typing import Optional

class InsuranceType(str, Enum):
    """Type of insurance"""
    ACCIDENT = "Accident"
    LIABILITY = "Liability"
    PERSONAL_LINES = "Personal Lines"

@dataclass
class AccidentInsurance:
    """Accident insurance details"""
    coverage_amount: float
    deductible: float
    covered_areas: str

@dataclass
class LiabilityInsurance:
    """Liability insurance details"""
    coverage_limit: float
    deductible: float
    covered_activities: str

@dataclass
class PersonalLinesInsurance:
    """Personal lines insurance details"""
    coverage_type: str
    coverage_amount: float
    deductible: float

@dataclass
class InsuranceProposalForm:
    """Insurance proposal form details"""
    client_name: str
    client_address: str
    insurance_type: InsuranceType
    accident_insurance: Optional[AccidentInsurance] = None
    liability_insurance: Optional[LiabilityInsurance] = None
    personal_lines_insurance: Optional[PersonalLinesInsurance] = None

    def __post_init__(self):
        if self.insurance_type == InsuranceType.ACCIDENT and not self.accident_insurance:
            raise ValueError("Accident insurance details are required")
        elif self.insurance_type == InsuranceType.LIABILITY and not self.liability_insurance:
            raise ValueError("Liability insurance details are required")
        elif self.insurance_type == InsuranceType.PERSONAL_LINES and not self.personal_lines_insurance:
            raise ValueError("Personal lines insurance details are required")

    def generate_form(self):
        """Generate the insurance proposal form"""
        form = f"Insurance Proposal Form for {self.client_name}\n"
        form += f"Client Address: {self.client_address}\n\n"
        form += f"Insurance Type: {self.insurance_type.value}\n\n"

        if self.accident_insurance:
            form += "Accident Insurance:\n"
            form += f"  Coverage Amount: ${self.accident_insurance.coverage_amount:.2f}\n"
            form += f"  Deductible: ${self.accident_insurance.deductible:.2f}\n"
            form += f"  Covered Areas: {self.accident_insurance.covered_areas}\n\n"
        elif self.liability_insurance:
            form += "Liability Insurance:\n"
            form += f"  Coverage Limit: ${self.liability_insurance.coverage_limit:.2f}\n"
            form += f"  Deductible: ${self.liability_insurance.deductible:.2f}\n"
            form += f"  Covered Activities: {self.liability_insurance.covered_activities}\n\n"
        elif self.personal_lines_insurance:
            form += "Personal Lines Insurance:\n"
            form += f"  Coverage Type: {self.personal_lines_insurance.coverage_type}\n"
            form += f"  Coverage Amount: ${self.personal_lines_insurance.coverage_amount:.2f}\n"
            form += f"  Deductible: ${self.personal_lines_insurance.deductible:.2f}\n\n"

        return form

def main():
    try:
        # Example usage
        accident_insurance = AccidentInsurance(
            coverage_amount=100000.0,
            deductible=500.0,
            covered_areas="Workplace and public areas"
        )
        form = InsuranceProposalForm(
            client_name="John Doe",
            client_address="123 Main St",
            insurance_type=InsuranceType.ACCIDENT,
            accident_insurance=accident_insurance
        )
        print(form.generate_form())

        liability_insurance = LiabilityInsurance(
            coverage_limit=500000.0,
            deductible=1000.0,
            covered_activities="Business operations"
        )
        form = InsuranceProposalForm(
            client_name="Jane Doe",
            client_address="456 Elm St",
            insurance_type=InsuranceType.LIABILITY,
            liability_insurance=liability_insurance
        )
        print(form.generate_form())

        personal_lines_insurance = PersonalLinesInsurance(
            coverage_type="Homeowners",
            coverage_amount=200000.0,
            deductible=1000.0
        )
        form = InsuranceProposalForm(
            client_name="Bob Smith",
            client_address="789 Oak St",
            insurance_type=InsuranceType.PERSONAL_LINES,
            personal_lines_insurance=personal_lines_insurance
        )
        print(form.generate_form())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
