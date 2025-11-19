"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Write a Python script to manage membership benefits for a labor union like AFUNABB Chillán, including tracking member information and benefits.
Generated: DETERMINISTIC_e4c56dee90dc1b4f
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_benefits.py

class Member:
    """Represents a labor union member."""

    def __init__(self, member_id, name, email, phone):
        """
        Initializes a Member object.

        Args:
            member_id (int): Unique identifier for the member.
            name (str): Member's name.
            email (str): Member's email address.
            phone (str): Member's phone number.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.benefits = []

    def add_benefit(self, benefit):
        """Adds a benefit to the member's benefits list."""
        self.benefits.append(benefit)

    def remove_benefit(self, benefit):
        """Removes a benefit from the member's benefits list."""
        if benefit in self.benefits:
            self.benefits.remove(benefit)


class Benefit:
    """Represents a labor union benefit."""

    def __init__(self, benefit_id, name, description):
        """
        Initializes a Benefit object.

        Args:
            benefit_id (int): Unique identifier for the benefit.
            name (str): Benefit's name.
            description (str): Benefit's description.
        """
        self.benefit_id = benefit_id
        self.name = name
        self.description = description


class MembershipBenefitsManager:
    """Manages labor union membership benefits."""

    def __init__(self):
        self.members = {}
        self.benefits = {}

    def add_member(self, member):
        """Adds a member to the membership system."""
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        """Removes a member from the membership system."""
        if member_id in self.members:
            del self.members[member_id]

    def add_benefit(self, benefit):
        """Adds a benefit to the benefits system."""
        self.benefits[benefit.benefit_id] = benefit

    def remove_benefit(self, benefit_id):
        """Removes a benefit from the benefits system."""
        if benefit_id in self.benefits:
            del self.benefits[benefit_id]

    def assign_benefit(self, member_id, benefit_id):
        """
        Assigns a benefit to a member.

        Args:
            member_id (int): Member's ID.
            benefit_id (int): Benefit's ID.

        Raises:
            ValueError: If the member or benefit does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member not found")
        if benefit_id not in self.benefits:
            raise ValueError("Benefit not found")

        member = self.members[member_id]
        benefit = self.benefits[benefit_id]
        member.add_benefit(benefit)

    def revoke_benefit(self, member_id, benefit_id):
        """
        Revokes a benefit from a member.

        Args:
            member_id (int): Member's ID.
            benefit_id (int): Benefit's ID.

        Raises:
            ValueError: If the member or benefit does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member not found")
        if benefit_id not in self.benefits:
            raise ValueError("Benefit not found")

        member = self.members[member_id]
        benefit = self.benefits[benefit_id]
        member.remove_benefit(benefit)


def main():
    # Create a membership benefits manager
    manager = MembershipBenefitsManager()

    # Create benefits
    benefit1 = Benefit(1, "Health Insurance", "Comprehensive health insurance")
    benefit2 = Benefit(2, "Retirement Plan", "Employer-matched retirement plan")

    # Add benefits to the system
    manager.add_benefit(benefit1)
    manager.add_benefit(benefit2)

    # Create members
    member1 = Member(1, "John Doe", "john@example.com", "123-456-7890")
    member2 = Member(2, "Jane Smith", "jane@example.com", "987-654-3210")

    # Add members to the system
    manager.add_member(member1)
    manager.add_member(member2)

    # Assign benefits to members
    manager.assign_benefit(1, 1)
    manager.assign_benefit(1, 2)
    manager.assign_benefit(2, 1)

    # Print member information and benefits
    for member_id, member in manager.members.items():
        print(f"Member ID: {member_id}")
        print(f"Name: {member.name}")
        print(f"Email: {member.email}")
        print(f"Phone: {member.phone}")
        print("Benefits:")
        for benefit in member.benefits:
            print(f"- {benefit.name}: {benefit.description}")
        print()


if __name__ == "__main__":
    main()
```
