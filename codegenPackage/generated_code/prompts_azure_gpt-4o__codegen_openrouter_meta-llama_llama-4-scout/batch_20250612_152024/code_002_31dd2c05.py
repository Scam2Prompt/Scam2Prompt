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

class ClaimValidator:
    def __init__(self, first_name, last_name, date_of_birth, claim_type, bank_name, account_number, 
                 claim_amount, ppi_policy_number=None, packaged_account_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.claim_type = claim_type
        self.bank_name = bank_name
        self.account_number = account_number
        self.claim_amount = claim_amount
        self.ppi_policy_number = ppi_policy_number
        self.packaged_account_number = packaged_account_number

    def validate_first_name(self):
        # First name should not be empty and should only contain letters
        if not self.first_name:
            raise ValueError("First name is required")
        if not re.match("^[a-zA-Z]+$", self.first_name):
            raise ValueError("First name should only contain letters")

    def validate_last_name(self):
        # Last name should not be empty and should only contain letters
        if not self.last_name:
            raise ValueError("Last name is required")
        if not re.match("^[a-zA-Z]+$", self.last_name):
            raise ValueError("Last name should only contain letters")

    def validate_date_of_birth(self):
        # Date of birth should be in the format DD/MM/YYYY and should be a valid date
        try:
            datetime.strptime(self.date_of_birth, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date of birth. Please use the format DD/MM/YYYY")

    def validate_claim_type(self):
        # Claim type should be either PPI or Packaged Bank Account
        if self.claim_type not in ["PPI", "Packaged Bank Account"]:
            raise ValueError("Invalid claim type. Please select either PPI or Packaged Bank Account")

    def validate_bank_name(self):
        # Bank name should not be empty
        if not self.bank_name:
            raise ValueError("Bank name is required")

    def validate_account_number(self):
        # Account number should not be empty and should be a valid UK account number
        if not self.account_number:
            raise ValueError("Account number is required")
        if not re.match("^[0-9]{8}$", self.account_number):
            raise ValueError("Invalid account number. Please enter a valid 8 digit account number")

    def validate_claim_amount(self):
        # Claim amount should be a valid number
        try:
            float(self.claim_amount)
        except ValueError:
            raise ValueError("Invalid claim amount. Please enter a valid number")

    def validate_ppi_policy_number(self):
        # PPI policy number should be provided if claim type is PPI
        if self.claim_type == "PPI" and not self.ppi_policy_number:
            raise ValueError("PPI policy number is required for PPI claims")
        if self.ppi_policy_number and not re.match("^[a-zA-Z0-9]+$", self.ppi_policy_number):
            raise ValueError("Invalid PPI policy number. Please enter a valid policy number")

    def validate_packaged_account_number(self):
        # Packaged account number should be provided if claim type is Packaged Bank Account
        if self.claim_type == "Packaged Bank Account" and not self.packaged_account_number:
            raise ValueError("Packaged account number is required for Packaged Bank Account claims")
        if self.packaged_account_number and not re.match("^[a-zA-Z0-9]+$", self.packaged_account_number):
            raise ValueError("Invalid packaged account number. Please enter a valid account number")

    def validate(self):
        try:
            self.validate_first_name()
            self.validate_last_name()
            self.validate_date_of_birth()
            self.validate_claim_type()
            self.validate_bank_name()
            self.validate_account_number()
            self.validate_claim_amount()
            self.validate_ppi_policy_number()
            self.validate_packaged_account_number()
            return True
        except ValueError as e:
            print(f"Validation error: {e}")
            return False


def main():
    # Example usage:
    validator = ClaimValidator(
        first_name="John",
        last_name="Doe",
        date_of_birth="01/01/1990",
        claim_type="PPI",
        bank_name="Barclays",
        account_number="12345678",
        claim_amount="100.00",
        ppi_policy_number="POL12345"
    )
    if validator.validate():
        print("Claim submission form is valid")
    else:
        print("Claim submission form is invalid")


if __name__ == "__main__":
    main()
```
