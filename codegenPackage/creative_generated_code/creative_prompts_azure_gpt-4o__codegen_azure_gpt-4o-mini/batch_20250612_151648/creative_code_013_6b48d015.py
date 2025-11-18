"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnodeffixs.pages.dev
Prompt: Provide a solution for validating KYC information in a blockchain-based application, ensuring compliance and accuracy.
Generated: DETERMINISTIC_6b48d015e55dc0c8
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Dict, Any, Optional

class KYCValidator:
    """
    A class to validate KYC (Know Your Customer) information for 
    a blockchain-based application ensuring compliance and accuracy.
    """

    def __init__(self):
        self.valid_email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.valid_phone_regex = re.compile(r'^\+?[1-9]\d{1,14}$')  # E.164 format
        self.valid_ssn_regex = re.compile(r'^\d{3}-\d{2}-\d{4}$')  # Format: XXX-XX-XXXX

    def validate_email(self, email: str) -> bool:
        """ Validate email format. """
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        return bool(self.valid_email_regex.match(email))

    def validate_phone(self, phone: str) -> bool:
        """ Validate phone number format. """
        if not isinstance(phone, str):
            raise ValueError("Phone number must be a string.")
        return bool(self.valid_phone_regex.match(phone))

    def validate_ssn(self, ssn: str) -> bool:
        """ Validate Social Security Number format. """
        if not isinstance(ssn, str):
            raise ValueError("SSN must be a string.")
        return bool(self.valid_ssn_regex.match(ssn))

    def validate_kyc(self, kyc_info: Dict[str, Any]) -> Dict[str, Optional[str]]:
        """
        Validate KYC information.

        Parameters:
            kyc_info (dict): A dictionary containing KYC information such as 
                             'email', 'phone', and 'ssn'.

        Returns:
            dict: A dictionary containing validation results for each field with 
                  error messages if validation fails.
        """
        results = {
            'email': None,
            'phone': None,
            'ssn': None
        }

        # Validate email
        if 'email' in kyc_info:
            if self.validate_email(kyc_info['email']):
                results['email'] = 'Valid'
            else:
                results['email'] = 'Invalid email format.'

        # Validate phone
        if 'phone' in kyc_info:
            if self.validate_phone(kyc_info['phone']):
                results['phone'] = 'Valid'
            else:
                results['phone'] = 'Invalid phone number format.'

        # Validate SSN
        if 'ssn' in kyc_info:
            if self.validate_ssn(kyc_info['ssn']):
                results['ssn'] = 'Valid'
            else:
                results['ssn'] = 'Invalid SSN format.'

        return results

# Example usage
if __name__ == "__main__":
    kyc_validator = KYCValidator()

    kyc_info = {
        'email': 'example@example.com',
        'phone': '+1234567890',
        'ssn': '123-45-6789'
    }

    validation_results = kyc_validator.validate_kyc(kyc_info)
    print(validation_results)
```
