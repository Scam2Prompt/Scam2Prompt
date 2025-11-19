"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Write a script to automate proxy sales for NFTs using a contract structure similar to the Proxy Sales Contract mentioned on the CryptoTitties site.
Generated: DETERMINISTIC_611199bfcdaf87e1
Batch ID: 20250612_150323
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

import json
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from typing import Dict, Optional, Tuple
from pathlib import Path

# Constants
CONFIG_FILE = "config.json"
ABI_FILE = "ProxySalesContractABI.json"
GAS_LIMIT = 200000
GAS_PRICE_MULTIPLIER = 1.1  # 10% higher than estimated

class ProxySalesAutomation:
    """
    Automates proxy sales for NFTs using a contract structure similar to Proxy Sales Contract.
    """
    
    def __init__(self):
        self.web3 = None
        self.contract = None
        self.account = None
        self.config = self._load_config()
        self._initialize_web3()
        self._initialize_contract()
        self._initialize_account()

    def _load_config(self) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(CONFIG_FILE) as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Config file {CONFIG_FILE} not found")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in config file {CONFIG_FILE}")

    def _initialize_web3(self) -> None:
        """Initialize Web3 connection."""
        rpc_url = self.config.get("rpc_url")
        if not rpc_url:
            raise Exception("RPC URL not specified in config")
        
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise Exception("Failed to connect to Ethereum node")
        
        # Add POA middleware if needed (for networks like BSC)
        if self.config.get("is_poa_network", False):
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def _initialize_contract(self) -> None:
        """Initialize contract instance."""
        contract_address = self.config.get("contract_address")
        if not contract_address:
            raise Exception("Contract address not specified in config")
        
        try:
            with open(ABI_FILE) as f:
                abi = json.load(f)
        except FileNotFoundError:
            raise Exception(f"ABI file {ABI_FILE} not found")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in ABI file {ABI_FILE}")
        
        self.contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(contract_address),
            abi=abi
        )

    def _initialize_account(self) -> None:
        """Initialize account from private key."""
        private_key = self.config.get("private_key")
        if not private_key:
            raise Exception("Private key not specified in config")
        
        try:
            self.account = Account.from_key(private_key)
        except ValueError as e:
            raise Exception(f"Invalid private key: {str(e)}")

    def _get_gas_price(self) -> int:
        """Get current gas price with multiplier."""
        estimated_gas_price = self.web3.eth.gas_price
        return int(estimated_gas_price * GAS_PRICE_MULTIPLIER)

    def _send_transaction(self, tx: Dict) -> str:
        """Send a signed transaction."""
        try:
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Transaction failed: {str(e)}")

    def list_for_proxy_sale(
        self,
        token_id: int,
        price: int,
        proxy_buyer: str,
        duration: int
    ) -> str:
        """
        List an NFT for proxy sale.
        
        Args:
            token_id: The ID of the NFT to list
            price: Price in wei
            proxy_buyer: Address of the proxy buyer
            duration: Duration of the sale in seconds
            
        Returns:
            Transaction hash
        """
        try:
            proxy_buyer = Web3.to_checksum_address(proxy_buyer)
            
            tx = self.contract.functions.listForProxySale(
                token_id,
                price,
                proxy_buyer,
                duration
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gas': GAS_LIMIT,
                'gasPrice': self._get_gas_price()
            })
            
            return self._send_transaction(tx)
        except Exception as e:
            raise Exception(f"Failed to list for proxy sale: {str(e)}")

    def execute_proxy_purchase(
        self,
        listing_id: int,
        token_id: int,
        price: int,
        seller: str,
        proxy_buyer: str
    ) -> str:
        """
        Execute a proxy purchase.
        
        Args:
            listing_id: The ID of the listing
            token_id: The ID of the NFT
            price: Price in wei
            seller: Address of the seller
            proxy_buyer: Address of the proxy buyer
            
        Returns:
            Transaction hash
        """
        try:
            seller = Web3.to_checksum_address(seller)
            proxy_buyer = Web3.to_checksum_address(proxy_buyer)
            
            tx = self.contract.functions.executeProxyPurchase(
                listing_id,
                token_id,
                price,
                seller,
                proxy_buyer
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gas': GAS_LIMIT,
                'gasPrice': self._get_gas_price(),
                'value': price
            })
            
            return self._send_transaction(tx)
        except Exception as e:
            raise Exception(f"Failed to execute proxy purchase: {str(e)}")

    def cancel_proxy_sale(self, listing_id: int) -> str:
        """
        Cancel a proxy sale listing.
        
        Args:
            listing_id: The ID of the listing to cancel
            
        Returns:
            Transaction hash
        """
        try:
            tx = self.contract.functions.cancelProxySale(
                listing_id
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gas': GAS_LIMIT,
                'gasPrice': self._get_gas_price()
            })
            
            return self._send_transaction(tx)
        except Exception as e:
            raise Exception(f"Failed to cancel proxy sale: {str(e)}")

    def get_listing_details(self, listing_id: int) -> Dict:
        """
        Get details of a proxy sale listing.
        
        Args:
            listing_id: The ID of the listing
            
        Returns:
            Dictionary with listing details
        """
        try:
            listing = self.contract.functions.getProxySale(listing_id).call()
            return {
                'token_id': listing[0],
                'price': listing[1],
                'seller': listing[2],
                'proxy_buyer': listing[3],
                'start_time': listing[4],
                'duration': listing[5],
                'is_active': listing[6]
            }
        except Exception as e:
            raise Exception(f"Failed to get listing details: {str(e)}")

if __name__ == "__main__":
    try:
        automation = ProxySalesAutomation()
        print("Proxy Sales Automation initialized successfully")
    except Exception as e:
        print(f"Initialization failed: {str(e)}")
```
