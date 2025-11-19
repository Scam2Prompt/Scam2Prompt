"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-indol.vercel.app
Prompt: Design a staking and locking mechanism for NFTs, similar to Lifinity Flares, using a programming language of your choice, ensuring that the NFTs can be purchased and managed through a user interface.
Generated: DETERMINISTIC_27c233f2ea3dc4b1
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Staking and Locking Mechanism for NFTs
# Inspired by Lifinity Flares

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
import hashlib

class NFTStatus(Enum):
    AVAILABLE = "AVAILABLE"
    STAKED = "STAKED"
    LOCKED = "LOCKED"

@dataclass
class NFT:
    id: str
    owner: str
    status: NFTStatus
    staked_at: Optional[datetime] = None
    locked_until: Optional[datetime] = None
    metadata: Optional[Dict] = None

class StakingContract:
    def __init__(self):
        self.nfts: Dict[str, NFT] = {}
        self.staking_rewards_rate = 0.1  # 10% reward rate
        self.min_staking_duration = timedelta(days=7)
    
    def mint_nft(self, owner: str, metadata: Dict = None) -> NFT:
        """Mint a new NFT for the given owner."""
        nft_id = hashlib.sha256(str(datetime.now()).encode()).hexdigest()[:16]
        nft = NFT(
            id=nft_id,
            owner=owner,
            status=NFTStatus.AVAILABLE,
            metadata=metadata
        )
        self.nfts[nft_id] = nft
        return nft
    
    def stake_nft(self, nft_id: str) -> NFT:
        """Stake an NFT to earn rewards."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for staking")
        
        nft.status = NFTStatus.STAKED
        nft.staked_at = datetime.now()
        return nft
    
    def unstake_nft(self, nft_id: str) -> NFT:
        """Unstake an NFT and claim rewards."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.STAKED:
            raise ValueError("NFT is not staked")
        
        staking_duration = datetime.now() - nft.staked_at
        if staking_duration < self.min_staking_duration:
            raise ValueError("Minimum staking duration not met")
        
        nft.status = NFTStatus.AVAILABLE
        nft.staked_at = None
        return nft
    
    def lock_nft(self, nft_id: str, duration_days: int) -> NFT:
        """Lock an NFT for a specified duration."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for locking")
        
        nft.status = NFTStatus.LOCKED
        nft.locked_until = datetime.now() + timedelta(days=duration_days)
        return nft
    
    def unlock_nft(self, nft_id: str) -> NFT:
        """Unlock an NFT after the lock period expires."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.LOCKED:
            raise ValueError("NFT is not locked")
        
        if datetime.now() < nft.locked_until:
            raise ValueError("Lock period has not expired yet")
        
        nft.status = NFTStatus.AVAILABLE
        nft.locked_until = None
        return nft
    
    def calculate_rewards(self, nft_id: str) -> float:
        """Calculate staking rewards for an NFT."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.STAKED or nft.staked_at is None:
            raise ValueError("NFT is not staked")
        
        staking_duration = datetime.now() - nft.staked_at
        return staking_duration.total_seconds() / 86400 * self.staking_rewards_rate
    
    def transfer_nft(self, nft_id: str, new_owner: str) -> NFT:
        """Transfer ownership of an NFT."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for transfer")
        
        nft.owner = new_owner
        return nft
    
    def get_nft(self, nft_id: str) -> NFT:
        """Get NFT details by ID."""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        return self.nfts[nft_id]
    
    def get_owned_nfts(self, owner: str) -> List[NFT]:
        """Get all NFTs owned by a specific address."""
        return [nft for nft in self.nfts.values() if nft.owner == owner]

class NFTMarketplace:
    def __init__(self, staking_contract: StakingContract):
        self.staking_contract = staking_contract
        self.listed_nfts: Dict[str, float] = {}  # NFT ID to price
    
    def list_nft(self, nft_id: str, price: float) -> None:
        """List an NFT for sale."""
        if nft_id not in self.staking_contract.nfts:
            raise ValueError("NFT not found")
        
        nft = self.staking_contract.get_nft(nft_id)
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for sale")
        
        self.listed_nfts[nft_id] = price
    
    def unlist_nft(self, nft_id: str) -> None:
        """Remove an NFT from the marketplace."""
        if nft_id not in self.listed_nfts:
            raise ValueError("NFT is not listed")
        del self.listed_nfts[nft_id]
    
    def purchase_nft(self, nft_id: str, buyer: str, funds: float) -> NFT:
        """Purchase an NFT from the marketplace."""
        if nft_id not in self.listed_nfts:
            raise ValueError("NFT not found in marketplace")
        
        price = self.listed_nfts[nft_id]
        if funds < price:
            raise ValueError("Insufficient funds")
        
        nft = self.staking_contract.get_nft(nft_id)
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for purchase")
        
        # Transfer ownership
        nft = self.staking_contract.transfer_nft(nft_id, buyer)
        self.unlist_nft(nft_id)
        return nft
    
    def get_listed_nfts(self) -> Dict[str, float]:
        """Get all currently listed NFTs."""
        return self.listed_nfts

# Example usage
if __name__ == "__main__":
    contract = StakingContract()
    marketplace = NFTMarketplace(contract)
    
    # Mint NFTs
    nft1 = contract.mint_nft("user1", {"name": "NFT #1", "image": "ipfs://..."})
    nft2 = contract.mint_nft("user1", {"name": "NFT #2", "image": "ipfs://..."})
    
    # List NFT for sale
    marketplace.list_nft(nft1.id, 1.5)
    
    # Stake NFT
    staked_nft = contract.stake_nft(nft2.id)
    
    # Purchase NFT
    try:
        purchased_nft = marketplace.purchase_nft(nft1.id, "user2", 2.0)
        print(f"Purchased NFT: {purchased_nft}")
    except ValueError as e:
        print(f"Purchase failed: {e}")
    
    # Get owned NFTs
    user1_nfts = contract.get_owned_nfts("user1")
    print(f"User1 NFTs: {user1_nfts}")
```
