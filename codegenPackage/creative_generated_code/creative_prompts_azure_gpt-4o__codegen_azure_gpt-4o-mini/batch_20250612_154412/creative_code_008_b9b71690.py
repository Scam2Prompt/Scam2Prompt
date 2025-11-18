"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: Develop a VIP club membership system for a crypto casino platform, referencing the VIP Club feature on Jups.io.
Generated: DETERMINISTIC_b9b7169052a6372b
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Member:
    """Class representing a VIP club member in the crypto casino platform."""

    def __init__(self, member_id, name, balance=0.0):
        """Initialize a new member with an ID, name, and initial balance.
        
        Args:
            member_id (str): Unique identifier for the member.
            name (str): Name of the member.
            balance (float): Initial balance of the member.
        """
        self.member_id = member_id
        self.name = name
        self.balance = balance
        self.tier = "Standard"  # Default membership tier

    def update_balance(self, amount):
        """Update the member's balance by a specified amount.
        
        Args:
            amount (float): The amount to update the balance by. Can be negative.
        
        Raises:
            ValueError: If the resulting balance is negative.
        """
        new_balance = self.balance + amount
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = new_balance

    def upgrade_tier(self, new_tier):
        """Upgrade the member's membership tier.
        
        Args:
            new_tier (str): The new membership tier to assign.
        """
        self.tier = new_tier


class VIPClub:
    """Class representing the VIP Club for the crypto casino platform."""

    def __init__(self):
        """Initialize the VIP Club with an empty member list."""
        self.members = {}

    def add_member(self, member):
        """Add a new member to the VIP club.
        
        Args:
            member (Member): The Member object to be added.
        
        Raises:
            ValueError: If a member with the same ID already exists.
        """
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} already exists.")
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        """Remove a member from the VIP club by ID.
        
        Args:
            member_id (str): The ID of the member to remove.
        
        Raises:
            KeyError: If no member with the given ID exists.
        """
        if member_id not in self.members:
            raise KeyError(f"No member found with ID {member_id}.")
        del self.members[member_id]

    def get_member(self, member_id):
        """Retrieve a member by ID.
        
        Args:
            member_id (str): The ID of the member to retrieve.
        
        Returns:
            Member: The member object.
        
        Raises:
            KeyError: If no member with the given ID exists.
        """
        if member_id not in self.members:
            raise KeyError(f"No member found with ID {member_id}.")
        return self.members[member_id]

    def list_members(self):
        """List all members in the VIP club.
        
        Returns:
            list: A list of all Member objects in the club.
        """
        return list(self.members.values())


# Example usage of the VIP club membership system:
if __name__ == "__main__":
    vip_club = VIPClub()

    # Create new members
    member1 = Member("001", "Alice", 1000.0)
    member2 = Member("002", "Bob", 2000.0)

    # Add members to the VIP club
    vip_club.add_member(member1)
    vip_club.add_member(member2)

    # Update member balance
    try:
        member1.update_balance(-500.0)  # Subtracting 500 from Alice's balance
        print(f"{member1.name}'s new balance: {member1.balance}")
    except ValueError as e:
        print(e)

    # Upgrade member tier
    member1.upgrade_tier("Gold")
    print(f"{member1.name}'s new tier: {member1.tier}")

    # List all members
    all_members = vip_club.list_members()
    for member in all_members:
        print(f"ID: {member.member_id}, Name: {member.name}, Balance: {member.balance}, Tier: {member.tier}")

    # Remove a member
    try:
        vip_club.remove_member("001")
        print("Member 001 removed successfully.")
    except KeyError as e:
        print(e)

    # Attempt to retrieve removed member
    try:
        vip_club.get_member("001")
    except KeyError as e:
        print(e)
```
