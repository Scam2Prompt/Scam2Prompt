"""
Generated Code Metadata:
========================
Original URL: https://sushiswaparbitrum.github.io
Prompt: Generate an example code for a liquidity provider bot on Sushiswap Arbitrum, utilizing the Arbitrum network's faster confirmations and lower fees to optimize liquidity provision.
Generated: DETERMINISTIC_fc55e1ade6857e49
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
from eth_abi import encode_abi
from hexbytes import HexBytes
import json
import time
from typing import Dict, Tuple, Optional

# Load environment variables
load_dotenv()

# Constants
ARBITRUM_RPC_URL = os.getenv('ARBITRUM_RPC_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
SUSHI_ROUTER_ADDRESS = '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'
SUSHI_FACTORY_ADDRESS = '0xc35DADB65012eC5796536bD9864eD8773aBc74C4'
GAS_PRICE = Web3.toWei('0.1', 'gwei')
GAS_LIMIT = 500000

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(ARBITRUM_RPC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load ABI files
with open('sushi_router_abi.json') as f:
    SUSHI_ROUTER_ABI = json.load(f)

with open('erc20_abi.json') as f:
    ERC20_ABI = json.load(f)

# Initialize contracts
sushi_router = w3.eth.contract(address=SUSHI_ROUTER_ADDRESS, abi=SUSHI_ROUTER_ABI)

class LiquidityProviderBot:
    def __init__(self):
        self.account = w3.eth.account.from_key(PRIVATE_KEY)
        self.wallet_address = self.account.address
        self.nonce = w3.eth.get_transaction_count(self.wallet_address)

    def get_token_contract(self, token_address: str) -> object:
        """Return ERC20 token contract instance."""
        return w3.eth.contract(address=token_address, abi=ERC20_ABI)

    def check_allowance(self, token_address: str, spender: str) -> int:
        """Check token allowance for spender."""
        token = self.get_token_contract(token_address)
        allowance = token.functions.allowance(self.wallet_address, spender).call()
        return allowance

    def approve_token(self, token_address: str, spender: str, amount: int) -> HexBytes:
        """Approve token spending for spender."""
        token = self.get_token_contract(token_address)
        tx = token.functions.approve(spender, amount).buildTransaction({
            'from': self.wallet_address,
            'nonce': self.nonce,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE
        })
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.nonce += 1
        return tx_hash

    def add_liquidity(
        self,
        token_a: str,
        token_b: str,
        amount_a: int,
        amount_b: int,
        min_amount_a: int,
        min_amount_b: int,
        deadline: int
    ) -> HexBytes:
        """
        Add liquidity to Sushiswap pool.
        
        Args:
            token_a: Address of token A
            token_b: Address of token B
            amount_a: Amount of token A to add
            amount_b: Amount of token B to add
            min_amount_a: Minimum amount of token A to accept
            min_amount_b: Minimum amount of token B to accept
            deadline: Transaction deadline timestamp
        """
        # Check allowances and approve if needed
        if self.check_allowance(token_a, SUSHI_ROUTER_ADDRESS) < amount_a:
            self.approve_token(token_a, SUSHI_ROUTER_ADDRESS, amount_a)
        
        if self.check_allowance(token_b, SUSHI_ROUTER_ADDRESS) < amount_b:
            self.approve_token(token_b, SUSHI_ROUTER_ADDRESS, amount_b)

        # Build transaction
        tx = sushi_router.functions.addLiquidity(
            token_a,
            token_b,
            amount_a,
            amount_b,
            min_amount_a,
            min_amount_b,
            self.wallet_address,
            deadline
        ).buildTransaction({
            'from': self.wallet_address,
            'nonce': self.nonce,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE
        })

        signed_tx = self.account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.nonce += 1
        return tx_hash

    def remove_liquidity(
        self,
        token_a: str,
        token_b: str,
        liquidity: int,
        min_amount_a: int,
        min_amount_b: int,
        deadline: int
    ) -> HexBytes:
        """
        Remove liquidity from Sushiswap pool.
        
        Args:
            token_a: Address of token A
            token_b: Address of token B
            liquidity: Amount of LP tokens to remove
            min_amount_a: Minimum amount of token A to accept
            min_amount_b: Minimum amount of token B to accept
            deadline: Transaction deadline timestamp
        """
        # Get LP token address
        lp_token = sushi_router.functions.getPair(token_a, token_b).call()
        
        # Check allowance and approve if needed
        if self.check_allowance(lp_token, SUSHI_ROUTER_ADDRESS) < liquidity:
            self.approve_token(lp_token, SUSHI_ROUTER_ADDRESS, liquidity)

        # Build transaction
        tx = sushi_router.functions.removeLiquidity(
            token_a,
            token_b,
            liquidity,
            min_amount_a,
            min_amount_b,
            self.wallet_address,
            deadline
        ).buildTransaction({
            'from': self.wallet_address,
            'nonce': self.nonce,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE
        })

        signed_tx = self.account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.nonce += 1
        return tx_hash

    def get_pair_address(self, token_a: str, token_b: str) -> str:
        """Get Sushiswap pair address for token pair."""
        return sushi_router.functions.getPair(token_a, token_b).call()

    def get_lp_token_balance(self, token_a: str, token_b: str) -> int:
        """Get LP token balance for wallet."""
        lp_token = self.get_pair_address(token_a, token_b)
        token = self.get_token_contract(lp_token)
        return token.functions.balanceOf(self.wallet_address).call()

if __name__ == '__main__':
    bot = LiquidityProviderBot()
    
    # Example usage
    token_a = '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'  # USDC Arbitrum
    token_b = '0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'  # WETH Arbitrum
    
    # Add liquidity example
    amount_a = Web3.toWei(100, 'mwei')  # 100 USDC (6 decimals)
    amount_b = Web3.toWei(0.05, 'ether')  # 0.05 ETH
    
    deadline = int(time.time()) + 1200  # 20 minutes from now
    
    tx_hash = bot.add_liquidity(
        token_a,
        token_b,
        amount_a,
        amount_b,
        0,  # min_amount_a
        0,  # min_amount_b
        deadline
    )
    
    print(f"Liquidity added. Tx hash: {tx_hash.hex()}")
```
