"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: Generate a code example for a decentralized application (dApp) that utilizes the Data Ownership Protocol (DOP) for private transactions and selective disclosure of token holdings.
Generated: DETERMINISTIC_2255f9e9bc462764
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dApp using Data Ownership Protocol (DOP) for private transactions and selective disclosure
import hashlib
import json
from typing import Dict, List, Optional, Tuple
from web3 import Web3
from eth_account import Account
from eth_keys import keys
from eth_utils import keccak, to_checksum_address

# DOP Contract ABI (simplified for example)
DOP_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "bytes32", "name": "commitment", "type": "bytes32"}
        ],
        "name": "registerCommitment",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "nullifier", "type": "bytes32"}
        ],
        "name": "checkNullifier",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "receiver", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes32", "name": "nullifier", "type": "bytes32"},
            {"internalType": "bytes32", "name": "commitment", "type": "bytes32"},
            {"internalType": "bytes", "name": "zkProof", "type": "bytes"}
        ],
        "name": "transferPrivate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "verifier", "type": "address"},
            {"internalType": "bytes32", "name": "commitment", "type": "bytes32"},
            {"internalType": "bytes", "name": "zkProof", "type": "bytes"}
        ],
        "name": "discloseBalance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

class DOPClient:
    """
    Client for interacting with the Data Ownership Protocol (DOP) smart contract.
    Handles private transactions and selective disclosure of token holdings.
    """
    
    def __init__(self, web3: Web3, contract_address: str, private_key: str):
        """
        Initialize DOP client with Web3 instance and contract details.
        
        Args:
            web3: Web3 instance connected to blockchain
            contract_address: Address of DOP smart contract
            private_key: Private key for signing transactions
        """
        self.web3 = web3
        self.contract_address = contract_address
        self.private_key = private_key
        self.account = Account.from_key(private_key)
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=DOP_ABI
        )
    
    def generate_commitment(self, secret: str) -> bytes:
        """
        Generate a commitment hash from a secret.
        
        Args:
            secret: Random secret for commitment
            
        Returns:
            bytes32 commitment hash
        """
        return keccak(text=secret)
    
    def register_commitment(self, commitment: bytes) -> str:
        """
        Register a commitment on the DOP contract.
        
        Args:
            commitment: Commitment hash to register
            
        Returns:
            Transaction hash
        """
        tx = self.contract.functions.registerCommitment(
            self.account.address,
            commitment
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 200000
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def transfer_private(
        self,
        receiver: str,
        amount: int,
        nullifier: bytes,
        commitment: bytes,
        zk_proof: bytes
    ) -> str:
        """
        Execute a private token transfer using DOP.
        
        Args:
            receiver: Recipient address
            amount: Amount to transfer
            nullifier: Nullifier to prevent double spending
            commitment: New commitment for receiver
            zk_proof: Zero-knowledge proof
            
        Returns:
            Transaction hash
        """
        tx = self.contract.functions.transferPrivate(
            receiver,
            amount,
            nullifier,
            commitment,
            zk_proof
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 500000
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def disclose_balance(
        self,
        verifier: str,
        commitment: bytes,
        zk_proof: bytes
    ) -> str:
        """
        Disclose balance selectively to a verifier using DOP.
        
        Args:
            verifier: Address of verifier
            commitment: Commitment to disclose
            zk_proof: Zero-knowledge proof
            
        Returns:
            Transaction hash
        """
        tx = self.contract.functions.discloseBalance(
            verifier,
            commitment,
            zk_proof
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 300000
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def check_nullifier(self, nullifier: bytes) -> bool:
        """
        Check if a nullifier has been used.
        
        Args:
            nullifier: Nullifier to check
            
        Returns:
            bool: True if nullifier has been used, False otherwise
        """
        return self.contract.functions.checkNullifier(nullifier).call()

class DOPApp:
    """
    Example dApp using DOP for private transactions and selective disclosure.
    """
    
    def __init__(self, web3: Web3, contract_address: str, private_key: str):
        """
        Initialize the dApp with DOP client.
        
        Args:
            web3: Web3 instance
            contract_address: DOP contract address
            private_key: User's private key
        """
        self.client = DOPClient(web3, contract_address, private_key)
        self.secrets = {}  # Store secrets for commitments
    
    def create_private_account(self) -> Tuple[str, bytes]:
        """
        Create a new private account with commitment.
        
        Returns:
            Tuple of (secret, commitment)
        """
        secret = Account.create().privateKey.hex()
        commitment = self.client.generate_commitment(secret)
        self.secrets[commitment.hex()] = secret
        return secret, commitment
    
    def register_account(self) -> str:
        """
        Register a new private account on DOP.
        
        Returns:
            Transaction hash
        """
        secret, commitment = self.create_private_account()
        return self.client.register_commitment(commitment)
    
    def private_transfer(
        self,
        receiver: str,
        amount: int,
        nullifier_secret: str,
        new_secret: str
    ) -> str:
        """
        Perform a private transfer using DOP.
        
        Args:
            receiver: Recipient address
            amount: Amount to transfer
            nullifier_secret: Secret to generate nullifier
            new_secret: Secret for new commitment
            
        Returns:
            Transaction hash
        """
        nullifier = self.client.generate_commitment(nullifier_secret)
        new_commitment = self.client.generate_commitment(new_secret)
        
        # In a real implementation, this would be generated by a zk-SNARK circuit
        zk_proof = b'\x00' * 128  # Placeholder for actual zkProof
        
        return self.client.transfer_private(
            receiver,
            amount,
            nullifier,
            new_commitment,
            zk_proof
        )
    
    def selective_disclosure(
        self,
        verifier: str,
        commitment_secret: str
    ) -> str:
        """
        Disclose balance selectively to a verifier.
        
        Args:
            verifier: Address of verifier
            commitment_secret: Secret for the commitment to disclose
            
        Returns:
            Transaction hash
        """
        commitment = self.client.generate_commitment(commit
