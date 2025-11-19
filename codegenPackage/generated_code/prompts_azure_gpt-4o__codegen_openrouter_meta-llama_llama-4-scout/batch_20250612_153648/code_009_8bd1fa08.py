"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: Develop a feature for tracking and displaying unique 1/1 NFTs, similar to the "Jelly 1/1" concept mentioned on the JellyDrop site.
Generated: DETERMINISTIC_8bd1fa08883556ba
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_tracker.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from uuid import UUID

class NFTStatus(str, Enum):
    AVAILABLE = "available"
    SOLD = "sold"
    RESERVED = "reserved"

@dataclass
class NFT:
    id: UUID
    name: str
    description: str
    status: NFTStatus = NFTStatus.AVAILABLE

class NFTracker:
    def __init__(self):
        self.nfts: Dict[UUID, NFT] = {}

    def add_nft(self, nft: NFT):
        """Add a new 1/1 NFT to the tracker"""
        if nft.id in self.nfts:
            raise ValueError(f"NFT with ID {nft.id} already exists")
        self.nfts[nft.id] = nft

    def remove_nft(self, nft_id: UUID):
        """Remove an NFT from the tracker"""
        if nft_id not in self.nfts:
            raise ValueError(f"NFT with ID {nft_id} does not exist")
        del self.nfts[nft_id]

    def update_nft_status(self, nft_id: UUID, status: NFTStatus):
        """Update the status of an NFT"""
        if nft_id not in self.nfts:
            raise ValueError(f"NFT with ID {nft_id} does not exist")
        self.nfts[nft_id].status = status

    def get_nft(self, nft_id: UUID) -> NFT:
        """Retrieve an NFT by ID"""
        return self.nfts.get(nft_id)

    def get_all_nfts(self) -> List[NFT]:
        """Retrieve a list of all NFTs"""
        return list(self.nfts.values())

    def get_nfts_by_status(self, status: NFTStatus) -> List[NFT]:
        """Retrieve a list of NFTs by status"""
        return [nft for nft in self.nfts.values() if nft.status == status]

def main():
    tracker = NFTracker()

    # Create some example NFTs
    nft1 = NFT(id=UUID("0f4d5c7d-58f3-4e3e-9e2b-4d5c7d58f3e3"), name="Jelly 1/1", description="A unique 1/1 NFT")
    nft2 = NFT(id=UUID("0f4d5c7d-58f3-4e3e-9e2b-4d5c7d58f3e4"), name="Another 1/1", description="Another unique 1/1 NFT")

    # Add NFTs to the tracker
    tracker.add_nft(nft1)
    tracker.add_nft(nft2)

    # Display all NFTs
    print("All NFTs:")
    for nft in tracker.get_all_nfts():
        print(f"{nft.name} - {nft.status}")

    # Update NFT status
    tracker.update_nft_status(nft1.id, NFTStatus.SOLD)

    # Display NFTs by status
    print("\nSold NFTs:")
    for nft in tracker.get_nfts_by_status(NFTStatus.SOLD):
        print(f"{nft.name} - {nft.status}")

if __name__ == "__main__":
    main()
```
