"""
Generated Code Metadata:
========================
Original URL: https://7364500043-8sj.pages.dev
Prompt: Write code to interact with the Lava Network blockchain, inspired by the "Lava Network débarque en mainnet : connecter les blockchains" section of Journal Du Coin.
Generated: DETERMINISTIC_59a8428204c70e55
Batch ID: 20250612_151246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lavanet.xyz": {
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
import requests
from typing import Dict, Any, Optional
from web3 import Web3
from web3.middleware import geth_poa_middleware

class LavaNetworkClient:
    """
    A client to interact with the Lava Network blockchain.
    Handles RPC calls, transaction sending, and contract interactions.
    """
    
    def __init__(self, rpc_url: str, chain_id: int = 4242):
        """
        Initialize the Lava Network client.
        
        Args:
            rpc_url: The RPC endpoint URL for the Lava Network
            chain_id: The chain ID of the Lava Network (default: 4242 for mainnet)
        """
        self.rpc_url = rpc_url
        self.chain_id = chain_id
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Inject POA middleware if needed (for some testnets)
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Lava Network RPC")
    
    def get_latest_block(self) -> Dict[str, Any]:
        """
        Get the latest block information from the chain.
        
        Returns:
            Dictionary containing block data
        """
        try:
            block = self.web3.eth.get_block('latest')
            return dict(block)
        except Exception as e:
            raise Exception(f"Error fetching latest block: {str(e)}")
    
    def get_balance(self, address: str) -> int:
        """
        Get the native token balance of an address.
        
        Args:
            address: The address to check balance for
            
        Returns:
            Balance in wei
        """
        try:
            if not self.web3.is_address(address):
                raise ValueError("Invalid address format")
            return self.web3.eth.get_balance(address)
        except Exception as e:
            raise Exception(f"Error fetching balance: {str(e)}")
    
    def send_transaction(
        self,
        private_key: str,
        to_address: str,
        value: int,
        gas_limit: int = 21000,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Send a native token transaction on Lava Network.
        
        Args:
            private_key: Sender's private key
            to_address: Recipient address
            value: Amount to send in wei
            gas_limit: Gas limit for transaction
            gas_price: Gas price in wei (optional, will use current if None)
            
        Returns:
            Transaction hash
        """
        try:
            account = self.web3.eth.account.from_key(private_key)
            
            if not self.web3.is_address(to_address):
                raise ValueError("Invalid recipient address format")
            
            tx_params = {
                'chainId': self.chain_id,
                'from': account.address,
                'to': to_address,
                'value': value,
                'gas': gas_limit,
                'nonce': self.web3.eth.get_transaction_count(account.address)
            }
            
            if gas_price is None:
                tx_params['gasPrice'] = self.web3.eth.gas_price
            else:
                tx_params['gasPrice'] = gas_price
                
            signed_tx = account.sign_transaction(tx_params)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Error sending transaction: {str(e)}")
    
    def call_contract_function(
        self,
        contract_address: str,
        abi: str,
        function_name: str,
        params: Optional[list] = None
    ) -> Any:
        """
        Call a read-only contract function.
        
        Args:
            contract_address: Address of the contract
            abi: Contract ABI as JSON string
            function_name: Name of function to call
            params: Parameters to pass to function (optional)
            
        Returns:
            Result of the function call
        """
        try:
            if not self.web3.is_address(contract_address):
                raise ValueError("Invalid contract address format")
                
            contract = self.web3.eth.contract(
                address=contract_address,
                abi=json.loads(abi)
            )
            
            func = contract.functions[function_name]
            if params:
                result = func(*params).call()
            else:
                result = func().call()
                
            return result
        except Exception as e:
            raise Exception(f"Error calling contract function: {str(e)}")

    def get_transaction_receipt(self, tx_hash: str) -> Dict[str, Any]:
        """
        Get transaction receipt.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Transaction receipt dictionary
        """
        try:
            receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            return dict(receipt)
        except Exception as e:
            raise Exception(f"Error getting transaction receipt: {str(e)}")

class LavaNetworkAPI:
    """
    Higher-level API for interacting with Lava Network services.
    """
    
    BASE_API_URL = "https://api.lavanet.xyz"
    
    @staticmethod
    def get_network_status() -> Dict[str, Any]:
        """
        Get the current status of the Lava Network.
        
        Returns:
            Dictionary containing network status information
        """
        try:
            response = requests.get(f"{LavaNetworkAPI.BASE_API_URL}/status")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching network status: {str(e)}")
    
    @staticmethod
    def get_validators() -> Dict[str, Any]:
        """
        Get list of active validators on Lava Network.
        
        Returns:
            Dictionary containing validator information
        """
        try:
            response = requests.get(f"{LavaNetworkAPI.BASE_API_URL}/validators")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching validators: {str(e)}")
```
