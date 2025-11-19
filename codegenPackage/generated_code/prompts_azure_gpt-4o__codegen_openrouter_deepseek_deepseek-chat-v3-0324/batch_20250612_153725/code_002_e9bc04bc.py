"""
Generated Code Metadata:
========================
Original URL: https://rodeo.pages.dev
Prompt: Generate code to toggle the bot list and display the number of bot transactions using the Rodeo ETH Toolbox.
Generated: DETERMINISTIC_e9bc04bc74e21c88
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_utils import to_checksum_address

class RodeoETHToolbox:
    """
    A toolbox for interacting with the Rodeo ETH smart contract to manage bot transactions.
    """
    
    def __init__(self, provider_url: str, contract_address: str, contract_abi: str):
        """
        Initialize the RodeoETHToolbox with provider URL, contract address, and ABI.
        
        Args:
            provider_url: URL of the Ethereum provider (e.g., Infura, Alchemy)
            contract_address: Address of the Rodeo ETH smart contract
            contract_abi: ABI of the Rodeo ETH smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum provider")
        
        self.contract_address = to_checksum_address(contract_address)
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=json.loads(contract_abi)
        )
    
    def toggle_bot_list(self, bot_address: str, private_key: str) -> str:
        """
        Toggle a bot's status in the bot list (add if not present, remove if present).
        
        Args:
            bot_address: Address of the bot to toggle
            private_key: Private key of the account executing the transaction
            
        Returns:
            Transaction hash of the toggle operation
            
        Raises:
            ValueError: If bot_address is invalid
            ContractLogicError: If contract call fails
            Exception: For other transaction errors
        """
        try:
            bot_address = to_checksum_address(bot_address)
            account = self.web3.eth.account.from_key(private_key)
            
            # Build transaction
            tx = self.contract.functions.toggleBotList(bot_address).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price
            })
            
            # Sign and send transaction
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        
        except ValueError as ve:
            raise ValueError(f"Invalid bot address: {ve}")
        except ContractLogicError as cle:
            raise ContractLogicError(f"Contract logic error: {cle}")
        except Exception as e:
            raise Exception(f"Transaction failed: {e}")
    
    def get_bot_transaction_count(self, bot_address: str) -> int:
        """
        Get the number of transactions performed by a specific bot.
        
        Args:
            bot_address: Address of the bot to query
            
        Returns:
            Number of transactions performed by the bot
            
        Raises:
            ValueError: If bot_address is invalid
            ContractLogicError: If contract call fails
        """
        try:
            bot_address = to_checksum_address(bot_address)
            return self.contract.functions.getBotTransactionCount(bot_address).call()
        
        except ValueError as ve:
            raise ValueError(f"Invalid bot address: {ve}")
        except ContractLogicError as cle:
            raise ContractLogicError(f"Contract logic error: {cle}")
    
    def get_bot_list(self) -> List[str]:
        """
        Get the current list of bot addresses.
        
        Returns:
            List of bot addresses
            
        Raises:
            ContractLogicError: If contract call fails
        """
        try:
            return self.contract.functions.getBotList().call()
        except ContractLogicError as cle:
            raise ContractLogicError(f"Contract logic error: {cle}")
    
    def get_transaction_status(self, tx_hash: str) -> Optional[Dict]:
        """
        Get the status of a transaction.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Dictionary containing transaction status and details, or None if not found
            
        Raises:
            ValueError: If tx_hash is invalid
        """
        try:
            tx_hash_bytes = bytes.fromhex(tx_hash[2:] if tx_hash.startswith('0x') else tx_hash)
            tx_receipt = self.web3.eth.get_transaction_receipt(tx_hash_bytes)
            
            if tx_receipt is None:
                return None
                
            return {
                'status': tx_receipt.status,
                'blockNumber': tx_receipt.blockNumber,
                'gasUsed': tx_receipt.gasUsed,
                'logs': tx_receipt.logs
            }
            
        except ValueError as ve:
            raise ValueError(f"Invalid transaction hash: {ve}")
        except TransactionNotFound:
            return None
```
