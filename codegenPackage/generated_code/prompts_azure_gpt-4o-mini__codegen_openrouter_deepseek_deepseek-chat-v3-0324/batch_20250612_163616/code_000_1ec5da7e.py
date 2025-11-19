"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Generate a code snippet for a crypto wallet integration that emphasizes user ownership and permissionless networks, as discussed by Innodapter ApS.
Generated: DETERMINISTIC_1ec5da7e553bf1b2
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import hmac
from typing import Dict, Optional, Tuple
from web3 import Web3, HTTPProvider
from eth_account import Account
from eth_keys import keys
from eth_utils import to_checksum_address

class CryptoWallet:
    """
    A permissionless, non-custodial crypto wallet integration.
    Emphasizes user ownership of private keys and interaction with permissionless networks.
    """
    
    def __init__(self, rpc_url: str, chain_id: int):
        """
        Initialize the wallet with a connection to a blockchain node.
        
        Args:
            rpc_url: URL of the Ethereum node RPC endpoint
            chain_id: Chain ID of the network (1=Mainnet, 5=Goerli, etc.)
        """
        self.web3 = Web3(HTTPProvider(rpc_url))
        self.chain_id = chain_id
        self.account = None
        
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")
    
    def create_wallet(self) -> Tuple[str, str]:
        """
        Generate a new wallet with private key and address.
        
        Returns:
            Tuple of (private_key, address)
        """
        acct = Account.create()
        self.account = acct
        return acct.key.hex(), acct.address
    
    def import_wallet(self, private_key: str) -> str:
        """
        Import an existing wallet from a private key.
        
        Args:
            private_key: Hex string of the private key
            
        Returns:
            Wallet address
        """
        if not private_key.startswith('0x'):
            private_key = '0x' + private_key
            
        acct = Account.from_key(private_key)
        self.account = acct
        return acct.address
    
    def sign_transaction(self, to: str, value: float, gas_limit: int, 
                        gas_price: Optional[int] = None) -> Dict:
        """
        Create and sign a transaction.
        
        Args:
            to: Recipient address
            value: Amount to send in ETH
            gas_limit: Gas limit for transaction
            gas_price: Optional gas price (defaults to current network price)
            
        Returns:
            Signed transaction dictionary
        """
        if not self.account:
            raise ValueError("No wallet loaded")
            
        if not self.web3.is_address(to):
            raise ValueError("Invalid recipient address")
            
        to = to_checksum_address(to)
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        
        tx = {
            'chainId': self.chain_id,
            'from': self.account.address,
            'to': to,
            'value': self.web3.to_wei(value, 'ether'),
            'gas': gas_limit,
            'nonce': nonce,
        }
        
        if gas_price:
            tx['gasPrice'] = gas_price
        else:
            tx['gasPrice'] = self.web3.eth.gas_price
            
        signed = self.account.sign_transaction(tx)
        return signed.rawTransaction.hex()
    
    def sign_message(self, message: str) -> str:
        """
        Sign a message with the wallet's private key.
        
        Args:
            message: String message to sign
            
        Returns:
            Hex string of the signature
        """
        if not self.account:
            raise ValueError("No wallet loaded")
            
        msg_hash = self.web3.keccak(text=message)
        signed = self.account.sign_message(msg_hash)
        return signed.signature.hex()
    
    def verify_signature(self, address: str, message: str, signature: str) -> bool:
        """
        Verify a message signature.
        
        Args:
            address: Address that supposedly signed the message
            message: Original message
            signature: Signature to verify
            
        Returns:
            True if signature is valid
        """
        msg_hash = self.web3.keccak(text=message)
        pubkey = keys.Signature(bytes.fromhex(signature[2:])).recover_public_key_from_msg_hash(msg_hash)
        recovered_address = pubkey.to_checksum_address()
        return recovered_address == to_checksum_address(address)
```
