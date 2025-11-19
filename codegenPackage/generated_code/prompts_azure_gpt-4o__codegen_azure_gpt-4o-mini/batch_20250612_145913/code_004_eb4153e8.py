"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Write a script to calculate membership fees for a tennis club based on different categories (e.g., active member, passive member, youth player) and generate invoices using Python.
Generated: DETERMINISTIC_eb4153e8ca34828e
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class Member:
    """Class to represent a tennis club member."""
    
    def __init__(self, name: str, member_type: str):
        """
        Initialize a new member.

        :param name: Name of the member
        :param member_type: Type of membership (active, passive, youth)
        """
        self.name = name
        self.member_type = member_type
        self.fee = self.calculate_fee()

    def calculate_fee(self) -> float:
        """
        Calculate the membership fee based on member type.

        :return: Membership fee
        """
        fees = {
            'active': 120.0,
            'passive': 80.0,
            'youth': 50.0
        }
        return fees.get(self.member_type.lower(), 0.0)

    def generate_invoice(self) -> Dict[str, str]:
        """
        Generate an invoice for the member.

        :return: Invoice details as a dictionary
        """
        return {
            'name': self.name,
            'member_type': self.member_type,
            'fee': self.fee
        }

class TennisClub:
    """Class to represent a tennis club."""
    
    def __init__(self):
        """Initialize the tennis club with an empty member list."""
        self.members: List[Member] = []

    def add_member(self, name: str, member_type: str) -> None:
        """
        Add a new member to the club.

        :param name: Name of the member
        :param member_type: Type of membership
        """
        try:
            new_member = Member(name, member_type)
            self.members.append(new_member)
            print(f"Member {name} added successfully.")
        except Exception as e:
            print(f"Error adding member: {e}")

    def generate_invoices(self) -> List[Dict[str, str]]:
        """
        Generate invoices for all members.

        :return: List of invoices
        """
        invoices = []
        for member in self.members:
            invoices.append(member.generate_invoice())
        return invoices

    def save_invoices_to_file(self, filename: str) -> None:
        """
        Save the generated invoices to a JSON file.

        :param filename: Name of the file to save invoices
        """
        try:
            invoices = self.generate_invoices()
            with open(filename, 'w') as file:
                json.dump(invoices, file, indent=4)
            print(f"Invoices saved to {filename}.")
        except IOError as e:
            print(f"Error saving invoices to file: {e}")

# Example usage
if __name__ == "__main__":
    club = TennisClub()
    club.add_member("Alice Smith", "active")
    club.add_member("Bob Johnson", "passive")
    club.add_member("Charlie Brown", "youth")
    
    # Save invoices to a file
    club.save_invoices_to_file("invoices.json")
```
