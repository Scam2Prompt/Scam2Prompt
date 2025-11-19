"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Write a Python script that allows users to invite friends to a coin-collecting game and track their progress.
Generated: DETERMINISTIC_637c0fc07215672a
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class FriendInvitationSystem:
    """
    A system to manage friend invitations and track coin collection progress.
    """
    
    def __init__(self, data_file: str = "game_data.json"):
        """
        Initialize the system with a data file.
        
        Args:
            data_file: Path to the JSON file storing game data.
        """
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """
        Load game data from JSON file or create new if file doesn't exist.
        
        Returns:
            Dictionary containing game data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
        
        return {
            "users": {},
            "invitations": {},
            "coin_progress": {}
        }
    
    def _save_data(self) -> None:
        """
        Save game data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def register_user(self, user_id: str, username: str) -> bool:
        """
        Register a new user in the system.
        
        Args:
            user_id: Unique identifier for the user.
            username: Display name for the user.
            
        Returns:
            True if registration was successful, False otherwise.
        """
        if user_id in self.data["users"]:
            print(f"User {user_id} already exists.")
            return False
        
        self.data["users"][user_id] = username
        self.data["coin_progress"][user_id] = 0
        self._save_data()
        return True
    
    def invite_friend(self, inviter_id: str, invitee_id: str) -> bool:
        """
        Send an invitation from one user to another.
        
        Args:
            inviter_id: ID of the user sending the invitation.
            invitee_id: ID of the user receiving the invitation.
            
        Returns:
            True if invitation was sent successfully, False otherwise.
        """
        if inviter_id not in self.data["users"]:
            print(f"Inviter {inviter_id} not found.")
            return False
        
        if invitee_id not in self.data["users"]:
            print(f"Invitee {invitee_id} not found.")
            return False
        
        if invitee_id in self.data["invitations"].get(inviter_id, []):
            print(f"Invitation already sent to {invitee_id}.")
            return False
        
        if inviter_id not in self.data["invitations"]:
            self.data["invitations"][inviter_id] = []
        
        self.data["invitations"][inviter_id].append(invitee_id)
        self._save_data()
        return True
    
    def accept_invitation(self, inviter_id: str, invitee_id: str) -> bool:
        """
        Accept an invitation from another user.
        
        Args:
            inviter_id: ID of the user who sent the invitation.
            invitee_id: ID of the user accepting the invitation.
            
        Returns:
            True if invitation was accepted successfully, False otherwise.
        """
        if inviter_id not in self.data["invitations"]:
            print(f"No invitations found from {inviter_id}.")
            return False
        
        if invitee_id not in self.data["invitations"][inviter_id]:
            print(f"No invitation found from {inviter_id} to {invitee_id}.")
            return False
        
        self.data["invitations"][inviter_id].remove(invitee_id)
        
        # Add to each other's friend lists
        if "friends" not in self.data:
            self.data["friends"] = {}
        
        if inviter_id not in self.data["friends"]:
            self.data["friends"][inviter_id] = []
        if invitee_id not in self.data["friends"]:
            self.data["friends"][invitee_id] = []
        
        if invitee_id not in self.data["friends"][inviter_id]:
            self.data["friends"][inviter_id].append(invitee_id)
        if inviter_id not in self.data["friends"][invitee_id]:
            self.data["friends"][invitee_id].append(inviter_id)
        
        self._save_data()
        return True
    
    def update_coin_progress(self, user_id: str, coins: int) -> bool:
        """
        Update a user's coin collection progress.
        
        Args:
            user_id: ID of the user to update.
            coins: Number of coins collected.
            
        Returns:
            True if update was successful, False otherwise.
        """
        if user_id not in self.data["users"]:
            print(f"User {user_id} not found.")
            return False
        
        self.data["coin_progress"][user_id] = coins
        self._save_data()
        return True
    
    def get_friend_progress(self, user_id: str) -> Optional[Dict[str, int]]:
        """
        Get coin progress for all friends of a user.
        
        Args:
            user_id: ID of the user whose friends to check.
            
        Returns:
            Dictionary mapping friend usernames to their coin counts,
            or None if user has no friends or doesn't exist.
        """
        if user_id not in self.data.get("friends", {}):
            return None
        
        friend_progress = {}
        for friend_id in self.data["friends"][user_id]:
            if friend_id in self.data["coin_progress"]:
                friend_progress[self.data["users"][friend_id]] = self.data["coin_progress"][friend_id]
        
        return friend_progress
    
    def get_pending_invitations(self, user_id: str) -> Optional[List[str]]:
        """
        Get pending invitations sent to a user.
        
        Args:
            user_id: ID of the user to check invitations for.
            
        Returns:
            List of usernames who sent invitations to this user,
            or None if no invitations exist.
        """
        pending_inviters = []
        for inviter_id, invitees in self.data["invitations"].items():
            if user_id in invitees:
                pending_inviters.append(self.data["users"][inviter_id])
        
        return pending_inviters if pending_inviters else None


def main():
    """Example usage of the FriendInvitationSystem."""
    game = FriendInvitationSystem()
    
    # Register users
    game.register_user("user1", "Alice")
    game.register_user("user2", "Bob")
    game.register_user("user3", "Charlie")
    
    # Send invitations
    game.invite_friend("user1", "user2")
    game.invite_friend("user1", "user3")
    
    # Accept invitations
    game.accept_invitation("user1", "user2")
    
    # Update coin progress
    game.update_coin_progress("user1", 50)
    game.update_coin_progress("user2", 30)
    game.update_coin_progress("user3", 10)
    
    # Check friend progress
    print("Alice's friends progress:", game.get_friend_progress("user1"))
    print("Bob's friends progress:", game.get_friend_progress("user2"))
    
    # Check pending invitations
    print("Charlie's pending invitations:", game.get_pending_invitations("user3"))


if __name__ == "__main__":
    main()
```
