"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfreespin.com
Prompt: Write code to implement a "Free Spin" feature that checks NFT ownership and generates rewards, similar to the mechanism outlined on TONfreespin.com.
Generated: DETERMINISTIC_72a9cc8c94d9764b
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class NFT:
    """A class to represent an NFT with its owner."""
    def __init__(self, token_id: str, owner: str):
        self.token_id = token_id
        self.owner = owner

class FreeSpin:
    """A class to represent the Free Spin feature for NFT owners."""
    
    def __init__(self):
        self.nft_owners: Dict[str, NFT] = {}  # Dictionary to store NFTs by token ID

    def add_nft(self, token_id: str, owner: str) -> None:
        """Add an NFT to the system.
        
        Args:
            token_id (str): The unique identifier for the NFT.
            owner (str): The owner of the NFT.
        """
        if token_id in self.nft_owners:
            raise ValueError(f"NFT with token ID {token_id} already exists.")
        
        self.nft_owners[token_id] = NFT(token_id, owner)

    def check_ownership(self, token_id: str, user: str) -> bool:
        """Check if a user owns the specified NFT.
        
        Args:
            token_id (str): The unique identifier for the NFT.
            user (str): The user's identifier to check ownership against.
        
        Returns:
            bool: True if the user owns the NFT, False otherwise.
        """
        nft = self.nft_owners.get(token_id)
        return nft is not None and nft.owner == user

    def generate_reward(self) -> str:
        """Generate a random reward for the user.
        
        Returns:
            str: A random reward.
        """
        rewards = ["10 Tokens", "20 Tokens", "30 Tokens", "Mystery Box", "Nothing"]
        return random.choice(rewards)

    def free_spin(self, token_id: str, user: str) -> str:
        """Perform a free spin for the user if they own the NFT.
        
        Args:
            token_id (str): The unique identifier for the NFT.
            user (str): The user attempting to perform the free spin.
        
        Returns:
            str: The result of the free spin, whether a reward was generated or not.
        
        Raises:
            PermissionError: If the user does not own the NFT.
        """
        if not self.check_ownership(token_id, user):
            raise PermissionError(f"User {user} does not own the NFT with token ID {token_id}.")
        
        # Generate a reward for the user
        reward = self.generate_reward()
        return f"User {user} received: {reward}"

# Example usage
if __name__ == "__main__":
    free_spin_system = FreeSpin()
    
    # Adding NFTs
    free_spin_system.add_nft("token1", "user123")
    free_spin_system.add_nft("token2", "user456")
    
    # Attempting to perform free spins
    try:
        print(free_spin_system.free_spin("token1", "user123"))  # Expected: User user123 received: <random reward>
        print(free_spin_system.free_spin("token2", "user123"))  # Expected: PermissionError
    except Exception as e:
        print(f"Error: {e}")
```
