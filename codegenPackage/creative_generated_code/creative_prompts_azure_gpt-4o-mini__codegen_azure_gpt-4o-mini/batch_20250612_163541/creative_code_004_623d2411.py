"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-ie.web.app
Prompt: Explain how to integrate the Kangamoon Play To Earn mechanics into a gaming application, focusing on user rewards and NFT management.
Generated: DETERMINISTIC_623d2411f530461f
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# kangamoon_game.py

from typing import List, Dict, Any
import random
import json

# Custom exceptions for better error handling
class NFTError(Exception):
    """Exception raised for errors in the NFT management."""
    pass

class RewardError(Exception):
    """Exception raised for errors in user rewards management."""
    pass

class User:
    """Class representing a user in the gaming application."""

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.nfts: List[str] = []  # List to store NFT IDs
        self.rewards: float = 0.0  # User rewards balance

    def add_nft(self, nft_id: str) -> None:
        """Add an NFT to the user's collection."""
        self.nfts.append(nft_id)

    def remove_nft(self, nft_id: str) -> None:
        """Remove an NFT from the user's collection."""
        try:
            self.nfts.remove(nft_id)
        except ValueError:
            raise NFTError(f"NFT {nft_id} not found in user's collection.")

    def add_reward(self, amount: float) -> None:
        """Add rewards to the user's account."""
        if amount < 0:
            raise RewardError("Reward amount must be positive.")
        self.rewards += amount

    def get_rewards(self) -> float:
        """Get the total rewards of the user."""
        return self.rewards

class Game:
    """Class representing the gaming application."""

    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to manage users

    def register_user(self, user_id: str) -> None:
        """Register a new user in the game."""
        if user_id in self.users:
            raise ValueError("User already registered.")
        self.users[user_id] = User(user_id)

    def reward_user(self, user_id: str) -> None:
        """Reward the user for their in-game activities."""
        if user_id not in self.users:
            raise ValueError("User not found.")

        amount = random.uniform(1, 100)  # Random reward amount
        self.users[user_id].add_reward(amount)
        print(f"User {user_id} rewarded with {amount:.2f} tokens.")

    def mint_nft(self, user_id: str, nft_id: str) -> None:
        """Mint an NFT for the user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id].add_nft(nft_id)
        print(f"NFT {nft_id} minted for user {user_id}.")

    def serialize_data(self) -> str:
        """Serialize user data to JSON format for storage."""
        try:
            serialized_data = json.dumps({
                user_id: {
                    "nfts": user.nfts,
                    "rewards": user.get_rewards()
                } for user_id, user in self.users.items()
            })
            return serialized_data
        except Exception as e:
            raise Exception("Error serializing user data.") from e

# Example usage
if __name__ == "__main__":
    game = Game()
    
    try:
        # Register users
        game.register_user("user1")
        game.register_user("user2")
        
        # Reward users
        game.reward_user("user1")
        game.reward_user("user2")
        
        # Mint NFTs for users
        game.mint_nft("user1", "nft_001")
        game.mint_nft("user2", "nft_002")

        # Serialize user data to JSON
        data = game.serialize_data()
        print("Serialized user data:", data)

    except (ValueError, NFTError, RewardError) as e:
        print(f"An error occurred: {e}")
```
