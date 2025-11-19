"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Create a tool to automate the generation of impugnation requests and security mandates for public licitations, based on Licitare's licitation services.
Generated: DETERMINISTIC_00eedab82fe48c86
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Automated Impugnation and Security Mandate Generator for Public Licitations

This tool generates legal documents for public licitation processes,
specifically impugnation requests and security mandates, based on
Licitare's licitation services.
"""

import json
import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
import jinja2
import uuid
import os


@dataclass
class LicitationDetails:
    """Data structure holding licitation details."""
    process_number: str
    entity_name: str
    process_description: str
    publication_date: str
    deadline: str
    budget: float
    currency: str = "EUR"


@dataclass
class CompanyDetails:
    """Data structure holding company details."""
    name: str
    tax_id: str
    address: str
    representative_name: str
    representative_id: str
    contact_email: str
    contact_phone: str


@dataclass
class ImpugnationRequest:
    """Data structure for impugnation request document."""
    reference_number: str
    submission_date: str
    licitation_details: LicitationDetails
    company_details: CompanyDetails
    grounds: str
    supporting_documents: list[str]


@dataclass
class SecurityMandate:
    """Data structure for security mandate document."""
    reference_number: str
    issue_date: str
    expiration_date: str
    licitation_details: LicitationDetails
    company_details: CompanyDetails
    amount: float
    currency: str
    bank_guarantee_details: Optional[Dict[str, Any]] = None


class DocumentGenerator:
    """Main class for document generation."""
    
    def __init__(self, template_dir: str = "templates"):
        """Initialize with template directory."""
        self.template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
        self.template_env = jinja2.Environment(loader=self.template_loader)
        
    def _generate_reference_number(self) -> str:
        """Generate a unique reference number."""
        return f"REF-{uuid.uuid4().hex[:8].upper()}"
    
    def _get_current_date(self) -> str:
        """Get current date in YYYY-MM-DD format."""
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    def _validate_input_data(self, data: Dict[str, Any]) -> bool:
        """Validate input data structure."""
        required_fields = {
            'licitation': ['process_number', 'entity_name', 'process_description'],
            'company': ['name', 'tax_id', 'representative_name']
        }
        
        for category, fields in required_fields.items():
            if category not in data:
                return False
            for field in fields:
                if field not in data[category]:
                    return False
        return True
    
    def _render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render a template with the given context."""
        try:
            template = self.template_env.get_template(template_name)
            return template.render(context)
        except jinja2.TemplateNotFound:
            raise FileNotFoundError(f"Template {template_name} not found")
        except jinja2.TemplateError as e:
            raise ValueError(f"Template rendering error: {str(e)}")
    
    def generate_impugnation_request(
        self,
        licitation_data: Dict[str, Any],
        company_data: Dict[str, Any],
        grounds: str,
        supporting_docs: list[str]
    ) -> Dict[str, Any]:
        """
        Generate an impugnation request document.
        
        Args:
            licitation_data: Dictionary with licitation details
            company_data: Dictionary with company details
            grounds: Text describing the grounds for impugnation
            supporting_docs: List of supporting document references
            
        Returns:
            Dictionary containing the document data and rendered text
        """
        if not self._validate_input_data({
            'licitation': licitation_data,
            'company': company_data
        }):
            raise ValueError("Invalid input data structure")
        
        licitation = LicitationDetails(**licitation_data)
        company = CompanyDetails(**company_data)
        
        impugnation = ImpugnationRequest(
            reference_number=self._generate_reference_number(),
            submission_date=self._get_current_date(),
            licitation_details=licitation,
            company_details=company,
            grounds=grounds,
            supporting_documents=supporting_docs
        )
        
        context = asdict(impugnation)
        document_text = self._render_template("impugnation_template.html", context)
        
        return {
            "metadata": asdict(impugnation),
            "document": document_text
        }
    
    def generate_security_mandate(
        self,
        licitation_data: Dict[str, Any],
        company_data: Dict[str, Any],
        amount: float,
        currency: str = "EUR",
        bank_details: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate a security mandate document.
        
        Args:
            licitation_data: Dictionary with licitation details
            company_data: Dictionary with company details
            amount: Guarantee amount
            currency: Currency (default: EUR)
            bank_details: Optional bank guarantee details
            
        Returns:
            Dictionary containing the document data and rendered text
        """
        if not self._validate_input_data({
            'licitation': licitation_data,
            'company': company_data
        }):
            raise ValueError("Invalid input data structure")
        
        licitation = LicitationDetails(**licitation_data)
        company = CompanyDetails(**company_data)
        
        today = datetime.datetime.now()
        expiration_date = (today + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        
        mandate = SecurityMandate(
            reference_number=self._generate_reference_number(),
            issue_date=self._get_current_date(),
            expiration_date=expiration_date,
            licitation_details=licitation,
            company_details=company,
            amount=amount,
            currency=currency,
            bank_guarantee_details=bank_details
        )
        
        context = asdict(mandate)
        document_text = self._render_template("security_mandate_template.html", context)
        
        return {
            "metadata": asdict(mandate),
            "document": document_text
        }
    
    def save_document(self, document: Dict[str, Any], output_dir: str = "output") -> str:
        """
        Save generated document to file.
        
        Args:
            document: Dictionary containing document data
            output_dir: Output directory path
            
        Returns:
            Path to saved file
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        ref_number = document['metadata']['reference_number']
        filename = f"{output_dir}/{ref_number}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(document, f, indent=2, ensure_ascii=False)
            return filename
        except IOError as e:
            raise IOError(f"Failed to save document: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize generator
    generator = DocumentGenerator()
    
    # Sample data
    licitation_data = {
        "process_number": "LIC-2023-001",
        "entity_name": "City Council of Example",
        "process_description": "Construction of new municipal library",
        "publication_date": "2023-01-15",
        "deadline": "2023-02-15",
        "budget": 2500000.00,
        "currency": "EUR"
    }
    
    company_data = {
        "name": "Constructora Ejemplo S.L.",
        "tax_id": "B12345678",
        "address": "Calle Ejemplo 123, 28001 Madrid",
        "representative_name": "Ana García López",
        "representative_id": "12345678A",
        "contact_email": "info@constructora-ejemplo.com",
        "contact_phone": "+34 912 345 678"
    }
    
    try:
        # Generate impugnation request
        impugnation = generator.generate_impugnation_request(
            licitation_data=licitation_data,
            company_data=company_data,
            grounds="The technical requirements are unfairly restrictive and favor a specific competitor.",
            supporting_docs=["Technical_Report_2023.pdf", "Market_Analysis.pdf"]
        )
        generator.save_document(impugnation)
        
        # Generate security mandate
        mandate = generator.generate_security_mandate(
            licitation_data=licitation_data,
            company_data=company_data,
            amount=50000.00,
            bank_details={
                "bank_name": "Example Bank",
                "account_number": "ES12 3456 7890 1234 5678 9012",
                "guarantee_number": "GB-2023-001"
            }
        )
        generator.save_document(mandate)
        
        print("Documents generated successfully")
        
    except Exception as e:
        print(f"Error generating documents: {str(e)}")
```
