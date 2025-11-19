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
class Membership:
    """Class to represent a membership in the tennis club."""
    
    def __init__(self, member_type, contribution):
        """
        Initialize a new membership.

        Args:
            member_type (str): Type of membership ('active', 'passive', 'youth').
            contribution (float): Annual contribution amount for the membership type.
        """
        self.member_type = member_type
        self.contribution = contribution

    def __str__(self):
        """Return a string representation of the membership."""
        return f"{self.member_type.capitalize()} Membership: ${self.contribution:.2f}"


class TennisClub:
    """Class to manage memberships and contributions for the tennis club."""
    
    def __init__(self):
        """Initialize the Tennis Club with an empty membership list."""
        self.memberships = []

    def add_membership(self, member_type, contribution):
        """
        Add a new membership to the club.

        Args:
            member_type (str): Type of membership ('active', 'passive', 'youth').
            contribution (float): Annual contribution amount for the membership type.
        """
        if member_type not in ['active', 'passive', 'youth']:
            raise ValueError("Invalid membership type. Must be 'active', 'passive', or 'youth'.")
        if contribution < 0:
            raise ValueError("Contribution must be a non-negative value.")

        new_membership = Membership(member_type, contribution)
        self.memberships.append(new_membership)

    def total_contributions(self):
        """Calculate the total contributions from all memberships."""
        total = sum(membership.contribution for membership in self.memberships)
        return total

    def display_memberships(self):
        """Display all memberships and their contributions."""
        if not self.memberships:
            print("No memberships found.")
            return
        
        print("Membership Contributions:")
        for membership in self.memberships:
            print(membership)


def main():
    """Main function to run the Tennis Club membership management."""
    club = TennisClub()

    # Example memberships
    try:
        club.add_membership('active', 300.00)
        club.add_membership('passive', 150.00)
        club.add_membership('youth', 100.00)

        # Display memberships
        club.display_memberships()

        # Calculate and display total contributions
        total = club.total_contributions()
        print(f"Total Contributions: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
