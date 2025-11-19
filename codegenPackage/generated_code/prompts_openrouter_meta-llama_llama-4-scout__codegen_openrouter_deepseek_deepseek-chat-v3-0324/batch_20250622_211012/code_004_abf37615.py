"""
Generated Code Metadata:
========================
Original URL: https://dappass.neocities.org
Prompt: Create a library for interacting with the Dapp Pass smart contract, including functions for minting, transferring, and checking ownership of the digital asset.
Generated: DETERMINISTIC_abf376150060de72
Batch ID: 20250622_211012
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
from web3.exceptions import ContractLogicError, TransactionNotFound
from typing import Optional, Dict, Any

class DappPassContract:
    """
    A library for interacting with the Dapp Pass smart contract.
    Handles minting, transferring, and checking ownership of digital assets.
    """

    def __init__(self, provider_url: str, contract_address: str, abi_path: str, private_key: str):
        """
        Initialize the DappPassContract with provider, contract details, and private key.

        Args:
            provider_url: URL of the Ethereum provider (e.g., Infura, local node)
            contract_address: Address of the deployed Dapp Pass contract
            abi_path: Path to the contract's ABI JSON file
            private_key: Private key for transaction signing
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.private_key = private_key
        self.account = self.web3.eth.account.from_key(private_key)
        
        with open(abi_path) as f:
            abi = json.load(f)
        
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)

    def mint(self, to_address: str, token_id: int, token_uri: str) -> Dict[str, Any]:
        """
        Mint a new Dapp Pass token.

        Args:
            to_address: Address to receive the minted token
            token_id: Unique ID for the new token
            token_uri: URI pointing to the token's metadata

        Returns:
            Transaction receipt

        Raises:
            ValueError: If input validation fails
            ContractLogicError: If contract operation fails
            Exception: For other transaction errors
        """
        if not self.web3.is_address(to_address):
            raise ValueError("Invalid recipient address")
        
        if not isinstance(token_id, int) or token_id <= 0:
            raise ValueError("Token ID must be a positive integer")

        try:
            nonce = self.web3.eth.get_transaction_count(self.account.address)
            tx = self.contract.functions.mint(
                to_address,
                token_id,
                token_uri
            ).build_transaction({
                'from': self.account.address,
                'nonce': nonce,
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price
            })

            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.web3.eth.wait_for_transaction_receipt(tx_hash)
        except ContractLogicError as e:
            raise ContractLogicError(f"Contract error during mint: {e}")
        except Exception as e:
            raise Exception(f"Transaction failed: {e}")

    def transfer(self, from_address: str, to_address: str, token_id: int) -> Dict[str, Any]:
        """
        Transfer a Dapp Pass token between addresses.

        Args:
            from_address: Current owner's address
            to_address: New owner's address
            token_id: ID of the token to transfer

        Returns:
            Transaction receipt

        Raises:
            ValueError: If input validation fails
            ContractLogicError: If contract operation fails
            Exception: For other transaction errors
        """
        if not (self.web3.is_address(from_address) and self.web3.is_address(to_address)):
            raise ValueError("Invalid address provided")

        if not isinstance(token_id, int) or token_id <= 0:
            raise ValueError("Token ID must be a positive integer")

        try:
            nonce = self.web3.eth.get_transaction_count(self.account.address)
            tx = self.contract.functions.transferFrom(
                from_address,
                to_address,
                token_id
            ).build_transaction({
                'from': self.account.address,
                'nonce': nonce,
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price
            })

            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.web3.eth.wait_for_transaction_receipt(tx_hash)
        except ContractLogicError as e:
            raise ContractLogicError(f"Contract error during transfer: {e}")
        except Exception as e:
            raise Exception(f"Transaction failed: {e}")

    def get_owner(self, token_id: int) -> Optional[str]:
        """
        Get the owner of a specific Dapp Pass token.

        Args:
            token_id: ID of the token to query

        Returns:
            Owner's address if token exists, None otherwise

        Raises:
            ValueError: If token_id is invalid
            ContractLogicError: If contract operation fails
        """
        if not isinstance(token_id, int) or token_id <= 0:
            raise ValueError("Token ID must be a positive integer")

        try:
            owner = self.contract.functions.ownerOf(token_id).call()
            return owner
        except ContractLogicError as e:
            if "nonexistent token" in str(e).lower():
                return None
            raise ContractLogicError(f"Contract error during owner query: {e}")

    def get_token_uri(self, token_id: int) -> Optional[str]:
        """
        Get the URI of a specific Dapp Pass token's metadata.

        Args:
            token_id: ID of the token to query

        Returns:
            Token URI if token exists, None otherwise

        Raises:
            ValueError: If token_id is invalid
            ContractLogicError: If contract operation fails
        """
        if not isinstance(token_id, int) or token_id <= 0:
            raise ValueError("Token ID must be a positive integer")

        try:
            uri = self.contract.functions.tokenURI(token_id).call()
            return uri
        except ContractLogicError as e:
            if "nonexistent token" in str(e).lower():
                return None
            raise ContractLogicError(f"Contract error during URI query: {e}")
```
