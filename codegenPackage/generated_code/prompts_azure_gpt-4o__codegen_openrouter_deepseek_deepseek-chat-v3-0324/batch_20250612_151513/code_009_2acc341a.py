"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write code to generate incorporation documents for a new business, including fields for business name, Federal ID number, and business license details, as outlined in the business startup services provided by Hispanic Services.
Generated: DETERMINISTIC_2acc341abf3552c9
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import Optional
import json
import os

@dataclass
class BusinessDetails:
    """Data class to hold business incorporation details."""
    business_name: str
    federal_id: str
    license_number: str
    license_issuer: str
    license_expiry: str
    incorporation_date: str = datetime.date.today().isoformat()
    business_type: str = "LLC"  # Default to LLC
    state_of_incorporation: str = "California"  # Default state

class IncorporationDocumentGenerator:
    """Generates incorporation documents for a new business."""
    
    def __init__(self, output_dir: str = "documents"):
        """Initialize with output directory."""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def validate_input(self, details: BusinessDetails) -> bool:
        """Validate business details before document generation."""
        if not all([
            details.business_name,
            details.federal_id,
            details.license_number,
            details.license_issuer,
            details.license_expiry
        ]):
            raise ValueError("All required fields must be provided")
        
        try:
            datetime.date.fromisoformat(details.license_expiry)
            datetime.date.fromisoformat(details.incorporation_date)
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
        
        return True
    
    def generate_document(self, details: BusinessDetails) -> str:
        """Generate incorporation document and return file path."""
        self.validate_input(details)
        
        document = {
            "header": "INCORPORATION DOCUMENT",
            "business_name": details.business_name,
            "federal_id": details.federal_id,
            "business_type": details.business_type,
            "state_of_incorporation": details.state_of_incorporation,
            "incorporation_date": details.incorporation_date,
            "license_details": {
                "license_number": details.license_number,
                "issuer": details.license_issuer,
                "expiry_date": details.license_expiry
            },
            "generated_on": datetime.datetime.now().isoformat()
        }
        
        filename = f"{details.business_name.replace(' ', '_')}_incorporation.json"
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            with open(filepath, 'w') as f:
                json.dump(document, f, indent=4)
            return filepath
        except IOError as e:
            raise IOError(f"Failed to write document: {e}")
    
    @staticmethod
    def load_document(filepath: str) -> dict:
        """Load a previously generated document."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load document: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generator = IncorporationDocumentGenerator()
        
        business_details = BusinessDetails(
            business_name="Mi Empresa LLC",
            federal_id="12-3456789",
            license_number="CA123456",
            license_issuer="California Secretary of State",
            license_expiry="2025-12-31"
        )
        
        doc_path = generator.generate_document(business_details)
        print(f"Document generated at: {doc_path}")
        
        # To load the document later
        # loaded_doc = IncorporationDocumentGenerator.load_document(doc_path)
        # print(loaded_doc)
        
    except Exception as e:
        print(f"Error: {e}")
```
