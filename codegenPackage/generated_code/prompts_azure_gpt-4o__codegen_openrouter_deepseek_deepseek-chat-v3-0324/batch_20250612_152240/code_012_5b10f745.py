"""
Generated Code Metadata:
========================
Original URL: https://wandyaeer.pages.dev
Prompt: Write code to manage Defi farming or commercial farming tasks using the decentralized protocol outlined on the Decentralized Dapps website.
Generated: DETERMINISTIC_5b10f7459a3d91de
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, List, Optional, Tuple
from eth_abi import encode_abi
from eth_utils import to_checksum_address, to_hex

# Constants
CONTRACT_ABI = json.loads('''[
    {
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserStake",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]''')

class DeFiFarmingManager:
    """
    A class to manage DeFi farming operations on a decentralized protocol.
    """
    
    def __init__(self, rpc_url: str, contract_address: str, private_key: str):
        """
        Initialize the DeFi farming manager.
        
        Args:
            rpc_url: The RPC URL of the blockchain node.
            contract_address: The address of the farming contract.
            private_key: The private key of the user's wallet.
        """
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to the blockchain node")
            
        self.contract_address = to_checksum_address(contract_address)
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=CONTRACT_ABI)
        self.private_key = private_key
        self.account = self.w3.eth.account.from_key(private_key)
        
    def deposit(self, amount: int) -> str:
        """
        Deposit funds into the farming contract.
        
        Args:
            amount: The amount to deposit in wei.
            
        Returns:
            The transaction hash.
            
        Raises:
            ValueError: If the deposit amount is invalid.
            Exception: If the transaction fails.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
            
        tx = self.contract.functions.deposit().build_transaction({
            'from': self.account.address,
            'value': amount,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def withdraw(self) -> str:
        """
        Withdraw funds and rewards from the farming contract.
        
        Returns:
            The transaction hash.
            
        Raises:
            Exception: If the transaction fails.
        """
        tx = self.contract.functions.withdraw().build_transaction({
            'from': self.account.address,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_user_stake(self, user_address: str) -> int:
        """
        Get the staked amount for a user.
        
        Args:
            user_address: The address of the user.
            
        Returns:
            The staked amount in wei.
        """
        user_address = to_checksum_address(user_address)
        return self.contract.functions.getUserStake(user_address).call()
    
    def get_user_rewards(self, user_address: str) -> int:
        """
        Get the pending rewards for a user.
        
        Args:
            user_address: The address of the user.
            
        Returns:
            The pending rewards in wei.
        """
        user_address = to_checksum_address(user_address)
        return self.contract.functions.getUserRewards(user_address).call()
    
    def wait_for_transaction(self, tx_hash: str) -> Dict:
        """
        Wait for a transaction to be mined and return the receipt.
        
        Args:
            tx_hash: The transaction hash.
            
        Returns:
            The transaction receipt.
            
        Raises:
            Exception: If the transaction fails.
        """
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt.status != 1:
            raise Exception(f"Transaction failed: {tx_hash}")
        return tx_receipt
```
