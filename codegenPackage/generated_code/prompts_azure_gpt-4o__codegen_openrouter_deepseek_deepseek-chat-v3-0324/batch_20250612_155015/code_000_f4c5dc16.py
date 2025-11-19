"""
Generated Code Metadata:
========================
Original URL: https://pythnew.com
Prompt: Write Python code to integrate a price feed oracle from Pyth Network into a smart contract for real-time market data retrieval.
Generated: DETERMINISTIC_f4c5dc1658dabfa0
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from web3 import Web3
from web3.contract import Contract
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class PythPriceFeed:
    price: float
    confidence: float
    exponent: int
    publish_time: int

class PythOracle:
    """
    A class to interact with Pyth Network's price feed oracle.
    """
    
    def __init__(self, pyth_endpoint: str, web3_provider: str, contract_address: str, contract_abi: str):
        """
        Initialize the Pyth Oracle.
        
        Args:
            pyth_endpoint: URL of Pyth Network's HTTP API
            web3_provider: Web3 provider URL (e.g., Infura, Alchemy)
            contract_address: Address of the smart contract to update
            contract_abi: ABI of the smart contract
        """
        self.pyth_endpoint = pyth_endpoint
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract_address = contract_address
        self.contract_abi = json.loads(contract_abi)
        self.contract: Contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
    
    def get_price_feed(self, feed_id: str) -> Optional[PythPriceFeed]:
        """
        Fetch price feed data from Pyth Network.
        
        Args:
            feed_id: The ID of the price feed to retrieve
            
        Returns:
            PythPriceFeed object if successful, None otherwise
        """
        try:
            url = f"{self.pyth_endpoint}/api/latest_price_feeds?ids[]={feed_id}"
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            if not data:
                return None
                
            price_data = data[0]['price']
            return PythPriceFeed(
                price=float(price_data['price']),
                confidence=float(price_data['confidence']),
                exponent=int(price_data['exponent']),
                publish_time=int(price_data['publish_time'])
            )
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price feed: {e}")
            return None
    
    def update_price_feed(
        self,
        feed_id: str,
        private_key: str,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> Optional[str]:
        """
        Update the smart contract with the latest price feed data.
        
        Args:
            feed_id: The ID of the price feed to update
            private_key: Private key for transaction signing
            gas_limit: Gas limit for the transaction
            gas_price: Gas price for the transaction (optional)
            
        Returns:
            Transaction hash if successful, None otherwise
        """
        price_feed = self.get_price_feed(feed_id)
        if not price_feed:
            return None
            
        try:
            account = self.web3.eth.account.from_key(private_key)
            nonce = self.web3.eth.get_transaction_count(account.address)
            
            if gas_price is None:
                gas_price = self.web3.eth.gas_price
                
            tx = self.contract.functions.updatePrice(
                feed_id,
                int(price_feed.price * (10 ** -price_feed.exponent)),
                int(price_feed.confidence * (10 ** -price_feed.exponent)),
                price_feed.publish_time
            ).build_transaction({
                'chainId': self.web3.eth.chain_id,
                'gas': gas_limit,
                'gasPrice': gas_price,
                'nonce': nonce,
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
            
        except Exception as e:
            print(f"Error updating price feed: {e}")
            return None
```
