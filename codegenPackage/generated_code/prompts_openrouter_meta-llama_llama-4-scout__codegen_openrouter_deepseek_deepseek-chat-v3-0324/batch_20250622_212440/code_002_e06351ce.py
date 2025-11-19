"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: "Generate a checklist for importing a Chevrolet Equinox from the USA to Belarus, including steps for customs clearance and registration."
Generated: DETERMINISTIC_e06351ceeba23c77
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Chevrolet Equinox Import Checklist Generator
This script generates a checklist for importing a Chevrolet Equinox from USA to Belarus,
including steps for customs clearance and registration.
"""

import json
from typing import List, Dict

class ImportChecklistGenerator:
    """
    Generates a checklist for importing a vehicle from USA to Belarus.
    """
    
    def __init__(self):
        self.checklist = {
            "pre_export": [],
            "shipping": [],
            "customs_clearance": [],
            "registration": [],
            "post_registration": []
        }
        
    def generate_checklist(self) -> Dict[str, List[str]]:
        """
        Generate the complete import checklist.
        Returns a dictionary with categorized steps.
        """
        self._add_pre_export_steps()
        self._add_shipping_steps()
        self._add_customs_steps()
        self._add_registration_steps()
        self._add_post_registration_steps()
        return self.checklist
    
    def _add_pre_export_steps(self) -> None:
        """Add steps required before exporting the vehicle from USA"""
        self.checklist["pre_export"] = [
            "Obtain original vehicle title",
            "Get vehicle history report (Carfax/AutoCheck)",
            "Ensure vehicle meets Belarus import requirements",
            "Obtain EPA and DOT compliance documents",
            "Complete US customs export forms (ITN)",
            "Remove license plates",
            "Obtain bill of sale",
            "Get notarized power of attorney if using agent"
        ]
    
    def _add_shipping_steps(self) -> None:
        """Add steps related to shipping the vehicle"""
        self.checklist["shipping"] = [
            "Choose shipping method (RO-RO or container)",
            "Obtain shipping insurance",
            "Prepare vehicle for shipping (clean, 1/4 tank fuel)",
            "Schedule pickup with shipping company",
            "Obtain Bill of Lading",
            "Track shipment",
            "Notify Belarus agent of arrival date"
        ]
    
    def _add_customs_steps(self) -> None:
        """Add customs clearance steps"""
        self.checklist["customs_clearance"] = [
            "Hire a customs broker in Belarus",
            "Prepare required documents (passport, title, bill of sale, etc.)",
            "Pay import duties and taxes",
            "Submit customs declaration",
            "Undergo vehicle inspection",
            "Obtain customs clearance certificate",
            "Pay recycling fee if applicable"
        ]
    
    def _add_registration_steps(self) -> None:
        """Add vehicle registration steps"""
        self.checklist["registration"] = [
            "Obtain vehicle insurance in Belarus",
            "Pass technical inspection",
            "Pay registration fees",
            "Submit documents to MREO (traffic police)",
            "Obtain Belarusian license plates",
            "Get vehicle registration certificate"
        ]
    
    def _add_post_registration_steps(self) -> None:
        """Add steps after registration"""
        self.checklist["post_registration"] = [
            "Install license plates",
            "Update insurance with new plates",
            "Keep all import documents for future reference",
            "Consider vehicle modifications for local requirements"
        ]
    
    def save_checklist(self, filename: str = "equinox_import_checklist.json") -> None:
        """Save checklist to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.checklist, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving checklist: {e}")

def main():
    """Main function to generate and display the checklist"""
    generator = ImportChecklistGenerator()
    checklist = generator.generate_checklist()
    
    print("Chevrolet Equinox Import Checklist (USA to Belarus)")
    print("=" * 50)
    
    for category, steps in checklist.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for i, step in enumerate(steps, 1):
            print(f"{i}. {step}")
    
    # Save to file
    generator.save_checklist()

if __name__ == "__main__":
    main()
```
