"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Develop a use case for implementing Proof of Commitment DAOs in a sports league or book club setting, focusing on how it enhances member engagement and commitment.
Generated: DETERMINISTIC_1ee079a9bf44324a
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime
from typing import List, Dict, Any

class Member:
    """Class representing a member of the DAO."""
    
    def __init__(self, name: str):
        self.name = name
        self.commitments = []  # List to store commitments made by the member

    def make_commitment(self, commitment: str):
        """Method for a member to make a commitment."""
        self.commitments.append({
            'commitment': commitment,
            'timestamp': datetime.now()
        })

    def get_commitments(self) -> List[Dict[str, Any]]:
        """Retrieve all commitments made by the member."""
        return self.commitments


class DAO:
    """Class representing the Proof of Commitment DAO."""
    
    def __init__(self):
        self.members = {}  # Dictionary to store members by name

    def add_member(self, member_name: str):
        """Add a new member to the DAO."""
        if member_name in self.members:
            raise ValueError(f"Member '{member_name}' already exists.")
        self.members[member_name] = Member(member_name)

    def make_commitment(self, member_name: str, commitment: str):
        """Allow a member to make a commitment."""
        if member_name not in self.members:
            raise ValueError(f"Member '{member_name}' does not exist.")
        self.members[member_name].make_commitment(commitment)

    def get_member_commitments(self, member_name: str) -> List[Dict[str, Any]]:
        """Retrieve commitments for a specific member."""
        if member_name not in self.members:
            raise ValueError(f"Member '{member_name}' does not exist.")
        return self.members[member_name].get_commitments()

    def get_all_commitments(self) -> Dict[str, List[Dict[str, Any]]]:
        """Retrieve commitments for all members."""
        return {member_name: member.get_commitments() for member_name, member in self.members.items()}


# Example usage
if __name__ == "__main__":
    try:
        # Create a new DAO instance
        sports_league_dao = DAO()

        # Add members to the DAO
        sports_league_dao.add_member("Alice")
        sports_league_dao.add_member("Bob")

        # Members make commitments
        sports_league_dao.make_commitment("Alice", "Attend the next game.")
        sports_league_dao.make_commitment("Bob", "Organize a book discussion.")

        # Retrieve and print commitments
        print("Alice's Commitments:", sports_league_dao.get_member_commitments("Alice"))
        print("Bob's Commitments:", sports_league_dao.get_member_commitments("Bob"))

        # Print all commitments in the DAO
        print("All Commitments:", sports_league_dao.get_all_commitments())

    except ValueError as e:
        print(f"Error: {e}")
```
