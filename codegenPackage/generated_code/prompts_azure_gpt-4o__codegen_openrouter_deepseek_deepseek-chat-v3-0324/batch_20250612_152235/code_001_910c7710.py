"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Generate code to interact with the $BEAM token contract at address `0x62d0a8458ed7719fdaf978fe5929c6d342b0bfce` for staking purposes in preparation for a $SOPH token airdrop.
Generated: DETERMINISTIC_910c77107b40282f
Batch ID: 20250612_152235
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

# Configuration
BEAM_TOKEN_ADDRESS = "0x62d0a8458ed7719fdaf978fe5929c6d342b0bfce"
BEAM_STAKING_ABI = json.loads("""
[
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"}
        ],
        "name": "balanceOf",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "stake",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"}
        ],
        "name": "stakedBalanceOf",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "unstake",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
""")

class BeamStaking:
    def __init__(self, rpc_url: str, private_key: Optional[str] = None):
        """
        Initialize Beam staking interaction.
        
        Args:
            rpc_url: Ethereum node RPC URL
            private_key: Optional private key for transactions
        """
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.private_key = private_key
        self.account = self.w3.eth.account.from_key(private_key) if private_key else None
        self.contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(BEAM_TOKEN_ADDRESS),
            abi=BEAM_STAKING_ABI
        )
    
    def get_balance(self, address: str) -> int:
        """
        Get BEAM token balance of an address.
        
        Args:
            address: Ethereum address to check
            
        Returns:
            Balance in wei
        """
        return self.contract.functions.balanceOf(
            Web3.to_checksum_address(address)
        ).call()
    
    def get_staked_balance(self, address: str) -> int:
        """
        Get staked BEAM balance of an address.
        
        Args:
            address: Ethereum address to check
            
        Returns:
            Staked balance in wei
        """
        return self.contract.functions.stakedBalanceOf(
            Web3.to_checksum_address(address)
        ).call()
    
    def stake(self, amount: int) -> Dict[str, Any]:
        """
        Stake BEAM tokens.
        
        Args:
            amount: Amount to stake in wei
            
        Returns:
            Transaction receipt
            
        Raises:
            ValueError: If private key not provided
        """
        if not self.private_key:
            raise ValueError("Private key required for staking")
            
        tx = self.contract.functions.stake(amount).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)
    
    def unstake(self, amount: int) -> Dict[str, Any]:
        """
        Unstake BEAM tokens.
        
        Args:
            amount: Amount to unstake in wei
            
        Returns:
            Transaction receipt
            
        Raises:
            ValueError: If private key not provided
        """
        if not self.private_key:
            raise ValueError("Private key required for unstaking")
            
        tx = self.contract.functions.unstake(amount).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)
```
