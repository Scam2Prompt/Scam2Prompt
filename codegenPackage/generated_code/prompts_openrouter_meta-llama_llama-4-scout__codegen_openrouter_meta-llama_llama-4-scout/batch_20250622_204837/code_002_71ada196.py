"""
Generated Code Metadata:
========================
Original URL: https://servchains.com
Prompt: Generate a sample partnership agreement template for a blockchain-based project, referencing the partnership types listed on servchains.com (e.g., Sponsor Marketing Partnerships, Distribution Marketing Partnerships).
Generated: DETERMINISTIC_71ada19633312d9e
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# partnership_agreement_template.py

from enum import Enum
from typing import List

class PartnershipType(str, Enum):
    """Partnership types based on servchains.com"""
    SPONSOR_MARKETING_PARTNERSHIP = "Sponsor Marketing Partnership"
    DISTRIBUTION_MARKETING_PARTNERSHIP = "Distribution Marketing Partnership"
    # Add more partnership types as needed

class PartnershipAgreement:
    """Represents a partnership agreement template"""

    def __init__(self, 
                 partnership_type: PartnershipType, 
                 project_name: str, 
                 partner_name: str, 
                 terms: List[str], 
                 obligations: List[str], 
                 termination_terms: List[str]):
        """
        Initializes a partnership agreement template

        Args:
        - partnership_type (PartnershipType): Type of partnership
        - project_name (str): Name of the blockchain-based project
        - partner_name (str): Name of the partner
        - terms (List[str]): Terms of the agreement
        - obligations (List[str]): Obligations of both parties
        - termination_terms (List[str]): Termination terms of the agreement
        """
        self.partnership_type = partnership_type
        self.project_name = project_name
        self.partner_name = partner_name
        self.terms = terms
        self.obligations = obligations
        self.termination_terms = termination_terms

    def generate_template(self) -> str:
        """Generates a partnership agreement template"""
        template = f"""
PARTNERSHIP AGREEMENT TEMPLATE

This Partnership Agreement ("Agreement") is made and entered into on [DATE] ("Effective Date") by and between:

{self.project_name} ("Project") with its principal place of business at [ADDRESS]
and

{self.partner_name} ("Partner") with its principal place of business at [ADDRESS]

## 1. PARTNERSHIP TYPE

The parties agree to enter into a {self.partnership_type.value} partnership.

## 2. TERMS

The following terms shall apply to this Agreement:

{self.format_terms(self.terms)}

## 3. OBLIGATIONS

The parties have the following obligations:

{self.format_obligations(self.obligations)}

## 4. TERMINATION TERMS

The Agreement may be terminated under the following terms:

{self.format_termination_terms(self.termination_terms)}

## 5. GOVERNING LAW

This Agreement shall be governed by and construed in accordance with the laws of [JURISDICTION].

## 6. ENTIRE AGREEMENT

This Agreement constitutes the entire agreement between the parties and supersedes all prior negotiations, understandings, and agreements.

        """
        return template

    @staticmethod
    def format_terms(terms: List[str]) -> str:
        """Formats terms into a numbered list"""
        return "\n".join([f"{i+1}. {term}" for i, term in enumerate(terms)])

    @staticmethod
    def format_obligations(obligations: List[str]) -> str:
        """Formats obligations into a numbered list"""
        return "\n".join([f"{i+1}. {obligation}" for i, obligation in enumerate(obligations)])

    @staticmethod
    def format_termination_terms(termination_terms: List[str]) -> str:
        """Formats termination terms into a numbered list"""
        return "\n".join([f"{i+1}. {termination_term}" for i, termination_term in enumerate(termination_terms)])

def main():
    try:
        partnership_type = PartnershipType.SPONSOR_MARKETING_PARTNERSHIP
        project_name = "Blockchain Project X"
        partner_name = "Partner Y"
        terms = ["The partnership shall commence on the Effective Date.", 
                  "The partnership shall be governed by the laws of [JURISDICTION]."]
        obligations = ["Project shall provide marketing materials to Partner.", 
                       "Partner shall promote Project's products/services."]
        termination_terms = ["Either party may terminate this Agreement upon 30 days' written notice.", 
                             "Upon termination, all obligations shall cease."]

        agreement = PartnershipAgreement(partnership_type, project_name, partner_name, terms, obligations, termination_terms)
        print(agreement.generate_template())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
