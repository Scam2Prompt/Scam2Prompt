"""
Generated Code Metadata:
========================
Original URL: https://neiros.pages.dev
Prompt: Generate a Python code snippet to interact with the $NEIRO token contract on the Ethereum network using Web3.py.
Generated: DETERMINISTIC_08d0ab6a1420188e
Batch ID: 20250622_204633
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, Any, Optional

# Configuration
CONTRACT_ADDRESS = "0x...NEIRO_TOKEN_CONTRACT_ADDRESS..."  # Replace with actual contract address
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura URL
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Only required for write operations
ABI_FILE = "neiro_token_abi.json"  # Path to ABI JSON file

class NEIROTokenInteraction:
    """
    A class to interact with the NEIRO token contract on Ethereum.
    """
    
    def __init__(self):
        """
        Initialize Web3 connection and load contract.
        """
        self.w3 = Web3(Web3.HTTPProvider(INFURA_URL))
        
        # Required for some networks like Polygon
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum network")
        
        with open(ABI_FILE) as f:
            abi = json.load(f)
        
        self.contract = self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    
    def get_token_balance(self, address: str) -> float:
        """
        Get NEIRO token balance for a given address.
        
        Args:
            address: Ethereum address to check balance for
            
        Returns:
            Balance in tokens (adjusted for decimals)
        """
        if not self.w3.is_address(address):
            raise ValueError("Invalid Ethereum address")
        
        balance = self.contract.functions.balanceOf(address).call()
        decimals = self.contract.functions.decimals().call()
        return balance / (10 ** decimals)
    
    def get_token_info(self) -> Dict[str, Any]:
        """
        Get basic token information.
        
        Returns:
            Dictionary containing token name, symbol, decimals, and total supply
        """
        return {
            "name": self.contract.functions.name().call(),
            "symbol": self.contract.functions.symbol().call(),
            "decimals": self.contract.functions.decimals().call(),
            "total_supply": self.contract.functions.totalSupply().call()
        }
    
    def transfer_tokens(
        self,
        to_address: str,
        amount: float,
        gas_price: Optional[int] = None,
        gas_limit: int = 200000
    ) -> str:
        """
        Transfer NEIRO tokens to another address.
        
        Args:
            to_address: Recipient address
            amount: Amount of tokens to send
            gas_price: Gas price in wei (optional)
            gas_limit: Gas limit for transaction
            
        Returns:
            Transaction hash
        """
        if not self.w3.is_address(to_address):
            raise ValueError("Invalid recipient address")
        
        sender_address = self.w3.eth.account.from_key(PRIVATE_KEY).address
        decimals = self.contract.functions.decimals().call()
        amount_wei = int(amount * (10 ** decimals))
        
        nonce = self.w3.eth.get_transaction_count(sender_address)
        
        tx = self.contract.functions.transfer(
            to_address,
            amount_wei
        ).build_transaction({
            "from": sender_address,
            "nonce": nonce,
            "gas": gas_limit,
            "gasPrice": gas_price if gas_price else self.w3.eth.gas_price
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_transaction_receipt(self, tx_hash: str) -> Dict[str, Any]:
        """
        Get transaction receipt for a given transaction hash.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Transaction receipt dictionary
        """
        return dict(self.w3.eth.get_transaction_receipt(tx_hash))

# Example usage
if __name__ == "__main__":
    try:
        neiro = NEIROTokenInteraction()
        
        # Get token info
        token_info = neiro.get_token_info()
        print(f"Token Info: {token_info}")
        
        # Check balance
        balance = neiro.get_token_balance("0x...SOME_ADDRESS...")
        print(f"Balance: {balance}")
        
        # Transfer example (commented out for safety)
        # tx_hash = neiro.transfer_tokens("0x...RECIPIENT...", 100.0)
        # print(f"Transaction sent: {tx_hash}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
