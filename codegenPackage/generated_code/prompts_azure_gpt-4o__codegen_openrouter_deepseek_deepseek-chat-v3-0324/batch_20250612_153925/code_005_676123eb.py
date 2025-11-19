"""
Generated Code Metadata:
========================
Original URL: https://woobridge.net
Prompt: Develop a script to integrate WOOFi's staking features (Stake 1.0 and Stake 2.0) into a custom DeFi dashboard, including wallet connection and token management.
Generated: DETERMINISTIC_676123ebe71a4bb2
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

# Constants
WOOFI_STAKE_1_0_ABI = json.loads('''[{"inputs":[],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unstake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]''')
WOOFI_STAKE_2_0_ABI = json.loads('''[{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"unstake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]''')

WOOFI_STAKE_1_0_ADDRESS = "0xBA485b556399123261a5F9c95d413B4f93107407"
WOOFI_STAKE_2_0_ADDRESS = "0x2B99e3D67dAD973c1B9747Da742B7E26c8Bdd67B"
WOOFI_TOKEN_ADDRESS = "0xD0660cD418a64a1d44E9214ad8e459324D8157f1"

@dataclass
class StakeInfo:
    version: str
    staked_amount: float
    contract_address: str

class WOOFiStakingIntegration:
    def __init__(self, rpc_url: str):
        """
        Initialize WOOFi staking integration with blockchain RPC URL.
        
        Args:
            rpc_url: URL of the Ethereum RPC endpoint
        """
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.account = None
        self.woofi_token_contract = None
        self.stake_1_0_contract = None
        self.stake_2_0_contract = None
        
        # Initialize contracts
        try:
            self.woofi_token_contract = self.w3.eth.contract(
                address=WOOFI_TOKEN_ADDRESS,
                abi=WOOFI_STAKE_1_0_ABI  # Using same ABI for simplicity
            )
            self.stake_1_0_contract = self.w3.eth.contract(
                address=WOOFI_STAKE_1_0_ADDRESS,
                abi=WOOFI_STAKE_1_0_ABI
            )
            self.stake_2_0_contract = self.w3.eth.contract(
                address=WOOFI_STAKE_2_0_ADDRESS,
                abi=WOOFI_STAKE_2_0_ABI
            )
        except Exception as e:
            raise Exception(f"Failed to initialize contracts: {str(e)}")

    def connect_wallet(self, private_key: str) -> None:
        """
        Connect wallet using private key.
        
        Args:
            private_key: Private key of the wallet
        """
        try:
            self.account = Account.from_key(private_key)
        except Exception as e:
            raise Exception(f"Invalid private key: {str(e)}")

    def get_token_balance(self) -> float:
        """
        Get WOOFi token balance of connected wallet.
        
        Returns:
            float: Token balance in human-readable format
        """
        if not self.account:
            raise Exception("Wallet not connected")
        
        try:
            balance = self.woofi_token_contract.functions.balanceOf(
                self.account.address
            ).call()
            return self.w3.from_wei(balance, 'ether')
        except Exception as e:
            raise Exception(f"Failed to get token balance: {str(e)}")

    def get_staking_info(self) -> List[StakeInfo]:
        """
        Get staking information from both Stake 1.0 and Stake 2.0 contracts.
        
        Returns:
            List[StakeInfo]: List of staking information objects
        """
        if not self.account:
            raise Exception("Wallet not connected")
        
        stake_info = []
        try:
            # Stake 1.0
            balance_1_0 = self.stake_1_0_contract.functions.balanceOf(
                self.account.address
            ).call()
            stake_info.append(StakeInfo(
                version="1.0",
                staked_amount=self.w3.from_wei(balance_1_0, 'ether'),
                contract_address=WOOFI_STAKE_1_0_ADDRESS
            ))
            
            # Stake 2.0
            balance_2_0 = self.stake_2_0_contract.functions.balanceOf(
                self.account.address
            ).call()
            stake_info.append(StakeInfo(
                version="2.0",
                staked_amount=self.w3.from_wei(balance_2_0, 'ether'),
                contract_address=WOOFI_STAKE_2_0_ADDRESS
            ))
            
            return stake_info
        except Exception as e:
            raise Exception(f"Failed to get staking info: {str(e)}")

    def stake(self, version: str, amount: float) -> str:
        """
        Stake WOOFi tokens to specified version.
        
        Args:
            version: "1.0" or "2.0"
            amount: Amount to stake in WOOFi tokens
            
        Returns:
            str: Transaction hash
        """
        if not self.account:
            raise Exception("Wallet not connected")
        
        if version not in ["1.0", "2.0"]:
            raise Exception("Invalid staking version")
        
        try:
            amount_wei = self.w3.to_wei(amount, 'ether')
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            
            if version == "1.0":
                tx = self.stake_1_0_contract.functions.stake().build_transaction({
                    'from': self.account.address,
                    'nonce': nonce,
                    'gas': 200000,
                    'gasPrice': self.w3.eth.gas_price
                })
            else:
                tx = self.stake_2_0_contract.functions.stake(amount_wei).build_transaction({
                    'from': self.account.address,
                    'nonce': nonce,
                    'gas': 200000,
                    'gasPrice': self.w3.eth.gas_price
                })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.account.key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Staking failed: {str(e)}")

    def unstake(self, version: str, amount: Optional[float] = None) -> str:
        """
        Unstake WOOFi tokens from specified version.
        
        Args:
            version: "1.0" or "2.0"
            amount: Amount to unstake (required for 2.0)
            
        Returns:
            str: Transaction hash
        """
        if not self.account:
            raise Exception("Wallet not connected")
        
        if version not in ["1.0", "2.0"]:
            raise Exception("Invalid staking version")
        
        if version == "2.0" and amount is None:
            raise Exception("Amount is required for Stake 2.0")
        
        try:
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            
            if version == "1.0":
                tx = self.stake_1_0_contract.functions.unstake().build_transaction({
                    'from': self.account.address,
                    'nonce': nonce,
                    'gas': 200000,
                    'gasPrice': self.w3.eth.gas_price
                })
            else:
                amount_wei = self.w3.to_wei(amount, 'ether')
                tx = self.stake_2_0_contract.functions.unstake(amount_wei).build_transaction({
                    'from': self.account.address,
                    'nonce': nonce,
                    'gas': 200000,
                    'gasPrice': self.w3.eth.gas
