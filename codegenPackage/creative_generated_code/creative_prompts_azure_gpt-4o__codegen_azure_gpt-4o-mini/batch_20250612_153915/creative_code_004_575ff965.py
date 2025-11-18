"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruletonka.xyz
Prompt: Write Python code to simulate a TON reward system where users can receive notifications in USDT or NFTs and claim rewards by connecting their wallets.
Generated: DETERMINISTIC_575ff965b6d0aeb9
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, Union, List, Optional

class User:
    """Class representing a user in the reward system."""
    def __init__(self, username: str):
        self.username = username
        self.wallet_connected = False
        self.reward_balance: Dict[str, float] = {"USDT": 0.0, "NFTs": 0}
    
    def connect_wallet(self):
        """Simulate connecting a wallet."""
        self.wallet_connected = True
        print(f"{self.username}'s wallet connected successfully.")
        
    def disconnect_wallet(self):
        """Simulate disconnecting a wallet."""
        self.wallet_connected = False
        print(f"{self.username}'s wallet disconnected.")

class RewardSystem:
    """Class representing the reward system."""
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str) -> User:
        """Add a new user to the reward system."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        
        user = User(username)
        self.users[username] = user
        return user
    
    def notify_user(self, username: str, reward_type: str, amount: Union[float, int]) -> None:
        """Notify a user of a reward."""
        if username not in self.users:
            raise ValueError(f"User '{username}' not found.")
        
        user = self.users[username]
        
        if reward_type == "USDT":
            user.reward_balance["USDT"] += amount
            print(f"User '{username}' notified of {amount} USDT reward.")
        elif reward_type == "NFTs":
            user.reward_balance["NFTs"] += amount
            print(f"User '{username}' notified of {amount} NFTs reward.")
        else:
            raise ValueError(f"Unknown reward type: {reward_type}")
    
    def claim_rewards(self, username: str) -> Optional[str]:
        """Allow user to claim rewards if their wallet is connected."""
        if username not in self.users:
            raise ValueError(f"User '{username}' not found.")
        
        user = self.users[username]
        
        if not user.wallet_connected:
            return "Wallet not connected. Please connect your wallet to claim rewards."
        
        claimed_rewards = user.reward_balance
        user.reward_balance = {"USDT": 0.0, "NFTs": 0}
        
        return f"Claimed rewards for {username}: {claimed_rewards}"

# Example of using the RewardSystem
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Add users to the system
    alice = reward_system.add_user("Alice")
    bob = reward_system.add_user("Bob")
    
    # Connect wallets
    alice.connect_wallet()
    bob.connect_wallet()
    
    # Notify users of rewards
    reward_system.notify_user("Alice", "USDT", 100.0)
    reward_system.notify_user("Bob", "NFTs", 5)
    
    # Users claim their rewards
    print(reward_system.claim_rewards("Alice"))
    print(reward_system.claim_rewards("Bob"))
    
    # Attempt to claim rewards with a disconnected wallet
    bob.disconnect_wallet()
    print(reward_system.claim_rewards("Bob"))
```
