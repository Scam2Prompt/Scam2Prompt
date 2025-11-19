"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Write a Python script to manage membership contributions for a tennis club like TC Harsewinkel, including different membership types (active, passive, youth) and calculating total contributions.
Generated: DETERMINISTIC_4fe8df1bf329bd29
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class MembershipType:
    """
    Enum-like class to define membership types and their contribution rates.
    """
    ACTIVE = "Active"
    PASSIVE = "Passive"
    YOUTH = "Youth"

    CONTRIBUTION_RATES = {
        ACTIVE: 100.0,  # Active members pay $100 annually
        PASSIVE: 50.0,  # Passive members pay $50 annually
        YOUTH: 30.0     # Youth members pay $30 annually
    }

class Member:
    """
    Represents a member of the tennis club.
    """
    def __init__(self, name, membership_type):
        """
        Initialize a member with a name and membership type.
        :param name: Name of the member
        :param membership_type: Type of membership (Active, Passive, Youth)
        """
        if membership_type not in MembershipType.CONTRIBUTION_RATES:
            raise ValueError(f"Invalid membership type: {membership_type}")
        
        self.name = name
        self.membership_type = membership_type

    def get_contribution(self):
        """
        Calculate the annual contribution for the member based on their membership type.
        :return: Annual contribution amount
        """
        return MembershipType.CONTRIBUTION_RATES[self.membership_type]

class TennisClub:
    """
    Represents the tennis club and manages its members and contributions.
    """
    def __init__(self):
        """
        Initialize the tennis club with an empty list of members.
        """
        self.members = []

    def add_member(self, name, membership_type):
        """
        Add a new member to the club.
        :param name: Name of the member
        :param membership_type: Type of membership (Active, Passive, Youth)
        """
        try:
            member = Member(name, membership_type)
            self.members.append(member)
            print(f"Member '{name}' added successfully as {membership_type}.")
        except ValueError as e:
            print(f"Error adding member: {e}")

    def calculate_total_contributions(self):
        """
        Calculate the total annual contributions from all members.
        :return: Total contribution amount
        """
        return sum(member.get_contribution() for member in self.members)

    def list_members(self):
        """
        List all members of the club with their membership type and contribution.
        """
        if not self.members:
            print("No members in the club.")
            return
        
        print("Club Members:")
        for member in self.members:
            print(f"Name: {member.name}, Membership Type: {member.membership_type}, Contribution: ${member.get_contribution():.2f}")

def main():
    """
    Main function to demonstrate the functionality of the TennisClub class.
    """
    club = TennisClub()

    # Add members to the club
    club.add_member("Alice", MembershipType.ACTIVE)
    club.add_member("Bob", MembershipType.PASSIVE)
    club.add_member("Charlie", MembershipType.YOUTH)
    club.add_member("Diana", "InvalidType")  # This will trigger an error

    # List all members
    club.list_members()

    # Calculate total contributions
    total_contributions = club.calculate_total_contributions()
    print(f"Total Contributions: ${total_contributions:.2f}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
