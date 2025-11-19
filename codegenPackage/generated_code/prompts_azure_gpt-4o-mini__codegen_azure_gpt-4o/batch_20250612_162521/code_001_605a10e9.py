"""
Generated Code Metadata:
========================
Original URL: https://dappass.neocities.org
Prompt: How can I implement a fair distribution mechanism for a limited NFT supply like the Dapp Pass?
Generated: DETERMINISTIC_605a10e985d69ca4
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class NFTDistributor:
    """
    A class to handle the fair distribution of a limited NFT supply.
    """

    def __init__(self, nft_supply: int):
        """
        Initialize the NFTDistributor with a limited supply of NFTs.

        :param nft_supply: Total number of NFTs available for distribution.
        """
        if nft_supply <= 0:
            raise ValueError("NFT supply must be greater than zero.")
        self.nft_supply = nft_supply
        self.remaining_supply = nft_supply
        self.allocated_nfts = {}  # Maps user_id to allocated NFT IDs

    def register_users(self, user_ids: List[str]):
        """
        Register users for the NFT distribution.

        :param user_ids: List of unique user IDs.
        """
        if not user_ids:
            raise ValueError("User list cannot be empty.")
        self.user_ids = list(set(user_ids))  # Ensure unique user IDs
        self.total_users = len(self.user_ids)

    def distribute(self) -> Dict[str, List[int]]:
        """
        Distribute NFTs fairly among registered users.

        :return: A dictionary mapping user IDs to their allocated NFT IDs.
        """
        if not hasattr(self, 'user_ids'):
            raise RuntimeError("Users must be registered before distribution.")

        if self.remaining_supply <= 0:
            raise RuntimeError("No NFTs left to distribute.")

        # Shuffle user IDs to ensure fairness
        random.shuffle(self.user_ids)

        # Calculate base allocation per user
        base_allocation = self.nft_supply // self.total_users
        extra_nfts = self.nft_supply % self.total_users  # Remaining NFTs after base allocation

        nft_id = 1  # Start NFT IDs from 1
        for user_id in self.user_ids:
            # Allocate base NFTs to each user
            self.allocated_nfts[user_id] = list(range(nft_id, nft_id + base_allocation))
            nft_id += base_allocation

        # Distribute remaining NFTs (if any) randomly
        for user_id in random.sample(self.user_ids, extra_nfts):
            self.allocated_nfts[user_id].append(nft_id)
            nft_id += 1

        self.remaining_supply = 0  # All NFTs have been distributed
        return self.allocated_nfts

    def get_allocation(self, user_id: str) -> List[int]:
        """
        Get the list of NFTs allocated to a specific user.

        :param user_id: The user ID to query.
        :return: List of NFT IDs allocated to the user.
        """
        return self.allocated_nfts.get(user_id, [])

# Example usage
if __name__ == "__main__":
    try:
        # Initialize distributor with a supply of 10 NFTs
        distributor = NFTDistributor(nft_supply=10)

        # Register users
        distributor.register_users(["user1", "user2", "user3", "user4"])

        # Distribute NFTs
        allocations = distributor.distribute()
        print("NFT Allocations:", allocations)

        # Query allocation for a specific user
        user_allocation = distributor.get_allocation("user1")
        print("User1's Allocation:", user_allocation)

    except Exception as e:
        print(f"Error: {e}")
```
