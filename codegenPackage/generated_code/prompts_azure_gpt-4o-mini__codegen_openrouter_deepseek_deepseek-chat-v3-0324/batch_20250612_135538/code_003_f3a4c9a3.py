"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Explain how the Buildoors ecosystem works, focusing on minting and earning $BLD.
Generated: DETERMINISTIC_f3a4c9a3a74e9438
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# buildoors_ecosystem.py

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional
import hashlib
import time

class BuildoorType(Enum):
    """Types of Buildoors available in the ecosystem."""
    COMMON = auto()
    RARE = auto()
    LEGENDARY = auto()

@dataclass
class Buildoor:
    """Represents a Buildoor NFT in the ecosystem."""
    id: str
    buildoor_type: BuildoorType
    owner: str
    mint_time: float
    last_claim_time: float = 0.0

class BuildoorsEcosystem:
    """Main class representing the Buildoors ecosystem."""
    
    def __init__(self):
        self.buildoors: Dict[str, Buildoor] = {}
        self.bld_balance: Dict[str, float] = {}
        self.bld_rate = {
            BuildoorType.COMMON: 1.0,
            BuildoorType.RARE: 2.5,
            BuildoorType.LEGENDARY: 5.0
        }
    
    def mint_buildoor(self, owner: str, buildoor_type: BuildoorType) -> Buildoor:
        """
        Mints a new Buildoor NFT for the specified owner.
        
        Args:
            owner: Wallet address of the owner
            buildoor_type: Type of Buildoor to mint
            
        Returns:
            The newly minted Buildoor
            
        Raises:
            ValueError: If invalid Buildoor type is provided
        """
        if not isinstance(buildoor_type, BuildoorType):
            raise ValueError("Invalid Buildoor type")
            
        buildoor_id = self._generate_buildoor_id(owner)
        current_time = time.time()
        
        new_buildoor = Buildoor(
            id=buildoor_id,
            buildoor_type=buildoor_type,
            owner=owner,
            mint_time=current_time,
            last_claim_time=current_time
        )
        
        self.buildoors[buildoor_id] = new_buildoor
        
        # Initialize BLD balance if needed
        if owner not in self.bld_balance:
            self.bld_balance[owner] = 0.0
            
        return new_buildoor
    
    def claim_bld(self, buildoor_id: str) -> float:
        """
        Claims accumulated $BLD tokens for a Buildoor.
        
        Args:
            buildoor_id: ID of the Buildoor to claim for
            
        Returns:
            Amount of $BLD claimed
            
        Raises:
            ValueError: If Buildoor ID doesn't exist
        """
        if buildoor_id not in self.buildoors:
            raise ValueError("Buildoor ID not found")
            
        buildoor = self.buildoors[buildoor_id]
        current_time = time.time()
        
        # Calculate earned BLD since last claim
        time_elapsed = current_time - buildoor.last_claim_time
        bld_earned = time_elapsed * self.bld_rate[buildoor.buildoor_type] / 3600  # Per hour
        
        # Update balances and timestamps
        self.bld_balance[buildoor.owner] += bld_earned
        buildoor.last_claim_time = current_time
        
        return bld_earned
    
    def get_bld_balance(self, owner: str) -> float:
        """
        Gets the current $BLD balance for an owner.
        
        Args:
            owner: Wallet address to check balance for
            
        Returns:
            Current $BLD balance
        """
        return self.bld_balance.get(owner, 0.0)
    
    def get_buildoors_by_owner(self, owner: str) -> List[Buildoor]:
        """
        Gets all Buildoors owned by a specific wallet.
        
        Args:
            owner: Wallet address to filter by
            
        Returns:
            List of Buildoors owned by the wallet
        """
        return [b for b in self.buildoors.values() if b.owner == owner]
    
    def _generate_buildoor_id(self, owner: str) -> str:
        """
        Generates a unique ID for a new Buildoor.
        
        Args:
            owner: Wallet address of the owner
            
        Returns:
            Unique Buildoor ID
        """
        hash_input = f"{owner}{time.time()}".encode()
        return hashlib.sha256(hash_input).hexdigest()[:16]
```
