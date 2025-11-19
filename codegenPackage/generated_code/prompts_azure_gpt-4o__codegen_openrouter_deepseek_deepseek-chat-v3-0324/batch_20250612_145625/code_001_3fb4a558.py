"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: Generate Python code to interact with the $MASA token on the Ethereum blockchain, including functions for checking balances, transferring tokens, and retrieving token metadata.
Generated: DETERMINISTIC_3fb4a558c66ddf3e
Batch ID: 20250612_145625
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
from eth_utils import to_checksum_address
from typing import Dict, Union, Optional

# ERC-20 ABI for token interactions
ERC20_ABI = json.loads('''
[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
''')

class MasaToken:
    def __init__(self, rpc_url: str, token_address: str, private_key: Optional[str] = None):
        """
        Initialize MASA token interaction class.
        
        Args:
            rpc_url: Ethereum node RPC URL
            token_address: MASA token contract address
            private_key: Optional private key for sending transactions
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Add middleware for POA networks if needed
        try:
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        except ValueError:
            pass
        
        self.token_address = to_checksum_address(token_address)
        self.contract = self.web3.eth.contract(address=self.token_address, abi=ERC20_ABI)
        
        if private_key:
            self.account = self.web3.eth.account.from_key(private_key)
            self.web3.eth.default_account = self.account.address
        else:
            self.account = None

    def get_balance(self, address: str) -> int:
        """
        Get MASA token balance for an address.
        
        Args:
            address: Ethereum address to check balance for
            
        Returns:
            Token balance in smallest unit (wei)
        """
        checksum_address = to_checksum_address(address)
        return self.contract.functions.balanceOf(checksum_address).call()

    def get_balance_human(self, address: str) -> float:
        """
        Get MASA token balance in human-readable format.
        
        Args:
            address: Ethereum address to check balance for
            
        Returns:
            Token balance adjusted for decimals
        """
        balance = self.get_balance(address)
        decimals = self.contract.functions.decimals().call()
        return balance / (10 ** decimals)

    def get_metadata(self) -> Dict[str, Union[str, int]]:
        """
        Get MASA token metadata (name, symbol, decimals).
        
        Returns:
            Dictionary containing token metadata
        """
        return {
            'name': self.contract.functions.name().call(),
            'symbol': self.contract.functions.symbol().call(),
            'decimals': self.contract.functions.decimals().call()
        }

    def transfer(self, to_address: str, amount: int, gas_price: Optional[int] = None, gas_limit: int = 200000) -> str:
        """
        Transfer MASA tokens to another address.
        
        Args:
            to_address: Recipient address
            amount: Amount to send in smallest unit (wei)
            gas_price: Optional gas price in wei
            gas_limit: Gas limit for transaction
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If no private key was provided during initialization
        """
        if not self.account:
            raise ValueError("Private key required for sending transactions")
            
        checksum_to = to_checksum_address(to_address)
        
        # Build transaction
        tx = self.contract.functions.transfer(checksum_to, amount).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': gas_limit,
            'gasPrice': gas_price if gas_price else self.web3.eth.gas_price
        })
        
        # Sign and send transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()

    def transfer_human(self, to_address: str, amount: float, gas_price: Optional[int] = None, gas_limit: int = 200000) -> str:
        """
        Transfer MASA tokens with human-readable amount.
        
        Args:
            to_address: Recipient address
            amount: Amount to send in token units
            gas_price: Optional gas price in wei
            gas_limit: Gas limit for transaction
            
        Returns:
            Transaction hash
        """
        decimals = self.contract.functions.decimals().call()
        amount_wei = int(amount * (10 ** decimals))
        return self.transfer(to_address, amount_wei, gas_price, gas_limit)

    def wait_for_transaction(self, tx_hash: str) -> Dict:
        """
        Wait for a transaction to be mined and return receipt.
        
        Args:
            tx_hash: Transaction hash to wait for
            
        Returns:
            Transaction receipt
        """
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
```
