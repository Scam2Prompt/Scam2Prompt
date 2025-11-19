"""
Generated Code Metadata:
========================
Original URL: https://sjkjs-2ct.pages.dev
Prompt: Generate code to create a simple NFT marketplace with functionality for buying, selling, and transferring NFTs, inspired by the Guildhall platform.
Generated: DETERMINISTIC_a3fcef3ceb60a9d9
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_marketplace.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from uuid import uuid4

class NFTStatus(Enum):
    """NFT Status Enum"""
    AVAILABLE = 1
    SOLD = 2
    TRANSFERRED = 3

@dataclass
class NFT:
    """NFT Data Class"""
    id: str
    name: str
    description: str
    owner: str
    status: NFTStatus

class NFTMarketplace:
    """NFT Marketplace Class"""

    def __init__(self):
        self.nfts: Dict[str, NFT] = {}
        self.users: Dict[str, List[NFT]] = {}

    def create_nft(self, name: str, description: str, owner: str) -> NFT:
        """Create a new NFT"""
        nft_id = str(uuid4())
        nft = NFT(nft_id, name, description, owner, NFTStatus.AVAILABLE)
        self.nfts[nft_id] = nft
        if owner not in self.users:
            self.users[owner] = []
        self.users[owner].append(nft)
        return nft

    def buy_nft(self, nft_id: str, buyer: str) -> NFT:
        """Buy an NFT"""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for sale")
        nft.status = NFTStatus.SOLD
        nft.owner = buyer
        if buyer not in self.users:
            self.users[buyer] = []
        self.users[buyer].append(nft)
        return nft

    def sell_nft(self, nft_id: str, seller: str) -> NFT:
        """Sell an NFT (make it available for sale)"""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        nft = self.nfts[nft_id]
        if nft.owner != seller:
            raise ValueError("Seller is not the owner of the NFT")
        nft.status = NFTStatus.AVAILABLE
        return nft

    def transfer_nft(self, nft_id: str, sender: str, recipient: str) -> NFT:
        """Transfer an NFT"""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        nft = self.nfts[nft_id]
        if nft.owner != sender:
            raise ValueError("Sender is not the owner of the NFT")
        nft.owner = recipient
        self.users[sender].remove(nft)
        if recipient not in self.users:
            self.users[recipient] = []
        self.users[recipient].append(nft)
        nft.status = NFTStatus.TRANSFERRED
        return nft

    def get_nft(self, nft_id: str) -> NFT:
        """Get an NFT by ID"""
        return self.nfts.get(nft_id)

    def get_user_nfts(self, user: str) -> List[NFT]:
        """Get all NFTs owned by a user"""
        return self.users.get(user, [])

def main():
    marketplace = NFTMarketplace()

    # Create NFTs
    nft1 = marketplace.create_nft("NFT 1", "Description 1", "User 1")
    nft2 = marketplace.create_nft("NFT 2", "Description 2", "User 2")

    # Buy NFT
    bought_nft = marketplace.buy_nft(nft1.id, "User 3")
    print(f"Bought NFT: {bought_nft.name}")

    # Sell NFT
    sold_nft = marketplace.sell_nft(nft2.id, "User 2")
    print(f"Sold NFT: {sold_nft.name}")

    # Transfer NFT
    transferred_nft = marketplace.transfer_nft(nft1.id, "User 3", "User 4")
    print(f"Transferred NFT: {transferred_nft.name}")

    # Get NFT
    nft = marketplace.get_nft(nft1.id)
    print(f"NFT: {nft.name}")

    # Get user NFTs
    user_nfts = marketplace.get_user_nfts("User 4")
    print(f"User NFTs: {[nft.name for nft in user_nfts]}")

if __name__ == "__main__":
    main()
```
