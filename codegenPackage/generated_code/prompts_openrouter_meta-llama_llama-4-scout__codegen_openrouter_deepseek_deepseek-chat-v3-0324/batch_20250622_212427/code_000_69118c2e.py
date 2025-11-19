"""
Generated Code Metadata:
========================
Original URL: https://stakeflarre.com
Prompt: What is the purpose of Stakeflarre's Time Series Oracle (FTSO) and how does it provide decentralized data to dapps on the network?
Generated: DETERMINISTIC_69118c2ec9345c4c
Batch ID: 20250622_212427
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://flare-testnet.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://ftso-providers.flare.network": {
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
# FTSO (Flare Time Series Oracle) Implementation Example

import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from web3 import Web3
from eth_account import Account
from eth_abi import encode_abi
import requests

@dataclass
class DataProvider:
    address: str
    weight: float
    is_active: bool

class FTSO:
    """
    Flare Time Series Oracle implementation that provides decentralized data feeds to dApps.
    """
    
    def __init__(self, web3: Web3, contract_address: str, provider_url: str):
        """
        Initialize FTSO with Web3 connection and contract details.
        
        Args:
            web3: Web3 instance connected to the Flare network
            contract_address: Address of the FTSO smart contract
            provider_url: URL for fetching provider data
        """
        self.web3 = web3
        self.contract_address = contract_address
        self.provider_url = provider_url
        self.data_providers: Dict[str, DataProvider] = {}
        
    def update_data_providers(self) -> bool:
        """
        Fetch and update the list of active data providers from the network.
        
        Returns:
            bool: True if providers were updated successfully
        """
        try:
            response = requests.get(f"{self.provider_url}/providers")
            response.raise_for_status()
            providers_data = response.json()
            
            self.data_providers.clear()
            for provider in providers_data:
                self.data_providers[provider['address']] = DataProvider(
                    address=provider['address'],
                    weight=provider['weight'],
                    is_active=provider['is_active']
                )
            return True
        except Exception as e:
            print(f"Error updating data providers: {e}")
            return False
    
    def get_price_data(self, symbol: str) -> Optional[float]:
        """
        Get decentralized price data for a given symbol from the FTSO.
        
        Args:
            symbol: The symbol to get price data for (e.g., "BTC", "ETH")
            
        Returns:
            Optional[float]: The aggregated price or None if unavailable
        """
        try:
            # Get price data from active providers
            provider_prices = []
            total_weight = 0.0
            
            for provider in self.data_providers.values():
                if not provider.is_active:
                    continue
                    
                # In a real implementation, this would query each provider's submitted data
                # For this example, we'll simulate getting price data
                price = self._simulate_provider_price(provider.address, symbol)
                if price is not None:
                    provider_prices.append((price, provider.weight))
                    total_weight += provider.weight
            
            if not provider_prices:
                return None
                
            # Calculate weighted median price
            sorted_prices = sorted(provider_prices, key=lambda x: x[0])
            cumulative_weight = 0.0
            median_weight = total_weight / 2
            
            for price, weight in sorted_prices:
                cumulative_weight += weight
                if cumulative_weight >= median_weight:
                    return price
                    
            return sorted_prices[-1][0]
        except Exception as e:
            print(f"Error getting price data: {e}")
            return None
    
    def submit_price_data(self, private_key: str, symbol: str, price: float) -> bool:
        """
        Submit price data to the FTSO as a data provider.
        
        Args:
            private_key: Private key of the submitting account
            symbol: The symbol being submitted
            price: The price being submitted
            
        Returns:
            bool: True if submission was successful
        """
        try:
            account = Account.from_key(private_key)
            nonce = self.web3.eth.get_transaction_count(account.address)
            
            # Construct transaction data (simplified for example)
            tx_data = {
                'chainId': self.web3.eth.chain_id,
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price,
                'nonce': nonce,
                'to': self.contract_address,
                'value': 0,
                'data': self._encode_submit_data(symbol, price)
            }
            
            signed_tx = account.sign_transaction(tx_data)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            return receipt.status == 1
        except Exception as e:
            print(f"Error submitting price data: {e}")
            return False
    
    def _encode_submit_data(self, symbol: str, price: float) -> str:
        """
        Encode submission data for the smart contract call.
        
        Args:
            symbol: The symbol being submitted
            price: The price being submitted
            
        Returns:
            str: Encoded function call data
        """
        # Simplified encoding - actual implementation would use contract ABI
        return encode_abi(['string', 'uint256'], [symbol, int(price * 10**18)])
    
    def _simulate_provider_price(self, provider_address: str, symbol: str) -> Optional[float]:
        """
        Simulate getting price data from a provider (for example purposes).
        
        Args:
            provider_address: Address of the provider
            symbol: Symbol to get price for
            
        Returns:
            Optional[float]: Simulated price or None
        """
        # In a real implementation, this would query the provider's submitted data
        # For this example, we'll return a random price around a base value
        base_prices = {
            "BTC": 50000,
            "ETH": 3000,
            "XRP": 0.5,
            "FLR": 0.1
        }
        
        if symbol not in base_prices:
            return None
            
        import random
        variation = random.uniform(-0.05, 0.05)  # ±5% variation
        return base_prices[symbol] * (1 + variation)

# Example usage
if __name__ == "__main__":
    # Initialize Web3 connection (using testnet for example)
    web3 = Web3(Web3.HTTPProvider("https://flare-testnet.infura.io/v3/YOUR_INFURA_KEY"))
    
    # Initialize FTSO
    ftso = FTSO(
        web3=web3,
        contract_address="0x123...abc",  # Example contract address
        provider_url="https://ftso-providers.flare.network"
    )
    
    # Update data providers
    if ftso.update_data_providers():
        print("Successfully updated data providers")
    
    # Get price data
    btc_price = ftso.get_price_data("BTC")
    if btc_price is not None:
        print(f"BTC price: {btc_price}")
    
    # Example of submitting price data (would need valid private key)
    # if ftso.submit_price_data("0xprivkey...", "BTC", 51000):
    #     print("Price submitted successfully")
```
