"""
Generated Code Metadata:
========================
Original URL: https://bafybeihkqxli7rn4yzsjh3zws5jdrmorjdo3zjivditajb6tkzq73e7ona.ipfs.dweb.link
Prompt: Create a script to provide pxETH/WETH liquidity on PancakeSwap and track CAKE rewards.
Generated: DETERMINISTIC_2f5c043812fadfa4
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
from typing import Dict, Tuple, Optional

# Load environment variables
load_dotenv()

# Constants
PANCAKE_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
PANCAKE_FACTORY_ADDRESS = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"
WETH_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
CAKE_ADDRESS = "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
CAKE_REWARDS_PID = 0  # Update with correct Pool ID for pxETH/WETH

# ABIs
with open("abis/pancake_router.json") as f:
    PANCAKE_ROUTER_ABI = json.load(f)

with open("abis/pancake_factory.json") as f:
    PANCAKE_FACTORY_ABI = json.load(f)

with open("abis/erc20.json") as f:
    ERC20_ABI = json.load(f)

with open("abis/masterchef.json") as f:
    MASTERCHEF_ABI = json.load(f)

class PancakeLiquidityProvider:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(os.getenv("BSC_NODE_URL")))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.private_key = os.getenv("PRIVATE_KEY")
        self.account = self.web3.eth.account.from_key(self.private_key)
        
        self.router = self.web3.eth.contract(
            address=PANCAKE_ROUTER_ADDRESS,
            abi=PANCAKE_ROUTER_ABI
        )
        
        self.factory = self.web3.eth.contract(
            address=PANCAKE_FACTORY_ADDRESS,
            abi=PANCAKE_FACTORY_ABI
        )
        
        self.masterchef = self.web3.eth.contract(
            address=os.getenv("MASTERCHEF_ADDRESS"),
            abi=MASTERCHEF_ABI
        )
        
        self.weth = self.web3.eth.contract(
            address=WETH_ADDRESS,
            abi=ERC20_ABI
        )
        
        self.cake = self.web3.eth.contract(
            address=CAKE_ADDRESS,
            abi=ERC20_ABI
        )

    def get_token_contract(self, token_address: str):
        return self.web3.eth.contract(
            address=token_address,
            abi=ERC20_ABI
        )

    def get_token_balance(self, token_address: str, account: str) -> int:
        token = self.get_token_contract(token_address)
        return token.functions.balanceOf(account).call()

    def approve_token(self, token_address: str, spender: str, amount: int) -> bool:
        token = self.get_token_contract(token_address)
        tx = token.functions.approve(
            spender,
            amount
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.status == 1

    def add_liquidity(
        self,
        token_a: str,
        token_b: str,
        amount_a: int,
        amount_b: int,
        slippage: float = 0.5
    ) -> Tuple[bool, Optional[str]]:
        # Calculate minimum amounts with slippage
        min_amount_a = int(amount_a * (1 - slippage / 100))
        min_amount_b = int(amount_b * (1 - slippage / 100))
        
        # Approve tokens
        if not self.approve_token(token_a, PANCAKE_ROUTER_ADDRESS, amount_a):
            return False, None
        if not self.approve_token(token_b, PANCAKE_ROUTER_ADDRESS, amount_b):
            return False, None
        
        deadline = int(time.time()) + 1200  # 20 minutes from now
        
        try:
            tx = self.router.functions.addLiquidity(
                token_a,
                token_b,
                amount_a,
                amount_b,
                min_amount_a,
                min_amount_b,
                self.account.address,
                deadline
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            if receipt.status == 1:
                return True, receipt.transactionHash.hex()
            return False, None
        except Exception as e:
            print(f"Error adding liquidity: {e}")
            return False, None

    def get_lp_token_address(self, token_a: str, token_b: str) -> Optional[str]:
        try:
            return self.factory.functions.getPair(token_a, token_b).call()
        except Exception as e:
            print(f"Error getting LP token address: {e}")
            return None

    def stake_lp_tokens(self, lp_token_address: str, amount: int) -> bool:
        if not self.approve_token(lp_token_address, self.masterchef.address, amount):
            return False
        
        try:
            tx = self.masterchef.functions.deposit(
                CAKE_REWARDS_PID,
                amount
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt.status == 1
        except Exception as e:
            print(f"Error staking LP tokens: {e}")
            return False

    def get_pending_cake_rewards(self) -> int:
        try:
            return self.masterchef.functions.pendingCake(
                CAKE_REWARDS_PID,
                self.account.address
            ).call()
        except Exception as e:
            print(f"Error getting pending CAKE rewards: {e}")
            return 0

    def harvest_cake_rewards(self) -> bool:
        try:
            tx = self.masterchef.functions.deposit(
                CAKE_REWARDS_PID,
                0  # Amount 0 triggers harvest
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt.status == 1
        except Exception as e:
            print(f"Error harvesting CAKE rewards: {e}")
            return False

    def provide_liquidity_and_stake(
        self,
        pxeth_address: str,
        pxeth_amount: int,
        weth_amount: int
    ) -> Dict[str, any]:
        result = {
            "liquidity_added": False,
            "lp_token_staked": False,
            "lp_token_address": None,
            "tx_hash": None,
            "pending_rewards": 0
        }
        
        # Add liquidity
        success, tx_hash = self.add_liquidity(
            pxeth_address,
            WETH_ADDRESS,
            pxeth_amount,
            weth_amount
        )
        
        if not success:
            return result
        
        result["liquidity_added"] = True
        result["tx_hash"] = tx_hash
        
        # Get LP
