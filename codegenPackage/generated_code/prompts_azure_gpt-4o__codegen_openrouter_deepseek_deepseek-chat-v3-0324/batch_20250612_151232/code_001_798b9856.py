"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: Recommend libraries or APIs for integrating Ethereum-based blockchain functionality into a decentralized marketplace like Pushd, focusing on token management and secure transactions.
Generated: DETERMINISTIC_798b9856db48b91f
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from eth_utils import to_wei, from_wei
from hexbytes import HexBytes
import json
import os
from typing import Optional, Dict, Any, Union

# Constants
DEFAULT_GAS = 200000
DEFAULT_GAS_PRICE = to_wei('50', 'gwei')

class EthereumManager:
    """
    A class to manage Ethereum blockchain interactions including:
    - Token management (ERC20/ERC721)
    - Secure transactions
    - Smart contract interactions
    """
    
    def __init__(self, provider_url: str, chain_id: int = 1, poa: bool = False):
        """
        Initialize Ethereum connection.
        
        Args:
            provider_url: URL of Ethereum node/provider (Infura/Alchemy/etc.)
            chain_id: Network chain ID (1=Mainnet, 5=Goerli, etc.)
            poa: Whether the network uses Proof of Authority consensus
        """
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        
        if poa:
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            
        self.chain_id = chain_id
        self.account = None
        
    def load_account(self, private_key: str) -> None:
        """
        Load an account from private key.
        
        Args:
            private_key: The private key of the Ethereum account
        """
        self.account = Account.from_key(private_key)
        
    def create_account(self) -> Dict[str, str]:
        """
        Create a new Ethereum account.
        
        Returns:
            Dictionary containing address and private key
        """
        account = Account.create()
        return {
            'address': account.address,
            'private_key': account.key.hex()
        }
        
    def get_balance(self, address: Optional[str] = None) -> float:
        """
        Get ETH balance of an address.
        
        Args:
            address: Ethereum address (defaults to loaded account)
            
        Returns:
            Balance in ETH
        """
        if not address and not self.account:
            raise ValueError("No address provided and no account loaded")
            
        address = address or self.account.address
        wei_balance = self.w3.eth.get_balance(address)
        return float(from_wei(wei_balance, 'ether'))
        
    def get_token_balance(
        self,
        token_address: str,
        address: Optional[str] = None
    ) -> float:
        """
        Get token balance of an address for an ERC20 token.
        
        Args:
            token_address: Contract address of the token
            address: Ethereum address (defaults to loaded account)
            
        Returns:
            Token balance
        """
        if not address and not self.account:
            raise ValueError("No address provided and no account loaded")
            
        address = address or self.account.address
        contract = self._get_erc20_contract(token_address)
        balance = contract.functions.balanceOf(address).call()
        decimals = contract.functions.decimals().call()
        return balance / (10 ** decimals)
        
    def send_eth(
        self,
        to_address: str,
        amount: float,
        gas: int = DEFAULT_GAS,
        gas_price: int = DEFAULT_GAS_PRICE
    ) -> HexBytes:
        """
        Send ETH to another address.
        
        Args:
            to_address: Recipient address
            amount: Amount to send in ETH
            gas: Gas limit
            gas_price: Gas price in wei
            
        Returns:
            Transaction hash
        """
        if not self.account:
            raise ValueError("No account loaded")
            
        tx = {
            'chainId': self.chain_id,
            'to': to_address,
            'value': to_wei(amount, 'ether'),
            'gas': gas,
            'gasPrice': gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address)
        }
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.account.key)
        return self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
    def send_token(
        self,
        token_address: str,
        to_address: str,
        amount: float,
        gas: int = DEFAULT_GAS,
        gas_price: int = DEFAULT_GAS_PRICE
    ) -> HexBytes:
        """
        Send ERC20 tokens to another address.
        
        Args:
            token_address: Contract address of the token
            to_address: Recipient address
            amount: Amount to send
            gas: Gas limit
            gas_price: Gas price in wei
            
        Returns:
            Transaction hash
        """
        if not self.account:
            raise ValueError("No account loaded")
            
        contract = self._get_erc20_contract(token_address)
        decimals = contract.functions.decimals().call()
        amount_wei = int(amount * (10 ** decimals))
        
        tx = contract.functions.transfer(
            to_address,
            amount_wei
        ).build_transaction({
            'chainId': self.chain_id,
            'gas': gas,
            'gasPrice': gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address)
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.account.key)
        return self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
    def _get_erc20_contract(self, token_address: str) -> Any:
        """
        Get ERC20 contract instance.
        
        Args:
            token_address: Contract address of the token
            
        Returns:
            Contract instance
        """
        with open('erc20_abi.json') as f:
            abi = json.load(f)
            
        return self.w3.eth.contract(address=token_address, abi=abi)
        
    def wait_for_transaction(self, tx_hash: Union[str, HexBytes]) -> Dict[str, Any]:
        """
        Wait for a transaction to be mined and return receipt.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            Transaction receipt
        """
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
    def get_transaction_status(self, tx_hash: Union[str, HexBytes]) -> bool:
        """
        Check if a transaction was successful.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            True if transaction was successful, False otherwise
        """
        receipt = self.w3.eth.get_transaction_receipt(tx_hash)
        return receipt.status == 1


# Example ERC20 ABI (should be saved in erc20_abi.json)
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "from", "type": "address"},
            {"indexed": True, "name": "to", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    }
]

# Save ERC20 ABI to file
if not os.path.exists('erc20_abi.json'):
    with open('erc20_abi.json', 'w') as f:
        json.dump(ERC20_ABI, f)
```
