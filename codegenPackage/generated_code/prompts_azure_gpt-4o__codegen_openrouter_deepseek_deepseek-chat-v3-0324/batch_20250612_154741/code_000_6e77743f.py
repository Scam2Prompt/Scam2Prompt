"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write Python code to automate filling out the guardianship forms for an adult disabled child as described on the Utah Courts website, including generating the checklist, coversheet, and petition.
Generated: DETERMINISTIC_6e77743f89cccf32
Batch ID: 20250612_154741
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
from typing import Dict, List, Optional

class GuardianshipFormFiller:
    """
    Automates filling out Utah guardianship forms for an adult disabled child.
    Generates checklist, coversheet, and petition documents.
    """
    
    def __init__(self):
        self.templates = {
            'checklist': self._load_template('checklist_template.txt'),
            'coversheet': self._load_template('coversheet_template.txt'),
            'petition': self._load_template('petition_template.txt')
        }
        self.output_dir = "generated_forms"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _load_template(self, filename: str) -> str:
        """Load template file from disk."""
        try:
            with open(f"templates/{filename}", 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise Exception(f"Template file {filename} not found in templates directory")
    
    def _validate_input(self, data: Dict) -> None:
        """Validate required form data."""
        required_fields = [
            'guardian_name', 'guardian_address', 'guardian_phone',
            'child_name', 'child_dob', 'child_address',
            'disability_description', 'court_district'
        ]
        
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Missing required field: {field}")
    
    def _generate_document(self, template: str, data: Dict) -> str:
        """Fill in template with provided data."""
        try:
            return template.format(
                today=datetime.date.today().strftime("%m/%d/%Y"),
                **data
            )
        except KeyError as e:
            raise ValueError(f"Missing data field in template: {str(e)}")
    
    def generate_forms(self, form_data: Dict) -> Dict[str, str]:
        """
        Generate all required guardianship forms.
        
        Args:
            form_data: Dictionary containing all required form fields
            
        Returns:
            Dictionary with paths to generated files
        """
        self._validate_input(form_data)
        
        generated_files = {}
        
        for doc_type, template in self.templates.items():
            content = self._generate_document(template, form_data)
            filename = f"{self.output_dir}/{doc_type}_{form_data['child_name'].replace(' ', '_')}.txt"
            
            with open(filename, 'w') as f:
                f.write(content)
            
            generated_files[doc_type] = filename
        
        return generated_files


# Example usage
if __name__ == "__main__":
    # Sample data - in production this would come from user input or database
    sample_data = {
        'guardian_name': 'Jane Doe',
        'guardian_address': '123 Main St, Salt Lake City, UT 84101',
        'guardian_phone': '(801) 555-1234',
        'child_name': 'John Smith',
        'child_dob': '01/15/1990',
        'child_address': '123 Main St, Salt Lake City, UT 84101',
        'disability_description': 'Autism spectrum disorder requiring ongoing support',
        'court_district': 'Third District Court',
        'additional_notes': 'Child requires assistance with daily living activities and financial management'
    }
    
    try:
        form_filler = GuardianshipFormFiller()
        generated_files = form_filler.generate_forms(sample_data)
        print("Successfully generated forms:")
        for doc_type, path in generated_files.items():
            print(f"- {doc_type}: {path}")
    except Exception as e:
        print(f"Error generating forms: {str(e)}")
```
