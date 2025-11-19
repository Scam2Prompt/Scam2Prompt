"""
Generated Code Metadata:
========================
Original URL: https://lif3swap.pages.dev
Prompt: Design a basic architecture for a DeFi application that utilizes Lif3's ecosystem and services, including the Lif3 Wallet and cross-chain swap functionality.
Generated: DETERMINISTIC_9de5a0da2643f3e4
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DeFi Application Architecture using Lif3 Ecosystem

import json
from typing import Dict, List, Optional
from abc import ABC, abstractmethod
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_typing import ChecksumAddress

# Constants
LIF3_WALLET_CONTRACT_ADDRESS = "0x..."
LIF3_SWAP_CONTRACT_ADDRESS = "0x..."
CHAIN_IDS = {
    "ETHEREUM": 1,
    "BSC": 56,
    "POLYGON": 137,
    "AVALANCHE": 43114
}

# Exception Classes
class DeFiError(Exception):
    """Base exception for DeFi application errors"""
    pass

class WalletError(DeFiError):
    """Wallet-related exceptions"""
    pass

class SwapError(DeFiError):
    """Swap-related exceptions"""
    pass

class ChainNotSupportedError(DeFiError):
    """Chain not supported exception"""
    pass

# Abstract Base Classes
class BaseWallet(ABC):
    """Abstract base class for wallet functionality"""
    
    @abstractmethod
    def connect(self) -> bool:
        """Connect to wallet"""
        pass
    
    @abstractmethod
    def get_balance(self, token_address: str) -> float:
        """Get token balance"""
        pass
    
    @abstractmethod
    def send_transaction(self, to_address: str, amount: float, token_address: Optional[str] = None) -> str:
        """Send transaction"""
        pass

class BaseSwap(ABC):
    """Abstract base class for swap functionality"""
    
    @abstractmethod
    def get_quote(self, from_token: str, to_token: str, amount: float, chain_id: int) -> Dict:
        """Get swap quote"""
        pass
    
    @abstractmethod
    def execute_swap(self, from_token: str, to_token: str, amount: float, chain_id: int) -> str:
        """Execute swap"""
        pass

# Concrete Implementations
class Lif3Wallet(BaseWallet):
    """Concrete implementation of Lif3 Wallet"""
    
    def __init__(self, private_key: str, rpc_url: str):
        self.private_key = private_key
        self.rpc_url = rpc_url
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)
        self.connected = False
        
    def connect(self) -> bool:
        try:
            if not self.web3.is_connected():
                raise WalletError("Failed to connect to RPC")
            self.connected = True
            return True
        except Exception as e:
            raise WalletError(f"Connection error: {str(e)}")
    
    def get_balance(self, token_address: Optional[str] = None) -> float:
        if not self.connected:
            raise WalletError("Wallet not connected")
            
        try:
            if token_address:
                # ERC20 token balance
                contract = self.web3.eth.contract(
                    address=Web3.to_checksum_address(token_address),
                    abi=self._get_erc20_abi()
                )
                balance = contract.functions.balanceOf(self.account.address).call()
                decimals = contract.functions.decimals().call()
                return balance / (10 ** decimals)
            else:
                # Native token balance
                balance = self.web3.eth.get_balance(self.account.address)
                return self.web3.from_wei(balance, 'ether')
        except Exception as e:
            raise WalletError(f"Balance check failed: {str(e)}")
    
    def send_transaction(self, to_address: str, amount: float, token_address: Optional[str] = None) -> str:
        if not self.connected:
            raise WalletError("Wallet not connected")
            
        try:
            to_address = Web3.to_checksum_address(to_address)
            if token_address:
                # ERC20 token transfer
                contract = self.web3.eth.contract(
                    address=Web3.to_checksum_address(token_address),
                    abi=self._get_erc20_abi()
                )
                decimals = contract.functions.decimals().call()
                amount_wei = int(amount * (10 ** decimals))
                
                tx = contract.functions.transfer(
                    to_address,
                    amount_wei
                ).build_transaction({
                    'from': self.account.address,
                    'nonce': self.web3.eth.get_transaction_count(self.account.address),
                    'gasPrice': self.web3.eth.gas_price
                })
            else:
                # Native token transfer
                tx = {
                    'to': to_address,
                    'value': self.web3.to_wei(amount, 'ether'),
                    'from': self.account.address,
                    'nonce': self.web3.eth.get_transaction_count(self.account.address),
                    'gasPrice': self.web3.eth.gas_price
                }
            
            # Estimate gas and sign transaction
            tx['gas'] = self.web3.eth.estimate_gas(tx)
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            
            # Send transaction
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except ContractLogicError as e:
            raise WalletError(f"Contract logic error: {str(e)}")
        except Exception as e:
            raise WalletError(f"Transaction failed: {str(e)}")
    
    def _get_erc20_abi(self) -> List[Dict]:
        """Standard ERC20 ABI"""
        return [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
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
                "type": "function"
            }
        ]

class Lif3Swap(BaseSwap):
    """Concrete implementation of Lif3 Cross-Chain Swap"""
    
    def __init__(self, wallet: Lif3Wallet):
        self.wallet = wallet
        self.swap_contract = self.wallet.web3.eth.contract(
            address=Web3.to_checksum_address(LIF3_SWAP_CONTRACT_ADDRESS),
            abi=self._get_swap_abi()
        )
    
    def get_quote(self, from_token: str, to_token: str, amount: float, chain_id: int) -> Dict:
        try:
            if chain_id not in CHAIN_IDS.values():
                raise ChainNotSupportedError(f"Chain ID {chain_id} not supported")
                
            # Convert amount to wei/units
            from_token_contract = self.wallet.web3.eth.contract(
                address=Web3.to_checksum_address(from_token),
                abi=self.wallet._get_erc20_abi()
            )
            decimals = from_token_contract.functions.decimals().call()
            amount_units = int(amount * (10 ** decimals))
            
            # Get quote from swap contract
            quote = self.swap_contract.functions.getQuote(
                Web3.to_checksum_address(from_token),
                Web3.to_checksum_address(to_token),
                amount_units,
                chain_id
            ).call()
            
            return {
                "from_token": from_token,
                "to_token": to_token,
                "amount_in": amount,
                "amount_out": quote[0] / (10 ** decimals),
                "min_amount_out": quote[1] / (10 ** decimals),
                "fee": quote[2] / (10 ** decimals),
                "estimated_gas": quote[3]
            }
        except ContractLogicError as e:
            raise SwapError(f"Contract error getting quote: {str(e)}")
        except Exception as e:
            raise SwapError(f"Failed to get quote: {str(e)}")
    
    def execute_swap(self, from_token: str, to_token: str, amount: float, chain_id: int) -> str:
        try:
            if chain_id not in CHAIN_IDS.values():
                raise ChainNotSupportedError(f"Chain ID {chain_id} not supported")
                
            # Get quote first
            quote = self.get_quote(from_token, to_token, amount, chain_id)
            
            # Convert amount to wei/units
            from_token_contract = self.wallet.web3.eth.contract(
                address=Web3.to_checksum_address(from_token),
                abi=self.wallet._get_erc20_abi()
            )
            decimals = from_token_contract.functions.decimals().call()
            amount_units =
