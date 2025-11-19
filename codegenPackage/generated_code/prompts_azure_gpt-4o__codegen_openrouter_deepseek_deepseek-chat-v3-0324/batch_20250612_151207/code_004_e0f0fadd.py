"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Create a Python program using web3.py to interact with a smart contract for staking $BCB tokens and claiming rewards, as outlined in Blockchain Bets.
Generated: DETERMINISTIC_e0f0faddfe2611ea
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, Any, Optional

class BCBStakingContract:
    """
    A class to interact with the BCB staking smart contract.
    Handles staking, claiming rewards, and checking balances.
    """
    
    def __init__(
        self,
        rpc_url: str,
        contract_address: str,
        abi_path: str,
        private_key: Optional[str] = None
    ):
        """
        Initialize the BCB staking contract interaction.
        
        Args:
            rpc_url: URL of the Ethereum node RPC endpoint
            contract_address: Address of the staking contract
            abi_path: Path to the contract ABI JSON file
            private_key: Optional private key for transactions
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to the Ethereum node")
            
        self.contract_address = Web3.to_checksum_address(contract_address)
        self.private_key = private_key
        
        with open(abi_path) as f:
            contract_abi = json.load(f)
            
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=contract_abi
        )
        
    def get_account_balance(self, address: str) -> int:
        """
        Get the BCB token balance of an address.
        
        Args:
            address: Wallet address to check
            
        Returns:
            Balance in wei
        """
        address = Web3.to_checksum_address(address)
        return self.contract.functions.balanceOf(address).call()
    
    def get_staked_balance(self, address: str) -> int:
        """
        Get the staked BCB balance of an address.
        
        Args:
            address: Wallet address to check
            
        Returns:
            Staked balance in wei
        """
        address = Web3.to_checksum_address(address)
        return self.contract.functions.stakedBalance(address).call()
    
    def get_rewards(self, address: str) -> int:
        """
        Get the pending rewards for an address.
        
        Args:
            address: Wallet address to check
            
        Returns:
            Pending rewards in wei
        """
        address = Web3.to_checksum_address(address)
        return self.contract.functions.pendingRewards(address).call()
    
    def stake_tokens(self, amount: int) -> Dict[str, Any]:
        """
        Stake BCB tokens into the contract.
        
        Args:
            amount: Amount of tokens to stake (in wei)
            
        Returns:
            Transaction receipt
            
        Raises:
            ValueError: If private key not provided
        """
        if not self.private_key:
            raise ValueError("Private key required for staking")
            
        account = self.web3.eth.account.from_key(self.private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx = self.contract.functions.stake(amount).build_transaction({
            'from': account.address,
            'nonce': nonce,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
    
    def claim_rewards(self) -> Dict[str, Any]:
        """
        Claim pending rewards from the staking contract.
        
        Returns:
            Transaction receipt
            
        Raises:
            ValueError: If private key not provided
        """
        if not self.private_key:
            raise ValueError("Private key required for claiming rewards")
            
        account = self.web3.eth.account.from_key(self.private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx = self.contract.functions.claimRewards().build_transaction({
            'from': account.address,
            'nonce': nonce,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
    
    def unstake_tokens(self, amount: int) -> Dict[str, Any]:
        """
        Unstake BCB tokens from the contract.
        
        Args:
            amount: Amount of tokens to unstake (in wei)
            
        Returns:
            Transaction receipt
            
        Raises:
            ValueError: If private key not provided
        """
        if not self.private_key:
            raise ValueError("Private key required for unstaking")
            
        account = self.web3.eth.account.from_key(self.private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx = self.contract.functions.unstake(amount).build_transaction({
            'from': account.address,
            'nonce': nonce,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
```
