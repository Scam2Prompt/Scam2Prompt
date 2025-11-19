"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Generate code to validate user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions Ltd, ensuring eligibility for PPI or packaged bank account claims.
Generated: DETERMINISTIC_31dd2c05a262591c
Batch ID: 20250612_152024
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
from typing import Optional, Dict, List, Tuple

class ClaimValidator:
    """
    Validates user input for PPI or packaged bank account claim submissions.
    Ensures data meets Financial Recovery Solutions Ltd requirements.
    """
    
    def __init__(self):
        # Regular expressions for validation
        self.name_regex = re.compile(r'^[a-zA-Z\s\-\.\']{2,50}$')
        self.email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.phone_regex = re.compile(r'^(\+44|0)[1-9]\d{8,9}$')
        self.postcode_regex = re.compile(r'^[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{2}$')
        self.account_regex = re.compile(r'^[0-9]{8,16}$')
        self.sort_code_regex = re.compile(r'^\d{2}-\d{2}-\d{2}$')
        
        # Claim type constants
        self.VALID_CLAIM_TYPES = {'PPI', 'PACKAGED_BANK_ACCOUNT'}
        
        # Minimum age requirement (18 years)
        self.MIN_AGE = 18
        
    def validate_name(self, name: str) -> Tuple[bool, str]:
        """
        Validates a name field (first or last name).
        Returns (is_valid, error_message)
        """
        if not name:
            return False, "Name is required"
        if not self.name_regex.match(name):
            return False, "Name must be 2-50 characters and contain only letters, spaces, hyphens, periods or apostrophes"
        return True, ""
    
    def validate_email(self, email: str) -> Tuple[bool, str]:
        """
        Validates an email address.
        Returns (is_valid, error_message)
        """
        if not email:
            return False, "Email is required"
        if not self.email_regex.match(email):
            return False, "Please enter a valid email address"
        return True, ""
    
    def validate_phone(self, phone: str) -> Tuple[bool, str]:
        """
        Validates a UK phone number.
        Returns (is_valid, error_message)
        """
        if not phone:
            return False, "Phone number is required"
        if not self.phone_regex.match(phone):
            return False, "Please enter a valid UK phone number (e.g., 01234567890 or +441234567890)"
        return True, ""
    
    def validate_postcode(self, postcode: str) -> Tuple[bool, str]:
        """
        Validates a UK postcode.
        Returns (is_valid, error_message)
        """
        if not postcode:
            return False, "Postcode is required"
        postcode = postcode.upper().strip()
        if not self.postcode_regex.match(postcode):
            return False, "Please enter a valid UK postcode (e.g., SW1A 1AA)"
        return True, ""
    
    def validate_date_of_birth(self, dob: str) -> Tuple[bool, str]:
        """
        Validates date of birth (must be at least 18 years old).
        Returns (is_valid, error_message)
        """
        if not dob:
            return False, "Date of birth is required"
        
        try:
            birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            return False, "Please enter date in YYYY-MM-DD format"
        
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        if age < self.MIN_AGE:
            return False, f"You must be at least {self.MIN_AGE} years old to submit a claim"
        
        return True, ""
    
    def validate_account_details(self, account_number: str, sort_code: str) -> Tuple[bool, str]:
        """
        Validates bank account details.
        Returns (is_valid, error_message)
        """
        if not account_number:
            return False, "Account number is required"
        if not sort_code:
            return False, "Sort code is required"
        
        if not self.account_regex.match(account_number):
            return False, "Account number must be 8-16 digits"
        
        if not self.sort_code_regex.match(sort_code):
            return False, "Sort code must be in format XX-XX-XX"
        
        return True, ""
    
    def validate_claim_type(self, claim_type: str) -> Tuple[bool, str]:
        """
        Validates the claim type (PPI or PACKAGED_BANK_ACCOUNT).
        Returns (is_valid, error_message)
        """
        if not claim_type:
            return False, "Claim type is required"
        if claim_type.upper() not in self.VALID_CLAIM_TYPES:
            return False, f"Claim type must be one of: {', '.join(self.VALID_CLAIM_TYPES)}"
        return True, ""
    
    def validate_claim_period(self, start_date: str, end_date: Optional[str] = None) -> Tuple[bool, str]:
        """
        Validates the claim period dates.
        Returns (is_valid, error_message)
        """
        if not start_date:
            return False, "Start date is required"
        
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            return False, "Start date must be in YYYY-MM-DD format"
        
        if end_date:
            try:
                end = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return False, "End date must be in YYYY-MM-DD format"
            
            if end < start:
                return False, "End date cannot be before start date"
        
        return True, ""
    
    def validate_ppi_claim(self, had_loan: bool, had_credit_card: bool) -> Tuple[bool, str]:
        """
        Validates PPI-specific claim requirements.
        Returns (is_valid, error_message)
        """
        if not had_loan and not had_credit_card:
            return False, "For PPI claims, you must have had either a loan or credit card"
        return True, ""
    
    def validate_pba_claim(self, monthly_fee: float, benefits_used: List[str]) -> Tuple[bool, str]:
        """
        Validates packaged bank account-specific claim requirements.
        Returns (is_valid, error_message)
        """
        if monthly_fee <= 0:
            return False, "Monthly fee must be greater than 0 for packaged bank account claims"
        if not benefits_used:
            return False, "At least one benefit must be selected for packaged bank account claims"
        return True, ""
    
    def validate_claim_form(self, form_data: Dict) -> Dict[str, List[str]]:
        """
        Validates all fields in the claim submission form.
        Returns a dictionary of error messages keyed by field name.
        """
        errors = {}
        
        # Personal details validation
        first_name_valid, first_name_error = self.validate_name(form_data.get('first_name', ''))
        if not first_name_valid:
            errors['first_name'] = [first_name_error]
        
        last_name_valid, last_name_error = self.validate_name(form_data.get('last_name', ''))
        if not last_name_valid:
            errors['last_name'] = [last_name_error]
        
        email_valid, email_error = self.validate_email(form_data.get('email', ''))
        if not email_valid:
            errors['email'] = [email_error]
        
        phone_valid, phone_error = self.validate_phone(form_data.get('phone', ''))
        if not phone_valid:
            errors['phone'] = [phone_error]
        
        postcode_valid, postcode_error = self.validate_postcode(form_data.get('postcode', ''))
        if not postcode_valid:
            errors['postcode'] = [postcode_error]
        
        dob_valid, dob_error = self.validate_date_of_birth(form_data.get('date_of_birth', ''))
        if not dob_valid:
            errors['date_of_birth'] = [dob_error]
        
        # Account details validation
        account_valid, account_error = self.validate_account_details(
            form_data.get('account_number', ''),
            form_data.get('sort_code', '')
        )
        if not account_valid:
            errors['account_number'] = [account_error]
            errors['sort_code'] = [account_error]
        
        # Claim type validation
        claim_type_valid, claim_type_error = self.validate_claim_type(form_data.get('claim_type', ''))
        if not claim_type_valid:
            errors['claim_type'] = [claim_type_error]
        else:
            claim_type = form_data['claim_type'].upper()
            
            # Claim period validation
            period_valid, period_error = self.validate_claim_period(
                form_data.get('claim
