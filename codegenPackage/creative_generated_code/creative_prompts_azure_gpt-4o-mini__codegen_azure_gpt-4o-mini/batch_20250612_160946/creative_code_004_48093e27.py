"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-ai.pages.dev
Prompt: What are the benefits of inviting friends using the Open Loot access code system in Big Time?
Generated: DETERMINISTIC_48093e279ea86e06
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OpenLootInviteSystem:
    """
    A class to manage the Open Loot access code invitation system in Big Time.
    Provides methods to invite friends and track the benefits of the invitation.
    """

    def __init__(self):
        """
        Initializes the OpenLootInviteSystem with an empty invitation list.
        """
        self.invites = []
        self.benefits = [
            "Enhanced gameplay experience for invited users.",
            "Access to exclusive in-game items and rewards.",
            "Ability to participate in special events.",
            "Strengthened social connections within the game community."
        ]

    def invite_friend(self, friend_email):
        """
        Invites a friend using their email address.

        Args:
            friend_email (str): The email address of the friend to invite.

        Raises:
            ValueError: If the email format is invalid or if the friend is already invited.
        """
        # Validate email format
        if not self.is_valid_email(friend_email):
            raise ValueError(f"Invalid email format: {friend_email}")

        # Check if the friend is already invited
        if friend_email in self.invites:
            raise ValueError(f"Friend already invited: {friend_email}")

        # Send invitation (simulated here)
        self.invites.append(friend_email)
        print(f"Invitation sent to {friend_email}!")

    def is_valid_email(self, email):
        """
        Validates the email format using a simple regex pattern.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        import re
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

    def get_benefits(self):
        """
        Returns the list of benefits of inviting friends using the Open Loot access code system.

        Returns:
            list: A list of benefits.
        """
        return self.benefits


# Example usage
if __name__ == "__main__":
    invite_system = OpenLootInviteSystem()

    try:
        invite_system.invite_friend("friend@example.com")
        benefits = invite_system.get_benefits()
        print("Benefits of inviting friends:")
        for benefit in benefits:
            print(f"- {benefit}")
    except ValueError as e:
        print(f"Error: {e}")
```
