"""
Generated Code Metadata:
========================
Original URL: https://xyzwthelly.com
Prompt: "How can I use Valantis's stHYPE AMM to earn yield on swap fees, staking yield, and lending on Hyperlend?"
Generated: DETERMINISTIC_382002266c5b8e88
Batch ID: 20250622_212817
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
from typing import Dict, Optional, Tuple
from eth_abi import encode_abi
from eth_utils import to_checksum_address

# Configuration
STHYPE_AMM_ADDRESS = "0x..."  # Replace with actual stHYPE AMM contract address
HYPERLEND_ADDRESS = "0x..."   # Replace with actual Hyperlend contract address
ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
STHYPE_AMM_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lpToken","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]')
HYPERLEND_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

class YieldStrategy:
    def __init__(self, web3: Web3, private_key: str):
        self.web3 = web3
        self.account = web3.eth.account.from_key(private_key)
        self.sthype_amm = web3.eth.contract(address=STHYPE_AMM_ADDRESS, abi=STHYPE_AMM_ABI)
        self.hyperlend = web3.eth.contract(address=HYPERLEND_ADDRESS, abi=HYPERLEND_ABI)
        
    def _get_token_decimals(self, token_address: str) -> int:
        token_contract = self.web3.eth.contract(
            address=to_checksum_address(token_address),
            abi=ERC20_ABI
        )
        return token_contract.functions.decimals().call()
    
    def _approve_token(self, token_address: str, spender: str, amount: int) -> bool:
        token_contract = self.web3.eth.contract(
            address=to_checksum_address(token_address),
            abi=ERC20_ABI
        )
        tx = token_contract.functions.approve(
            to_checksum_address(spender),
            amount
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 200000,
            'gasPrice': self.web3.eth.gas_price
        })
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.status == 1
    
    def add_liquidity(
        self,
        token_a: str,
        token_b: str,
        amount_a: int,
        amount_b: int,
        slippage: float = 0.01,
        deadline: int = 20 * 60  # 20 minutes
    ) -> Tuple[int, int, int]:
        # Approve tokens first
        if not self._approve_token(token_a, STHYPE_AMM_ADDRESS, amount_a):
            raise Exception(f"Failed to approve token {token_a}")
        if not self._approve_token(token_b, STHYPE_AMM_ADDRESS, amount_b):
            raise Exception(f"Failed to approve token {token_b}")
        
        # Calculate min amounts with slippage
        amount_a_min = int(amount_a * (1 - slippage))
        amount_b_min = int(amount_b * (1 - slippage))
        
        # Add liquidity
        tx = self.sthype_amm.functions.addLiquidity(
            to_checksum_address(token_a),
            to_checksum_address(token_b),
            amount_a,
            amount_b,
            amount_a_min,
            amount_b_min,
            self.account.address,
            self.web3.eth.get_block('latest')['timestamp'] + deadline
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 500000,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status != 1:
            raise Exception("Failed to add liquidity")
            
        # Parse logs to get actual amounts and liquidity
        logs = self.sthype_amm.events.LiquidityAdded().process_receipt(receipt)
        if not logs:
            raise Exception("No liquidity added event found")
            
        return (
            logs[0]['args']['amountA'],
            logs[0]['args']['amountB'],
            logs[0]['args']['liquidity']
        )
    
    def stake_lp_tokens(self, lp_token: str, amount: int) -> bool:
        if not self._approve_token(lp_token, HYPERLEND_ADDRESS, amount):
            raise Exception(f"Failed to approve LP token {lp_token}")
            
        tx = self.hyperlend.functions.deposit(
            to_checksum_address(lp_token),
            amount
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 300000,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        return receipt.status == 1
    
    def remove_liquidity(
        self,
        lp_token: str,
        liquidity: int,
        amount_token_min: int,
        amount_eth_min: int,
        deadline: int = 20 * 60
    ) -> Tuple[int, int]:
        tx = self.sthype_amm.functions.removeLiquidity(
            to_checksum_address(lp_token),
            liquidity,
            amount_token_min,
            amount_eth_min,
            self.account.address,
            self.web3.eth.get_block('latest')['timestamp'] + deadline
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 500000,
            'gasPrice': self.web3.eth.g
