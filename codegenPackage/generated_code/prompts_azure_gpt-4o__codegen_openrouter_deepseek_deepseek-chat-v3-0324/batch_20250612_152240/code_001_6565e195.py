"""
Generated Code Metadata:
========================
Original URL: https://decentralizedchain.on.fleek.co
Prompt: Generate code to mint or transfer NFTs using Decentralize Chain's self-custodial wallet system and provide support for receiving NFTs.
Generated: DETERMINISTIC_6565e195259f2f74
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
import requests
from web3 import Web3
from web3.exceptions import TransactionNotFound
from eth_account import Account
from eth_account.messages import encode_defunct
from typing import Optional, Dict, Any, Union

class NFTManager:
    """
    A class to handle NFT minting, transferring, and receiving operations 
    using Decentralize Chain's self-custodial wallet system.
    """
    
    def __init__(self, rpc_url: str, chain_id: int, contract_address: str, contract_abi: str):
        """
        Initialize the NFTManager with blockchain connection details.
        
        Args:
            rpc_url: The RPC URL of the blockchain node.
            chain_id: The chain ID of the blockchain network.
            contract_address: The address of the NFT contract.
            contract_abi: The ABI of the NFT contract.
        """
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to the blockchain node")
        
        self.chain_id = chain_id
        self.contract_address = contract_address
        self.contract_abi = json.loads(contract_abi)
        self.contract = self.w3.eth.contract(
            address=self.w3.to_checksum_address(contract_address),
            abi=self.contract_abi
        )
    
    def _sign_transaction(self, private_key: str, transaction: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sign a transaction with the provided private key.
        
        Args:
            private_key: The private key to sign the transaction.
            transaction: The transaction dictionary.
            
        Returns:
            The signed transaction.
        """
        account = Account.from_key(private_key)
        signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key)
        return signed_txn
    
    def _send_transaction(self, signed_txn: Dict[str, Any]) -> str:
        """
        Send a signed transaction to the blockchain.
        
        Args:
            signed_txn: The signed transaction.
            
        Returns:
            The transaction hash.
            
        Raises:
            ValueError: If the transaction fails.
        """
        try:
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise ValueError(f"Transaction failed: {str(e)}")
    
    def mint_nft(self, private_key: str, to_address: str, token_uri: str) -> str:
        """
        Mint a new NFT and assign it to the specified address.
        
        Args:
            private_key: The private key of the minter.
            to_address: The address to receive the NFT.
            token_uri: The URI of the NFT metadata.
            
        Returns:
            The transaction hash of the mint operation.
        """
        to_address = self.w3.to_checksum_address(to_address)
        nonce = self.w3.eth.get_transaction_count(Account.from_key(private_key).address)
        
        transaction = self.contract.functions.mint(to_address, token_uri).build_transaction({
            'chainId': self.chain_id,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': nonce,
        })
        
        signed_txn = self._sign_transaction(private_key, transaction)
        return self._send_transaction(signed_txn)
    
    def transfer_nft(self, private_key: str, from_address: str, to_address: str, token_id: int) -> str:
        """
        Transfer an NFT from one address to another.
        
        Args:
            private_key: The private key of the sender.
            from_address: The current owner's address.
            to_address: The address to receive the NFT.
            token_id: The ID of the NFT to transfer.
            
        Returns:
            The transaction hash of the transfer operation.
        """
        from_address = self.w3.to_checksum_address(from_address)
        to_address = self.w3.to_checksum_address(to_address)
        nonce = self.w3.eth.get_transaction_count(Account.from_key(private_key).address)
        
        transaction = self.contract.functions.transferFrom(from_address, to_address, token_id).build_transaction({
            'chainId': self.chain_id,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': nonce,
        })
        
        signed_txn = self._sign_transaction(private_key, transaction)
        return self._send_transaction(signed_txn)
    
    def get_nft_owner(self, token_id: int) -> str:
        """
        Get the current owner of an NFT.
        
        Args:
            token_id: The ID of the NFT.
            
        Returns:
            The owner's address.
        """
        return self.contract.functions.ownerOf(token_id).call()
    
    def get_nft_metadata(self, token_id: int) -> Dict[str, Any]:
        """
        Get the metadata of an NFT.
        
        Args:
            token_id: The ID of the NFT.
            
        Returns:
            The NFT metadata as a dictionary.
        """
        token_uri = self.contract.functions.tokenURI(token_id).call()
        response = requests.get(token_uri)
        response.raise_for_status()
        return response.json()
    
    def get_transaction_receipt(self, tx_hash: str) -> Optional[Dict[str, Any]]:
        """
        Get the transaction receipt for a given transaction hash.
        
        Args:
            tx_hash: The transaction hash.
            
        Returns:
            The transaction receipt, or None if not found.
        """
        try:
            return self.w3.eth.get_transaction_receipt(tx_hash)
        except TransactionNotFound:
            return None
    
    def is_nft_received(self, address: str, token_id: int) -> bool:
        """
        Check if an address has received a specific NFT.
        
        Args:
            address: The address to check.
            token_id: The ID of the NFT.
            
        Returns:
            True if the address owns the NFT, False otherwise.
        """
        address = self.w3.to_checksum_address(address)
        owner = self.get_nft_owner(token_id)
        return owner.lower() == address.lower()
```
