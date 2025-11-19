"""
Generated Code Metadata:
========================
Original URL: https://swap-dex.dexkit.app
Prompt: Generate API calls to retrieve token information and facilitate swaps on the DexKit platform.
Generated: DETERMINISTIC_71d7080f893cb0b8
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Optional, Union
from web3 import Web3
from eth_typing import ChecksumAddress
from web3.exceptions import TransactionNotFound
from web3.contract import Contract
from web3.types import TxReceipt

class DexKitAPI:
    """
    A class to interact with DexKit platform's API for token information and swaps.
    """
    
    def __init__(self, api_base_url: str, web3_provider_url: str):
        """
        Initialize DexKitAPI with base API URL and Web3 provider URL.
        
        Args:
            api_base_url: Base URL for DexKit API
            web3_provider_url: URL for Web3 provider (e.g., Infura, Alchemy)
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_url))
        
    def get_token_info(self, token_address: str) -> Dict:
        """
        Retrieve information about a token from DexKit API.
        
        Args:
            token_address: Ethereum address of the token
            
        Returns:
            Dictionary containing token information
            
        Raises:
            ValueError: If token_address is invalid
            requests.exceptions.RequestException: If API request fails
        """
        if not Web3.is_address(token_address):
            raise ValueError("Invalid token address provided")
            
        url = f"{self.api_base_url}/tokens/{token_address.lower()}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_swap_quote(
        self,
        from_token: str,
        to_token: str,
        amount: Union[int, str],
        slippage: float = 0.5,
        recipient: Optional[str] = None
    ) -> Dict:
        """
        Get a swap quote from DexKit API.
        
        Args:
            from_token: Address of token to swap from
            to_token: Address of token to swap to
            amount: Amount to swap (in smallest units)
            slippage: Maximum slippage percentage (default: 0.5%)
            recipient: Optional recipient address (default: sender)
            
        Returns:
            Dictionary containing swap quote information
            
        Raises:
            ValueError: If any address is invalid or amount is invalid
            requests.exceptions.RequestException: If API request fails
        """
        if not all(Web3.is_address(addr) for addr in [from_token, to_token]):
            raise ValueError("Invalid token address provided")
            
        params = {
            "fromToken": from_token.lower(),
            "toToken": to_token.lower(),
            "amount": str(amount),
            "slippage": str(slippage)
        }
        
        if recipient and Web3.is_address(recipient):
            params["recipient"] = recipient.lower()
            
        url = f"{self.api_base_url}/swap/quote"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def execute_swap(
        self,
        private_key: str,
        swap_quote: Dict,
        gas_price: Optional[int] = None,
        gas_limit: Optional[int] = None
    ) -> TxReceipt:
        """
        Execute a swap transaction on Ethereum blockchain.
        
        Args:
            private_key: Private key of the sender
            swap_quote: Swap quote from get_swap_quote()
            gas_price: Optional gas price in wei
            gas_limit: Optional gas limit
            
        Returns:
            Transaction receipt
            
        Raises:
            ValueError: If private key is invalid or swap quote is malformed
            Exception: If transaction fails
        """
        if not swap_quote.get('tx'):
            raise ValueError("Invalid swap quote provided")
            
        account = self.web3.eth.account.from_key(private_key)
        sender_address = account.address
        
        tx = swap_quote['tx']
        tx['from'] = sender_address
        tx['nonce'] = self.web3.eth.get_transaction_count(sender_address)
        
        if gas_price:
            tx['gasPrice'] = gas_price
        if gas_limit:
            tx['gas'] = gas_limit
        else:
            tx['gas'] = self.web3.eth.estimate_gas(tx)
            
        signed_tx = account.sign_transaction(tx)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
    
    def get_transaction_status(self, tx_hash: str) -> Dict:
        """
        Get the status of a transaction.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            Dictionary containing transaction status
            
        Raises:
            ValueError: If tx_hash is invalid
            TransactionNotFound: If transaction not found
        """
        try:
            tx_receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            return {
                'status': 'success' if tx_receipt.status == 1 else 'failed',
                'blockNumber': tx_receipt.blockNumber,
                'gasUsed': tx_receipt.gasUsed,
                'logs': tx_receipt.logs
            }
        except TransactionNotFound:
            return {'status': 'pending'}
```
