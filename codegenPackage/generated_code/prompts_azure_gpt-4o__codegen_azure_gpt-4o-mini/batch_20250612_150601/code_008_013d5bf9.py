"""
Generated Code Metadata:
========================
Original URL: https://nft-solaj.web.app
Prompt: Write code to implement a rewards system for NFT creators, similar to the "Rewards" feature mentioned on the Magic Eden Launchpad.
Generated: DETERMINISTIC_013d5bf998c0fbf7
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Optional

class NFT:
    """Class representing a Non-Fungible Token (NFT)."""
    
    def __init__(self, token_id: str, creator: str, base_price: float):
        """
        Initialize an NFT instance.

        :param token_id: Unique identifier for the NFT.
        :param creator: Address of the NFT creator.
        :param base_price: Base price of the NFT.
        """
        self.token_id = token_id
        self.creator = creator
        self.base_price = base_price
        self.rewards = 0.0  # Initialize rewards to zero

    def add_rewards(self, amount: float):
        """
        Add rewards to the creator of the NFT.

        :param amount: Amount of rewards to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Reward amount cannot be negative.")
        self.rewards += amount


class RewardsSystem:
    """Class to manage the rewards system for NFT creators."""
    
    def __init__(self):
        """Initialize the rewards system with an empty NFT registry."""
        self.nfts: Dict[str, NFT] = {}

    def register_nft(self, token_id: str, creator: str, base_price: float):
        """
        Register a new NFT in the rewards system.

        :param token_id: Unique identifier for the NFT.
        :param creator: Address of the NFT creator.
        :param base_price: Base price of the NFT.
        :raises ValueError: If the NFT is already registered.
        """
        if token_id in self.nfts:
            raise ValueError("NFT with this token_id is already registered.")
        self.nfts[token_id] = NFT(token_id, creator, base_price)

    def sell_nft(self, token_id: str, sale_price: float):
        """
        Process the sale of an NFT and allocate rewards to the creator.

        :param token_id: Unique identifier for the NFT being sold.
        :param sale_price: Sale price of the NFT.
        :raises ValueError: If the NFT is not registered or sale price is invalid.
        """
        if token_id not in self.nfts:
            raise ValueError("NFT not found.")
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")

        nft = self.nfts[token_id]
        # Calculate rewards as a percentage of the sale price
        reward_percentage = 0.1  # 10% reward for the creator
        rewards_to_add = sale_price * reward_percentage
        nft.add_rewards(rewards_to_add)

    def get_rewards(self, token_id: str) -> Optional[float]:
        """
        Retrieve the total rewards for a given NFT creator.

        :param token_id: Unique identifier for the NFT.
        :return: Total rewards for the creator or None if NFT not found.
        """
        nft = self.nfts.get(token_id)
        if nft:
            return nft.rewards
        return None

    def list_nfts(self) -> List[str]:
        """
        List all registered NFTs.

        :return: List of token IDs of registered NFTs.
        """
        return list(self.nfts.keys())


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()
    
    # Registering NFTs
    rewards_system.register_nft("nft1", "creator1", 100.0)
    rewards_system.register_nft("nft2", "creator2", 200.0)

    # Selling NFTs
    rewards_system.sell_nft("nft1", 150.0)
    rewards_system.sell_nft("nft2", 250.0)

    # Retrieving rewards
    print(f"Rewards for creator1: {rewards_system.get_rewards('nft1')}")
    print(f"Rewards for creator2: {rewards_system.get_rewards('nft2')}")

    # Listing all NFTs
    print("Registered NFTs:", rewards_system.list_nfts())
```
