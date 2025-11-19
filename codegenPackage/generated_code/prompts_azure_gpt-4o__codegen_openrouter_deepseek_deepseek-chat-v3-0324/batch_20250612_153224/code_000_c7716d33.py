"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write Python code to automate the generation of legal correspondence templates based on the concepts outlined in the "Manual de Correspondência Jurídica" from the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_c7716d338efe0415
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Dict, List

class DocumentType(Enum):
    """Enum representing different types of legal documents."""
    PETITION = auto()
    MEMORANDUM = auto()
    NOTICE = auto()
    CONTRACT = auto()
    LEGAL_OPINION = auto()

@dataclass
class Party:
    """Represents a party involved in the legal document."""
    name: str
    role: str  # e.g., "Plaintiff", "Defendant", "Client"
    address: str
    identification: str  # e.g., CPF/CNPJ

@dataclass
class LegalDocument:
    """Base class for legal document templates."""
    document_type: DocumentType
    title: str
    parties: List[Party]
    body: str
    jurisdiction: str
    case_number: Optional[str] = None
    date: Optional[datetime.date] = None
    attachments: Optional[List[str]] = None

class LegalCorrespondenceGenerator:
    """Automates generation of legal correspondence templates."""
    
    def __init__(self):
        self.templates = self._load_templates()
        
    def _load_templates(self) -> Dict[DocumentType, str]:
        """Load predefined templates for each document type."""
        return {
            DocumentType.PETITION: self._petition_template(),
            DocumentType.MEMORANDUM: self._memorandum_template(),
            DocumentType.NOTICE: self._notice_template(),
            DocumentType.CONTRACT: self._contract_template(),
            DocumentType.LEGAL_OPINION: self._legal_opinion_template()
        }
    
    def generate_document(self, document: LegalDocument) -> str:
        """Generate a legal document based on the provided details."""
        if document.document_type not in self.templates:
            raise ValueError(f"Unsupported document type: {document.document_type}")
            
        template = self.templates[document.document_type]
        return self._populate_template(template, document)
    
    def _populate_template(self, template: str, document: LegalDocument) -> str:
        """Populate the template with document details."""
        replacements = {
            "{TITLE}": document.title,
            "{JURISDICTION}": document.jurisdiction,
            "{CASE_NUMBER}": document.case_number or "N/A",
            "{DATE}": document.date.strftime("%d/%m/%Y") if document.date else datetime.date.today().strftime("%d/%m/%Y"),
            "{BODY}": document.body,
            "{ATTACHMENTS}": self._format_attachments(document.attachments) if document.attachments else "N/A",
            "{PARTIES}": self._format_parties(document.parties)
        }
        
        for placeholder, value in replacements.items():
            template = template.replace(placeholder, value)
            
        return template
    
    def _format_parties(self, parties: List[Party]) -> str:
        """Format parties information for the document."""
        return "\n".join(
            f"{party.role}: {party.name}, {party.address}, {party.identification}"
            for party in parties
        )
    
    def _format_attachments(self, attachments: List[str]) -> str:
        """Format attachments list for the document."""
        return "\n".join(f"- {attachment}" for attachment in attachments)
    
    def _petition_template(self) -> str:
        """Template for legal petitions."""
        return """{TITLE}

To: {JURISDICTION}
Case No.: {CASE_NUMBER}
Date: {DATE}

Parties:
{PARTIES}

Body:
{BODY}

Attachments:
{ATTACHMENTS}

Respectfully submitted,
[Attorney Name]
[Law Firm Name]
[Contact Information]"""
    
    def _memorandum_template(self) -> str:
        """Template for legal memoranda."""
        return """MEMORANDUM

To: [Recipient]
From: [Sender]
Date: {DATE}
Re: {TITLE}

{BODY}

Attachments:
{ATTACHMENTS}"""
    
    def _notice_template(self) -> str:
        """Template for legal notices."""
        return """NOTICE

To: {PARTIES}
Date: {DATE}
Re: {TITLE}

{BODY}

This serves as official notice regarding the matter referenced above.

[Attorney Name]
[Law Firm Name]"""
    
    def _contract_template(self) -> str:
        """Template for contracts."""
        return """CONTRACT AGREEMENT

This Agreement is made and entered into as of {DATE} by and between:

{PARTIES}

1. PURPOSE
{BODY}

[Additional contract clauses...]

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

[Signatures]"""
    
    def _legal_opinion_template(self) -> str:
        """Template for legal opinions."""
        return """LEGAL OPINION

To: [Recipient]
From: [Sender]
Date: {DATE}
Re: {TITLE}

OPINION:
{BODY}

CONCLUSION:
[Conclusion summary]

[Attorney Name]
[Bar Registration Number]"""

    def save_document(self, content: str, filename: str, output_dir: str = "output") -> str:
        """Save the generated document to a file."""
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return filepath
        except IOError as e:
            raise IOError(f"Failed to save document: {e}")

# Example usage
if __name__ == "__main__":
    generator = LegalCorrespondenceGenerator()
    
    parties = [
        Party(
            name="John Doe",
            role="Plaintiff",
            address="123 Main St, Anytown, ST",
            identification="CPF: 123.456.789-00"
        ),
        Party(
            name="Acme Corp",
            role="Defendant",
            address="456 Business Ave, Anytown, ST",
            identification="CNPJ: 12.345.678/0001-90"
        )
    ]
    
    document = LegalDocument(
        document_type=DocumentType.PETITION,
        title="Petition for Damages",
        parties=parties,
        body="The plaintiff seeks compensation for damages caused by the defendant's negligence...",
        jurisdiction="Civil Court of Anytown",
        case_number="2023-CV-12345",
        attachments=["Exhibit A - Medical Records", "Exhibit B - Photographic Evidence"]
    )
    
    try:
        generated_doc = generator.generate_document(document)
        saved_path = generator.save_document(generated_doc, "petition_example.txt")
        print(f"Document successfully generated and saved to: {saved_path}")
    except Exception as e:
        print(f"Error generating document: {e}")
```
