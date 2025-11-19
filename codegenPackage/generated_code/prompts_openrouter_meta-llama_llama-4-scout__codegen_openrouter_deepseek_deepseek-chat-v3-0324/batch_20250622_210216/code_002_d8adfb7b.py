"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Generate code to implement a staking mechanism for an NFT collection, where holders can stake their NFTs to receive rewards in the form of airdropped NFTs or other benefits.
Generated: DETERMINISTIC_d8adfb7ba100e868
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import hashlib

@dataclass
class NFT:
    token_id: str
    owner: str
    metadata: Dict

@dataclass
class StakingPosition:
    token_id: str
    staker: str
    staked_at: datetime
    last_claimed: Optional[datetime]
    rewards_accumulated: int

class NFTStakingSystem:
    def __init__(self):
        self.staked_nfts: Dict[str, StakingPosition] = {}
        self.reward_rate: int = 10  # Rewards per NFT per day
        self.min_staking_duration: timedelta = timedelta(days=7)
        self.reward_nft_collection: List[NFT] = []
        self.nft_holders: Dict[str, List[NFT]] = {}

    def stake_nft(self, token_id: str, staker: str) -> bool:
        """
        Stake an NFT from the holder's collection.
        
        Args:
            token_id: ID of the NFT to stake
            staker: Address of the staker
            
        Returns:
            bool: True if staking was successful, False otherwise
        """
        if token_id in self.staked_nfts:
            return False  # Already staked
        
        # Check if staker owns the NFT
        if staker not in self.nft_holders:
            return False
            
        nfts = self.nft_holders[staker]
        nft_to_stake = next((nft for nft in nfts if nft.token_id == token_id), None)
        if not nft_to_stake:
            return False
            
        # Create staking position
        now = datetime.now()
        self.staked_nfts[token_id] = StakingPosition(
            token_id=token_id,
            staker=staker,
            staked_at=now,
            last_claimed=None,
            rewards_accumulated=0
        )
        
        # Remove from holder's collection
        self.nft_holders[staker].remove(nft_to_stake)
        return True

    def unstake_nft(self, token_id: str, staker: str) -> bool:
        """
        Unstake an NFT and return it to the holder's collection.
        
        Args:
            token_id: ID of the NFT to unstake
            staker: Address of the staker
            
        Returns:
            bool: True if unstaking was successful, False otherwise
        """
        if token_id not in self.staked_nfts:
            return False
            
        position = self.staked_nfts[token_id]
        if position.staker != staker:
            return False
            
        # Check minimum staking duration
        if datetime.now() - position.staked_at < self.min_staking_duration:
            return False
            
        # Return NFT to holder
        nft = NFT(
            token_id=token_id,
            owner=staker,
            metadata={}  # In a real implementation, this would be preserved
        )
        
        if staker not in self.nft_holders:
            self.nft_holders[staker] = []
            
        self.nft_holders[staker].append(nft)
        del self.staked_nfts[token_id]
        return True

    def claim_rewards(self, staker: str) -> Optional[List[NFT]]:
        """
        Claim accumulated rewards for all staked NFTs.
        
        Args:
            staker: Address of the staker
            
        Returns:
            Optional[List[NFT]]: List of reward NFTs if successful, None otherwise
        """
        if staker not in self.nft_holders:
            return None
            
        staked_positions = [pos for pos in self.staked_nfts.values() if pos.staker == staker]
        if not staked_positions:
            return None
            
        now = datetime.now()
        reward_nfts = []
        
        for position in staked_positions:
            # Calculate rewards since last claim (or since staking if never claimed)
            last_claim = position.last_claimed if position.last_claimed else position.staked_at
            days_staked = (now - last_claim).days
            rewards = days_staked * self.reward_rate
            
            if rewards > 0:
                # Mint reward NFTs
                for _ in range(rewards):
                    if self.reward_nft_collection:
                        reward_nft = self.reward_nft_collection.pop()
                        reward_nft.owner = staker
                        reward_nfts.append(reward_nft)
                
                # Update position
                position.last_claimed = now
                position.rewards_accumulated += rewards
        
        return reward_nfts if reward_nfts else None

    def get_staked_nfts(self, staker: str) -> List[StakingPosition]:
        """
        Get all staked NFTs for a given staker.
        
        Args:
            staker: Address of the staker
            
        Returns:
            List[StakingPosition]: List of staking positions
        """
        return [pos for pos in self.staked_nfts.values() if pos.staker == staker]

    def add_reward_nft(self, nft: NFT) -> None:
        """
        Add an NFT to the reward pool.
        
        Args:
            nft: NFT to add to the reward pool
        """
        self.reward_nft_collection.append(nft)

    def add_nft_to_holder(self, holder: str, nft: NFT) -> None:
        """
        Add an NFT to a holder's collection.
        
        Args:
            holder: Address of the holder
            nft: NFT to add
        """
        if holder not in self.nft_holders:
            self.nft_holders[holder] = []
        self.nft_holders[holder].append(nft)

    def calculate_rewards(self, staker: str) -> int:
        """
        Calculate pending rewards for a staker.
        
        Args:
            staker: Address of the staker
            
        Returns:
            int: Total pending rewards
        """
        staked_positions = [pos for pos in self.staked_nfts.values() if pos.staker == staker]
        if not staked_positions:
            return 0
            
        now = datetime.now()
        total_rewards = 0
        
        for position in staked_positions:
            last_claim = position.last_claimed if position.last_claimed else position.staked_at
            days_staked = (now - last_claim).days
            total_rewards += days_staked * self.reward_rate
        
        return total_rewards

    def to_json(self) -> str:
        """
        Serialize the staking system to JSON.
        
        Returns:
            str: JSON representation of the staking system
        """
        data = {
            "staked_nfts": {
                token_id: {
                    "token_id": pos.token_id,
                    "staker": pos.staker,
                    "staked_at": pos.staked_at.isoformat(),
                    "last_claimed": pos.last_claimed.isoformat() if pos.last_claimed else None,
                    "rewards_accumulated": pos.rewards_accumulated
                }
                for token_id, pos in self.staked_nfts.items()
            },
            "reward_rate": self.reward_rate,
            "min_staking_duration_days": self.min_staking_duration.days,
            "reward_nft_collection": [
                {
                    "token_id": nft.token_id,
                    "owner": nft.owner,
                    "metadata": nft.metadata
                }
                for nft in self.reward_nft_collection
            ],
            "nft_holders": {
                holder: [
                    {
                        "token_id": nft.token_id,
                        "owner": nft.owner,
                        "metadata": nft.metadata
                    }
                    for nft in nfts
                ]
                for holder, nfts in self.nft_holders.items()
            }
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str: str) -> 'NFTStakingSystem':
        """
        Deserialize a staking system from JSON.
        
        Args:
            json_str: JSON string to deserialize
            
        Returns:
            NFTStakingSystem: Deserialized staking system
        """
        data = json.loads(json_str)
        system = cls()
        system.reward_rate = data["reward_rate"]
        system.min_staking_duration = timedelta(days=data["min_staking_duration_days"])
        
        # Load staked NFTs
        for token_id, pos_data in data["staked_nfts"].items():
            system.staked_nfts[token_id] = StakingPosition(
                token_id=token_id,
                staker=pos_data["staker"],
                staked_at=datetime.fromisoformat(pos_data["staked_at"]),
                last_claimed=datetime.fromisoformat(pos_data["last_claimed"]) if pos_data["last_claimed"] else None,
                rewards_accumulated=pos_data["rewards_accumulated"]
            )
        
        # Load reward NFTs
        system.reward_nft_collection = [
            NFT(
                token_id=n
