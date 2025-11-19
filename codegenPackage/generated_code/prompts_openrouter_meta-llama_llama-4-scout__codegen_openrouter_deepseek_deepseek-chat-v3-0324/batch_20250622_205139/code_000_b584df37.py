"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: What is Sophon and how does it enable gasless transactions for consumer applications?
Generated: DETERMINISTIC_b584df37670fe109
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sophon_gasless_transactions.py

from typing import Optional, Dict, Any
from dataclasses import dataclass
import json
import requests
from eth_account import Account
from web3 import Web3, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware

@dataclass
class SophonTransaction:
    """
    Represents a gasless transaction processed through Sophon.
    """
    sender: str
    receiver: str
    amount: float
    token_address: Optional[str] = None  # None for native token
    nonce: Optional[int] = None
    signature: Optional[str] = None

class SophonClient:
    """
    Client for interacting with Sophon to enable gasless transactions.
    """
    
    def __init__(self, rpc_url: str, sophon_api_url: str, sponsor_private_key: str):
        """
        Initialize Sophon client.
        
        Args:
            rpc_url: Ethereum RPC endpoint URL
            sophon_api_url: Sophon API endpoint URL
            sponsor_private_key: Private key of the transaction sponsor
        """
        self.web3 = Web3(HTTPProvider(rpc_url))
        self.api_url = sophon_api_url
        self.sponsor_account = Account.from_key(sponsor_private_key)
        
        # Add sponsor account as default account for transactions
        self.web3.middleware_onion.add(
            construct_sign_and_send_raw_middleware(self.sponsor_account)
        )
        self.web3.eth.default_account = self.sponsor_account.address

    def create_gasless_transaction(
        self,
        sender: str,
        receiver: str,
        amount: float,
        token_address: Optional[str] = None
    ) -> SophonTransaction:
        """
        Create a gasless transaction object.
        
        Args:
            sender: Sender's Ethereum address
            receiver: Receiver's Ethereum address
            amount: Amount to transfer
            token_address: Token contract address (None for native token)
            
        Returns:
            SophonTransaction object
        """
        return SophonTransaction(
            sender=sender,
            receiver=receiver,
            amount=amount,
            token_address=token_address
        )

    def sign_transaction(self, transaction: SophonTransaction, private_key: str) -> SophonTransaction:
        """
        Sign the transaction with user's private key.
        
        Args:
            transaction: SophonTransaction to sign
            private_key: User's private key
            
        Returns:
            Signed SophonTransaction
        """
        user_account = Account.from_key(private_key)
        
        # Create message hash
        message = {
            "sender": transaction.sender,
            "receiver": transaction.receiver,
            "amount": transaction.amount,
            "token_address": transaction.token_address,
            "nonce": transaction.nonce
        }
        message_hash = Web3.keccak(text=json.dumps(message))
        
        # Sign the message
        signed_message = Account.sign_message(
            {
                "messageHash": message_hash,
                "message": message
            },
            private_key
        )
        
        transaction.signature = signed_message.signature.hex()
        return transaction

    def submit_gasless_transaction(self, transaction: SophonTransaction) -> Dict[str, Any]:
        """
        Submit gasless transaction to Sophon network.
        
        Args:
            transaction: Signed SophonTransaction
            
        Returns:
            API response from Sophon
            
        Raises:
            Exception: If transaction submission fails
        """
        if not transaction.signature:
            raise ValueError("Transaction must be signed before submission")
        
        payload = {
            "sender": transaction.sender,
            "receiver": transaction.receiver,
            "amount": transaction.amount,
            "token_address": transaction.token_address,
            "nonce": transaction.nonce,
            "signature": transaction.signature
        }
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            f"{self.api_url}/transactions",
            data=json.dumps(payload),
            headers=headers
        )
        
        if response.status_code != 200:
            raise Exception(f"Transaction failed: {response.text}")
            
        return response.json()

    def get_transaction_status(self, tx_hash: str) -> Dict[str, Any]:
        """
        Get status of a submitted transaction.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            Transaction status information
            
        Raises:
            Exception: If status retrieval fails
        """
        response = requests.get(f"{self.api_url}/transactions/{tx_hash}")
        
        if response.status_code != 200:
            raise Exception(f"Status check failed: {response.text}")
            
        return response.json()
```
