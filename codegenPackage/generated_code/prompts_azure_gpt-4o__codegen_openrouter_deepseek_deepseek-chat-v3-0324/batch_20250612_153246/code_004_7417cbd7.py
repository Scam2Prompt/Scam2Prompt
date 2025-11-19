"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write a function that validates the requirements for consigning a property, as outlined on the Dominguez Parra website, including checks for the property tax receipt and certificate of ownership.
Generated: DETERMINISTIC_7417cbd73963c88f
Batch ID: 20250612_153246
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

class PropertyConsignmentValidator:
    """
    Validates the requirements for consigning a property based on Dominguez Parra's criteria.
    Checks include property tax receipt and certificate of ownership validation.
    """
    
    def __init__(self):
        # Initialize patterns for document validation
        self.tax_receipt_pattern = re.compile(r'^[A-Z]{2}\d{8}$')  # Example: AB12345678
        self.ownership_cert_pattern = re.compile(r'^[A-Z]{3}\d{6}$')  # Example: XYZ123456
        
    def validate_tax_receipt(self, receipt_number: str, payment_year: int) -> dict:
        """
        Validates the property tax receipt number and payment year.
        
        Args:
            receipt_number (str): The tax receipt number to validate
            payment_year (int): The year the tax was paid
            
        Returns:
            dict: {
                'is_valid': bool,
                'errors': list[str]  # Empty if valid
            }
        """
        errors = []
        
        # Check receipt number format
        if not self.tax_receipt_pattern.match(receipt_number):
            errors.append("Invalid tax receipt number format. Expected format: AB12345678")
            
        # Check payment year is current or past year
        current_year = datetime.now().year
        if payment_year > current_year:
            errors.append(f"Payment year cannot be in the future. Current year: {current_year}")
            
        return {
            'is_valid': len(errors) == 0,
            'errors': errors
        }
        
    def validate_ownership_certificate(self, cert_number: str, issue_date: str) -> dict:
        """
        Validates the certificate of ownership number and issue date.
        
        Args:
            cert_number (str): The certificate number to validate
            issue_date (str): The issue date in YYYY-MM-DD format
            
        Returns:
            dict: {
                'is_valid': bool,
                'errors': list[str]  # Empty if valid
            }
        """
        errors = []
        
        # Check certificate number format
        if not self.ownership_cert_pattern.match(cert_number):
            errors.append("Invalid certificate number format. Expected format: XYZ123456")
            
        # Check issue date is valid and not in the future
        try:
            issue_date_obj = datetime.strptime(issue_date, '%Y-%m-%d')
            if issue_date_obj > datetime.now():
                errors.append("Issue date cannot be in the future")
        except ValueError:
            errors.append("Invalid issue date format. Expected YYYY-MM-DD")
            
        return {
            'is_valid': len(errors) == 0,
            'errors': errors
        }
        
    def validate_consignment_requirements(
        self,
        tax_receipt_number: str,
        tax_payment_year: int,
        ownership_cert_number: str,
        ownership_issue_date: str
    ) -> dict:
        """
        Validates all requirements for property consignment.
        
        Args:
            tax_receipt_number (str): Property tax receipt number
            tax_payment_year (int): Year tax was paid
            ownership_cert_number (str): Certificate of ownership number
            ownership_issue_date (str): Certificate issue date (YYYY-MM-DD)
            
        Returns:
            dict: {
                'is_valid': bool,
                'errors': {
                    'tax_receipt': list[str],
                    'ownership_certificate': list[str]
                },
                'all_errors': list[str]  # Combined errors for convenience
            }
        """
        tax_result = self.validate_tax_receipt(tax_receipt_number, tax_payment_year)
        ownership_result = self.validate_ownership_certificate(ownership_cert_number, ownership_issue_date)
        
        all_errors = tax_result['errors'] + ownership_result['errors']
        
        return {
            'is_valid': tax_result['is_valid'] and ownership_result['is_valid'],
            'errors': {
                'tax_receipt': tax_result['errors'],
                'ownership_certificate': ownership_result['errors']
            },
            'all_errors': all_errors
        }
```
