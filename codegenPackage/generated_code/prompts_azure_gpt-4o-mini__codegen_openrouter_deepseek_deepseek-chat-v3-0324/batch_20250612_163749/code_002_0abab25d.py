"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: Generate a sample Bacs payment file format that can be used with Perfect Payrolls for making electronic payments to employees and HMRC.
Generated: DETERMINISTIC_0abab25d094d1a72
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BACS Payment File Generator for Perfect Payrolls
This script generates a BACS payment file in the standard format for electronic payments
to employees and HMRC through Perfect Payrolls.

The file follows the BACS 18 format specifications.
"""

import datetime
import csv
from typing import List, Dict

class BACSPaymentGenerator:
    """
    A class to generate BACS payment files in the required format.
    """
    
    def __init__(self, company_details: Dict, payments: List[Dict]):
        """
        Initialize the generator with company and payment details.
        
        Args:
            company_details: Dictionary containing company information
                - name: Company name (max 18 chars)
                - number: Company BACS reference number (6 digits)
                - sort_code: Company bank sort code (6 digits)
                - account_number: Company bank account number (8 digits)
            payments: List of payment dictionaries
                - recipient_name: Recipient name (max 18 chars)
                - recipient_sort_code: Recipient sort code (6 digits)
                - recipient_account_number: Recipient account number (8 digits)
                - amount: Payment amount in pounds (positive float)
                - reference: Payment reference (max 18 chars)
                - payment_date: Payment date (YYYY-MM-DD)
        """
        self.company = company_details
        self.payments = payments
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Validate all inputs meet BACS requirements."""
        # Validate company details
        if len(self.company['name']) > 18:
            raise ValueError("Company name must be 18 characters or less")
        if not (len(self.company['number']) == 6 and self.company['number'].isdigit()):
            raise ValueError("Company number must be 6 digits")
        if not (len(self.company['sort_code']) == 6 and self.company['sort_code'].isdigit()):
            raise ValueError("Sort code must be 6 digits")
        if not (len(self.company['account_number']) == 8 and self.company['account_number'].isdigit()):
            raise ValueError("Account number must be 8 digits")
            
        # Validate each payment
        for payment in self.payments:
            if len(payment['recipient_name']) > 18:
                raise ValueError(f"Recipient name '{payment['recipient_name']}' exceeds 18 chars")
            if not (len(payment['recipient_sort_code']) == 6 and payment['recipient_sort_code'].isdigit()):
                raise ValueError(f"Invalid sort code for {payment['recipient_name']}")
            if not (len(payment['recipient_account_number']) == 8 and payment['recipient_account_number'].isdigit()):
                raise ValueError(f"Invalid account number for {payment['recipient_name']}")
            if payment['amount'] <= 0:
                raise ValueError(f"Invalid amount for {payment['recipient_name']}")
            if len(payment['reference']) > 18:
                raise ValueError(f"Reference '{payment['reference']}' exceeds 18 chars")
                
    def generate_file(self, filename: str):
        """
        Generate the BACS payment file.
        
        Args:
            filename: Output filename for the BACS file
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
            
            # Volume Header
            writer.writerow([
                'VOL1',
                '1',  # Volume number
                '0',  # Not used
                self.company['name'].ljust(18),
                datetime.datetime.now().strftime('%d%m%y')
            ])
            
            # Header Label
            writer.writerow([
                'HDR1',
                'A',  # Standard label
                '01',  # File type (01 for payments)
                self.company['name'].ljust(18),
                '0',  # Not used
                self.company['number'],
                '1',  # Processing day (1-7)
                datetime.datetime.now().strftime('%d%m%y')
            ])
            
            # User Header
            writer.writerow([
                'UHL1',
                '01',  # File type
                '0',  # Not used
                self.company['name'].ljust(18),
                '0',  # Not used
                self.company['number'],
                '0',  # Not used
                datetime.datetime.now().strftime('%d%m%y'),
                '0'  # Not used
            ])
            
            # Company Header
            writer.writerow([
                'CDR1',
                '01',  # File type
                '0',  # Not used
                self.company['name'].ljust(18),
                self.company['number'],
                self.company['sort_code'],
                self.company['account_number'],
                '0',  # Not used
                datetime.datetime.now().strftime('%d%m%y'),
                '0'  # Not used
            ])
            
            # Payment Records
            total_amount = 0
            for payment in self.payments:
                amount_pence = int(payment['amount'] * 100)
                total_amount += amount_pence
                
                writer.writerow([
                    'PDT1',
                    '01',  # File type
                    '0',  # Not used
                    payment['recipient_name'].ljust(18),
                    payment['recipient_sort_code'],
                    payment['recipient_account_number'],
                    '0',  # Not used
                    str(amount_pence).zfill(10),
                    payment['reference'].ljust(18),
                    '0',  # Not used
                    payment['payment_date'].replace('-', ''),
                    '0'  # Not used
                ])
            
            # Company Trailer
            writer.writerow([
                'CTR1',
                '01',  # File type
                str(len(self.payments)).zfill(6),  # Number of transactions
                str(total_amount).zfill(12),  # Total amount in pence
                '0',  # Not used
                '0',  # Not used
                '0'  # Not used
            ])
            
            # User Trailer
            writer.writerow([
                'UTL1',
                '01',  # File type
                str(len(self.payments)).zfill(6),  # Number of transactions
                str(total_amount).zfill(12),  # Total amount in pence
                '0',  # Not used
                '0',  # Not used
                '0'  # Not used
            ])
            
            # EOF Marker
            writer.writerow(['EOF1'])

# Example usage
if __name__ == "__main__":
    company = {
        'name': 'ACME LTD',
        'number': '123456',
        'sort_code': '112233',
        'account_number': '12345678'
    }
    
    payments = [
        {
            'recipient_name': 'JOHN SMITH',
            'recipient_sort_code': '445566',
            'recipient_account_number': '87654321',
            'amount': 1250.50,
            'reference': 'SALARY JAN',
            'payment_date': '2023-01-28'
        },
        {
            'recipient_name': 'HMRC',
            'recipient_sort_code': '083210',
            'recipient_account_number': '12001039',
            'amount': 3500.00,
            'reference': 'TAX JAN',
            'payment_date': '2023-01-28'
        }
    ]
    
    generator = BACSPaymentGenerator(company, payments)
    generator.generate_file('bacspayments.txt')
```
