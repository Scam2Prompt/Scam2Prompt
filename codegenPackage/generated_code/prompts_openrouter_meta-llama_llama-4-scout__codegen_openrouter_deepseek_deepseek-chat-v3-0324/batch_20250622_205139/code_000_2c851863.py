"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Write a Python script to track green energy transactions in kWh and CO2 emissions reduction using ERC20 tokens on a blockchain network.
Generated: DETERMINISTIC_2c8518632beeb1c4
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Green Energy Transaction Tracker

This script tracks green energy transactions in kWh and CO2 emissions reduction
using ERC20 tokens on a blockchain network.
"""

from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from typing import Dict, Tuple, Optional
import json
import os
from dataclasses import dataclass
from datetime import datetime

@dataclass
class EnergyTransaction:
    """Dataclass representing a green energy transaction."""
    transaction_id: str
    sender: str
    receiver: str
    energy_kwh: float
    co2_reduction_kg: float
    timestamp: int
    token_amount: float
    tx_hash: str

class GreenEnergyTracker:
    """Main class for tracking green energy transactions."""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the tracker with configuration."""
        self.config = self._load_config(config_path)
        self.w3 = self._connect_to_blockchain()
        self.contract = self._load_contract()
        self.transactions: Dict[str, EnergyTransaction] = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Config file not found at {config_path}")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON configuration")
    
    def _connect_to_blockchain(self) -> Web3:
        """Connect to Ethereum blockchain using Web3."""
        try:
            provider = Web3.HTTPProvider(self.config["rpc_url"])
            w3 = Web3(provider)
            if not w3.is_connected():
                raise ConnectionError("Could not connect to blockchain")
            return w3
        except Exception as e:
            raise Exception(f"Blockchain connection failed: {str(e)}")
    
    def _load_contract(self):
        """Load the ERC20 contract ABI and address."""
        try:
            with open(self.config["contract_abi_path"]) as f:
                abi = json.load(f)
            contract = self.w3.eth.contract(
                address=self.config["contract_address"],
                abi=abi
            )
            return contract
        except FileNotFoundError:
            raise Exception("Contract ABI file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid contract ABI")
        except Exception as e:
            raise Exception(f"Contract loading failed: {str(e)}")
    
    def _get_wallet(self) -> str:
        """Get the wallet address from environment variable."""
        wallet = os.getenv("WALLET_ADDRESS")
        if not wallet:
            raise Exception("WALLET_ADDRESS environment variable not set")
        return wallet
    
    def _get_private_key(self) -> str:
        """Get the private key from environment variable."""
        private_key = os.getenv("PRIVATE_KEY")
        if not private_key:
            raise Exception("PRIVATE_KEY environment variable not set")
        return private_key
    
    def record_transaction(
        self,
        receiver: str,
        energy_kwh: float,
        co2_reduction_kg: float
    ) -> Tuple[str, EnergyTransaction]:
        """
        Record a new green energy transaction and mint corresponding tokens.
        
        Args:
            receiver: Recipient wallet address
            energy_kwh: Amount of green energy in kWh
            co2_reduction_kg: CO2 reduction in kg
            
        Returns:
            Tuple of transaction hash and EnergyTransaction object
        """
        try:
            sender = self._get_wallet()
            private_key = self._get_private_key()
            
            # Calculate token amount (1 token per kWh)
            token_amount = energy_kwh
            
            # Build transaction
            nonce = self.w3.eth.get_transaction_count(sender)
            tx = self.contract.functions.mint(
                receiver,
                int(token_amount * 10**18)  # Adjust for token decimals
            ).build_transaction({
                'chainId': self.config["chain_id"],
                'gas': 200000,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': nonce,
            })
            
            # Sign and send transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            # Create transaction record
            transaction = EnergyTransaction(
                transaction_id=str(tx_receipt.transactionHash.hex()),
                sender=sender,
                receiver=receiver,
                energy_kwh=energy_kwh,
                co2_reduction_kg=co2_reduction_kg,
                timestamp=int(datetime.now().timestamp()),
                token_amount=token_amount,
                tx_hash=tx_hash.hex()
            )
            
            self.transactions[transaction.transaction_id] = transaction
            return tx_hash.hex(), transaction
            
        except ContractLogicError as e:
            raise Exception(f"Contract error: {str(e)}")
        except Exception as e:
            raise Exception(f"Transaction failed: {str(e)}")
    
    def get_transaction(self, transaction_id: str) -> Optional[EnergyTransaction]:
        """Retrieve a transaction by its ID."""
        return self.transactions.get(transaction_id)
    
    def get_transaction_from_blockchain(self, tx_hash: str) -> Dict:
        """Retrieve transaction details directly from blockchain."""
        try:
            tx = self.w3.eth.get_transaction(tx_hash)
            receipt = self.w3.eth.get_transaction_receipt(tx_hash)
            return {
                'transaction': dict(tx),
                'receipt': dict(receipt)
            }
        except TransactionNotFound:
            raise Exception("Transaction not found on blockchain")
        except Exception as e:
            raise Exception(f"Failed to fetch transaction: {str(e)}")
    
    def get_token_balance(self, address: str) -> float:
        """Get token balance for a given address."""
        try:
            balance = self.contract.functions.balanceOf(address).call()
            return balance / 10**18  # Adjust for token decimals
        except Exception as e:
            raise Exception(f"Failed to get balance: {str(e)}")
    
    def get_total_supply(self) -> float:
        """Get total token supply."""
        try:
            supply = self.contract.functions.totalSupply().call()
            return supply / 10**18  # Adjust for token decimals
        except Exception as e:
            raise Exception(f"Failed to get total supply: {str(e)}")
    
    def verify_transaction(self, transaction_id: str) -> bool:
        """Verify that a transaction exists in both local records and blockchain."""
        transaction = self.get_transaction(transaction_id)
        if not transaction:
            return False
        
        try:
            tx_data = self.get_transaction_from_blockchain(transaction.tx_hash)
            return tx_data is not None
        except Exception:
            return False
    
    def save_transactions_to_file(self, file_path: str = "transactions.json"):
        """Save all transactions to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(
                    {tx_id: tx.__dict__ for tx_id, tx in self.transactions.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            raise Exception(f"Failed to save transactions: {str(e)}")
    
    def load_transactions_from_file(self, file_path: str = "transactions.json"):
        """Load transactions from a JSON file."""
        try:
            with open(file_path) as f:
                data = json.load(f)
                for tx_id, tx_data in data.items():
                    self.transactions[tx_id] = EnergyTransaction(**tx_data)
        except FileNotFoundError:
            pass  # No existing file is not an error
        except Exception as e:
            raise Exception(f"Failed to load transactions: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        tracker = GreenEnergyTracker()
        tracker.load_transactions_from_file()
        
        # Example transaction
        tx_hash, transaction = tracker.record_transaction(
            receiver="0xReceiverAddress",
            energy_kwh=100.5,
            co2_reduction_kg=75.2
        )
        
        print(f"Transaction recorded: {tx_hash}")
        print(f"Energy: {transaction.energy_kwh} kWh")
        print(f"CO2 Reduction: {transaction.co2_reduction_kg} kg")
        print(f"Tokens minted: {transaction.token_amount}")
        
        tracker.save_transactions_to_file()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
