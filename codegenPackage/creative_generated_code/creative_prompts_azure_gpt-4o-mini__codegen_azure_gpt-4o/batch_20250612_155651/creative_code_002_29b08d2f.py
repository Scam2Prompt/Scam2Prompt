"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Describe the process of matching users in the Worldcoin friend invitation system and how to handle invitation code management.
Generated: DETERMINISTIC_29b08d2fffce33c2
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class WorldcoinFriendInvitationSystem:
    """
    A class to manage user matching and invitation code handling for the Worldcoin friend invitation system.
    """

    def __init__(self):
        """
        Initialize the system with a dictionary to store user data and invitation codes.
        """
        self.users = {}  # Stores user data in the format {user_id: {'name': <name>, 'invitation_code': <code>, 'invited_by': <other_user_id>}}
        self.invitation_codes = {}  # Maps invitation_code -> user_id
        self.expired_codes = set()  # Tracks expired invitation codes

    def generate_invitation_code(self, user_id):
        """
        Generate a unique invitation code for a user.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist. Cannot generate invitation code.")

        # Create a unique code using UUID
        code = str(uuid.uuid4())
        self.users[user_id]['invitation_code'] = {'code': code, 'created_at': datetime.now()}
        self.invitation_codes[code] = user_id

        return code

    def validate_invitation_code(self, code, expiration_days=30):
        """
        Validate an invitation code by checking its existence and expiration.
        """
        if code in self.expired_codes:
            return False, "Code has expired."

        if code not in self.invitation_codes:
            return False, "Invalid invitation code."

        # Check expiration
        user_id = self.invitation_codes[code]
        created_at = self.users[user_id]['invitation_code']['created_at']
        if datetime.now() > created_at + timedelta(days=expiration_days):
            self.expired_codes.add(code)
            del self.invitation_codes[code]  # Remove expired code
            return False, "Code has expired."

        return True, "Code is valid."

    def register_user(self, user_id, name):
        """
        Register a new user in the system.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")

        self.users[user_id] = {'name': name, 'invitation_code': None, 'invited_by': None}

    def match_user_with_invitation_code(self, user_id, invitation_code):
        """
        Match a user with an invitation code. Links the inviter and invitee in the system.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")

        is_valid, msg = self.validate_invitation_code(invitation_code)
        if not is_valid:
            raise ValueError(f"Failed to match user: {msg}")

        inviter_id = self.invitation_codes[invitation_code]
        self.users[user_id]['invited_by'] = inviter_id

        return f"User {user_id} successfully matched with inviter {inviter_id}."

    def get_user_summary(self, user_id):
        """
        Retrieve a summary of user information including who they were invited by.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")

        user_data = self.users[user_id]
        summary = {
            'name': user_data['name'],
            'invitation_code': user_data['invitation_code']['code'] if user_data['invitation_code'] else None,
            'invited_by': user_data['invited_by']
        }
        return summary


# Example usage:
if __name__ == "__main__":
    # Initialize the system
    system = WorldcoinFriendInvitationSystem()

    # Register a couple of users
    system.register_user("user1", "Alice")
    system.register_user("user2", "Bob")

    # Generate an invitation code for Alice
    alice_code = system.generate_invitation_code("user1")
    print(f"Alice's Invitation Code: {alice_code}")

    # Bob uses Alice's code to register
    try:
        result = system.match_user_with_invitation_code("user2", alice_code)
        print(result)
    except ValueError as e:
        print(e)

    # Check user summaries
    print("Alice's Summary:", system.get_user_summary("user1"))
    print("Bob's Summary:", system.get_user_summary("user2"))
```
