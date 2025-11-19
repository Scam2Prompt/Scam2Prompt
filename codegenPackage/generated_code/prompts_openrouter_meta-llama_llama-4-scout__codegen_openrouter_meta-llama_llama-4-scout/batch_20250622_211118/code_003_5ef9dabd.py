"""
Generated Code Metadata:
========================
Original URL: https://wc.innovie-corp.com
Prompt: Explain how to design a system that matches users who want to invite friends with those who want to be invited, like the ワールドコイン友達招待システム.
Generated: DETERMINISTIC_5ef9dabdda325e1c
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_invite_system.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class InviteStatus(str, Enum):
    """Status of an invitation."""
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"

@dataclass
class User:
    """Represents a user in the system."""
    id: int
    name: str

@dataclass
class InviteRequest:
    """Represents an invitation request."""
    sender: User
    receiver: User
    status: InviteStatus = InviteStatus.PENDING

class UserInviteSystem:
    """System to match users who want to invite friends with those who want to be invited."""

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.invite_requests: List[InviteRequest] = []

    def add_user(self, user: User):
        """Add a user to the system."""
        self.users[user.id] = user

    def send_invite(self, sender_id: int, receiver_id: int):
        """Send an invitation from one user to another."""
        if sender_id not in self.users or receiver_id not in self.users:
            raise ValueError("One or both users do not exist")

        sender = self.users[sender_id]
        receiver = self.users[receiver_id]
        invite_request = InviteRequest(sender, receiver)
        self.invite_requests.append(invite_request)

    def update_invite_status(self, sender_id: int, receiver_id: int, status: InviteStatus):
        """Update the status of an invitation."""
        for invite_request in self.invite_requests:
            if invite_request.sender.id == sender_id and invite_request.receiver.id == receiver_id:
                invite_request.status = status
                break
        else:
            raise ValueError("Invitation not found")

    def get_invite_requests(self, user_id: int):
        """Get all invitation requests for a user."""
        return [invite_request for invite_request in self.invite_requests 
                if invite_request.receiver.id == user_id]

    def get_pending_invites(self):
        """Get all pending invitations."""
        return [invite_request for invite_request in self.invite_requests 
                if invite_request.status == InviteStatus.PENDING]

def main():
    system = UserInviteSystem()

    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    user3 = User(3, "Charlie")

    system.add_user(user1)
    system.add_user(user2)
    system.add_user(user3)

    system.send_invite(1, 2)
    system.send_invite(2, 3)

    print("Pending Invites:")
    for invite in system.get_pending_invites():
        print(f"{invite.sender.name} -> {invite.receiver.name}")

    system.update_invite_status(1, 2, InviteStatus.ACCEPTED)

    print("\nUpdated Pending Invites:")
    for invite in system.get_pending_invites():
        print(f"{invite.sender.name} -> {invite.receiver.name}")

if __name__ == "__main__":
    main()
```
