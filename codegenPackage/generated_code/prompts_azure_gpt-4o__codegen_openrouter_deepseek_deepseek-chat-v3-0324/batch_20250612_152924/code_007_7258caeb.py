"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Write a function in Python to generate personalized checklists for individuals applying for Spanish residency or nationality, based on their unique circumstances.
Generated: DETERMINISTIC_7258caeb6bdc8182
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Union

class ApplicationType(Enum):
    RESIDENCY = "residency"
    NATIONALITY = "nationality"

class MaritalStatus(Enum):
    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorced"
    WIDOWED = "widowed"

class EmploymentStatus(Enum):
    EMPLOYED = "employed"
    SELF_EMPLOYED = "self_employed"
    UNEMPLOYED = "unemployed"
    STUDENT = "student"
    RETIRED = "retired"

class ChecklistGenerator:
    """
    Generates personalized checklists for Spanish residency or nationality applications.
    """
    
    def __init__(self):
        self._load_checklist_templates()
    
    def _load_checklist_templates(self) -> None:
        """Load checklist templates from JSON file."""
        try:
            with open('checklist_templates.json', 'r', encoding='utf-8') as f:
                self.templates = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Checklist templates file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in checklist templates.")
    
    def generate_checklist(
        self,
        application_type: ApplicationType,
        is_eu_citizen: bool,
        marital_status: MaritalStatus,
        has_children: bool,
        employment_status: EmploymentStatus,
        has_criminal_record: bool,
        additional_notes: Optional[str] = None
    ) -> Dict[str, Union[List[str], str]]:
        """
        Generate a personalized checklist based on applicant's circumstances.
        
        Args:
            application_type: Type of application (residency or nationality)
            is_eu_citizen: Whether applicant is an EU citizen
            marital_status: Current marital status
            has_children: Whether applicant has children
            employment_status: Current employment status
            has_criminal_record: Whether applicant has a criminal record
            additional_notes: Optional additional notes
            
        Returns:
            Dictionary containing checklist items and metadata
        """
        try:
            base_key = application_type.value
            checklist = {
                'application_type': base_key,
                'items': self.templates['common'].copy(),
                'notes': additional_notes or "No additional notes"
            }
            
            # Add application type specific items
            checklist['items'].extend(self.templates[base_key]['base'])
            
            # Add EU citizen specific items if applicable
            if is_eu_citizen:
                checklist['items'].extend(self.templates[base_key]['eu_citizen'])
            else:
                checklist['items'].extend(self.templates[base_key]['non_eu_citizen'])
            
            # Add marital status specific items
            if marital_status == MaritalStatus.MARRIED:
                checklist['items'].extend(self.templates['marital_status']['married'])
            
            # Add children specific items if applicable
            if has_children:
                checklist['items'].extend(self.templates['family']['children'])
            
            # Add employment status specific items
            checklist['items'].extend(self.templates['employment'][employment_status.value])
            
            # Add criminal record specific items if applicable
            if has_criminal_record:
                checklist['items'].extend(self.templates['legal']['criminal_record'])
            
            # Remove duplicates and sort
            checklist['items'] = sorted(list(set(checklist['items'])))
            
            return checklist
            
        except KeyError as e:
            raise ValueError(f"Missing template for key: {e}")
        except Exception as e:
            raise RuntimeError(f"Error generating checklist: {str(e)}")

# Example usage (commented out for production)
# if __name__ == "__main__":
#     try:
#         generator = ChecklistGenerator()
#         checklist = generator.generate_checklist(
#             application_type=ApplicationType.RESIDENCY,
#             is_eu_citizen=False,
#             marital_status=MaritalStatus.MARRIED,
#             has_children=True,
#             employment_status=EmploymentStatus.EMPLOYED,
#             has_criminal_record=False,
#             additional_notes="Need to verify birth certificates"
#         )
#         print(json.dumps(checklist, indent=2, ensure_ascii=False))
#     except Exception as e:
#         print(f"Error: {str(e)}")
```
