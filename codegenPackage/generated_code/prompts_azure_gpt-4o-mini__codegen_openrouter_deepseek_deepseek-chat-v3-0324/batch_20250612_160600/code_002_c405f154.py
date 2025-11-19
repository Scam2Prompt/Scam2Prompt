"""
Generated Code Metadata:
========================
Original URL: https://cedarlake.org
Prompt: Create a code snippet that simulates the process of applying for services at Cedar Lake Foundation, including necessary data fields and validation.
Generated: DETERMINISTIC_c405f15409a24a2e
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from typing import Dict, Optional, Tuple

class CedarLakeApplication:
    """
    Simulates the process of applying for services at Cedar Lake Foundation.
    Handles data collection, validation, and submission.
    """
    
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'date_of_birth',
        'email',
        'phone',
        'address',
        'city',
        'state',
        'zip_code',
        'service_type',
        'emergency_contact_name',
        'emergency_contact_phone'
    ]
    
    SERVICE_TYPES = [
        'Residential',
        'Day Program',
        'Employment Services',
        'Behavioral Health',
        'Family Support'
    ]
    
    STATES = [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ]
    
    def __init__(self):
        self.application_data: Dict[str, str] = {}
        self.errors: Dict[str, str] = {}
    
    def validate_field(self, field_name: str, value: str) -> Optional[str]:
        """Validate individual field based on its requirements."""
        if not value:
            return f"{field_name.replace('_', ' ').title()} is required."
            
        if field_name == 'email':
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
                return "Please enter a valid email address."
                
        elif field_name == 'phone' or field_name == 'emergency_contact_phone':
            digits = re.sub(r'[^0-9]', '', value)
            if len(digits) != 10:
                return "Phone number must be 10 digits."
                
        elif field_name == 'zip_code':
            if not re.match(r'^\d{5}(-\d{4})?$', value):
                return "Please enter a valid ZIP code."
                
        elif field_name == 'date_of_birth':
            try:
                dob = datetime.strptime(value, '%Y-%m-%d')
                if dob > datetime.now():
                    return "Date of birth cannot be in the future."
            except ValueError:
                return "Please enter date in YYYY-MM-DD format."
                
        elif field_name == 'state':
            if value.upper() not in self.STATES:
                return "Please enter a valid 2-letter state code."
                
        elif field_name == 'service_type':
            if value not in self.SERVICE_TYPES:
                return "Please select a valid service type."
                
        return None
    
    def collect_data(self, data: Dict[str, str]) -> bool:
        """Collect and validate application data."""
        self.errors.clear()
        
        # Validate required fields
        for field in self.REQUIRED_FIELDS:
            value = data.get(field, '').strip()
            error = self.validate_field(field, value)
            if error:
                self.errors[field] = error
            else:
                self.application_data[field] = value
        
        # Validate optional fields if provided
        if 'additional_notes' in data and data['additional_notes'].strip():
            self.application_data['additional_notes'] = data['additional_notes'].strip()
            
        return not bool(self.errors)
    
    def submit_application(self) -> Tuple[bool, str]:
        """Simulate submitting the application to Cedar Lake Foundation."""
        if self.errors:
            return False, "Cannot submit application with validation errors."
            
        # In a real implementation, this would connect to an API or database
        # Here we just simulate a successful submission
        return True, "Application submitted successfully to Cedar Lake Foundation."


# Example usage
if __name__ == "__main__":
    application = CedarLakeApplication()
    
    sample_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'date_of_birth': '1990-05-15',
        'email': 'john.doe@example.com',
        'phone': '(555) 123-4567',
        'address': '123 Main St',
        'city': 'Louisville',
        'state': 'KY',
        'zip_code': '40202',
        'service_type': 'Residential',
        'emergency_contact_name': 'Jane Doe',
        'emergency_contact_phone': '555-987-6543',
        'additional_notes': 'Requires wheelchair accessibility'
    }
    
    if application.collect_data(sample_data):
        success, message = application.submit_application()
        print(message)
    else:
        print("Validation errors:")
        for field, error in application.errors.items():
            print(f"{field}: {error}")
```
