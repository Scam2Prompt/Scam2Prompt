"""
Generated Code Metadata:
========================
Original URL: https://veipeicoin.pages.dev
Prompt: Generate a code example for a cross-chain bridge to facilitate asset swapping between different blockchain networks, considering the issues related to cross-transfer mentioned on this website.
Generated: DETERMINISTIC_528549c9431523de
Batch ID: 20250622_204943
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
from typing import Dict, Optional, Tuple
from eth_account import Account
from eth_account.messages import encode_defunct
from enum import Enum

# Error classes
class BridgeError(Exception):
    """Base class for bridge-related errors."""
    pass

class InvalidChainError(BridgeError):
    """Raised when an invalid chain is specified."""
    pass

class InsufficientFundsError(BridgeError):
    """Raised when there are insufficient funds for the transaction."""
    pass

class TransactionFailedError(BridgeError):
    """Raised when a blockchain transaction fails."""
    pass

class Chain(Enum):
    """Supported blockchain networks."""
    ETHEREUM = 1
    BINANCE_SMART_CHAIN = 2
    POLYGON = 3
    AVALANCHE = 4

class CrossChainBridge:
    """
    A cross-chain bridge implementation for asset transfers between different blockchains.
    Handles token locking, minting, and verification across chains.
    """
    
    def __init__(self, config_path: str):
        """
        Initialize the bridge with configuration.
        
        Args:
            config_path: Path to JSON configuration file containing RPC endpoints and contract addresses
        """
        with open(config_path) as f:
            self.config = json.load(f)
        
        # Initialize Web3 connections
        self.connections = {
            Chain.ETHEREUM: Web3(Web3.HTTPProvider(self.config['chains']['ethereum']['rpc'])),
            Chain.BINANCE_SMART_CHAIN: Web3(Web3.HTTPProvider(self.config['chains']['bsc']['rpc'])),
            Chain.POLYGON: Web3(Web3.HTTPProvider(self.config['chains']['polygon']['rpc'])),
            Chain.AVALANCHE: Web3(Web3.HTTPProvider(self.config['chains']['avalanche']['rpc']))
        }
        
        # Load contract ABIs
        with open(self.config['bridge_abi_path']) as f:
            self.bridge_abi = json.load(f)
        
        with open(self.config['token_abi_path']) as f:
            self.token_abi = json.load(f)
        
        # Initialize bridge contracts
        self.bridge_contracts = {
            chain: self.connections[chain].eth.contract(
                address=self.config['chains'][chain.name.lower()]['bridge_address'],
                abi=self.bridge_abi
            )
            for chain in Chain
        }
        
        # Initialize token contracts
        self.token_contracts = {
            chain: self.connections[chain].eth.contract(
                address=self.config['chains'][chain.name.lower()]['token_address'],
                abi=self.token_abi
            )
            for chain in Chain
        }
        
        # Initialize relayer service URL
        self.relayer_url = self.config['relayer_service_url']
    
    def _validate_chain(self, chain: Chain) -> None:
        """Validate that the chain is supported."""
        if chain not in Chain:
            raise InvalidChainError(f"Unsupported chain: {chain}")
    
    def _get_nonce(self, chain: Chain, address: str) -> int:
        """Get the transaction nonce for an address on a specific chain."""
        self._validate_chain(chain)
        return self.connections[chain].eth.get_transaction_count(address)
    
    def _sign_transaction(self, chain: Chain, tx: Dict, private_key: str) -> Dict:
        """
        Sign a transaction for the specified chain.
        
        Args:
            chain: Target blockchain
            tx: Transaction dictionary
            private_key: Private key for signing
            
        Returns:
            Signed transaction dictionary
        """
        self._validate_chain(chain)
        signed_tx = self.connections[chain].eth.account.sign_transaction(tx, private_key)
        return signed_tx
    
    def _send_transaction(self, chain: Chain, signed_tx: Dict) -> str:
        """
        Send a signed transaction to the specified chain.
        
        Args:
            chain: Target blockchain
            signed_tx: Signed transaction dictionary
            
        Returns:
            Transaction hash
        """
        self._validate_chain(chain)
        try:
            tx_hash = self.connections[chain].eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise TransactionFailedError(f"Transaction failed: {str(e)}")
    
    def _wait_for_transaction(self, chain: Chain, tx_hash: str) -> Dict:
        """
        Wait for a transaction to be mined and return the receipt.
        
        Args:
            chain: Target blockchain
            tx_hash: Transaction hash
            
        Returns:
            Transaction receipt
        """
        self._validate_chain(chain)
        try:
            receipt = self.connections[chain].eth.wait_for_transaction_receipt(tx_hash)
            return receipt
        except Exception as e:
            raise TransactionFailedError(f"Error waiting for transaction: {str(e)}")
    
    def _check_balance(self, chain: Chain, address: str) -> int:
        """
        Check the token balance of an address on a specific chain.
        
        Args:
            chain: Target blockchain
            address: Address to check
            
        Returns:
            Token balance in wei
        """
        self._validate_chain(chain)
        return self.token_contracts[chain].functions.balanceOf(address).call()
    
    def _check_native_balance(self, chain: Chain, address: str) -> int:
        """
        Check the native token balance of an address on a specific chain.
        
        Args:
            chain: Target blockchain
            address: Address to check
            
        Returns:
            Native token balance in wei
        """
        self._validate_chain(chain)
        return self.connections[chain].eth.get_balance(address)
    
    def _generate_proof(self, source_chain: Chain, destination_chain: Chain, tx_hash: str) -> Tuple[str, str]:
        """
        Generate a proof for cross-chain transfer verification.
        
        Args:
            source_chain: Source blockchain
            destination_chain: Destination blockchain
            tx_hash: Transaction hash of the lock/burn event
            
        Returns:
            Tuple of (proof, block_hash)
        """
        self._validate_chain(source_chain)
        self._validate_chain(destination_chain)
        
        # In a real implementation, this would query the source chain for proof data
        # For this example, we'll simulate it
        proof = f"proof_{tx_hash}"
        block_hash = f"block_{tx_hash}"
        
        return (proof, block_hash)
    
    def lock_tokens(
        self,
        source_chain: Chain,
        destination_chain: Chain,
        amount: int,
        sender_address: str,
        private_key: str,
        recipient_address: Optional[str] = None
    ) -> str:
        """
        Lock tokens on the source chain to be minted on the destination chain.
        
        Args:
            source_chain: Source blockchain
            destination_chain: Destination blockchain
            amount: Amount of tokens to transfer (in wei)
            sender_address: Address sending the tokens
            private_key: Private key for signing transactions
            recipient_address: Optional recipient address on destination chain
            
        Returns:
            Transaction hash of the lock operation
        """
        self._validate_chain(source_chain)
        self._validate_chain(destination_chain)
        
        if not recipient_address:
            recipient_address = sender_address
        
        # Check token balance
        balance = self._check_balance(source_chain, sender_address)
        if balance < amount:
            raise InsufficientFundsError("Insufficient token balance")
        
        # Check native token balance for gas
        native_balance = self._check_native_balance(source_chain, sender_address)
        if native_balance < self.config['min_gas_balance']:
            raise InsufficientFundsError("Insufficient native token balance for gas")
        
        # Approve token transfer to bridge contract
        approve_tx = self.token_contracts[source_chain].functions.approve(
            self.bridge_contracts[source_chain].address,
            amount
        ).build_transaction({
            'chainId': self.connections[source_chain].eth.chain_id,
            'gas': self.config['default_gas_limit'],
            'gasPrice': self.connections[source_chain].eth.gas_price,
            'nonce': self._get_nonce(source_chain, sender_address),
        })
        
        signed_approve = self._sign_transaction(source_chain, approve_tx, private_key)
        approve_hash = self._send_transaction(source_chain, signed_approve)
        self._wait_for_transaction(source_chain, approve_hash)
        
        # Lock tokens in bridge contract
        lock_tx = self.bridge_contracts[source_chain].functions.lockTokens(
            amount,
            destination_chain.value,
            recipient_address
        ).build_transaction({
            'chainId': self.connections[source_chain].eth.chain_id,
            'gas': self.config['default_gas_limit'],
            'gasPrice': self.connections[source_chain].eth.gas_price,
            'nonce':
