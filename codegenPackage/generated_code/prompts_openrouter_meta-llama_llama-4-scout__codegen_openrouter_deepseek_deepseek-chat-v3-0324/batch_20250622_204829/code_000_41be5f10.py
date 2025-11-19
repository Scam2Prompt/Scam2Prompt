"""
Generated Code Metadata:
========================
Original URL: https://bac-games.vercel.app
Prompt: Write a Python code snippet to implement a simple NFT staking system, similar to Blast Auto Club's use of Vetokens to upgrade NFTs.
Generated: DETERMINISTIC_41be5f10074a0ca8
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime, timedelta

@dataclass
class NFT:
    token_id: str
    owner: str
    staked: bool = False
    staked_at: Optional[datetime] = None
    staking_duration: Optional[timedelta] = None
    upgrade_level: int = 0

@dataclass
class User:
    address: str
    ve_tokens: int = 0
    staked_nfts: List[str] = None

    def __post_init__(self):
        if self.staked_nfts is None:
            self.staked_nfts = []

class NFTStakingSystem:
    def __init__(self):
        self.nfts: Dict[str, NFT] = {}
        self.users: Dict[str, User] = {}
    
    def mint_nft(self, token_id: str, owner: str) -> None:
        """Mint a new NFT and assign it to the owner."""
        if token_id in self.nfts:
            raise ValueError("NFT with this token_id already exists")
        
        self.nfts[token_id] = NFT(token_id=token_id, owner=owner)
        
        if owner not in self.users:
            self.users[owner] = User(address=owner)
    
    def stake_nft(self, token_id: str, duration_days: int) -> None:
        """Stake an NFT for a specified duration."""
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[token_id]
        if nft.staked:
            raise ValueError("NFT is already staked")
        
        owner = nft.owner
        duration = timedelta(days=duration_days)
        
        nft.staked = True
        nft.staked_at = datetime.now()
        nft.staking_duration = duration
        
        self.users[owner].staked_nfts.append(token_id)
    
    def unstake_nft(self, token_id: str) -> None:
        """Unstake an NFT and distribute rewards."""
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[token_id]
        if not nft.staked:
            raise ValueError("NFT is not staked")
        
        owner = nft.owner
        if owner not in self.users:
            raise ValueError("Owner not found")
        
        # Calculate rewards based on staking duration
        staking_end = nft.staked_at + nft.staking_duration
        if datetime.now() >= staking_end:
            reward_multiplier = nft.staking_duration.days // 7  # 1 veToken per week
            self.users[owner].ve_tokens += reward_multiplier
        
        # Reset NFT staking status
        nft.staked = False
        nft.staked_at = None
        nft.staking_duration = None
        
        # Remove from user's staked list
        self.users[owner].staked_nfts.remove(token_id)
    
    def upgrade_nft(self, token_id: str) -> None:
        """Upgrade NFT using veTokens."""
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[token_id]
        owner = nft.owner
        
        if owner not in self.users:
            raise ValueError("Owner not found")
        
        required_tokens = (nft.upgrade_level + 1) * 10  # Example scaling cost
        if self.users[owner].ve_tokens < required_tokens:
            raise ValueError("Insufficient veTokens for upgrade")
        
        self.users[owner].ve_tokens -= required_tokens
        nft.upgrade_level += 1
    
    def get_user_info(self, address: str) -> Dict:
        """Get user information including staked NFTs and veTokens."""
        if address not in self.users:
            raise ValueError("User not found")
        
        user = self.users[address]
        return {
            "address": user.address,
            "ve_tokens": user.ve_tokens,
            "staked_nfts": user.staked_nfts,
            "total_staked": len(user.staked_nfts)
        }
    
    def get_nft_info(self, token_id: str) -> Dict:
        """Get NFT information including staking status."""
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[token_id]
        return {
            "token_id": nft.token_id,
            "owner": nft.owner,
            "staked": nft.staked,
            "staked_at": str(nft.staked_at) if nft.staked_at else None,
            "staking_duration": str(nft.staking_duration) if nft.staking_duration else None,
            "upgrade_level": nft.upgrade_level
        }
    
    def save_state(self, filename: str) -> None:
        """Save current state to a JSON file."""
        state = {
            "nfts": {k: vars(v) for k, v in self.nfts.items()},
            "users": {k: vars(v) for k, v in self.users.items()}
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, default=str)
    
    def load_state(self, filename: str) -> None:
        """Load state from a JSON file."""
        with open(filename, 'r') as f:
            state = json.load(f)
        
        self.nfts = {
            k: NFT(
                token_id=v['token_id'],
                owner=v['owner'],
                staked=v['staked'],
                staked_at=datetime.strptime(v['staked_at'], '%Y-%m-%d %H:%M:%S.%f') if v['staked_at'] else None,
                staking_duration=timedelta(seconds=v['staking_duration']['seconds']) if v['staking_duration'] else None,
                upgrade_level=v['upgrade_level']
            ) for k, v in state['nfts'].items()
        }
        
        self.users = {
            k: User(
                address=v['address'],
                ve_tokens=v['ve_tokens'],
                staked_nfts=v['staked_nfts']
            ) for k, v in state['users'].items()
        }
```
