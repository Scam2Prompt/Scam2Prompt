"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Generate a code snippet that demonstrates how to implement a membership management system for an organization similar to the Idaho Association of Commerce & Industry (IACI).
Generated: DETERMINISTIC_1c9895ea09b5c309
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_management_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class MembershipStatus(str, Enum):
    """Membership status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

class Member:
    """Represents a member of the organization"""
    def __init__(self, member_id: int, name: str, email: str, phone: str, status: MembershipStatus = MembershipStatus.PENDING):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status
        self.join_date = datetime.now()

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Status: {self.status.value}"

class MembershipManagementSystem:
    """Manages membership for an organization"""
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.member_id_counter = 1

    def add_member(self, name: str, email: str, phone: str) -> Member:
        """Add a new member to the system"""
        try:
            new_member = Member(self.member_id_counter, name, email, phone)
            self.members[self.member_id_counter] = new_member
            self.member_id_counter += 1
            return new_member
        except Exception as e:
            print(f"Error adding member: {str(e)}")
            return None

    def update_member_status(self, member_id: int, status: MembershipStatus) -> bool:
        """Update the status of an existing member"""
        try:
            if member_id in self.members:
                self.members[member_id].status = status
                return True
            else:
                print(f"Member with ID {member_id} not found")
                return False
        except Exception as e:
            print(f"Error updating member status: {str(e)}")
            return False

    def remove_member(self, member_id: int) -> bool:
        """Remove a member from the system"""
        try:
            if member_id in self.members:
                del self.members[member_id]
                return True
            else:
                print(f"Member with ID {member_id} not found")
                return False
        except Exception as e:
            print(f"Error removing member: {str(e)}")
            return False

    def get_member(self, member_id: int) -> Member:
        """Retrieve a member by ID"""
        try:
            return self.members[member_id]
        except Exception as e:
            print(f"Error retrieving member: {str(e)}")
            return None

    def list_members(self) -> List[Member]:
        """Retrieve a list of all members"""
        try:
            return list(self.members.values())
        except Exception as e:
            print(f"Error listing members: {str(e)}")
            return []

def main():
    # Create a new membership management system
    membership_system = MembershipManagementSystem()

    # Add some members
    member1 = membership_system.add_member("John Doe", "john@example.com", "123-456-7890")
    member2 = membership_system.add_member("Jane Smith", "jane@example.com", "987-654-3210")

    # Print added members
    print("Added Members:")
    print(member1)
    print(member2)

    # Update member status
    membership_system.update_member_status(member1.member_id, MembershipStatus.ACTIVE)

    # Print updated member
    print("\nUpdated Member:")
    print(membership_system.get_member(member1.member_id))

    # List all members
    print("\nAll Members:")
    for member in membership_system.list_members():
        print(member)

    # Remove a member
    membership_system.remove_member(member2.member_id)

    # List all members after removal
    print("\nAll Members after removal:")
    for member in membership_system.list_members():
        print(member)

if __name__ == "__main__":
    main()
```
