"""
Generated Code Metadata:
========================
Original URL: https://reown.com
Prompt: "Design a demo for an on-chain payment system using Reown's platform, building beyond legacy systems and ensuring effortless, intuitive, and secure digital ownership."
Generated: DETERMINISTIC_df263da4731cf55b
Batch ID: 20250622_205139
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
On-Chain Payment System Demo for Reown Platform

Features:
- Secure digital ownership management
- Intuitive payment processing
- Blockchain-based transaction handling
- Error handling and validation
"""

import json
from typing import Dict, Optional, Tuple
from dataclasses import dataclass
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from eth_account import Account
from eth_typing import Address, ChecksumAddress, HexStr
from eth_utils import to_checksum_address

# Configuration
CONFIG = {
    "RPC_ENDPOINT": "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
    "CONTRACT_ADDRESS": "0xYourContractAddressHere",
    "CONTRACT_ABI": [],  # Replace with actual ABI
    "GAS_LIMIT": 200000,
    "CHAIN_ID": 1,
}

@dataclass
class PaymentDetails:
    sender: ChecksumAddress
    receiver: ChecksumAddress
    amount: int  # in wei
    token_address: Optional[ChecksumAddress] = None  # None for native token
    metadata: Optional[Dict] = None

class ReownPaymentSystem:
    def __init__(self):
        self.web3 = Web3(HTTPProvider(CONFIG["RPC_ENDPOINT"]))
        self.contract = self._load_contract()
        
    def _load_contract(self) -> Contract:
        """Initialize and return the contract instance"""
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to blockchain network")
        
        checksum_address = to_checksum_address(CONFIG["CONTRACT_ADDRESS"])
        return self.web3.eth.contract(
            address=checksum_address,
            abi=CONFIG["CONTRACT_ABI"]
        )
    
    def _validate_payment_details(self, details: PaymentDetails) -> None:
        """Validate payment details before processing"""
        if not self.web3.is_address(details.sender):
            raise ValueError("Invalid sender address")
        if not self.web3.is_address(details.receiver):
            raise ValueError("Invalid receiver address")
        if details.amount <= 0:
            raise ValueError("Amount must be positive")
    
    def _get_nonce(self, address: ChecksumAddress) -> int:
        """Get the current nonce for an address"""
        return self.web3.eth.get_transaction_count(address)
    
    def _sign_transaction(self, tx: Dict, private_key: str) -> HexStr:
        """Sign a transaction with the provided private key"""
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        return signed_tx.rawTransaction
    
    def process_payment(self, details: PaymentDetails, private_key: str) -> Tuple[str, Dict]:
        """
        Process an on-chain payment
        
        Args:
            details: PaymentDetails object containing transaction details
            private_key: Sender's private key for signing
            
        Returns:
            Tuple of (transaction_hash, receipt)
        """
        self._validate_payment_details(details)
        
        sender_address = to_checksum_address(details.sender)
        nonce = self._get_nonce(sender_address)
        
        if details.token_address:
            # ERC20 token transfer
            tx = self.contract.functions.transfer(
                details.receiver,
                details.amount
            ).build_transaction({
                'from': sender_address,
                'nonce': nonce,
                'gas': CONFIG["GAS_LIMIT"],
                'chainId': CONFIG["CHAIN_ID"]
            })
        else:
            # Native token transfer
            tx = {
                'to': details.receiver,
                'value': details.amount,
                'nonce': nonce,
                'gas': CONFIG["GAS_LIMIT"],
                'chainId': CONFIG["CHAIN_ID"]
            }
        
        try:
            signed_tx = self._sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            if details.metadata:
                self._store_metadata(tx_hash.hex(), details.metadata)
            
            return tx_hash.hex(), receipt
        except Exception as e:
            raise RuntimeError(f"Transaction failed: {str(e)}")
    
    def _store_metadata(self, tx_hash: str, metadata: Dict) -> None:
        """Store transaction metadata (implementation depends on storage solution)"""
        # This would typically interact with IPFS or a centralized database
        print(f"Storing metadata for tx {tx_hash}: {json.dumps(metadata)}")
    
    def verify_ownership(self, address: ChecksumAddress, token_address: Optional[ChecksumAddress] = None) -> bool:
        """
        Verify digital ownership of tokens
        
        Args:
            address: Address to check balance for
            token_address: Optional token address, None for native token
            
        Returns:
            bool indicating if address owns any tokens
        """
        address = to_checksum_address(address)
        
        if token_address:
            token_address = to_checksum_address(token_address)
            balance = self.contract.functions.balanceOf(address).call()
        else:
            balance = self.web3.eth.get_balance(address)
        
        return balance > 0

# Example usage
if __name__ == "__main__":
    try:
        payment_system = ReownPaymentSystem()
        
        # Example payment details
        payment = PaymentDetails(
            sender="0xSenderAddressHere",
            receiver="0xReceiverAddressHere",
            amount=100000000000000000,  # 0.1 ETH
            metadata={"invoice_id": "12345", "description": "Service payment"}
        )
        
        # In production, private key should be securely managed (e.g., vault, env vars)
        private_key = "0xYourPrivateKeyHere"
        
        tx_hash, receipt = payment_system.process_payment(payment, private_key)
        print(f"Payment successful! TX Hash: {tx_hash}")
        
        # Verify ownership
        owns_tokens = payment_system.verify_ownership(payment.receiver)
        print(f"Receiver owns tokens: {owns_tokens}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
