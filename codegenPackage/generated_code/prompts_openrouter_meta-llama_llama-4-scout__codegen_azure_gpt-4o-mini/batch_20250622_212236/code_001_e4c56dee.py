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
import json
from typing import List, Dict, Any

class Member:
    """Class to represent a union member."""
    
    def __init__(self, member_id: int, name: str, email: str, benefits: List[str]):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.benefits = benefits

    def to_dict(self) -> Dict[str, Any]:
        """Convert member information to a dictionary."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "benefits": self.benefits
        }

class MembershipManager:
    """Class to manage union membership and benefits."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.members: List[Member] = self.load_members()

    def load_members(self) -> List[Member]:
        """Load members from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                members_data = json.load(file)
                return [Member(**data) for data in members_data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the data file.")
            return []

    def save_members(self) -> None:
        """Save members to a JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump([member.to_dict() for member in self.members], file, indent=4)
        except IOError as e:
            print(f"Error: Could not write to file {self.data_file}. {e}")

    def add_member(self, member: Member) -> None:
        """Add a new member to the membership list."""
        self.members.append(member)
        self.save_members()

    def remove_member(self, member_id: int) -> None:
        """Remove a member from the membership list by ID."""
        self.members = [member for member in self.members if member.member_id != member_id]
        self.save_members()

    def get_member(self, member_id: int) -> Member:
        """Retrieve a member by ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise ValueError(f"Member with ID {member_id} not found.")

    def list_members(self) -> List[Dict[str, Any]]:
        """List all members and their benefits."""
        return [member.to_dict() for member in self.members]

def main():
    """Main function to manage membership benefits."""
    manager = MembershipManager('members.json')

    # Example usage
    try:
        # Adding a new member
        new_member = Member(member_id=1, name="John Doe", email="john.doe@example.com", benefits=["Health Insurance", "Pension Plan"])
        manager.add_member(new_member)

        # Listing all members
        members = manager.list_members()
        print("Current Members:")
        for member in members:
            print(member)

        # Removing a member
        manager.remove_member(1)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
