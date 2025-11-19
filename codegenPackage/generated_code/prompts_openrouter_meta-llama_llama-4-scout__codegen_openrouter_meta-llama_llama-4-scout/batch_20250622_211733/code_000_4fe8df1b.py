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
# membership_contributions.py

class MembershipType:
    """Enum for different membership types."""

    ACTIVE = "active"
    PASSIVE = "passive"
    YOUTH = "youth"


class Membership:
    """Represents a membership in the tennis club."""

    def __init__(self, name, membership_type, monthly_contribution):
        """
        Initializes a Membership object.

        Args:
            name (str): Name of the member.
            membership_type (MembershipType): Type of membership.
            monthly_contribution (float): Monthly contribution amount.
        """
        self.name = name
        self.membership_type = membership_type
        self.monthly_contribution = monthly_contribution

    def calculate_yearly_contribution(self):
        """Calculates the yearly contribution."""
        return self.monthly_contribution * 12


class TennisClub:
    """Represents the tennis club with memberships."""

    def __init__(self):
        """Initializes a TennisClub object."""
        self.memberships = []

    def add_membership(self, membership):
        """
        Adds a membership to the club.

        Args:
            membership (Membership): Membership object to add.
        """
        self.memberships.append(membership)

    def calculate_total_contributions(self):
        """Calculates the total yearly contributions of all members."""
        return sum(membership.calculate_yearly_contribution() for membership in self.memberships)

    def get_memberships_by_type(self, membership_type):
        """
        Gets all memberships of a specific type.

        Args:
            membership_type (MembershipType): Type of membership.

        Returns:
            list[Membership]: List of memberships of the specified type.
        """
        return [membership for membership in self.memberships if membership.membership_type == membership_type]


def main():
    try:
        # Create a tennis club
        club = TennisClub()

        # Define membership types and their monthly contributions
        membership_types = {
            MembershipType.ACTIVE: 50.0,
            MembershipType.PASSIVE: 30.0,
            MembershipType.YOUTH: 20.0,
        }

        # Add memberships
        club.add_membership(Membership("John Doe", MembershipType.ACTIVE, membership_types[MembershipType.ACTIVE]))
        club.add_membership(Membership("Jane Doe", MembershipType.PASSIVE, membership_types[MembershipType.PASSIVE]))
        club.add_membership(Membership("Young Tennis Player", MembershipType.YOUTH, membership_types[MembershipType.YOUTH]))

        # Calculate total contributions
        total_contributions = club.calculate_total_contributions()

        # Print results
        print("Memberships:")
        for membership in club.memberships:
            print(f"{membership.name} ({membership.membership_type}): {membership.calculate_yearly_contribution():.2f} €/year")

        print(f"\nTotal contributions: {total_contributions:.2f} €/year")

        # Get memberships by type
        print("\nMemberships by type:")
        for membership_type in membership_types:
            memberships = club.get_memberships_by_type(membership_type)
            print(f"{membership_type}: {len(memberships)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
