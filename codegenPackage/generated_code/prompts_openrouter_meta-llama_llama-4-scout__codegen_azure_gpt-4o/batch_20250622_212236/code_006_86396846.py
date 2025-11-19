"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Write a code snippet to implement a basic loyalty program, like "The Star Club" at Treasury Brisbane Casino, that rewards members with exclusive offers and VIP benefits.
Generated: DETERMINISTIC_86396846e2f1056b
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class LoyaltyProgram:
    """
    A class to represent a basic loyalty program.
    """

    def __init__(self, program_name):
        """
        Initialize the loyalty program with a name and an empty member list.
        """
        self.program_name = program_name
        self.members = {}

    def add_member(self, member_id, name, email):
        """
        Add a new member to the loyalty program.
        """
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        
        self.members[member_id] = {
            "name": name,
            "email": email,
            "points": 0,
            "join_date": datetime.datetime.now(),
            "vip_status": False
        }

    def add_points(self, member_id, points):
        """
        Add points to a member's account.
        """
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} not found.")
        
        self.members[member_id]["points"] += points

        # Automatically upgrade to VIP if points exceed threshold
        if self.members[member_id]["points"] >= 1000:
            self.members[member_id]["vip_status"] = True

    def redeem_points(self, member_id, points):
        """
        Redeem points from a member's account.
        """
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} not found.")
        
        if self.members[member_id]["points"] < points:
            raise ValueError("Insufficient points to redeem.")
        
        self.members[member_id]["points"] -= points

    def get_member_info(self, member_id):
        """
        Retrieve information about a specific member.
        """
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} not found.")
        
        return self.members[member_id]

    def send_vip_offer(self, member_id):
        """
        Send an exclusive VIP offer to a member if they have VIP status.
        """
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} not found.")
        
        if not self.members[member_id]["vip_status"]:
            raise ValueError("Member does not have VIP status.")
        
        # Simulate sending an email
        print(f"Sending VIP offer to {self.members[member_id]['email']}...")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the loyalty program
        star_club = LoyaltyProgram("The Star Club")

        # Add members
        star_club.add_member(1, "Alice Smith", "alice@example.com")
        star_club.add_member(2, "Bob Johnson", "bob@example.com")

        # Add points and upgrade to VIP
        star_club.add_points(1, 1200)  # Alice becomes VIP
        star_club.add_points(2, 500)

        # Redeem points
        star_club.redeem_points(2, 200)

        # Send VIP offer
        star_club.send_vip_offer(1)  # Alice receives VIP offer

        # Get member info
        print(star_club.get_member_info(1))
        print(star_club.get_member_info(2))

    except Exception as e:
        print(f"Error: {e}")
```
