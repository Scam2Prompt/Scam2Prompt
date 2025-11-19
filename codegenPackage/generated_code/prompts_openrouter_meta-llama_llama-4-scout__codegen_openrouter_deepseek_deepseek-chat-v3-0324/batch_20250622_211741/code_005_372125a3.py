"""
Generated Code Metadata:
========================
Original URL: https://o3-network.pages.dev
Prompt: Design a secure and cost-effective architecture for a decentralized application (dApp) utilizing O3 Wallet's cross-chain swap functionality.
Generated: DETERMINISTIC_372125a3e2bc3f81
Batch ID: 20250622_211741
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://api.avax.network/ext/bc/C/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.o3.network/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
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
  },
  "https://polygon-rpc.com/": {
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
# Import required libraries
from web3 import Web3
from eth_account import Account
from typing import Dict, Optional, Tuple
import requests
import json
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
O3_API_URL = "https://api.o3.network/v1"
GAS_LIMIT = 21000
GAS_PRICE_MULTIPLIER = 1.2  # Buffer for gas price fluctuations

class ChainID(Enum):
    ETHEREUM = 1
    BSC = 56
    POLYGON = 137
    AVAX = 43114

class Token:
    def __init__(self, symbol: str, address: str, decimals: int, chain_id: ChainID):
        self.symbol = symbol
        self.address = address
        self.decimals = decimals
        self.chain_id = chain_id

class O3WalletClient:
    def __init__(self, private_key: str, rpc_urls: Dict[ChainID, str]):
        """
        Initialize O3 Wallet client with private key and RPC URLs for different chains.
        
        Args:
            private_key: User's private key for signing transactions
            rpc_urls: Dictionary mapping ChainID to RPC URL
        """
        self.private_key = private_key
        self.rpc_urls = rpc_urls
        self.account = Account.from_key(private_key)
        self.w3_instances = {
            chain_id: Web3(Web3.HTTPProvider(url)) 
            for chain_id, url in rpc_urls.items()
        }

    def get_balance(self, token: Token) -> float:
        """
        Get token balance for the user's address.
        
        Args:
            token: Token object representing the token to check balance for
            
        Returns:
            Balance in human-readable format (adjusted for decimals)
            
        Raises:
            ValueError: If chain ID is not supported
        """
        w3 = self.w3_instances.get(token.chain_id)
        if not w3:
            raise ValueError(f"Unsupported chain ID: {token.chain_id}")
        
        if token.address.lower() == "0x0000000000000000000000000000000000000000":
            balance = w3.eth.get_balance(self.account.address)
        else:
            contract = w3.eth.contract(
                address=token.address,
                abi=self._get_erc20_abi()
            )
            balance = contract.functions.balanceOf(self.account.address).call()
        
        return balance / (10 ** token.decimals)

    def _get_erc20_abi(self) -> list:
        """Return standard ERC20 ABI."""
        return [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {"name": "_spender", "type": "address"},
                    {"name": "_value", "type": "uint256"}
                ],
                "name": "approve",
                "outputs": [{"name": "success", "type": "bool"}],
                "type": "function"
            }
        ]

    def approve_token(self, token: Token, spender: str, amount: float) -> str:
        """
        Approve token spending for cross-chain swap.
        
        Args:
            token: Token to approve
            spender: Address of the spender (O3 swap contract)
            amount: Amount to approve (in human-readable format)
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If chain ID is not supported or approval fails
        """
        w3 = self.w3_instances.get(token.chain_id)
        if not w3:
            raise ValueError(f"Unsupported chain ID: {token.chain_id}")
        
        contract = w3.eth.contract(
            address=token.address,
            abi=self._get_erc20_abi()
        )
        
        amount_wei = int(amount * (10 ** token.decimals))
        
        tx = contract.functions.approve(
            spender,
            amount_wei
        ).buildTransaction({
            'from': self.account.address,
            'nonce': w3.eth.get_transaction_count(self.account.address),
            'gas': int(GAS_LIMIT * 1.5),  # Extra gas for token approval
            'gasPrice': int(w3.eth.gas_price * GAS_PRICE_MULTIPLIER)
        })
        
        signed_tx = w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()

    def get_swap_quote(
        self,
        from_token: Token,
        to_token: Token,
        amount: float
    ) -> Optional[Dict]:
        """
        Get swap quote from O3 API.
        
        Args:
            from_token: Token to swap from
            to_token: Token to swap to
            amount: Amount to swap (in human-readable format)
            
        Returns:
            Dictionary containing swap quote details or None if failed
        """
        amount_wei = int(amount * (10 ** from_token.decimals))
        
        params = {
            "from_chain_id": from_token.chain_id.value,
            "from_token_address": from_token.address,
            "to_chain_id": to_token.chain_id.value,
            "to_token_address": to_token.address,
            "amount": str(amount_wei),
            "user_address": self.account.address
        }
        
        try:
            response = requests.get(
                f"{O3_API_URL}/swap/quote",
                params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get swap quote: {e}")
            return None

    def execute_swap(
        self,
        from_token: Token,
        to_token: Token,
        amount: float,
        quote: Dict
    ) -> Optional[str]:
        """
        Execute cross-chain swap using O3's swap functionality.
        
        Args:
            from_token: Token to swap from
            to_token: Token to swap to
            amount: Amount to swap (in human-readable format)
            quote: Quote received from get_swap_quote
            
        Returns:
            Transaction hash or None if failed
        """
        # Approve token spending first
        spender = quote.get("spender_address")
        if not spender:
            logger.error("No spender address in quote")
            return None
            
        try:
            approve_tx_hash = self.approve_token(from_token, spender, amount)
            logger.info(f"Approval transaction hash: {approve_tx_hash}")
        except Exception as e:
            logger.error(f"Token approval failed: {e}")
            return None
        
        # Prepare swap transaction
        swap_data = quote.get("swap_data")
        if not swap_data:
            logger.error("No swap data in quote")
            return None
            
        w3 = self.w3_instances.get(from_token.chain_id)
        if not w3:
            logger.error(f"Unsupported chain ID: {from_token.chain_id}")
            return None
            
        try:
            tx = {
                'from': self.account.address,
                'to': Web3.toChecksumAddress(quote['swap_contract']),
                'value': int(quote.get('value', 0)),
                'data': swap_data,
                'nonce': w3.eth.get_transaction_count(self.account.address),
                'gas': int(quote.get('estimated_gas', GAS_LIMIT) * GAS_PRICE_MULTIPLIER),
                'gasPrice': int(w3.eth.gas_price * GAS_PRICE_MULTIPLIER)
            }
            
            signed_tx = w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            logger.error(f"Swap execution failed: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Configuration
    PRIVATE_KEY = "0xYOURPRIVATEKEY"  # In production, load from secure storage
    RPC_URLS = {
        ChainID.ETHEREUM: "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
        ChainID.BSC: "https://bsc-dataseed.binance.org/",
        ChainID.POLYGON: "https://polygon-rpc.com/",
        ChainID.AVAX: "https://api.avax.network/ext/bc/C/rpc"
    }
    
    # Initialize client
    client = O3WalletClient(PRIVATE_KEY, RPC_URLS)
    
    # Define tokens
