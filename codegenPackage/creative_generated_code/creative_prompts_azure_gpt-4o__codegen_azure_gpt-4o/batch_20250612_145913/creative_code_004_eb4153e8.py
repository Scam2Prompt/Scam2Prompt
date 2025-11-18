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
from datetime import datetime

# Membership categories and their respective annual fees
MEMBERSHIP_FEES = {
    "active_member": 300,   # Fee for active members
    "passive_member": 150,  # Fee for passive members
    "youth_player": 100     # Fee for youth players
}

class Member:
    """
    Represents a club member.
    """
    def __init__(self, name: str, category: str, email: str):
        self.name = name
        self.category = category
        self.email = email
        self.validate_category()

    def validate_category(self):
        """
        Validates if the member's category exists in the configured membership fees.
        Raises ValueError if the category is invalid.
        """
        if self.category not in MEMBERSHIP_FEES:
            raise ValueError(f"Invalid membership category: {self.category}. Must be one of {list(MEMBERSHIP_FEES.keys())}")

    def calculate_fee(self) -> int:
        """
        Calculates the membership fee for the member based on their category.
        """
        return MEMBERSHIP_FEES[self.category]

    def generate_invoice(self) -> dict:
        """
        Generates an invoice for the member.

        Returns:
            dict: Invoice details including name, email, category, fee, and date.
        """
        return {
            "name": self.name,
            "email": self.email,
            "category": self.category,
            "fee": self.calculate_fee(),
            "date": datetime.now().strftime("%Y-%m-%d")
        }


def save_invoices_to_file(invoices: list, filename: str = "invoices.json"):
    """
    Saves the list of invoices to a JSON file.
    
    Args:
        invoices (list): List of invoice dictionaries to save.
        filename (str): The name of the file to save the invoices to.
    """
    try:
        with open(filename, "w") as file:
            json.dump(invoices, file, indent=4)
        print(f"Invoices successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving invoices to file: {e}")


def main():
    """
    Main function to handle the creation of members and invoice generation.
    """
    # Sample members; in a real application, this data could come from a database or user input
    members_data = [
        {"name": "John Doe", "category": "active_member", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "category": "passive_member", "email": "jane.smith@example.com"},
        {"name": "Alex Johnson", "category": "youth_player", "email": "alex.johnson@example.com"}
    ]

    invoices = []

    for data in members_data:
        try:
            # Create a new member and generate their invoice
            member = Member(name=data["name"], category=data["category"], email=data["email"])
            invoice = member.generate_invoice()
            invoices.append(invoice)
        except ValueError as e:
            print(f"Error creating member {data['name']}: {e}")

    # Save invoices to a file
    save_invoices_to_file(invoices)


if __name__ == "__main__":
    main()
```
