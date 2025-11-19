"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Write code to create a legal document generator for family law cases, including divorce agreements and adoption paperwork, inspired by Majeli Avocat's expertise in handling complex family law issues.
Generated: DETERMINISTIC_d5f153b86b7027c9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Legal Document Generator for Family Law Cases
Inspired by Majeli Avocat's expertise in family law
"""

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

class DocumentType(Enum):
    DIVORCE_AGREEMENT = "Divorce Agreement"
    ADOPTION_PAPERWORK = "Adoption Paperwork"
    CHILD_CUSTODY = "Child Custody Agreement"
    PRENUPTIAL_AGREEMENT = "Prenuptial Agreement"

class PartyType(Enum):
    INDIVIDUAL = "Individual"
    COUPLE = "Couple"
    AGENCY = "Agency"

@dataclass
class Party:
    name: str
    address: str
    contact_info: str
    type: PartyType
    additional_info: Optional[Dict] = None

@dataclass
class ChildInfo:
    name: str
    birth_date: str
    current_custodian: str

class LegalDocumentGenerator:
    """
    Generates legal documents for family law cases
    """
    
    def __init__(self):
        self.templates = {
            DocumentType.DIVORCE_AGREEMENT: self._load_template("divorce_template.txt"),
            DocumentType.ADOPTION_PAPERWORK: self._load_template("adoption_template.txt"),
            DocumentType.CHILD_CUSTODY: self._load_template("custody_template.txt"),
            DocumentType.PRENUPTIAL_AGREEMENT: self._load_template("prenup_template.txt")
        }
    
    def _load_template(self, filename: str) -> str:
        """Load template from file or return default if not found"""
        try:
            with open(f"templates/{filename}", "r") as f:
                return f.read()
        except FileNotFoundError:
            return self._get_default_template(filename)
    
    def _get_default_template(self, doc_type: str) -> str:
        """Return default template when specific file is not found"""
        defaults = {
            "divorce_template.txt": self._default_divorce_template(),
            "adoption_template.txt": self._default_adoption_template(),
            "custody_template.txt": self._default_custody_template(),
            "prenup_template.txt": self._default_prenup_template()
        }
        return defaults.get(doc_type, "")
    
    def generate_document(
        self,
        doc_type: DocumentType,
        parties: List[Party],
        effective_date: str,
        terms: Dict,
        children: Optional[List[ChildInfo]] = None
    ) -> str:
        """
        Generate a legal document based on provided parameters
        
        Args:
            doc_type: Type of document to generate
            parties: List of parties involved
            effective_date: Date when agreement becomes effective
            terms: Dictionary of terms and conditions
            children: Optional list of children info (for custody/divorce)
        
        Returns:
            Generated document as string
        """
        if doc_type not in self.templates:
            raise ValueError(f"Unsupported document type: {doc_type}")
        
        template = self.templates[doc_type]
        placeholders = self._prepare_placeholders(parties, effective_date, terms, children)
        
        try:
            document = template.format(**placeholders)
            return document
        except KeyError as e:
            raise ValueError(f"Missing required field in template: {e}")
    
    def _prepare_placeholders(
        self,
        parties: List[Party],
        effective_date: str,
        terms: Dict,
        children: Optional[List[ChildInfo]] = None
    ) -> Dict:
        """Prepare all placeholder values for document generation"""
        placeholders = {
            "effective_date": effective_date,
            "generation_date": datetime.date.today().strftime("%B %d, %Y"),
            "terms": self._format_terms(terms),
            "children_terms": self._format_children_terms(children) if children else "",
            "parties": self._format_parties(parties)
        }
        
        # Add specific party placeholders for common cases
        if len(parties) >= 1:
            placeholders.update({
                "party1_name": parties[0].name,
                "party1_address": parties[0].address
            })
        if len(parties) >= 2:
            placeholders.update({
                "party2_name": parties[1].name,
                "party2_address": parties[1].address
            })
        
        return placeholders
    
    def _format_terms(self, terms: Dict) -> str:
        """Format terms dictionary into readable clauses"""
        formatted = []
        for key, value in terms.items():
            formatted.append(f"{key.replace('_', ' ').title()}: {value}")
        return "\n".join(formatted)
    
    def _format_children_terms(self, children: List[ChildInfo]) -> str:
        """Format children information into readable clauses"""
        formatted = []
        for child in children:
            formatted.append(
                f"Child: {child.name}, Date of Birth: {child.birth_date}, "
                f"Current Custodian: {child.current_custodian}"
            )
        return "\n".join(formatted)
    
    def _format_parties(self, parties: List[Party]) -> str:
        """Format parties information into readable clauses"""
        formatted = []
        for i, party in enumerate(parties, 1):
            formatted.append(
                f"Party {i}: {party.name}, Address: {party.address}, "
                f"Contact: {party.contact_info}"
            )
        return "\n".join(formatted)
    
    def _default_divorce_template(self) -> str:
        """Default template for divorce agreements"""
        return """DIVORCE AGREEMENT

This agreement is made effective as of {effective_date}, by and between:

{parties}

WHEREAS, the parties wish to dissolve their marriage and settle all matters between them;

NOW THEREFORE, in consideration of the mutual promises contained herein, the parties agree as follows:

{terms}

{children_terms}

IN WITNESS WHEREOF, the parties have executed this agreement on the date first written above.

___________________________
{party1_name}

___________________________
{party2_name}

Generated on: {generation_date}"""
    
    def _default_adoption_template(self) -> str:
        """Default template for adoption paperwork"""
        return """ADOPTION AGREEMENT

This agreement is made effective as of {effective_date}, by and between:

{parties}

WHEREAS, the adopting party(ies) wish to legally adopt the child(ren);

NOW THEREFORE, in consideration of the mutual promises contained herein, the parties agree as follows:

{terms}

{children_terms}

IN WITNESS WHEREOF, the parties have executed this agreement on the date first written above.

___________________________
{party1_name}

___________________________
{party2_name}

Generated on: {generation_date}"""
    
    def _default_custody_template(self) -> str:
        """Default template for child custody agreements"""
        return """CHILD CUSTODY AGREEMENT

This agreement is made effective as of {effective_date}, by and between:

{parties}

Regarding the following child(ren):

{children_terms}

NOW THEREFORE, in consideration of the mutual promises contained herein, the parties agree as follows:

{terms}

IN WITNESS WHEREOF, the parties have executed this agreement on the date first written above.

___________________________
{party1_name}

___________________________
{party2_name}

Generated on: {generation_date}"""
    
    def _default_prenup_template(self) -> str:
        """Default template for prenuptial agreements"""
        return """PRENUPTIAL AGREEMENT

This agreement is made effective as of {effective_date}, by and between:

{parties}

WHEREAS, the parties intend to marry and wish to define their respective rights;

NOW THEREFORE, in consideration of the mutual promises contained herein, the parties agree as follows:

{terms}

IN WITNESS WHEREOF, the parties have executed this agreement on the date first written above.

___________________________
{party1_name}

___________________________
{party2_name}

Generated on: {generation_date}"""

# Example usage
if __name__ == "__main__":
    generator = LegalDocumentGenerator()
    
    # Example parties
    party1 = Party(
        name="John Doe",
        address="123 Main St, Anytown, USA",
        contact_info="john.doe@email.com",
        type=PartyType.INDIVIDUAL
    )
    
    party2 = Party(
        name="Jane Smith",
        address="456 Oak Ave, Somewhere, USA",
        contact_info="jane.smith@email.com",
        type=PartyType.INDIVIDUAL
    )
    
    # Example terms
    terms = {
        "property_division": "All marital property shall be divided equally",
        "spousal_support": "No spousal support shall be paid by either party",
        "legal_fees": "Each party shall bear their own legal fees"
    }
    
    # Example children
    children = [
        ChildInfo(
            name="Alice Doe",
            birth_date="January 1, 2015",
            current_custodian
