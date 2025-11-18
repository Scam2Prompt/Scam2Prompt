"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: Write code to validate and prepare tax refund documentation based on Yehudit Benedict's professional approach to quick and accurate submissions.
Generated: DETERMINISTIC_2bc569656f860fa6
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class TaxRefundProcessor:
    """
    Class to validate and prepare tax refund documentation.
    """

    def __init__(self, taxpayer_name: str, taxpayer_id: str, income: float, tax_paid: float):
        self.taxpayer_name = taxpayer_name
        self.taxpayer_id = taxpayer_id
        self.income = income
        self.tax_paid = tax_paid

    def validate_inputs(self) -> bool:
        """
        Validates user inputs for correctness.
        :return: True if all validations pass, False otherwise.
        """
        # Validate taxpayer name (non-empty and alphabetic)
        if not self.taxpayer_name or not self.taxpayer_name.replace(" ", "").isalpha():
            print("Invalid taxpayer name. Must be non-empty and contain only alphabetic characters.")
            return False

        # Validate taxpayer ID (must match a specific format, e.g., XXXXX-XXXXX)
        if not re.match(r"^\d{5}-\d{5}$", self.taxpayer_id):
            print("Invalid taxpayer ID. Must match the format XXXXX-XXXXX (digits only).")
            return False

        # Validate income (must be a non-negative number)
        if self.income < 0:
            print("Income cannot be negative.")
            return False

        # Validate tax paid (must be a non-negative number)
        if self.tax_paid < 0:
            print("Tax paid cannot be negative.")
            return False

        return True

    def calculate_tax_refund(self) -> float:
        """
        Calculates the tax refund based on a fixed tax rate.
        :return: The calculated refund amount.
        """
        # Define a fixed tax rate (e.g., 20%)
        TAX_RATE = 0.20

        # Calculate expected tax
        expected_tax = self.income * TAX_RATE

        # Calculate refund (if tax paid exceeds expected tax)
        refund = self.tax_paid - expected_tax

        # If the refund is negative, set it to 0 (no refund owed)
        return max(refund, 0)

    def prepare_documentation(self) -> dict:
        """
        Prepares the refund documentation for submission.
        :return: A dictionary containing the documentation details.
        """
        # Validate inputs first
        if not self.validate_inputs():
            raise ValueError("Validation failed. Cannot prepare documentation.")

        # Calculate refund
        refund = self.calculate_tax_refund()

        # Prepare documentation
        return {
            "Taxpayer Name": self.taxpayer_name,
            "Taxpayer ID": self.taxpayer_id,
            "Income": self.income,
            "Tax Paid": self.tax_paid,
            "Tax Refund": refund,
            "Submission Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# Example usage:
if __name__ == "__main__":
    try:
        # User inputs (replace with actual data in production)
        taxpayer_name = "Yehudit Benedict"
        taxpayer_id = "12345-67890"
        income = 50000.00
        tax_paid = 12000.00

        # Initialize processor
        processor = TaxRefundProcessor(taxpayer_name, taxpayer_id, income, tax_paid)

        # Prepare documentation
        documentation = processor.prepare_documentation()

        # Print documentation for review
        print("Tax Refund Documentation:")
        for key, value in documentation.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")
```
