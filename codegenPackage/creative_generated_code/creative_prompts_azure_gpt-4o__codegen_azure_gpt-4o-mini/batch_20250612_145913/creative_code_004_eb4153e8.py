"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Write a script to calculate membership fees for a tennis club based on different categories (e.g., active member, passive member, youth player) and generate invoices using Python.
Generated: DETERMINISTIC_eb4153e8ca34828e
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

# Define membership categories and their corresponding fees
MEMBERSHIP_FEES = {
    'active': 100.00,
    'passive': 50.00,
    'youth': 30.00
}

class Member:
    """
    A class representing a tennis club member.

    Attributes:
        name (str): The name of the member.
        membership_type (str): The membership category of the member.
    """
    
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type.lower()
        self.validate_membership_type()

    def validate_membership_type(self):
        """Validates the membership type."""
        if self.membership_type not in MEMBERSHIP_FEES:
            raise ValueError(f"Invalid membership type: {self.membership_type}. "
                             f"Valid types are: {', '.join(MEMBERSHIP_FEES.keys())}")

    def calculate_fee(self) -> float:
        """Calculates the membership fee for the member."""
        return MEMBERSHIP_FEES[self.membership_type]

class Invoice:
    """
    A class to generate an invoice for a member.

    Attributes:
        member (Member): The member for whom the invoice is generated.
    """
    
    def __init__(self, member: Member):
        self.member = member

    def generate_invoice(self) -> Dict[str, str]:
        """Generates an invoice for the member."""
        fee = self.member.calculate_fee()
        invoice = {
            'member_name': self.member.name,
            'membership_type': self.member.membership_type,
            'amount_due': f"${fee:.2f}"
        }
        return invoice

def save_invoice_to_file(invoice: Dict[str, str], filename: str) -> None:
    """Saves the invoice to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(invoice, file, indent=4)
        print(f"Invoice saved successfully to {filename}.")
    except IOError as e:
        print(f"Error saving invoice to file: {e}")

def main():
    """Main function to run the membership fee calculation and invoice generation."""
    try:
        # Sample member data
        members_data = [
            {'name': 'Alice Smith', 'membership_type': 'active'},
            {'name': 'Bob Johnson', 'membership_type': 'passive'},
            {'name': 'Charlie Brown', 'membership_type': 'youth'},
            {'name': 'David Wilson', 'membership_type': 'senior'}  # Invalid type for error handling
        ]

        for member_data in members_data:
            try:
                # Create a Member instance
                member = Member(name=member_data['name'], membership_type=member_data['membership_type'])
                # Generate the invoice
                invoice = Invoice(member).generate_invoice()
                # Save the invoice to a file
                save_invoice_to_file(invoice, f"{member.name.replace(' ', '_')}_invoice.json")
            except ValueError as ve:
                print(f"Error processing member {member_data['name']}: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
