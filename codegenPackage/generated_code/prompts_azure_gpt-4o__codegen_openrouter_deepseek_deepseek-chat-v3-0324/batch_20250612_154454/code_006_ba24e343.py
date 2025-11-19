"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Write Python code to automate the generation of official verification documents for water, gas, and heat meters, including fields for accreditation details and compliance with regulations.
Generated: DETERMINISTIC_ba24e34328a05793
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum, auto


class MeterType(Enum):
    WATER = auto()
    GAS = auto()
    HEAT = auto()


@dataclass
class Accreditation:
    body: str
    standard: str
    certificate_number: str
    valid_until: datetime.date


@dataclass
class MeterDetails:
    serial_number: str
    manufacturer: str
    model: str
    installation_date: datetime.date
    last_calibration: datetime.date
    next_calibration_due: datetime.date


@dataclass
class VerificationDocument:
    document_id: str
    issue_date: datetime.date
    meter_type: MeterType
    meter_details: MeterDetails
    accreditation: Accreditation
    compliance_standards: List[str]
    inspector_name: str
    inspector_id: str
    notes: Optional[str] = None


class DocumentGenerator:
    """
    Generates verification documents for various meter types.
    """
    
    def __init__(self, template_path: Optional[str] = None):
        """
        Initialize the document generator.
        
        Args:
            template_path: Path to a JSON template file. If None, uses default values.
        """
        self.templates = self._load_templates(template_path)
    
    def _load_templates(self, template_path: Optional[str]) -> Dict[str, str]:
        """Load templates from JSON file or use defaults."""
        default_templates = {
            "header": "OFFICIAL METER VERIFICATION DOCUMENT",
            "footer": "This document certifies compliance with all relevant regulations.",
            "water_section": "Water Meter Verification",
            "gas_section": "Gas Meter Verification",
            "heat_section": "Heat Meter Verification"
        }
        
        if template_path:
            try:
                with open(template_path, 'r') as f:
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Warning: Could not load template file. Using defaults. Error: {str(e)}")
                return default_templates
        return default_templates
    
    def _get_meter_section(self, meter_type: MeterType) -> str:
        """Get the appropriate section header based on meter type."""
        if meter_type == MeterType.WATER:
            return self.templates["water_section"]
        elif meter_type == MeterType.GAS:
            return self.templates["gas_section"]
        elif meter_type == MeterType.HEAT:
            return self.templates["heat_section"]
        else:
            raise ValueError(f"Unknown meter type: {meter_type}")
    
    def generate_document(self, verification: VerificationDocument) -> str:
        """
        Generate a verification document based on provided details.
        
        Args:
            verification: VerificationDocument containing all necessary information
            
        Returns:
            str: The generated document as a formatted string
        """
        try:
            section = self._get_meter_section(verification.meter_type)
            
            doc_lines = [
                f"{self.templates['header']}",
                f"Document ID: {verification.document_id}",
                f"Issue Date: {verification.issue_date.strftime('%Y-%m-%d')}",
                "",
                f"=== {section} ===",
                "",
                "Meter Details:",
                f"  Serial Number: {verification.meter_details.serial_number}",
                f"  Manufacturer: {verification.meter_details.manufacturer}",
                f"  Model: {verification.meter_details.model}",
                f"  Installation Date: {verification.meter_details.installation_date.strftime('%Y-%m-%d')}",
                f"  Last Calibration: {verification.meter_details.last_calibration.strftime('%Y-%m-%d')}",
                f"  Next Calibration Due: {verification.meter_details.next_calibration_due.strftime('%Y-%m-%d')}",
                "",
                "Accreditation:",
                f"  Body: {verification.accreditation.body}",
                f"  Standard: {verification.accreditation.standard}",
                f"  Certificate Number: {verification.accreditation.certificate_number}",
                f"  Valid Until: {verification.accreditation.valid_until.strftime('%Y-%m-%d')}",
                "",
                "Compliance Standards:",
                *[f"  - {standard}" for standard in verification.compliance_standards],
                "",
                "Inspector:",
                f"  Name: {verification.inspector_name}",
                f"  ID: {verification.inspector_id}",
            ]
            
            if verification.notes:
                doc_lines.extend([
                    "",
                    "Additional Notes:",
                    verification.notes
                ])
            
            doc_lines.extend([
                "",
                self.templates['footer']
            ])
            
            return "\n".join(doc_lines)
        
        except Exception as e:
            raise ValueError(f"Failed to generate document: {str(e)}")
    
    def save_document(self, document: str, file_path: str) -> None:
        """
        Save the generated document to a file.
        
        Args:
            document: The document content to save
            file_path: Path to save the document to
        """
        try:
            with open(file_path, 'w') as f:
                f.write(document)
        except IOError as e:
            raise IOError(f"Failed to save document: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Create sample data
        accreditation = Accreditation(
            body="International Standards Organization",
            standard="ISO 9001:2015",
            certificate_number="ISO-12345",
            valid_until=datetime.date(2025, 12, 31)
        )
        
        meter_details = MeterDetails(
            serial_number="WM-987654",
            manufacturer="AquaMeasure Inc.",
            model="WM-3000",
            installation_date=datetime.date(2020, 5, 15),
            last_calibration=datetime.date(2023, 1, 10),
            next_calibration_due=datetime.date(2024, 1, 10)
        )
        
        verification = VerificationDocument(
            document_id="VER-2023-0567",
            issue_date=datetime.date.today(),
            meter_type=MeterType.WATER,
            meter_details=meter_details,
            accreditation=accreditation,
            compliance_standards=["EN 14154", "ISO 4064"],
            inspector_name="John Doe",
            inspector_id="INSP-7890",
            notes="Meter shows normal wear but functions within specifications."
        )
        
        # Generate document
        generator = DocumentGenerator()
        doc = generator.generate_document(verification)
        print(doc)
        
        # Save to file
        generator.save_document(doc, "water_meter_verification.txt")
        print("Document saved successfully.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
