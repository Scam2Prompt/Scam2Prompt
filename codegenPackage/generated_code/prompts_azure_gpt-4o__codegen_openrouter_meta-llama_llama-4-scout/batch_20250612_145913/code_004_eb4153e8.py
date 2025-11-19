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
# membership_fees.py

class MembershipCategory:
    """Base class for membership categories."""

    def __init__(self, name, fee):
        """
        Initialize a membership category.

        Args:
            name (str): Category name.
            fee (float): Membership fee.
        """
        self.name = name
        self.fee = fee


class ActiveMember(MembershipCategory):
    """Active member category."""

    def __init__(self):
        super().__init__("Active Member", 100.0)


class PassiveMember(MembershipCategory):
    """Passive member category."""

    def __init__(self):
        super().__init__("Passive Member", 50.0)


class YouthPlayer(MembershipCategory):
    """Youth player category."""

    def __init__(self):
        super().__init__("Youth Player", 20.0)


class Member:
    """Member class."""

    def __init__(self, name, category, email):
        """
        Initialize a member.

        Args:
            name (str): Member name.
            category (MembershipCategory): Membership category.
            email (str): Member email.
        """
        self.name = name
        self.category = category
        self.email = email

    def calculate_fee(self):
        """Calculate membership fee."""
        return self.category.fee


class Invoice:
    """Invoice class."""

    def __init__(self, member, payment_method):
        """
        Initialize an invoice.

        Args:
            member (Member): Member object.
            payment_method (str): Payment method.
        """
        self.member = member
        self.payment_method = payment_method
        self.fee = member.calculate_fee()

    def generate_invoice(self):
        """Generate invoice."""
        invoice_text = f"Invoice for {self.member.name}\n"
        invoice_text += f"Category: {self.member.category.name}\n"
        invoice_text += f"Fee: ${self.fee:.2f}\n"
        invoice_text += f"Payment Method: {self.payment_method}\n"
        return invoice_text


def main():
    try:
        # Create membership categories
        active_member_category = ActiveMember()
        passive_member_category = PassiveMember()
        youth_player_category = YouthPlayer()

        # Create members
        member1 = Member("John Doe", active_member_category, "john@example.com")
        member2 = Member("Jane Doe", passive_member_category, "jane@example.com")
        member3 = Member("Youth Player", youth_player_category, "youth@example.com")

        # Generate invoices
        invoice1 = Invoice(member1, "Credit Card")
        invoice2 = Invoice(member2, "Bank Transfer")
        invoice3 = Invoice(member3, "Cash")

        # Print invoices
        print(invoice1.generate_invoice())
        print("\n")
        print(invoice2.generate_invoice())
        print("\n")
        print(invoice3.generate_invoice())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
