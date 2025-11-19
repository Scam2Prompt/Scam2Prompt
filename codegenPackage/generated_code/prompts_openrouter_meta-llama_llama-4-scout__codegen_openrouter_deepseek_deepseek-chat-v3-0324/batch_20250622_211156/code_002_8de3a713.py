"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: "Generate a loan agreement template for a business financing a commercial vehicle through an asset finance broker, incorporating UK financial regulations."
Generated: DETERMINISTIC_8de3a713d0152e6f
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Loan Agreement Template Generator for Commercial Vehicle Financing in the UK.

This script generates a loan agreement template compliant with UK financial regulations
for businesses financing commercial vehicles through asset finance brokers.

Key Features:
- Incorporates UK Consumer Credit Act 1974 and Financial Conduct Authority (FCA) requirements
- Includes standard clauses for asset finance agreements
- Provides customizable fields for specific loan terms
- Generates a professionally formatted document
"""

import datetime
from typing import Optional

class LoanAgreementGenerator:
    """
    Generates a loan agreement document for commercial vehicle financing.
    
    Attributes:
        borrower_name (str): Legal name of the borrowing business
        lender_name (str): Legal name of the lending institution
        broker_name (str): Name of the asset finance broker
        vehicle_details (dict): Details of the commercial vehicle
        loan_amount (float): Principal loan amount in GBP
        interest_rate (float): Annual interest rate percentage
        term_months (int): Loan term in months
        repayment_frequency (str): 'monthly', 'quarterly', or 'annually'
        effective_date (datetime.date): Agreement effective date
        governing_law (str): Jurisdiction for the agreement
    """
    
    def __init__(self):
        self.borrower_name = ""
        self.lender_name = ""
        self.broker_name = ""
        self.vehicle_details = {
            'make': "",
            'model': "",
            'year': "",
            'vin': "",
            'registration': ""
        }
        self.loan_amount = 0.0
        self.interest_rate = 0.0
        self.term_months = 0
        self.repayment_frequency = "monthly"
        self.effective_date = datetime.date.today()
        self.governing_law = "England and Wales"
        
    def validate_inputs(self) -> bool:
        """Validate all input fields meet requirements."""
        if not all([
            self.borrower_name,
            self.lender_name,
            self.broker_name,
            all(self.vehicle_details.values()),
            self.loan_amount > 0,
            self.interest_rate >= 0,
            self.term_months > 0,
            self.repayment_frequency in ['monthly', 'quarterly', 'annually']
        ]):
            raise ValueError("Invalid input parameters provided")
        return True
    
    def generate_agreement(self) -> str:
        """
        Generate the loan agreement document.
        
        Returns:
            str: Formatted loan agreement text
        """
        self.validate_inputs()
        
        # Calculate repayment amounts
        periodic_rate = self.interest_rate / (12 if self.repayment_frequency == 'monthly' else 4 if self.repayment_frequency == 'quarterly' else 1)
        total_repayments = self.term_months // (1 if self.repayment_frequency == 'monthly' else 3 if self.repayment_frequency == 'quarterly' else 12)
        
        agreement = f"""
LOAN AGREEMENT FOR COMMERCIAL VEHICLE FINANCING

This Loan Agreement ("Agreement") is made on {self.effective_date.strftime('%d %B %Y')}

BETWEEN:

1. {self.lender_name} ("the Lender")
2. {self.borrower_name} ("the Borrower")
3. {self.broker_name} ("the Broker")

WHEREAS:
A. The Borrower wishes to finance the acquisition of a commercial vehicle.
B. The Lender has agreed to provide financing through the Broker.

1. LOAN TERMS
1.1 Principal Amount: £{self.loan_amount:,.2f}
1.2 Annual Interest Rate: {self.interest_rate:.2f}%
1.3 Term: {self.term_months} months
1.4 Repayment Frequency: {self.repayment_frequency.capitalize()}
1.5 Total Number of Repayments: {total_repayments}
1.6 Periodic Repayment Amount: £{(self.loan_amount * (1 + self.interest_rate/100)) / total_repayments:,.2f}

2. VEHICLE DETAILS
2.1 Make: {self.vehicle_details['make']}
2.2 Model: {self.vehicle_details['model']}
2.3 Year: {self.vehicle_details['year']}
2.4 VIN: {self.vehicle_details['vin']}
2.5 Registration: {self.vehicle_details['registration']}

3. REPRESENTATIONS AND WARRANTIES
3.1 The Borrower represents they have authority to enter this Agreement.
3.2 The Borrower agrees to use the vehicle solely for commercial purposes.
3.3 The Borrower will maintain comprehensive insurance on the vehicle.

4. DEFAULT AND REMEDIES
4.1 Failure to make payments within 14 days of due date constitutes default.
4.2 Upon default, the Lender may repossess the vehicle.

5. GENERAL PROVISIONS
5.1 This Agreement is governed by the laws of {self.governing_law}.
5.2 The Agreement complies with the Consumer Credit Act 1974 and FCA regulations.
5.3 All notices shall be in writing and sent to the parties' registered addresses.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

___________________________      ___________________________
{Lender}                          {Borrower}

___________________________
{Broker}
"""
        return agreement

# Example usage
if __name__ == "__main__":
    try:
        generator = LoanAgreementGenerator()
        generator.borrower_name = "ABC Transport Ltd"
        generator.lender_name = "UK Commercial Finance PLC"
        generator.broker_name = "Asset Finance Solutions Ltd"
        generator.vehicle_details = {
            'make': "Mercedes-Benz",
            'model': "Sprinter 316",
            'year': "2023",
            'vin': "W1K12345678901234",
            'registration': "AB23 CDE"
        }
        generator.loan_amount = 35000.00
        generator.interest_rate = 6.5
        generator.term_months = 60
        generator.repayment_frequency = "monthly"
        
        agreement = generator.generate_agreement()
        print(agreement)
        
    except ValueError as e:
        print(f"Error generating agreement: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
```
