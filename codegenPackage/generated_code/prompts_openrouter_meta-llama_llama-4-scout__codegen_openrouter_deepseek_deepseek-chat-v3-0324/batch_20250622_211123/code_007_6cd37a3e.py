"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a protocol flow for a Galahad Finance-like platform, incorporating key features and use cases from the Good Games Guild ecosystem.
Generated: DETERMINISTIC_6cd37a3e90db7fcd
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Galahad Finance Protocol Flow
# This implements a simplified version of a DeFi platform similar to Galahad Finance
# with integrations for gaming ecosystems like Good Games Guild (GGG)

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
import time

class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REVERTED = "REVERTED"

class AssetType(Enum):
    TOKEN = "TOKEN"
    NFT = "NFT"
    LP_TOKEN = "LP_TOKEN"

@dataclass
class Asset:
    asset_id: str
    asset_type: AssetType
    amount: float
    metadata: Optional[Dict] = None

@dataclass
class User:
    user_id: str
    wallet_address: str
    assets: List[Asset]
    staked_assets: List[Asset] = None

    def __post_init__(self):
        self.staked_assets = self.staked_assets or []

@dataclass
class Pool:
    pool_id: str
    assets: List[Asset]
    apr: float
    lock_period: int  # in seconds
    stakers: List[str] = None  # list of user_ids

    def __post_init__(self):
        self.stakers = self.stakers or []

class GalahadFinanceProtocol:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.pools: Dict[str, Pool] = {}
        self.transactions: Dict[str, Dict] = {}
        self.ggg_nfts: Dict[str, Dict] = {}  # Simulated GGG NFT registry

    def _generate_tx_hash(self, user_id: str) -> str:
        """Generate a unique transaction hash"""
        timestamp = str(time.time())
        return hashlib.sha256(f"{user_id}{timestamp}".encode()).hexdigest()

    def register_user(self, wallet_address: str) -> User:
        """Register a new user with the platform"""
        user_id = f"user_{len(self.users) + 1}"
        new_user = User(user_id=user_id, wallet_address=wallet_address, assets=[])
        self.users[user_id] = new_user
        return new_user

    def create_pool(self, assets: List[Asset], apr: float, lock_period: int) -> Pool:
        """Create a new staking pool"""
        pool_id = f"pool_{len(self.pools) + 1}"
        new_pool = Pool(pool_id=pool_id, assets=assets, apr=apr, lock_period=lock_period)
        self.pools[pool_id] = new_pool
        return new_pool

    def stake_assets(self, user_id: str, pool_id: str, assets: List[Asset]) -> str:
        """Stake assets into a pool"""
        if user_id not in self.users:
            raise ValueError("User not found")
        if pool_id not in self.pools:
            raise ValueError("Pool not found")

        user = self.users[user_id]
        pool = self.pools[pool_id]

        # Verify user has the assets
        for asset in assets:
            if asset not in user.assets:
                raise ValueError(f"User doesn't own asset {asset.asset_id}")

        # Create transaction
        tx_hash = self._generate_tx_hash(user_id)
        self.transactions[tx_hash] = {
            "user_id": user_id,
            "pool_id": pool_id,
            "assets": [a.asset_id for a in assets],
            "timestamp": time.time(),
            "status": TransactionStatus.PENDING.value
        }

        try:
            # Move assets from user to pool
            for asset in assets:
                user.assets.remove(asset)
                user.staked_assets.append(asset)
            
            # Add user to pool stakers if not already there
            if user_id not in pool.stakers:
                pool.stakers.append(user_id)
            
            # Update transaction status
            self.transactions[tx_hash]["status"] = TransactionStatus.COMPLETED.value
            return tx_hash

        except Exception as e:
            self.transactions[tx_hash]["status"] = TransactionStatus.FAILED.value
            self.transactions[tx_hash]["error"] = str(e)
            raise

    def unstake_assets(self, user_id: str, pool_id: str, asset_ids: List[str]) -> str:
        """Unstake assets from a pool"""
        if user_id not in self.users:
            raise ValueError("User not found")
        if pool_id not in self.pools:
            raise ValueError("Pool not found")

        user = self.users[user_id]
        pool = self.pools[pool_id]

        # Verify user has staked these assets
        staked_assets = [a for a in user.staked_assets if a.asset_id in asset_ids]
        if len(staked_assets) != len(asset_ids):
            raise ValueError("Not all assets are staked by user")

        # Create transaction
        tx_hash = self._generate_tx_hash(user_id)
        self.transactions[tx_hash] = {
            "user_id": user_id,
            "pool_id": pool_id,
            "assets": asset_ids,
            "timestamp": time.time(),
            "status": TransactionStatus.PENDING.value
        }

        try:
            # Move assets back to user
            for asset in staked_assets:
                user.staked_assets.remove(asset)
                user.assets.append(asset)
            
            # Update transaction status
            self.transactions[tx_hash]["status"] = TransactionStatus.COMPLETED.value
            return tx_hash

        except Exception as e:
            self.transactions[tx_hash]["status"] = TransactionStatus.FAILED.value
            self.transactions[tx_hash]["error"] = str(e)
            raise

    def register_ggg_nft(self, nft_id: str, metadata: Dict) -> None:
        """Register a GGG NFT with the platform"""
        self.ggg_nfts[nft_id] = metadata

    def get_ggg_nft_metadata(self, nft_id: str) -> Dict:
        """Get metadata for a registered GGG NFT"""
        if nft_id not in self.ggg_nfts:
            raise ValueError("NFT not registered")
        return self.ggg_nfts[nft_id]

    def calculate_rewards(self, user_id: str, pool_id: str) -> float:
        """Calculate staking rewards for a user in a pool"""
        if user_id not in self.users:
            raise ValueError("User not found")
        if pool_id not in self.pools:
            raise ValueError("Pool not found")

        user = self.users[user_id]
        pool = self.pools[pool_id]

        if user_id not in pool.stakers:
            return 0.0

        # Simplified reward calculation
        total_staked = sum(a.amount for a in user.staked_assets if a.asset_id in [a.asset_id for a in pool.assets])
        return total_staked * (pool.apr / 100) * (pool.lock_period / 31536000)  # APR to annual rate

    def claim_rewards(self, user_id: str, pool_id: str) -> str:
        """Claim staking rewards from a pool"""
        rewards = self.calculate_rewards(user_id, pool_id)
        if rewards <= 0:
            raise ValueError("No rewards to claim")

        tx_hash = self._generate_tx_hash(user_id)
        self.transactions[tx_hash] = {
            "user_id": user_id,
            "pool_id": pool_id,
            "rewards": rewards,
            "timestamp": time.time(),
            "status": TransactionStatus.PENDING.value
        }

        try:
            # In a real implementation, this would mint tokens to the user
            # Here we just update the transaction status
            self.transactions[tx_hash]["status"] = TransactionStatus.COMPLETED.value
            return tx_hash
        except Exception as e:
            self.transactions[tx_hash]["status"] = TransactionStatus.FAILED.value
            self.transactions[tx_hash]["error"] = str(e)
            raise

# Example usage
if __name__ == "__main__":
    protocol = GalahadFinanceProtocol()
    
    # Register users
    user1 = protocol.register_user("0x123...")
    user2 = protocol.register_user("0x456...")
    
    # Create some assets
    ggg_token = Asset("GGG", AssetType.TOKEN, 1000)
    nft1 = Asset("GGG_NFT_1", AssetType.NFT, 1, {"game": "Axie Infinity", "rarity": "Legendary"})
    
    # Add assets to users
    user1.assets.append(ggg_token)
    user1.assets.append(nft1)
    
    # Register GGG NFT
    protocol.register_ggg_nft("GGG_NFT_1", {"game": "Axie Infinity", "rarity": "Legend
