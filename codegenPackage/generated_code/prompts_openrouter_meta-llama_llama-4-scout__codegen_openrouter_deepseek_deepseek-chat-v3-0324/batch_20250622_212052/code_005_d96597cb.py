"""
Generated Code Metadata:
========================
Original URL: https://dvhuh.pages.dev
Prompt: Design a bridge transfer function to enable seamless token transfers between different blockchain chains using a web3.0 platform.
Generated: DETERMINISTIC_d96597cb1eceb50d
Batch ID: 20250622_212052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
import json
import logging
from typing import Dict, Optional, Tuple
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BridgeTransfer:
    """
    A class to handle cross-chain token transfers between different blockchain networks.
    """
    
    def __init__(
        self,
        source_chain_rpc: str,
        destination_chain_rpc: str,
        bridge_contract_abi: str,
        private_key: str,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ):
        """
        Initialize the BridgeTransfer with chain connections and account.
        
        Args:
            source_chain_rpc: RPC URL for the source chain
            destination_chain_rpc: RPC URL for the destination chain
            bridge_contract_abi: JSON string of the bridge contract ABI
            private_key: Private key for the sender's account
            gas_limit: Gas limit for transactions
            gas_price: Gas price for transactions (None for automatic)
        """
        self.source_web3 = Web3(Web3.HTTPProvider(source_chain_rpc))
        self.dest_web3 = Web3(Web3.HTTPProvider(destination_chain_rpc))
        
        if not self.source_web3.is_connected() or not self.dest_web3.is_connected():
            raise ConnectionError("Failed to connect to one or more RPC endpoints")
            
        self.account: LocalAccount = Account.from_key(private_key)
        self.gas_limit = gas_limit
        self.gas_price = gas_price
        
        try:
            self.bridge_abi = json.loads(bridge_contract_abi)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid bridge contract ABI: {e}")
            raise
            
    def _get_contract(self, web3: Web3, contract_address: ChecksumAddress) -> Contract:
        """
        Get contract instance from address and ABI.
        
        Args:
            web3: Web3 instance
            contract_address: Address of the contract
            
        Returns:
            Contract instance
        """
        if not web3.is_checksum_address(contract_address):
            contract_address = web3.to_checksum_address(contract_address)
        return web3.eth.contract(address=contract_address, abi=self.bridge_abi)
    
    def _estimate_gas_price(self, web3: Web3) -> int:
        """
        Estimate gas price if not provided.
        
        Args:
            web3: Web3 instance
            
        Returns:
            Gas price in wei
        """
        return self.gas_price if self.gas_price is not None else web3.eth.gas_price
    
    def transfer_tokens(
        self,
        source_token_address: str,
        dest_token_address: str,
        bridge_contract_address: str,
        amount: int,
        dest_recipient: str,
        chain_id: int
    ) -> Tuple[str, str]:
        """
        Transfer tokens between chains using the bridge contract.
        
        Args:
            source_token_address: Address of the token contract on source chain
            dest_token_address: Address of the token contract on destination chain
            bridge_contract_address: Address of the bridge contract
            amount: Amount of tokens to transfer
            dest_recipient: Recipient address on destination chain
            chain_id: Destination chain ID
            
        Returns:
            Tuple of (source_tx_hash, bridge_tx_hash)
            
        Raises:
            ValueError: If input validation fails
            ContractLogicError: If contract call fails
        """
        # Validate inputs
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        if not all([
            self.source_web3.is_checksum_address(source_token_address),
            self.dest_web3.is_checksum_address(dest_token_address),
            self.source_web3.is_checksum_address(bridge_contract_address),
            self.dest_web3.is_checksum_address(dest_recipient)
        ]):
            raise ValueError("One or more addresses are invalid")
            
        try:
            # Get contracts
            token_contract = self._get_contract(self.source_web3, source_token_address)
            bridge_contract = self._get_contract(self.source_web3, bridge_contract_address)
            
            # Approve token transfer
            approve_tx = token_contract.functions.approve(
                bridge_contract_address,
                amount
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.source_web3.eth.get_transaction_count(self.account.address),
                'gas': self.gas_limit,
                'gasPrice': self._estimate_gas_price(self.source_web3)
            })
            
            signed_approve = self.account.sign_transaction(approve_tx)
            approve_tx_hash = self.source_web3.eth.send_raw_transaction(signed_approve.rawTransaction)
            
            # Wait for approval confirmation
            self.source_web3.eth.wait_for_transaction_receipt(approve_tx_hash)
            
            # Initiate bridge transfer
            bridge_tx = bridge_contract.functions.transferTokens(
                source_token_address,
                amount,
                dest_recipient,
                dest_token_address,
                chain_id
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.source_web3.eth.get_transaction_count(self.account.address),
                'gas': self.gas_limit,
                'gasPrice': self._estimate_gas_price(self.source_web3)
            })
            
            signed_bridge = self.account.sign_transaction(bridge_tx)
            bridge_tx_hash = self.source_web3.eth.send_raw_transaction(signed_bridge.rawTransaction)
            
            return (approve_tx_hash.hex(), bridge_tx_hash.hex())
            
        except ContractLogicError as e:
            logger.error(f"Contract logic error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during transfer: {e}")
            raise
            
    def check_transfer_status(self, tx_hash: str) -> Dict:
        """
        Check the status of a transfer transaction.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Dictionary with transaction status and details
            
        Raises:
            TransactionNotFound: If transaction doesn't exist
        """
        try:
            receipt = self.source_web3.eth.get_transaction_receipt(tx_hash)
            return {
                'status': receipt['status'],
                'block_number': receipt['blockNumber'],
                'gas_used': receipt['gasUsed'],
                'logs': receipt['logs']
            }
        except TransactionNotFound:
            logger.error(f"Transaction not found: {tx_hash}")
            raise
        except Exception as e:
            logger.error(f"Error checking transaction status: {e}")
            raise
```
