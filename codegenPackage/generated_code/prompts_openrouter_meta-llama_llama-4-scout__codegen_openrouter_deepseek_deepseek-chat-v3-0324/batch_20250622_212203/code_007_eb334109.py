"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Implement a staking and yield farming system for a cryptocurrency project, as part of its ecosystem expansion and partnership strategy.
Generated: DETERMINISTIC_eb334109d6cec073
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
import time
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum, auto
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError
from eth_typing import ChecksumAddress
from eth_account import Account
from eth_account.signers.local import LocalAccount


class StakingError(Exception):
    """Base exception for staking-related errors."""
    pass


class InsufficientBalanceError(StakingError):
    """Raised when user has insufficient balance for staking."""
    pass


class StakeNotFoundError(StakingError):
    """Raised when a stake is not found."""
    pass


class PoolNotFoundError(StakingError):
    """Raised when a pool is not found."""
    pass


class PoolState(Enum):
    ACTIVE = auto()
    PAUSED = auto()
    CLOSED = auto()


@dataclass
class Stake:
    stake_id: int
    user_address: ChecksumAddress
    pool_id: int
    amount: int
    start_time: int
    duration: int
    claimed_rewards: int = 0
    is_active: bool = True


@dataclass
class Pool:
    pool_id: int
    token_address: ChecksumAddress
    reward_token_address: ChecksumAddress
    apr: float
    min_stake_amount: int
    max_stake_amount: int
    min_stake_duration: int
    max_stake_duration: int
    total_staked: int = 0
    state: PoolState = PoolState.ACTIVE
    created_at: int = int(time.time())


class StakingSystem:
    def __init__(self, web3: Web3, staking_token_address: ChecksumAddress):
        self.web3 = web3
        self.staking_token_address = staking_token_address
        self.pools: Dict[int, Pool] = {}
        self.stakes: Dict[int, Stake] = {}
        self.next_pool_id = 1
        self.next_stake_id = 1
        self.admin: Optional[ChecksumAddress] = None

    def set_admin(self, address: ChecksumAddress) -> None:
        """Set the admin address for privileged operations."""
        self.admin = address

    def _validate_admin(self, caller: ChecksumAddress) -> None:
        """Validate that the caller is the admin."""
        if self.admin is None:
            raise StakingError("Admin address not set")
        if caller.lower() != self.admin.lower():
            raise StakingError("Caller is not the admin")

    def create_pool(
        self,
        caller: ChecksumAddress,
        token_address: ChecksumAddress,
        reward_token_address: ChecksumAddress,
        apr: float,
        min_stake_amount: int,
        max_stake_amount: int,
        min_stake_duration: int,
        max_stake_duration: int,
    ) -> int:
        """Create a new staking pool."""
        self._validate_admin(caller)

        if apr <= 0:
            raise StakingError("APR must be positive")
        if min_stake_amount <= 0:
            raise StakingError("Minimum stake amount must be positive")
        if max_stake_amount <= min_stake_amount:
            raise StakingError("Maximum stake amount must be greater than minimum")
        if min_stake_duration <= 0:
            raise StakingError("Minimum stake duration must be positive")
        if max_stake_duration <= min_stake_duration:
            raise StakingError("Maximum stake duration must be greater than minimum")

        pool_id = self.next_pool_id
        self.pools[pool_id] = Pool(
            pool_id=pool_id,
            token_address=token_address,
            reward_token_address=reward_token_address,
            apr=apr,
            min_stake_amount=min_stake_amount,
            max_stake_amount=max_stake_amount,
            min_stake_duration=min_stake_duration,
            max_stake_duration=max_stake_duration,
        )
        self.next_pool_id += 1
        return pool_id

    def update_pool_apr(self, caller: ChecksumAddress, pool_id: int, new_apr: float) -> None:
        """Update the APR for a staking pool."""
        self._validate_admin(caller)
        
        if pool_id not in self.pools:
            raise PoolNotFoundError(f"Pool {pool_id} not found")
        if new_apr <= 0:
            raise StakingError("APR must be positive")
            
        self.pools[pool_id].apr = new_apr

    def change_pool_state(self, caller: ChecksumAddress, pool_id: int, new_state: PoolState) -> None:
        """Change the state of a staking pool."""
        self._validate_admin(caller)
        
        if pool_id not in self.pools:
            raise PoolNotFoundError(f"Pool {pool_id} not found")
            
        self.pools[pool_id].state = new_state

    def stake(
        self,
        user_address: ChecksumAddress,
        pool_id: int,
        amount: int,
        duration: int,
        private_key: Optional[str] = None,
    ) -> int:
        """Stake tokens into a pool."""
        if pool_id not in self.pools:
            raise PoolNotFoundError(f"Pool {pool_id} not found")
            
        pool = self.pools[pool_id]
        
        if pool.state != PoolState.ACTIVE:
            raise StakingError("Pool is not active for staking")
        if amount < pool.min_stake_amount:
            raise StakingError(f"Amount below minimum stake of {pool.min_stake_amount}")
        if amount > pool.max_stake_amount:
            raise StakingError(f"Amount exceeds maximum stake of {pool.max_stake_amount}")
        if duration < pool.min_stake_duration:
            raise StakingError(f"Duration below minimum of {pool.min_stake_duration}")
        if duration > pool.max_stake_duration:
            raise StakingError(f"Duration exceeds maximum of {pool.max_stake_duration}")

        # In a real implementation, we would transfer tokens from user to contract here
        if private_key:
            account: LocalAccount = Account.from_key(private_key)
            if account.address.lower() != user_address.lower():
                raise StakingError("Private key does not match user address")
            
            # This would be replaced with actual token transfer in a real implementation
            # token_contract = self.web3.eth.contract(
            #     address=pool.token_address,
            #     abi=ERC20_ABI
            # )
            # tx_hash = token_contract.functions.transferFrom(
            #     user_address,
            #     self.web3.eth.default_account,
            #     amount
            # ).transact({'from': user_address})
            # self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
        stake_id = self.next_stake_id
        self.stakes[stake_id] = Stake(
            stake_id=stake_id,
            user_address=user_address,
            pool_id=pool_id,
            amount=amount,
            start_time=int(time.time()),
            duration=duration,
        )
        
        pool.total_staked += amount
        self.next_stake_id += 1
        return stake_id

    def unstake(self, user_address: ChecksumAddress, stake_id: int) -> None:
        """Unstake tokens from a pool."""
        if stake_id not in self.stakes:
            raise StakeNotFoundError(f"Stake {stake_id} not found")
            
        stake = self.stakes[stake_id]
        
        if stake.user_address.lower() != user_address.lower():
            raise StakingError("Stake does not belong to caller")
        if not stake.is_active:
            raise StakingError("Stake is already inactive")
        if time.time() < stake.start_time + stake.duration:
            raise StakingError("Stake duration has not ended")

        pool = self.pools[stake.pool_id]
        
        # Claim any remaining rewards first
        self._claim_rewards(stake)
        
        # In a real implementation, we would transfer tokens back to user here
        # token_contract = self.web3.eth.contract(
        #     address=pool.token_address,
        #     abi=ERC20_ABI
        # )
        # tx_hash = token_contract.functions.transfer(
        #     user_address,
        #     stake.amount
        # ).transact({'from': self.web3.eth.default_account})
        # self.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        stake.is_active = False
        pool.total_staked -= stake.amount

    def claim_rewards(self, user_address: ChecksumAddress, stake_id: int) -> int:
        """Claim rewards for a stake."""
        if stake_id not in self.stakes:
            raise StakeNotFoundError(f"Stake {stake_id} not found")
            
        stake = self.stakes[stake_id]
        
        if stake.user_address.lower() != user_address.lower():
            raise StakingError("
