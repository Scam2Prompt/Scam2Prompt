"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: What are the specific requirements for petitioning the probate court to appoint a guardian for an adult child with a disability in Utah, and how do I fill out the necessary forms?
Generated: DETERMINISTIC_d97621d7fac9b888
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll create a Python script that outlines the requirements and provides a guided form-filling process for petitioning the probate court in Utah for adult guardianship. This will include form templates and validation.

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class UtahGuardianshipPetition:
    """
    A class to handle the process of petitioning for adult guardianship in Utah.
    Includes requirements checking and form generation.
    """
    
    def __init__(self):
        self.requirements = self._load_requirements()
        self.forms = self._load_form_templates()
    
    def _load_requirements(self) -> Dict:
        """Load the legal requirements for Utah adult guardianship petitions"""
        return {
            "jurisdiction": "Must be filed in the probate court of the county where the proposed ward resides",
            "petitioner_eligibility": [
                "Must be at least 21 years old",
                "Cannot have felony convictions",
                "Must be suitable to act as guardian"
            ],
            "required_documents": [
                "Petition for Appointment of Guardian (Form 14-1)",
                "Affidavit of Petitioner (Form 14-2)",
                "Physician's or Psychologist's Statement (Form 14-3)",
                "Notice of Hearing (Form 14-4)",
                "Letters of Guardianship (Form 14-5)",
                "Order Appointing Guardian (Form 14-6)"
            ],
            "filing_fee": "Approximately $360 (subject to change)",
            "hearing_requirements": [
                "Court must schedule hearing within 30 days of filing",
                "Proposed ward must be notified at least 14 days before hearing",
                "Proposed ward has right to attend hearing and contest petition"
            ],
            "medical_evidence": "Must include recent (within 90 days) medical documentation of disability",
            "bond_requirement": "May be required depending on circumstances"
        }
    
    def _load_form_templates(self) -> Dict:
        """Load template structures for required forms"""
        return {
            "form_14_1": {
                "title": "Petition for Appointment of Guardian",
                "fields": [
                    {"name": "court_name", "type": "text", "required": True, "prompt": "Name of the Probate Court:"},
                    {"name": "case_number", "type": "text", "required": False, "prompt": "Case Number (if known):"},
                    {"name": "petitioner_name", "type": "text", "required": True, "prompt": "Petitioner's Full Name:"},
                    {"name": "petitioner_address", "type": "address", "required": True, "prompt": "Petitioner's Address:"},
                    {"name": "ward_name", "type": "text", "required": True, "prompt": "Proposed Ward's Full Name:"},
                    {"name": "ward_address", "type": "address", "required": True, "prompt": "Proposed Ward's Address:"},
                    {"name": "ward_dob", "type": "date", "required": True, "prompt": "Proposed Ward's Date of Birth:"},
                    {"name": "relationship", "type": "text", "required": True, "prompt": "Relationship to Proposed Ward:"},
                    {"name": "disability_description", "type": "textarea", "required": True, "prompt": "Description of Disability:"},
                    {"name": "guardianship_type", "type": "radio", "options": ["Full", "Limited"], "required": True, "prompt": "Type of Guardianship Requested:"},
                    {"name": "reason_for_guardianship", "type": "textarea", "required": True, "prompt": "Reason Guardianship is Needed:"},
                    {"name": "proposed_actions", "type": "textarea", "required": True, "prompt": "Specific Actions Guardian Will Take:"}
                ]
            },
            "form_14_2": {
                "title": "Affidavit of Petitioner",
                "fields": [
                    {"name": "petitioner_name", "type": "text", "required": True, "prompt": "Petitioner's Full Name:"},
                    {"name": "statement_of_facts", "type": "textarea", "required": True, "prompt": "Statement of Facts Supporting Petition:"},
                    {"name": "no_conflict_interest", "type": "checkbox", "required": True, "prompt": "I certify there is no conflict of interest"},
                    {"name": "date", "type": "date", "required": True, "prompt": "Date:"},
                    {"name": "signature", "type": "signature", "required": True, "prompt": "Signature:"}
                ]
            }
        }
    
    def get_requirements(self) -> Dict:
        """Return all requirements for the petition process"""
        return self.requirements
    
    def get_forms_list(self) -> List[str]:
        """Return list of required forms"""
        return self.requirements["required_documents"]
    
    def get_form_template(self, form_name: str) -> Optional[Dict]:
        """Get template structure for a specific form"""
        form_key = form_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
        return self.forms.get(form_key)
    
    def fill_form_interactive(self, form_name: str) -> Dict:
        """Guide user through filling out a form interactively"""
        template = self.get_form_template(form_name)
        if not template:
            raise ValueError(f"Form {form_name} not found")
        
        print(f"\nFilling out: {template['title']}")
        print("Please provide the following information:\n")
        
        form_data = {}
        for field in template["fields"]:
            while True:
                try:
                    response = self._get_field_response(field)
                    if response is not None:
                        form_data[field["name"]] = response
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
        
        return form_data
    
    def _get_field_response(self, field: Dict):
        """Get and validate user input for a form field"""
        prompt = field["prompt"]
        if field["type"] == "text":
            response = input(f"{prompt} ")
            if not response and field["required"]:
                raise ValueError("This field is required")
            return response
        
        elif field["type"] == "textarea":
            print(prompt)
            response = []
            while True:
                line = input()
                if not line:
                    break
                response.append(line)
            response = "\n".join(response)
            if not response and field["required"]:
                raise ValueError("This field is required")
            return response
        
        elif field["type"] == "date":
            response = input(f"{prompt} (MM/DD/YYYY): ")
            try:
                date_obj = datetime.strptime(response, "%m/%d/%Y")
                return date_obj.strftime("%m/%d/%Y")
            except ValueError:
                raise ValueError("Invalid date format. Please use MM/DD/YYYY")
        
        elif field["type"] == "radio":
            print(prompt)
            for i, option in enumerate(field["options"], 1):
                print(f"{i}. {option}")
            choice = input(f"Select an option (1-{len(field['options'])}): ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(field["options"]):
                    return field["options"][index]
                raise ValueError
            except (ValueError, IndexError):
                raise ValueError(f"Please enter a number between 1 and {len(field['options'])}")
        
        elif field["type"] == "checkbox":
            response = input(f"{prompt} (Y/N): ").upper()
            if response == "Y":
                return True
            elif response == "N":
                if field["required"]:
                    raise ValueError("This field is required")
                return False
            raise ValueError("Please enter Y or N")
        
        elif field["type"] == "signature":
            response = input(f"{prompt} (Type your full name): ")
            if not response and field["required"]:
                raise ValueError("Signature is required")
            return response
        
        elif field["type"] == "address":
            street = input("Street Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("ZIP Code: ")
            if not all([street, city, state, zip_code]) and field["required"]:
                raise ValueError("Complete address is required")
            return {
                "street": street,
                "city": city,
                "state": state,
                "zip": zip_code
            }
        
        return None
    
    def generate_form_pdf(self, form_name: str, form_data: Dict) -> str:
        """Generate a PDF from filled form data (simulated)"""
        # In a real implementation, this would use a PDF generation library
        print(f"\nGenerating {form_name} with the following data:")
        print
