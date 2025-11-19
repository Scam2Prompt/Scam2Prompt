"""
Generated Code Metadata:
========================
Original URL: https://app-cndl.net
Prompt: Generate code to interact with the $CNDL token on Uniswap, including fetching token details and performing a trade using the Candle Algorithm.
Generated: DETERMINISTIC_d5ebbfb7d8c050ac
Batch ID: 20250612_153809
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
from eth_abi import encode_abi
from eth_utils import to_checksum_address
from dotenv import load_dotenv
import json
import time

# Load environment variables
load_dotenv()

# Constants
CNDL_TOKEN_ADDRESS = "0xBC12aD556581ff7162E595E5956F5F3845FDB38c"  # Example address, replace with actual
UNISWAP_V2_ROUTER_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
UNISWAP_V2_FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
WETH_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

# ABI definitions
UNISWAP_V2_ROUTER_ABI = json.loads('''
[
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"}
        ],
        "name": "swapExactTokensForTokens",
        "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "WETH",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "pure",
        "type": "function"
    }
]
''')

ERC20_ABI = json.loads('''
[
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
''')

class UniswapCNDLTrader:
    def __init__(self):
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(os.getenv("INFURA_URL")))
        if not self.w3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum node")
        
        # Add POA middleware if needed (for networks like Rinkeby)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Set up accounts
        self.private_key = os.getenv("PRIVATE_KEY")
        self.account = self.w3.eth.account.from_key(self.private_key)
        
        # Initialize contracts
        self.router = self.w3.eth.contract(
            address=to_checksum_address(UNISWAP_V2_ROUTER_ADDRESS),
            abi=UNISWAP_V2_ROUTER_ABI
        )
        self.cndl_token = self.w3.eth.contract(
            address=to_checksum_address(CNDL_TOKEN_ADDRESS),
            abi=ERC20_ABI
        )
        self.weth_token = self.w3.eth.contract(
            address=to_checksum_address(WETH_ADDRESS),
            abi=ERC20_ABI
        )
    
    def get_token_details(self, token_address):
        """Fetch token details (name, symbol, decimals)"""
        token = self.w3.eth.contract(
            address=to_checksum_address(token_address),
            abi=ERC20_ABI
        )
        try:
            name = token.functions.name().call()
            symbol = token.functions.symbol().call()
            decimals = token.functions.decimals().call()
            return {
                "name": name,
                "symbol": symbol,
                "decimals": decimals
            }
        except Exception as e:
            raise Exception(f"Error fetching token details: {str(e)}")
    
    def get_token_balance(self, token_address, wallet_address=None):
        """Get token balance for a wallet"""
        if wallet_address is None:
            wallet_address = self.account.address
        
        token = self.w3.eth.contract(
            address=to_checksum_address(token_address),
            abi=ERC20_ABI
        )
        try:
            balance = token.functions.balanceOf(to_checksum_address(wallet_address)).call()
            decimals = token.functions.decimals().call()
            return balance / (10 ** decimals)
        except Exception as e:
            raise Exception(f"Error fetching token balance: {str(e)}")
    
    def approve_token_spend(self, token_address, spender_address, amount_in_wei):
        """Approve token spending for a contract"""
        token = self.w3.eth.contract(
            address=to_checksum_address(token_address),
            abi=ERC20_ABI
        )
        try:
            tx = token.functions.approve(
                to_checksum_address(spender_address),
                amount_in_wei
            ).buildTransaction({
                'chainId': 1,  # Mainnet
                'gas': 200000,
                'gasPrice': self.w3.toWei('50', 'gwei'),
                'nonce': self.w3.eth.getTransactionCount(self.account.address),
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Error approving token spend: {str(e)}")
    
    def candle_algorithm_swap(self, amount_in, slippage=0.5, is_buy=True):
        """
        Perform a swap using candle algorithm (simplified version)
        amount_in: amount to swap in ETH (for buy) or CNDL (for sell)
        slippage: acceptable slippage percentage
        is_buy: True to buy CNDL, False to sell CNDL
        """
        try:
            # Get current block timestamp for deadline
            deadline = int(time.time()) + 1200  # 20 minutes from now
            
            if is_buy:
                # Buy CNDL with ETH
                path = [WETH_ADDRESS, CNDL_TOKEN_ADDRESS]
                amount_in_wei = self.w3.toWei(amount_in, 'ether')
                amount_out_min = int(amount_in_wei * (1 - slippage / 100))
                
                # Build transaction
                tx = self.router.functions.swapExactETHForTokens(
                    amount_out_min,
                    path,
                    self.account.address,
                    deadline
                ).buildTransaction({
                    'value': amount_in_wei,
                    'chainId': 1,  # Mainnet
                    'gas': 250000,
                    'gasPrice': self.w3.toWei('50', 'gwei'),
                    'nonce': self.w3.eth.getTransactionCount(self.account.address),
                })
            else:
                # Sell CNDL for ETH
                path = [CNDL_TOKEN
