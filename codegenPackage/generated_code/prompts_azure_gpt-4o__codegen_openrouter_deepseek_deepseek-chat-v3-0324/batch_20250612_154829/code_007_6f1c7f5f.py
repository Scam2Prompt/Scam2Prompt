"""
Generated Code Metadata:
========================
Original URL: https://hovrachev.ru
Prompt: Create a tutorial for integrating Yield Yak's API into a DeFi application to enable auto-compounding and token swapping functionalities.
Generated: DETERMINISTIC_6f1c7f5f1ac16ef9
Batch ID: 20250612_154829
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.avax.network/ext/bc/C/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.yieldyak.com": {
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
import json
from web3 import Web3
from typing import Dict, Optional, List

# Constants
YIELD_YAK_API_BASE_URL = "https://api.yieldyak.com"
CHAIN_ID = 43114  # Avalanche C-Chain
WEB3_PROVIDER_URL = "https://api.avax.network/ext/bc/C/rpc"

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

class YieldYakIntegration:
    """
    A class to interact with Yield Yak's API for auto-compounding and token swapping.
    """
    
    def __init__(self, private_key: str):
        """
        Initialize the YieldYakIntegration with a private key.
        
        Args:
            private_key (str): The private key of the wallet to interact with the blockchain.
        """
        self.private_key = private_key
        self.account = web3.eth.account.from_key(private_key)
        self.address = self.account.address
        
    def _make_api_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a request to Yield Yak's API.
        
        Args:
            endpoint (str): The API endpoint to call.
            params (Optional[Dict]): Optional query parameters.
            
        Returns:
            Dict: The JSON response from the API.
            
        Raises:
            Exception: If the API request fails.
        """
        url = f"{YIELD_YAK_API_BASE_URL}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
    
    def get_auto_compounding_farms(self) -> List[Dict]:
        """
        Get a list of auto-compounding farms available on Yield Yak.
        
        Returns:
            List[Dict]: A list of auto-compounding farms.
        """
        return self._make_api_request("farms")
    
    def get_token_swap_routes(self, token_in: str, token_out: str) -> List[Dict]:
        """
        Get swap routes between two tokens.
        
        Args:
            token_in (str): The address of the input token.
            token_out (str): The address of the output token.
            
        Returns:
            List[Dict]: A list of possible swap routes.
        """
        params = {
            "tokenIn": token_in,
            "tokenOut": token_out,
            "chainId": CHAIN_ID
        }
        return self._make_api_request("swap", params=params)
    
    def build_swap_transaction(
        self,
        token_in: str,
        token_out: str,
        amount_in: int,
        slippage: float = 0.5,
        recipient: Optional[str] = None
    ) -> Dict:
        """
        Build a swap transaction.
        
        Args:
            token_in (str): The address of the input token.
            token_out (str): The address of the output token.
            amount_in (int): The amount of input token in smallest units.
            slippage (float): The maximum slippage percentage (default: 0.5%).
            recipient (Optional[str]): The recipient address (default: sender's address).
            
        Returns:
            Dict: The transaction data.
            
        Raises:
            Exception: If the swap route cannot be built.
        """
        if not recipient:
            recipient = self.address
            
        params = {
            "tokenIn": token_in,
            "tokenOut": token_out,
            "amountIn": amount_in,
            "slippage": slippage,
            "recipient": recipient,
            "chainId": CHAIN_ID
        }
        
        try:
            response = self._make_api_request("swap/build", params=params)
            return {
                "to": response["to"],
                "data": response["data"],
                "value": response["value"],
                "gas": response["gas"],
                "gasPrice": response["gasPrice"]
            }
        except Exception as e:
            raise Exception(f"Failed to build swap transaction: {e}")
    
    def execute_transaction(self, transaction_data: Dict) -> str:
        """
        Execute a transaction on the blockchain.
        
        Args:
            transaction_data (Dict): The transaction data.
            
        Returns:
            str: The transaction hash.
            
        Raises:
            Exception: If the transaction fails.
        """
        try:
            nonce = web3.eth.get_transaction_count(self.address)
            tx = {
                "nonce": nonce,
                "to": transaction_data["to"],
                "data": transaction_data["data"],
                "value": int(transaction_data["value"]),
                "gas": int(transaction_data["gas"]),
                "gasPrice": int(transaction_data["gasPrice"]),
                "chainId": CHAIN_ID
            }
            
            signed_tx = web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Transaction failed: {e}")
    
    def auto_compound(self, farm_address: str) -> str:
        """
        Execute an auto-compound transaction for a specific farm.
        
        Args:
            farm_address (str): The address of the farm to compound.
            
        Returns:
            str: The transaction hash.
            
        Raises:
            Exception: If the auto-compound transaction fails.
        """
        try:
            # Get the auto-compound transaction data
            params = {
                "farmAddress": farm_address,
                "account": self.address,
                "chainId": CHAIN_ID
            }
            response = self._make_api_request("farms/compound/build", params=params)
            
            # Execute the transaction
            tx_data = {
                "to": response["to"],
                "data": response["data"],
                "value": response["value"],
                "gas": response["gas"],
                "gasPrice": response["gasPrice"]
            }
            return self.execute_transaction(tx_data)
        except Exception as e:
            raise Exception(f"Auto-compound failed: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize with your private key (in production, use environment variables)
    private_key = "YOUR_PRIVATE_KEY"
    yak = YieldYakIntegration(private_key)
    
    # Example: Get auto-compounding farms
    farms = yak.get_auto_compounding_farms()
    print("Available farms:", farms)
    
    # Example: Swap tokens
    token_in = "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"  # WAVAX
    token_out = "0x60781C2586D68229fde47564546784ab3fACA982"  # PNG
    amount_in = web3.to_wei(1, 'ether')  # 1 AVAX
    
    swap_routes = yak.get_token_swap_routes(token_in, token_out)
    print("Swap routes:", swap_routes)
    
    tx_data = yak.build_swap_transaction(token_in, token_out, amount_in)
    tx_hash = yak.execute_transaction(tx_data)
    print("Swap transaction hash:", tx_hash)
    
    # Example: Auto-compound
    if farms:
        farm_address = farms[0]["address"]
        tx_hash = yak.auto_compound(farm_address)
        print("Auto-compound transaction hash:", tx_hash)
```
