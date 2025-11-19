"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Implement a staking solution using Stader Labs' platform on multiple chains (e.g., Ethereum, Polygon, BNB Chain), ensuring secure and efficient staking and reward distribution.
Generated: DETERMINISTIC_c2b7c2744539d1fe
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, List, Optional, Tuple
from eth_account import Account
from eth_typing import ChecksumAddress
from dotenv import load_dotenv
from enum import Enum

# Load environment variables
load_dotenv()

class Chain(Enum):
    ETHEREUM = "ethereum"
    POLYGON = "polygon"
    BNB = "bnb"

# Stader Labs contract addresses for different chains
STADER_CONTRACTS = {
    Chain.ETHEREUM: {
        "staking": "0x...",  # Replace with actual Ethereum staking contract
        "reward": "0x...",   # Replace with actual Ethereum reward contract
    },
    Chain.POLYGON: {
        "staking": "0x...",  # Replace with actual Polygon staking contract
        "reward": "0x...",   # Replace with actual Polygon reward contract
    },
    Chain.BNB: {
        "staking": "0x...",  # Replace with actual BNB staking contract
        "reward": "0x...",   # Replace with actual BNB reward contract
    }
}

# ABI for Stader Labs staking and reward contracts
STAKING_ABI = [...]  # Replace with actual staking contract ABI
REWARD_ABI = [...]   # Replace with actual reward contract ABI

class StaderStaking:
    def __init__(self, chain: Chain, private_key: str = None):
        """
        Initialize Stader staking client for a specific chain.
        
        Args:
            chain: Chain to interact with
            private_key: Optional private key for transactions
        """
        self.chain = chain
        self.private_key = private_key or os.getenv("PRIVATE_KEY")
        
        if not self.private_key:
            raise ValueError("Private key must be provided")
            
        self.account = Account.from_key(self.private_key)
        self.w3 = self._get_web3_instance()
        
        # Initialize contracts
        self.staking_contract = self.w3.eth.contract(
            address=STADER_CONTRACTS[chain]["staking"],
            abi=STAKING_ABI
        )
        self.reward_contract = self.w3.eth.contract(
            address=STADER_CONTRACTS[chain]["reward"],
            abi=REWARD_ABI
        )
    
    def _get_web3_instance(self) -> Web3:
        """Initialize Web3 instance for the specified chain."""
        rpc_url = {
            Chain.ETHEREUM: os.getenv("ETH_RPC_URL"),
            Chain.POLYGON: os.getenv("POLYGON_RPC_URL"),
            Chain.BNB: os.getenv("BNB_RPC_URL")
        }.get(self.chain)
        
        if not rpc_url:
            raise ValueError(f"RPC URL not configured for {self.chain.value}")
            
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Inject POA middleware for Polygon and BNB
        if self.chain in [Chain.POLYGON, Chain.BNB]:
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            
        if not w3.is_connected():
            raise ConnectionError(f"Failed to connect to {self.chain.value} RPC")
            
        return w3
    
    def stake(self, amount: int) -> str:
        """
        Stake tokens to the Stader protocol.
        
        Args:
            amount: Amount of tokens to stake (in wei)
            
        Returns:
            Transaction hash
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
            
        tx = self.staking_contract.functions.stake().build_transaction({
            "from": self.account.address,
            "value": amount,
            "nonce": self.w3.eth.get_transaction_count(self.account.address),
            "gas": 200000,  # Adjust based on chain requirements
            "gasPrice": self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def unstake(self, amount: int) -> str:
        """
        Unstake tokens from the Stader protocol.
        
        Args:
            amount: Amount of tokens to unstake (in wei)
            
        Returns:
            Transaction hash
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be positive")
            
        tx = self.staking_contract.functions.unstake(amount).build_transaction({
            "from": self.account.address,
            "nonce": self.w3.eth.get_transaction_count(self.account.address),
            "gas": 200000,  # Adjust based on chain requirements
            "gasPrice": self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def claim_rewards(self) -> str:
        """
        Claim staking rewards.
        
        Returns:
            Transaction hash
        """
        tx = self.reward_contract.functions.claimRewards().build_transaction({
            "from": self.account.address,
            "nonce": self.w3.eth.get_transaction_count(self.account.address),
            "gas": 200000,  # Adjust based on chain requirements
            "gasPrice": self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_staked_balance(self, address: Optional[ChecksumAddress] = None) -> int:
        """
        Get staked balance for an address.
        
        Args:
            address: Address to check (defaults to connected wallet)
            
        Returns:
            Staked balance in wei
        """
        address = address or self.account.address
        return self.staking_contract.functions.balanceOf(address).call()
    
    def get_pending_rewards(self, address: Optional[ChecksumAddress] = None) -> int:
        """
        Get pending rewards for an address.
        
        Args:
            address: Address to check (defaults to connected wallet)
            
        Returns:
            Pending rewards in wei
        """
        address = address or self.account.address
        return self.reward_contract.functions.pendingRewards(address).call()
    
    def wait_for_transaction(self, tx_hash: str) -> Dict:
        """
        Wait for a transaction to be mined and return receipt.
        
        Args:
            tx_hash: Transaction hash to wait for
            
        Returns:
            Transaction receipt
        """
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize for Polygon
        stader = StaderStaking(Chain.POLYGON)
        
        # Stake 1 MATIC (converted to wei)
        stake_amount = Web3.to_wei(1, "ether")
        tx_hash = stader.stake(stake_amount)
        print(f"Stake transaction sent: {tx_hash}")
        
        # Wait for confirmation
        receipt = stader.wait_for_transaction(tx_hash)
        print(f"Transaction confirmed in block {receipt['blockNumber']}")
        
        # Check staked balance
        balance = stader.get_staked_balance()
        print(f"Staked balance: {Web3.from_wei(balance, 'ether')} MATIC")
        
        # Claim rewards
        rewards = stader.get_pending_rewards()
        if rewards > 0:
            tx_hash = stader.claim_rewards()
            print(f"Claim rewards transaction sent: {tx_hash}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
