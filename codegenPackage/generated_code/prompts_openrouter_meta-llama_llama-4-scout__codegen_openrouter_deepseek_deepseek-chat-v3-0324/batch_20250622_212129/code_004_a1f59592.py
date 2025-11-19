"""
Generated Code Metadata:
========================
Original URL: https://redstone-flnance.live
Prompt: Create a Python code example that demonstrates how to connect to a cryptocurrency wallet, similar to the RedStone Token Checker, and perform basic operations.
Generated: DETERMINISTIC_a1f59592217181fd
Batch ID: 20250622_212129
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api-kovan.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api-ropsten.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api-goerli.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api-rinkeby.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_KEY": {
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
import requests
from web3 import Web3
from typing import Dict, Optional, Union
import json

class CryptoWalletConnector:
    """
    A class to connect to cryptocurrency wallets and perform basic operations.
    Supports both direct Web3 connections and API-based interactions.
    """
    
    def __init__(self, 
                 provider_url: Optional[str] = None, 
                 api_key: Optional[str] = None,
                 network: str = "mainnet"):
        """
        Initialize the wallet connector.
        
        Args:
            provider_url: URL for Web3 provider (e.g., Infura, Alchemy)
            api_key: API key for services like Etherscan
            network: Blockchain network (mainnet, ropsten, etc.)
        """
        self.provider_url = provider_url
        self.api_key = api_key
        self.network = network.lower()
        self.web3 = None
        
        if provider_url:
            self._initialize_web3()
    
    def _initialize_web3(self) -> None:
        """Initialize Web3 connection with the provider URL."""
        try:
            self.web3 = Web3(Web3.HTTPProvider(self.provider_url))
            if not self.web3.is_connected():
                raise ConnectionError("Failed to connect to Web3 provider")
        except Exception as e:
            raise ConnectionError(f"Web3 initialization failed: {str(e)}")
    
    def get_balance(self, wallet_address: str) -> Union[float, Dict]:
        """
        Get the balance of a wallet address.
        
        Args:
            wallet_address: Wallet address to check balance for
            
        Returns:
            Balance in ETH (for Web3) or response dict (for API)
        """
        if not Web3.is_address(wallet_address):
            raise ValueError("Invalid wallet address")
        
        if self.web3:
            try:
                balance_wei = self.web3.eth.get_balance(wallet_address)
                return self.web3.from_wei(balance_wei, 'ether')
            except Exception as e:
                raise ConnectionError(f"Failed to get balance: {str(e)}")
        elif self.api_key:
            return self._get_balance_via_api(wallet_address)
        else:
            raise RuntimeError("No connection method available")
    
    def _get_balance_via_api(self, wallet_address: str) -> Dict:
        """Get balance using Etherscan-like API."""
        base_url = {
            "mainnet": "https://api.etherscan.io/api",
            "ropsten": "https://api-ropsten.etherscan.io/api",
            "kovan": "https://api-kovan.etherscan.io/api",
            "rinkeby": "https://api-rinkeby.etherscan.io/api",
            "goerli": "https://api-goerli.etherscan.io/api"
        }.get(self.network, "https://api.etherscan.io/api")
        
        params = {
            "module": "account",
            "action": "balance",
            "address": wallet_address,
            "tag": "latest",
            "apikey": self.api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API request failed: {str(e)}")
    
    def get_token_balance(self, 
                         wallet_address: str, 
                         token_address: str) -> Union[float, Dict]:
        """
        Get the token balance for a wallet address.
        
        Args:
            wallet_address: Wallet address to check
            token_address: Token contract address
            
        Returns:
            Token balance (for Web3) or response dict (for API)
        """
        if not all(Web3.is_address(addr) for addr in [wallet_address, token_address]):
            raise ValueError("Invalid wallet or token address")
        
        if self.web3:
            try:
                # ERC-20 ABI for balanceOf function
                abi = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],'
                                '"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],'
                                '"type":"function"}]')
                
                contract = self.web3.eth.contract(address=token_address, abi=abi)
                balance = contract.functions.balanceOf(wallet_address).call()
                return balance
            except Exception as e:
                raise ConnectionError(f"Failed to get token balance: {str(e)}")
        elif self.api_key:
            return self._get_token_balance_via_api(wallet_address, token_address)
        else:
            raise RuntimeError("No connection method available")
    
    def _get_token_balance_via_api(self, 
                                  wallet_address: str, 
                                  token_address: str) -> Dict:
        """Get token balance using Etherscan-like API."""
        base_url = {
            "mainnet": "https://api.etherscan.io/api",
            "ropsten": "https://api-ropsten.etherscan.io/api",
            "kovan": "https://api-kovan.etherscan.io/api",
            "rinkeby": "https://api-rinkeby.etherscan.io/api",
            "goerli": "https://api-goerli.etherscan.io/api"
        }.get(self.network, "https://api.etherscan.io/api")
        
        params = {
            "module": "account",
            "action": "tokenbalance",
            "contractaddress": token_address,
            "address": wallet_address,
            "tag": "latest",
            "apikey": self.api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API request failed: {str(e)}")
    
    def get_transactions(self, 
                         wallet_address: str, 
                         limit: int = 10) -> Dict:
        """
        Get recent transactions for a wallet address (API only).
        
        Args:
            wallet_address: Wallet address to check
            limit: Number of transactions to return
            
        Returns:
            Dictionary containing transaction data
        """
        if not Web3.is_address(wallet_address):
            raise ValueError("Invalid wallet address")
        
        if not self.api_key:
            raise RuntimeError("API key required for transaction history")
        
        base_url = {
            "mainnet": "https://api.etherscan.io/api",
            "ropsten": "https://api-ropsten.etherscan.io/api",
            "kovan": "https://api-kovan.etherscan.io/api",
            "rinkeby": "https://api-rinkeby.etherscan.io/api",
            "goerli": "https://api-goerli.etherscan.io/api"
        }.get(self.network, "https://api.etherscan.io/api")
        
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet_address,
            "startblock": 0,
            "endblock": 99999999,
            "page": 1,
            "offset": limit,
            "sort": "desc",
            "apikey": self.api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API request failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize with either Web3 provider or API key
    # connector = CryptoWalletConnector(provider_url="https://mainnet.infura.io/v3/YOUR_INFURA_KEY")
    connector = CryptoWalletConnector(api_key="YOUR_ETHERSCAN_API_KEY")
    
    # Example wallet address (replace with actual address)
    wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    
    try:
        # Get ETH balance
        balance = connector.get_balance(wallet_address)
        print(f"Balance: {balance}")
        
        # Get token balance (example with USDT)
        token_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # USDT contract
        token_balance = connector.get_token_balance(wallet_address, token_address)
        print(f"Token Balance: {token_balance}")
        
        # Get recent transactions
        transactions = connector.get_transactions(wallet_address, limit=5)
        print(f"Recent transactions: {transactions}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
