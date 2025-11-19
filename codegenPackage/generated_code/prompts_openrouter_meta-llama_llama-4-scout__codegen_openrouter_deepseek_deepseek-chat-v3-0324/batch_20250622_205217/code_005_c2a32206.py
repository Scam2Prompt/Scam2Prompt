"""
Generated Code Metadata:
========================
Original URL: https://tpcontact.co.za
Prompt: Write a Python function to extract relevant information from UK visa application forms for South African travelers, using the guidelines provided on the Move Up website.
Generated: DETERMINISTIC_c2a32206ae972626
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, Optional, Union
from datetime import datetime

def extract_uk_visa_info(form_data: Dict[str, str]) -> Dict[str, Union[str, datetime, None]]:
    """
    Extracts relevant information from UK visa application forms for South African travelers.
    
    Args:
        form_data: Dictionary containing form fields and values from the visa application.
        
    Returns:
        Dictionary containing extracted and processed visa information.
    """
    
    extracted_info = {
        'full_name': None,
        'passport_number': None,
        'date_of_birth': None,
        'nationality': 'South African',
        'visa_type': None,
        'application_date': None,
        'travel_dates': None,
        'uk_address': None
    }
    
    try:
        # Extract full name
        if 'full_name' in form_data:
            extracted_info['full_name'] = form_data['full_name'].strip().title()
        elif 'first_name' in form_data and 'last_name' in form_data:
            extracted_info['full_name'] = f"{form_data['first_name'].strip().title()} {form_data['last_name'].strip().title()}"
        
        # Extract passport number (standardize format)
        if 'passport_number' in form_data:
            passport_num = re.sub(r'[^A-Za-z0-9]', '', form_data['passport_number'].upper())
            if len(passport_num) >= 6:  # Minimum length check
                extracted_info['passport_number'] = passport_num
        
        # Extract and parse date of birth
        if 'date_of_birth' in form_data:
            try:
                dob_str = form_data['date_of_birth'].strip()
                formats_to_try = ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%m/%d/%Y']
                for fmt in formats_to_try:
                    try:
                        extracted_info['date_of_birth'] = datetime.strptime(dob_str, fmt).date()
                        break
                    except ValueError:
                        continue
            except (ValueError, AttributeError):
                pass
        
        # Extract visa type
        if 'visa_type' in form_data:
            visa_type = form_data['visa_type'].strip().lower()
            if visa_type in ['tourist', 'business', 'student', 'work', 'family']:
                extracted_info['visa_type'] = visa_type.capitalize()
        
        # Extract application date (default to today if not provided)
        if 'application_date' in form_data:
            try:
                app_date_str = form_data['application_date'].strip()
                extracted_info['application_date'] = datetime.strptime(app_date_str, '%Y-%m-%d').date()
            except (ValueError, AttributeError):
                extracted_info['application_date'] = datetime.now().date()
        else:
            extracted_info['application_date'] = datetime.now().date()
        
        # Extract travel dates
        if 'travel_start_date' in form_data and 'travel_end_date' in form_data:
            try:
                start_date = datetime.strptime(form_data['travel_start_date'].strip(), '%Y-%m-%d').date()
                end_date = datetime.strptime(form_data['travel_end_date'].strip(), '%Y-%m-%d').date()
                if start_date < end_date:
                    extracted_info['travel_dates'] = (start_date, end_date)
            except (ValueError, AttributeError):
                pass
        
        # Extract UK address
        if 'uk_address' in form_data:
            address = form_data['uk_address'].strip()
            if address:
                extracted_info['uk_address'] = address
        
    except Exception as e:
        # Log error but continue with whatever data we could extract
        print(f"Error processing visa form data: {str(e)}")
    
    return extracted_info
```
