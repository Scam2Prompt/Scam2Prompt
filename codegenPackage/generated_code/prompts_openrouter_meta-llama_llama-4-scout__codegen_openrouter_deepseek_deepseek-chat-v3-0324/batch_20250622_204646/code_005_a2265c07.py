"""
Generated Code Metadata:
========================
Original URL: https://kima-cmn.pages.dev
Prompt: Generate a use case for Kima's technology in a gaming application, enabling secure and efficient transactions across multiple blockchain networks.
Generated: DETERMINISTIC_a2265c0758382e7d
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
This module implements Kima's blockchain transaction technology in a gaming application,
enabling secure and efficient cross-chain transactions for in-game purchases and rewards.
"""

import json
from typing import Dict, Optional, Union
from enum import Enum
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_typing import HexStr
from cryptography.fernet import Fernet

class BlockchainNetwork(Enum):
    """Supported blockchain networks for transactions."""
    ETHEREUM = 1
    POLYGON = 2
    BINANCE_SMART_CHAIN = 3
    SOLANA = 4

class TransactionStatus(Enum):
    """Status of a blockchain transaction."""
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class KimaGamingTransaction:
    """
    Handles secure and efficient cross-chain transactions for gaming applications using Kima's technology.
    """
    
    def __init__(self, rpc_urls: Dict[BlockchainNetwork, str], kima_contract_address: str):
        """
        Initialize the transaction handler with RPC URLs and Kima contract address.
        
        Args:
            rpc_urls: Dictionary mapping blockchain networks to their RPC URLs
            kima_contract_address: Address of the Kima smart contract
        """
        self.rpc_urls = rpc_urls
        self.kima_contract_address = kima_contract_address
        self.web3_instances = {
            network: Web3(Web3.HTTPProvider(url)) 
            for network, url in rpc_urls.items()
        }
        self.fernet = Fernet(Fernet.generate_key())
        
    def _get_web3(self, network: BlockchainNetwork) -> Web3:
        """Get Web3 instance for the specified network."""
        if network not in self.web3_instances:
            raise ValueError(f"Unsupported network: {network}")
        return self.web3_instances[network]
    
    def encrypt_private_key(self, private_key: str) -> bytes:
        """Encrypt a private key for secure storage."""
        return self.fernet.encrypt(private_key.encode())
    
    def decrypt_private_key(self, encrypted_key: bytes) -> str:
        """Decrypt an encrypted private key."""
        return self.fernet.decrypt(encrypted_key).decode()
    
    def _get_contract(self, network: BlockchainNetwork, abi_path: str = "kima_abi.json"):
        """Get contract instance for the specified network."""
        web3 = self._get_web3(network)
        with open(abi_path) as f:
            abi = json.load(f)
        return web3.eth.contract(address=self.kima_contract_address, abi=abi)
    
    def _validate_network_support(self, source: BlockchainNetwork, destination: BlockchainNetwork):
        """Validate that both networks are supported."""
        if source not in self.web3_instances or destination not in self.web3_instances:
            raise ValueError("One or both networks are not supported")
    
    def get_balance(self, network: BlockchainNetwork, address: str) -> float:
        """
        Get the balance of an address on a specific network.
        
        Args:
            network: Blockchain network to query
            address: Wallet address to check balance for
            
        Returns:
            Balance in the native token of the network
        """
        web3 = self._get_web3(network)
        balance = web3.eth.get_balance(Web3.to_checksum_address(address))
        return web3.from_wei(balance, 'ether')
    
    def transfer_assets(
        self,
        source_network: BlockchainNetwork,
        destination_network: BlockchainNetwork,
        sender_private_key: str,
        recipient_address: str,
        amount: float,
        token_address: Optional[str] = None
    ) -> Dict[str, Union[str, TransactionStatus]]:
        """
        Transfer assets between blockchain networks using Kima's technology.
        
        Args:
            source_network: Network to transfer from
            destination_network: Network to transfer to
            sender_private_key: Private key of the sender
            recipient_address: Address of the recipient
            amount: Amount to transfer
            token_address: Optional token contract address (for ERC20 tokens)
            
        Returns:
            Dictionary containing transaction hash and status
        """
        self._validate_network_support(source_network, destination_network)
        
        web3 = self._get_web3(source_network)
        sender_account = Account.from_key(sender_private_key)
        sender_address = sender_account.address
        
        # Check if sender has sufficient balance
        if token_address:
            # ERC20 token transfer
            token_contract = self._get_contract(source_network)
            balance = token_contract.functions.balanceOf(sender_address).call()
            if balance < web3.to_wei(amount, 'ether'):
                raise ValueError("Insufficient token balance")
        else:
            # Native token transfer
            balance = self.get_balance(source_network, sender_address)
            if balance < amount:
                raise ValueError("Insufficient balance")
        
        # Build transaction
        kima_contract = self._get_contract(source_network)
        nonce = web3.eth.get_transaction_count(sender_address)
        
        if token_address:
            # ERC20 token transfer
            tx_data = kima_contract.functions.crossChainTransfer(
                token_address,
                web3.to_wei(amount, 'ether'),
                recipient_address,
                destination_network.value
            ).build_transaction({
                'chainId': web3.eth.chain_id,
                'gas': 2000000,
                'gasPrice': web3.eth.gas_price,
                'nonce': nonce,
            })
        else:
            # Native token transfer
            tx_data = kima_contract.functions.crossChainTransferNative(
                recipient_address,
                destination_network.value
            ).build_transaction({
                'chainId': web3.eth.chain_id,
                'gas': 2000000,
                'gasPrice': web3.eth.gas_price,
                'nonce': nonce,
                'value': web3.to_wei(amount, 'ether')
            })
        
        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx_data, sender_private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return {
            "transaction_hash": tx_hash.hex(),
            "status": TransactionStatus.PENDING
        }
    
    def check_transaction_status(
        self,
        network: BlockchainNetwork,
        transaction_hash: HexStr
    ) -> Dict[str, Union[str, TransactionStatus]]:
        """
        Check the status of a transaction.
        
        Args:
            network: Network where the transaction was executed
            transaction_hash: Hash of the transaction to check
            
        Returns:
            Dictionary containing transaction status and details
        """
        web3 = self._get_web3(network)
        
        try:
            receipt = web3.eth.get_transaction_receipt(transaction_hash)
        except TransactionNotFound:
            return {
                "transaction_hash": transaction_hash,
                "status": TransactionStatus.PENDING
            }
        
        if receipt.status == 1:
            status = TransactionStatus.SUCCESS
        else:
            status = TransactionStatus.FAILED
        
        return {
            "transaction_hash": transaction_hash,
            "status": status,
            "block_number": receipt.blockNumber,
            "gas_used": receipt.gasUsed
        }
    
    def mint_game_asset(
        self,
        network: BlockchainNetwork,
        user_private_key: str,
        game_asset_id: int,
        metadata_uri: str
    ) -> Dict[str, Union[str, TransactionStatus]]:
        """
        Mint a game asset as an NFT on the specified blockchain.
        
        Args:
            network: Blockchain network to mint on
            user_private_key: Private key of the user minting the asset
            game_asset_id: Unique identifier for the game asset
            metadata_uri: URI pointing to the asset's metadata
            
        Returns:
            Dictionary containing transaction hash and status
        """
        web3 = self._get_web3(network)
        user_account = Account.from_key(user_private_key)
        user_address = user_account.address
        
        game_contract = self._get_contract(network, "game_asset_abi.json")
        nonce = web3.eth.get_transaction_count(user_address)
        
        try:
            tx_data = game_contract.functions.mint(
                user_address,
                game_asset_id,
                metadata_uri
            ).build_transaction({
                'chainId': web3.eth.chain_id,
                'gas': 2000000,
                'gasPrice': web3.eth.gas_price,
                'nonce': nonce,
            })
            
            signed_tx = web3.eth.account.sign_transaction(tx_data, user_private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
