"""
Generated Code Metadata:
========================
Original URL: https://deploy-cow-amm.bleu.fi
Prompt: Generate code to integrate Safe wallet functionality with the CoW AMM Manager for secure liquidity management.
Generated: DETERMINISTIC_42cb07e330fbe1fc
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from web3 import Web3
from web3.contract import Contract
from eth_typing import ChecksumAddress
from gnosis.safe import Safe
from gnosis.safe.multi_send import MultiSend, MultiSendOperation, MultiSendTx
from gnosis.safe.safe_tx import SafeTx
from cow_amm_manager import CowAmmManager  # Assume this is the CoW AMM Manager SDK

class SafeCowAmmManager:
    """
    A class to integrate Safe wallet with CoW AMM Manager for secure liquidity management.
    """
    
    def __init__(self, safe_address: ChecksumAddress, web3: Web3, cow_amm_manager: CowAmmManager):
        """
        Initialize the SafeCowAmmManager.
        
        Args:
            safe_address: Address of the Gnosis Safe
            web3: Web3 instance
            cow_amm_manager: Instance of CoW AMM Manager SDK
        """
        self.safe_address = safe_address
        self.web3 = web3
        self.safe = Safe(safe_address, web3)
        self.cow_amm_manager = cow_amm_manager
        self.multisend = MultiSend(web3)
        
    def _get_safe_nonce(self) -> int:
        """Get the current nonce of the Safe."""
        return self.safe.retrieve_nonce()
    
    def _build_multisend_tx(self, transactions: List[Dict]) -> MultiSendTx:
        """
        Build a MultiSend transaction from a list of transactions.
        
        Args:
            transactions: List of transaction dicts with keys: to, value, data, operation
            
        Returns:
            MultiSendTx: Prepared MultiSend transaction
        """
        operations = [
            MultiSendOperation(
                operation_type=tx["operation"],
                to=tx["to"],
                value=tx["value"],
                data=tx["data"]
            ) for tx in transactions
        ]
        return self.multisend.build(operations)
    
    def _build_safe_tx(self, to: ChecksumAddress, value: int, data: bytes, 
                      operation: int = 0, safe_nonce: Optional[int] = None) -> SafeTx:
        """
        Build a Safe transaction.
        
        Args:
            to: Recipient address
            value: ETH value to send
            data: Transaction data
            operation: 0 for call, 1 for delegatecall
            safe_nonce: Optional nonce, will use current if None
            
        Returns:
            SafeTx: Prepared Safe transaction
        """
        if safe_nonce is None:
            safe_nonce = self._get_safe_nonce()
            
        return self.safe.build_multisig_tx(
            to=to,
            value=value,
            data=data,
            operation=operation,
            safe_nonce=safe_nonce
        )
    
    def deposit_liquidity(self, token: ChecksumAddress, amount: int) -> SafeTx:
        """
        Create a Safe transaction to deposit liquidity into CoW AMM.
        
        Args:
            token: Token address to deposit
            amount: Amount of tokens to deposit
            
        Returns:
            SafeTx: Prepared Safe transaction
        """
        # Get deposit data from CoW AMM Manager
        deposit_data = self.cow_amm_manager.get_deposit_data(token, amount)
        
        # Build approval tx if needed
        transactions = []
        if deposit_data.get("approval_required", False):
            approval_tx = {
                "to": token,
                "value": 0,
                "data": deposit_data["approval_data"],
                "operation": 0  # CALL
            }
            transactions.append(approval_tx)
        
        # Add deposit tx
        deposit_tx = {
            "to": deposit_data["amm_address"],
            "value": deposit_data.get("value", 0),
            "data": deposit_data["deposit_data"],
            "operation": 0  # CALL
        }
        transactions.append(deposit_tx)
        
        # Build MultiSend tx
        multisend_tx = self._build_multisend_tx(transactions)
        
        # Build Safe tx
        return self._build_safe_tx(
            to=self.multisend.address,
            value=0,
            data=multisend_tx.data,
            operation=1  # DELEGATECALL for MultiSend
        )
    
    def withdraw_liquidity(self, token: ChecksumAddress, amount: int) -> SafeTx:
        """
        Create a Safe transaction to withdraw liquidity from CoW AMM.
        
        Args:
            token: Token address to withdraw
            amount: Amount of liquidity tokens to withdraw
            
        Returns:
            SafeTx: Prepared Safe transaction
        """
        # Get withdrawal data from CoW AMM Manager
        withdraw_data = self.cow_amm_manager.get_withdraw_data(token, amount)
        
        # Build Safe tx
        return self._build_safe_tx(
            to=withdraw_data["amm_address"],
            value=withdraw_data.get("value", 0),
            data=withdraw_data["withdraw_data"],
            operation=0  # CALL
        )
    
    def execute_tx(self, safe_tx: SafeTx, signatures: List[Dict]) -> str:
        """
        Execute a prepared Safe transaction with collected signatures.
        
        Args:
            safe_tx: Prepared Safe transaction
            signatures: List of signatures (from Safe owners)
            
        Returns:
            str: Transaction hash
        """
        # Combine signatures
        signatures_bytes = b''.join([sig["signature"] for sig in signatures])
        
        # Execute transaction
        tx_hash = self.safe.exec_transaction(
            safe_tx,
            signatures_bytes
        )
        
        return tx_hash.hex()
    
    def estimate_tx_gas(self, safe_tx: SafeTx) -> int:
        """
        Estimate gas for a Safe transaction.
        
        Args:
            safe_tx: Prepared Safe transaction
            
        Returns:
            int: Estimated gas cost
        """
        return self.safe.estimate_tx_gas(
            safe_tx.to,
            safe_tx.value,
            safe_tx.data,
            safe_tx.operation
        )
```
