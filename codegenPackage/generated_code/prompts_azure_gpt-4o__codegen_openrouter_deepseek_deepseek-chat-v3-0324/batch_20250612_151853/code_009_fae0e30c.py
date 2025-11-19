"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-feat-optimism-subgraph-venus-protocol.vercel.app
Prompt: Generate a code example for integrating the Venus Protocol with Optimism, focusing on reducing transaction costs for DeFi operations.
Generated: DETERMINISTIC_fae0e30c27c67126
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_abi import encode_abi
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
OPTIMISM_RPC_URL = os.getenv('OPTIMISM_RPC_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
VENUS_COMPTROLLER_ADDRESS = "0xfd36e2c2a6789db23113685031d7f16329158384"
VENUS_ORACLE_ADDRESS = "0x1D47D6B2d8a3f78D86A68a3714e1012A5a66eD5e"

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(OPTIMISM_RPC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check connection
if not w3.is_connected():
    raise ConnectionError("Failed to connect to Optimism network")

# Load ABI files
with open('venus_comptroller_abi.json') as f:
    comptroller_abi = json.load(f)

with open('venus_oracle_abi.json') as f:
    oracle_abi = json.load(f)

# Initialize contracts
comptroller = w3.eth.contract(address=VENUS_COMPTROLLER_ADDRESS, abi=comptroller_abi)
oracle = w3.eth.contract(address=VENUS_ORACLE_ADDRESS, abi=oracle_abi)

def get_account():
    """Get account from private key"""
    return w3.eth.account.from_key(PRIVATE_KEY)

def build_and_send_tx(contract_function, value=0, gas_limit=2000000):
    """Build and send a transaction with optimized gas"""
    account = get_account()
    nonce = w3.eth.get_transaction_count(account.address)
    
    tx = contract_function.build_transaction({
        'chainId': 10,  # Optimism chain ID
        'gas': gas_limit,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
        'value': value
    })
    
    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.eth.wait_for_transaction_receipt(tx_hash)

def enter_markets(vtoken_addresses):
    """Enter Venus markets to enable borrowing"""
    tx_receipt = build_and_send_tx(
        comptroller.functions.enterMarkets(vtoken_addresses)
    )
    return tx_receipt

def get_asset_price(asset_address):
    """Get asset price from Venus oracle"""
    return oracle.functions.getUnderlyingPrice(asset_address).call()

def borrow_asset(vtoken_address, borrow_amount):
    """Borrow asset from Venus protocol"""
    vtoken_abi = json.load(open('venus_vtoken_abi.json'))
    vtoken = w3.eth.contract(address=vtoken_address, abi=vtoken_abi)
    
    tx_receipt = build_and_send_tx(
        vtoken.functions.borrow(borrow_amount)
    )
    return tx_receipt

def repay_borrow(vtoken_address, repay_amount):
    """Repay borrowed asset"""
    vtoken_abi = json.load(open('venus_vtoken_abi.json'))
    vtoken = w3.eth.contract(address=vtoken_address, abi=vtoken_abi)
    
    tx_receipt = build_and_send_tx(
        vtoken.functions.repayBorrow(repay_amount),
        value=repay_amount if vtoken_address == "0x0000000000000000000000000000000000000000" else 0
    )
    return tx_receipt

def estimate_gas_for_operation(operation, *args):
    """Estimate gas cost for an operation"""
    account = get_account()
    return operation(*args).estimate_gas({'from': account.address})

# Example usage
if __name__ == "__main__":
    try:
        # Example vToken addresses (replace with actual addresses)
        vtoken_addresses = [
            "0x5c9476FcD6a4F9a97A7F1883FcDe3e80B5C5F4A5",  # vETH
            "0xec3422Ef92B2fb59e84c8B02Ba73F1fE84Ed8D71"   # vUSDC
        ]
        
        # Enter markets
        print("Entering markets...")
        enter_markets(vtoken_addresses)
        
        # Get asset price
        usdc_price = get_asset_price(vtoken_addresses[1])
        print(f"USDC price: {usdc_price}")
        
        # Borrow USDC
        borrow_amount = 100 * 10**6  # 100 USDC (6 decimals)
        print(f"Borrowing {borrow_amount/10**6} USDC...")
        borrow_asset(vtoken_addresses[1], borrow_amount)
        
        # Repay borrow
        print(f"Repaying {borrow_amount/10**6} USDC...")
        repay_borrow(vtoken_addresses[1], borrow_amount)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
