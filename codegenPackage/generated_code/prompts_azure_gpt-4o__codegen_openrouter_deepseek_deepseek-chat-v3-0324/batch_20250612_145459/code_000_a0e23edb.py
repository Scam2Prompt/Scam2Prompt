"""
Generated Code Metadata:
========================
Original URL: https://app-explorer.pages.dev
Prompt: Write a code snippet to interact with a decentralized application (DApp) using the Dapp Protocol's multichain-friendly features to perform transactions on both Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_a0e23edbac19fe11
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

class DAppInteractor:
    """
    A class to interact with DApps on multiple blockchains using the Dapp Protocol.
    Supports Ethereum and Binance Smart Chain (BSC).
    """
    
    def __init__(self, eth_rpc_url, bsc_rpc_url, private_key):
        """
        Initialize the DApp interactor with RPC URLs and private key.
        
        Args:
            eth_rpc_url (str): Ethereum RPC endpoint URL
            bsc_rpc_url (str): BSC RPC endpoint URL
            private_key (str): Private key for transaction signing
        """
        self.eth_web3 = Web3(Web3.HTTPProvider(eth_rpc_url))
        self.bsc_web3 = Web3(Web3.HTTPProvider(bsc_rpc_url))
        
        # Add POA middleware for BSC
        self.bsc_web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.private_key = private_key
        self.account = self.eth_web3.eth.account.from_key(private_key)
        
    def get_contract(self, web3, contract_address, abi_path):
        """
        Load contract ABI and create contract instance.
        
        Args:
            web3: Web3 instance (ETH or BSC)
            contract_address (str): Contract address
            abi_path (str): Path to contract ABI JSON file
            
        Returns:
            Contract: Web3 contract instance
        """
        with open(abi_path) as f:
            abi = json.load(f)
        return web3.eth.contract(address=contract_address, abi=abi)
    
    def build_transaction(self, web3, contract, function_name, *args, value=0):
        """
        Build a transaction for the specified contract function.
        
        Args:
            web3: Web3 instance (ETH or BSC)
            contract: Contract instance
            function_name (str): Name of contract function to call
            *args: Arguments for the contract function
            value (int): Value to send with transaction (in wei)
            
        Returns:
            dict: Unsigned transaction dictionary
        """
        nonce = web3.eth.get_transaction_count(self.account.address)
        function = contract.get_function_by_name(function_name)(*args)
        
        tx = function.build_transaction({
            'chainId': web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce,
            'value': value
        })
        return tx
    
    def sign_and_send_transaction(self, web3, tx):
        """
        Sign and send a transaction.
        
        Args:
            web3: Web3 instance (ETH or BSC)
            tx (dict): Unsigned transaction dictionary
            
        Returns:
            str: Transaction hash
        """
        signed_tx = web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def execute_on_ethereum(self, contract_address, abi_path, function_name, *args, value=0):
        """
        Execute a transaction on Ethereum.
        
        Args:
            contract_address (str): Contract address
            abi_path (str): Path to contract ABI JSON file
            function_name (str): Name of contract function to call
            *args: Arguments for the contract function
            value (int): Value to send with transaction (in wei)
            
        Returns:
            str: Transaction hash
        """
        contract = self.get_contract(self.eth_web3, contract_address, abi_path)
        tx = self.build_transaction(self.eth_web3, contract, function_name, *args, value=value)
        return self.sign_and_send_transaction(self.eth_web3, tx)
    
    def execute_on_bsc(self, contract_address, abi_path, function_name, *args, value=0):
        """
        Execute a transaction on Binance Smart Chain.
        
        Args:
            contract_address (str): Contract address
            abi_path (str): Path to contract ABI JSON file
            function_name (str): Name of contract function to call
            *args: Arguments for the contract function
            value (int): Value to send with transaction (in wei)
            
        Returns:
            str: Transaction hash
        """
        contract = self.get_contract(self.bsc_web3, contract_address, abi_path)
        tx = self.build_transaction(self.bsc_web3, contract, function_name, *args, value=value)
        return self.sign_and_send_transaction(self.bsc_web3, tx)
    
    def wait_for_transaction(self, web3, tx_hash):
        """
        Wait for transaction receipt and return it.
        
        Args:
            web3: Web3 instance (ETH or BSC)
            tx_hash (str): Transaction hash
            
        Returns:
            dict: Transaction receipt
        """
        return web3.eth.wait_for_transaction_receipt(tx_hash)
```
