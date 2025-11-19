"""
Generated Code Metadata:
========================
Original URL: https://deelance-fi.pages.dev
Prompt: Create a Python script using Web3.py to interact with an ERC20 token contract, similar to DeeLance's $DLANCE token, including functionalities for transferring tokens and checking balances.
Generated: DETERMINISTIC_c82cf323d00cc787
Batch ID: 20250612_152439
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
from typing import Optional, Dict, Any

class ERC20Token:
    """
    A class to interact with an ERC20 token contract using Web3.py.
    Supports balance checks, token transfers, and allowance management.
    """
    
    def __init__(self, rpc_url: str, contract_address: str, abi_path: str = None):
        """
        Initialize the ERC20Token instance.
        
        Args:
            rpc_url: URL of the Ethereum node or provider.
            contract_address: Address of the ERC20 token contract.
            abi_path: Path to the contract ABI JSON file. If None, uses a standard ERC20 ABI.
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Add POA middleware if needed (e.g., for Binance Smart Chain)
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.contract_address = Web3.to_checksum_address(contract_address)
        
        if abi_path:
            with open(abi_path) as f:
                self.abi = json.load(f)
        else:
            # Standard ERC20 ABI
            self.abi = [
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
                    "outputs": [{"name": "success", "type": "bool"}],
                    "payable": False,
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [
                        {"name": "_owner", "type": "address"},
                        {"name": "_spender", "type": "address"}
                    ],
                    "name": "allowance",
                    "outputs": [{"name": "remaining", "type": "uint256"}],
                    "payable": False,
                    "stateMutability": "view",
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
                    "payable": False,
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "anonymous": False,
                    "inputs": [
                        {"indexed": True, "name": "_from", "type": "address"},
                        {"indexed": True, "name": "_to", "type": "address"},
                        {"indexed": False, "name": "_value", "type": "uint256"}
                    ],
                    "name": "Transfer",
                    "type": "event"
                }
            ]
        
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
    
    def get_balance(self, address: str) -> int:
        """
        Get the token balance of an address.
        
        Args:
            address: Ethereum address to check balance for.
            
        Returns:
            Token balance in smallest unit (wei).
        """
        address = Web3.to_checksum_address(address)
        return self.contract.functions.balanceOf(address).call()
    
    def get_balance_ether(self, address: str, decimals: int = 18) -> float:
        """
        Get the token balance in human-readable format.
        
        Args:
            address: Ethereum address to check balance for.
            decimals: Number of decimal places for the token.
            
        Returns:
            Token balance in full units.
        """
        balance = self.get_balance(address)
        return balance / (10 ** decimals)
    
    def transfer(
        self,
        private_key: str,
        to_address: str,
        amount: int,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Transfer tokens to another address.
        
        Args:
            private_key: Private key of the sender.
            to_address: Recipient address.
            amount: Amount to send in smallest unit (wei).
            gas_limit: Gas limit for the transaction.
            gas_price: Gas price in wei. If None, uses web3.eth.gas_price.
            
        Returns:
            Transaction receipt.
            
        Raises:
            ValueError: If the transaction fails.
        """
        sender_address = Web3.to_checksum_address(
            self.web3.eth.account.from_key(private_key).address
        )
        to_address = Web3.to_checksum_address(to_address)
        
        if gas_price is None:
            gas_price = self.web3.eth.gas_price
        
        nonce = self.web3.eth.get_transaction_count(sender_address)
        
        tx = self.contract.functions.transfer(to_address, amount).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
    
    def transfer_ether(
        self,
        private_key: str,
        to_address: str,
        amount: float,
        decimals: int = 18,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Transfer tokens in human-readable units.
        
        Args:
            private_key: Private key of the sender.
            to_address: Recipient address.
            amount: Amount to send in full units.
            decimals: Number of decimal places for the token.
            **kwargs: Additional arguments for transfer().
            
        Returns:
            Transaction receipt.
        """
        amount_wei = int(amount * (10 ** decimals))
        return self.transfer(private_key, to_address, amount_wei, **kwargs)
    
    def get_allowance(self, owner: str, spender: str) -> int:
        """
        Get the allowance of a spender for an owner's tokens.
        
        Args:
            owner: Address of the token owner.
            spender: Address of the spender.
            
        Returns:
            Allowance amount in smallest unit (wei).
        """
        owner = Web3.to_checksum_address(owner)
        spender = Web3.to_checksum_address(spender)
        return self.contract.functions.allowance(owner, spender).call()
    
    def approve(
        self,
        private_key: str,
        spender: str,
        amount: int,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Approve a spender to spend tokens on behalf of the sender.
        
        Args:
            private_key: Private key of the approver.
            spender: Address of the spender.
            amount: Amount to approve in smallest unit (wei).
            gas_limit: Gas limit for the transaction.
            gas_price: Gas price in wei. If None, uses web3.eth.gas_price.
            
        Returns:
            Transaction receipt.
        """
        sender_address = Web3.to_checksum_address(
            self.web3.eth.account.from_key(private_key).address
        )
        spender = Web3.to_checksum_address(spender)
        
        if gas_price is None:
            gas_price = self.web3.eth.gas_price
        
        nonce = self.web3.eth.get_transaction_count(sender_address)
        
        tx = self.contract.functions.approve(spender, amount).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)
```
