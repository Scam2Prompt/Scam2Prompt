"""
Generated Code Metadata:
========================
Original URL: https://noderdapps.com
Prompt: Implement a wallet whitelist and retrieval system using the Dapp Tool protocol, ensuring secure and decentralized access to wallet data.
Generated: DETERMINISTIC_f4374f66c69c08c5
Batch ID: 20250622_212247
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
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from web3 import Web3
from web3.exceptions import ContractLogicError
from eth_account import Account
from eth_keys import keys
from eth_utils import to_checksum_address

# Constants
DAPP_TOOL_PROTOCOL_VERSION = "1.0"
WHITELIST_CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "_wallet", "type": "address"}
        ],
        "name": "isWhitelisted",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_wallet", "type": "address"}
        ],
        "name": "addToWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_wallet", "type": "address"}
        ],
        "name": "removeFromWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

@dataclass
class WalletData:
    address: str
    metadata: Dict[str, str]
    is_whitelisted: bool

class DappToolProtocolError(Exception):
    """Base exception for Dapp Tool Protocol errors"""
    pass

class WhitelistContractError(DappToolProtocolError):
    """Exception for whitelist contract interactions"""
    pass

class WalletValidationError(DappToolProtocolError):
    """Exception for wallet validation errors"""
    pass

class DappToolProtocol:
    def __init__(self, web3_provider: str, contract_address: str):
        """
        Initialize DappToolProtocol with Web3 provider and contract address.
        
        Args:
            web3_provider: URL of the Ethereum node provider
            contract_address: Address of the whitelist smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        if not self.web3.is_connected():
            raise DappToolProtocolError("Failed to connect to Web3 provider")
        
        self.contract_address = to_checksum_address(contract_address)
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=WHITELIST_CONTRACT_ABI
        )

    def validate_wallet_address(self, address: str) -> str:
        """
        Validate and convert wallet address to checksum address.
        
        Args:
            address: Wallet address to validate
            
        Returns:
            Checksum-formatted address
            
        Raises:
            WalletValidationError: If address is invalid
        """
        try:
            return to_checksum_address(address)
        except ValueError as e:
            raise WalletValidationError(f"Invalid wallet address: {e}")

    def is_wallet_whitelisted(self, wallet_address: str) -> bool:
        """
        Check if a wallet is whitelisted in the contract.
        
        Args:
            wallet_address: Address to check
            
        Returns:
            bool: True if whitelisted, False otherwise
            
        Raises:
            WhitelistContractError: If contract call fails
        """
        try:
            wallet_address = self.validate_wallet_address(wallet_address)
            return self.contract.functions.isWhitelisted(wallet_address).call()
        except ContractLogicError as e:
            raise WhitelistContractError(f"Contract call failed: {e}")

    def add_to_whitelist(
        self,
        wallet_address: str,
        private_key: str,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Add a wallet to the whitelist.
        
        Args:
            wallet_address: Address to add to whitelist
            private_key: Private key of the admin wallet
            gas_limit: Gas limit for the transaction
            gas_price: Gas price for the transaction (optional)
            
        Returns:
            str: Transaction hash
            
        Raises:
            WhitelistContractError: If transaction fails
        """
        try:
            wallet_address = self.validate_wallet_address(wallet_address)
            account = Account.from_key(private_key)
            
            tx = self.contract.functions.addToWhitelist(wallet_address).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': gas_limit,
                'gasPrice': gas_price if gas_price else self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except (ContractLogicError, ValueError) as e:
            raise WhitelistContractError(f"Failed to add to whitelist: {e}")

    def remove_from_whitelist(
        self,
        wallet_address: str,
        private_key: str,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Remove a wallet from the whitelist.
        
        Args:
            wallet_address: Address to remove from whitelist
            private_key: Private key of the admin wallet
            gas_limit: Gas limit for the transaction
            gas_price: Gas price for the transaction (optional)
            
        Returns:
            str: Transaction hash
            
        Raises:
            WhitelistContractError: If transaction fails
        """
        try:
            wallet_address = self.validate_wallet_address(wallet_address)
            account = Account.from_key(private_key)
            
            tx = self.contract.functions.removeFromWhitelist(wallet_address).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': gas_limit,
                'gasPrice': gas_price if gas_price else self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except (ContractLogicError, ValueError) as e:
            raise WhitelistContractError(f"Failed to remove from whitelist: {e}")

    def get_wallet_data(self, wallet_address: str) -> WalletData:
        """
        Retrieve wallet data including whitelist status.
        
        Args:
            wallet_address: Address to retrieve data for
            
        Returns:
            WalletData: Wallet data object
            
        Raises:
            WalletValidationError: If address is invalid
        """
        wallet_address = self.validate_wallet_address(wallet_address)
        is_whitelisted = self.is_wallet_whitelisted(wallet_address)
        
        # Generate deterministic metadata hash for demonstration
        metadata_hash = hashlib.sha256(wallet_address.encode()).hexdigest()
        metadata = {
            "protocol_version": DAPP_TOOL_PROTOCOL_VERSION,
            "address_hash": metadata_hash,
            "network": self.web3.eth.chain_id
        }
        
        return WalletData(
            address=wallet_address,
            metadata=metadata,
            is_whitelisted=is_whitelisted
        )

    def get_multiple_wallet_data(self, wallet_addresses: List[str]) -> List[WalletData]:
        """
        Retrieve data for multiple wallets in a single call.
        
        Args:
            wallet_addresses: List of addresses to retrieve data for
            
        Returns:
            List[WalletData]: List of wallet data objects
            
        Raises:
            WalletValidationError: If any address is invalid
        """
        return [self.get_wallet_data(addr) for addr in wallet_addresses]

    def verify_wallet_signature(
        self,
        wallet_address: str,
        message: str,
        signature: str
    ) -> bool:
        """
        Verify a wallet's signature for a given message.
        
        Args:
            wallet_address: Address that signed the message
            message: Original message that was signed
            signature: Signature to verify
            
        Returns:
            bool: True if signature is valid, False otherwise
            
        Raises:
            WalletValidationError: If address is invalid
        """
        wallet_address = self.validate_wallet_address(wallet_address)
        try:
            signer = Account.recover_message(
                text=message,
                signature=signature
            )
            return signer.lower() == wallet_address.lower()
        except ValueError as e:
            raise WalletValidationError(f"Signature verification failed: {e}")
```
