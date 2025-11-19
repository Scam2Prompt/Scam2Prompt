"""
Generated Code Metadata:
========================
Original URL: https://defyapps.com
Prompt: Generate a code snippet that interacts with DeFi protocols to earn interest on cryptocurrency holdings as described on DefyApps.
Generated: DETERMINISTIC_8893d0f785b3b463
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready code snippet for interacting with DeFi protocols to earn interest on cryptocurrency holdings using the Web3.py library for Ethereum-based protocols:

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, Optional, Tuple

# Configuration class for DeFi protocol settings
class DeFiConfig:
    """
    Configuration for DeFi protocol interaction.
    Includes contract addresses, ABI paths, and network settings.
    """
    def __init__(
        self,
        rpc_url: str,
        lending_pool_address: str,
        lending_pool_abi_path: str,
        erc20_abi_path: str,
        chain_id: int,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ):
        self.rpc_url = rpc_url
        self.lending_pool_address = lending_pool_address
        self.lending_pool_abi_path = lending_pool_abi_path
        self.erc20_abi_path = erc20_abi_path
        self.chain_id = chain_id
        self.gas_limit = gas_limit
        self.gas_price = gas_price

class DeFiInterestEarner:
    """
    A class to interact with DeFi lending protocols to earn interest on crypto holdings.
    Currently supports AAVE-like protocols.
    """
    
    def __init__(self, config: DeFiConfig, private_key: str):
        """
        Initialize the DeFi interest earner with configuration and private key.
        
        Args:
            config: DeFiConfig object with protocol settings
            private_key: Private key for the wallet with funds to deposit
        """
        self.config = config
        self.private_key = private_key
        
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(config.rpc_url))
        
        # Add POA middleware if needed (for chains like Polygon)
        if config.chain_id in [137, 80001]:  # Polygon mainnet and testnet
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Load contract ABIs
        with open(config.lending_pool_abi_path) as f:
            self.lending_pool_abi = json.load(f)
            
        with open(config.erc20_abi_path) as f:
            self.erc20_abi = json.load(f)
        
        # Initialize contracts
        self.lending_pool = self.w3.eth.contract(
            address=config.lending_pool_address,
            abi=self.lending_pool_abi
        )
        
        # Set up the account
        self.account = self.w3.eth.account.from_key(private_key)
        self.w3.eth.default_account = self.account.address

    def _get_gas_price(self) -> int:
        """Get current gas price, using config if specified or fetching from network."""
        if self.config.gas_price:
            return self.config.gas_price
        return self.w3.eth.gas_price

    def _build_transaction(self, function_call, value: int = 0) -> Dict:
        """Build a transaction with proper gas settings."""
        return {
            'chainId': self.config.chain_id,
            'gas': self.config.gas_limit,
            'gasPrice': self._get_gas_price(),
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'value': value
        }

    def _send_transaction(self, transaction) -> str:
        """Sign and send a transaction, returning the tx hash."""
        signed_tx = self.w3.eth.account.sign_transaction(transaction, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def deposit_to_lending_pool(
        self,
        token_address: str,
        amount: float,
        as_token: bool = True
    ) -> Tuple[bool, str]:
        """
        Deposit tokens to the lending pool to start earning interest.
        
        Args:
            token_address: Address of the ERC20 token to deposit
            amount: Amount to deposit (in token units if as_token=True, in wei if False)
            as_token: Whether amount is in token units (True) or wei (False)
            
        Returns:
            Tuple of (success, transaction_hash_or_error)
        """
        try:
            token_contract = self.w3.eth.contract(address=token_address, abi=self.erc20_abi)
            
            # Convert amount to wei if needed
            amount_wei = amount if not as_token else self.w3.to_wei(amount, 'ether')
            
            # Check and approve token spending first
            allowance = token_contract.functions.allowance(
                self.account.address,
                self.config.lending_pool_address
            ).call()
            
            if allowance < amount_wei:
                approve_tx = token_contract.functions.approve(
                    self.config.lending_pool_address,
                    amount_wei
                ).build_transaction(self._build_transaction())
                
                approve_tx_hash = self._send_transaction(approve_tx)
                self.w3.eth.wait_for_transaction_receipt(approve_tx_hash)
            
            # Deposit to lending pool
            deposit_tx = self.lending_pool.functions.deposit(
                token_address,
                amount_wei,
                self.account.address,
                0  # referral code
            ).build_transaction(self._build_transaction())
            
            deposit_tx_hash = self._send_transaction(deposit_tx)
            return (True, deposit_tx_hash)
            
        except Exception as e:
            return (False, f"Error depositing to lending pool: {str(e)}")

    def withdraw_from_lending_pool(
        self,
        token_address: str,
        amount: float,
        as_token: bool = True
    ) -> Tuple[bool, str]:
        """
        Withdraw tokens from the lending pool.
        
        Args:
            token_address: Address of the ERC20 token to withdraw
            amount: Amount to withdraw (in token units if as_token=True, in wei if False)
            as_token: Whether amount is in token units (True) or wei (False)
            
        Returns:
            Tuple of (success, transaction_hash_or_error)
        """
        try:
            # Convert amount to wei if needed
            amount_wei = amount if not as_token else self.w3.to_wei(amount, 'ether')
            
            withdraw_tx = self.lending_pool.functions.withdraw(
                token_address,
                amount_wei,
                self.account.address
            ).build_transaction(self._build_transaction())
            
            withdraw_tx_hash = self._send_transaction(withdraw_tx)
            return (True, withdraw_tx_hash)
            
        except Exception as e:
            return (False, f"Error withdrawing from lending pool: {str(e)}")

    def get_deposited_balance(self, token_address: str) -> float:
        """
        Get the current deposited balance for a token in the lending pool.
        
        Args:
            token_address: Address of the ERC20 token
            
        Returns:
            Balance in token units (not wei)
        """
        try:
            balance = self.lending_pool.functions.getUserAccountData(self.account.address).call()[0]
            token_contract = self.w3.eth.contract(address=token_address, abi=self.erc20_abi)
            decimals = token_contract.functions.decimals().call()
            return balance / (10 ** decimals)
        except Exception as e:
            print(f"Error getting deposited balance: {str(e)}")
            return 0.0
```

Note: To use this code, you'll need to:
1. Install required packages: `web3`
2. Have the contract ABIs for the lending protocol and ERC20 tokens
3. Configure the DeFiConfig with appropriate network settings
4. Handle private keys securely (consider using environment variables in production)
