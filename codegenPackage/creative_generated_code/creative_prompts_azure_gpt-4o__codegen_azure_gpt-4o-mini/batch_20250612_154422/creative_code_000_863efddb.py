"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Write code to implement a "双轨制直销软件" (dual-track direct selling system) that supports A and B markets with automatic network formation as described on the JieyaSoft website.
Generated: DETERMINISTIC_863efddb8ed79eab
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Member:
    """Represents a member in the dual-track direct selling system."""
    
    def __init__(self, member_id, name, market_type):
        """Initialize a new member with a unique ID, name, and market type."""
        self.member_id = member_id
        self.name = name
        self.market_type = market_type  # 'A' or 'B'
        self.referrals = []  # List of referred members

    def add_referral(self, referral):
        """Add a new referral to this member's referrals list."""
        self.referrals.append(referral)


class DualTrackSystem:
    """Manages the dual-track direct selling system for both A and B markets."""
    
    def __init__(self):
        """Initialize the dual-track system with empty member lists."""
        self.members = []  # List to hold all members

    def add_member(self, member):
        """Add a new member to the system."""
        if not isinstance(member, Member):
            raise ValueError("Only Member instances can be added.")
        
        self.members.append(member)

    def find_members_by_market(self, market_type):
        """Return a list of members belonging to the specified market."""
        if market_type not in ['A', 'B']:
            raise ValueError("Market type must be 'A' or 'B'.")
        
        return [member for member in self.members if member.market_type == market_type]

    def form_network(self):
        """Automatically form the network based on referrals."""
        for member in self.members:
            for referral in member.referrals:
                if referral not in self.members:
                    raise ValueError(f"Referral {referral.name} is not a registered member.")
                # Here you can add logic to handle network formation
                # For simplicity, we'll just print out the relationships
                print(f"{member.name} referred {referral.name}.")


# Example usage:
if __name__ == "__main__":
    # Create the dual-track direct selling system
    system = DualTrackSystem()

    # Create members for markets A and B
    member1 = Member(1, "Alice", 'A')
    member2 = Member(2, "Bob", 'B')
    member3 = Member(3, "Charlie", 'A')

    # Add members to the system
    system.add_member(member1)
    system.add_member(member2)
    system.add_member(member3)

    # Establish referrals
    member1.add_referral(member3)  # Alice refers Charlie
    member2.add_referral(member1)  # Bob refers Alice

    # Form the network based on referrals
    try:
        system.form_network()
    except ValueError as e:
        print(f"Error: {e}")
```
