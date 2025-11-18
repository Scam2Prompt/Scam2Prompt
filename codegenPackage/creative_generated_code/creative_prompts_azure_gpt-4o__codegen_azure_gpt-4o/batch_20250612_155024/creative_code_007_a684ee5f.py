"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoststandart.ru
Prompt: Write a detailed guide in code for purchasing BELT tokens on PancakeSwap and using them for governance voting on Belt Finance proposals.
Generated: DETERMINISTIC_a684ee5fd8cdd030
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for purchasing BELT tokens on PancakeSwap and using them for governance voting on Belt Finance proposals.

Prerequisites:
1. Install web3.py and python-dotenv libraries: `pip install web3 python-dotenv`
2. Ensure you have a wallet with sufficient funds (BNB for gas fees and tokens for purchasing BELT).
3. Set up a `.env` file with your private key and RPC URL.
4. Verify the contract addresses on PancakeSwap and Belt Finance governance platform.

Note: Replace placeholder values with actual contract addresses and configurations.
"""

import os
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
import time

# Load environment variables (private key and RPC URL)
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # For Binance Smart Chain

# Ensure connection is established
if not web3.isConnected():
    raise Exception("Failed to connect to RPC URL.")

# Wallet address derived from private key
wallet_address = web3.eth.account.from_key(PRIVATE_KEY).address

# Contract addresses (replace with actual addresses)
PANCAKESWAP_ROUTER = "0x10ED43C718714eb63d5aA57B78B54704E256024E"  # PancakeSwap Router
BELT_TOKEN = "0xE0e514c71282b6f4e823703a39374Cf58dc3eA4f"  # BELT token address
BELT_GOVERNANCE = "0xGovernanceContractAddress"  # Belt Finance governance contract

# ABI files (replace with actual ABIs)
# Load or define the ABIs for PancakeSwap Router and Belt Governance contracts
PANCAKESWAP_ROUTER_ABI = [...]  # Replace with PancakeSwap Router ABI
BELT_GOVERNANCE_ABI = [...]     # Replace with Belt Finance Governance ABI
ERC20_ABI = [...]               # Standard ERC-20 ABI

# Initialize contract instances
router_contract = web3.eth.contract(address=PANCAKESWAP_ROUTER, abi=PANCAKESWAP_ROUTER_ABI)
belt_token_contract = web3.eth.contract(address=BELT_TOKEN, abi=ERC20_ABI)
governance_contract = web3.eth.contract(address=BELT_GOVERNANCE, abi=BELT_GOVERNANCE_ABI)


def get_gas_price():
    """Fetch the current gas price."""
    return web3.eth.gas_price


def check_balance(address, token_contract):
    """Check the token balance of the given address."""
    balance = token_contract.functions.balanceOf(address).call()
    decimals = token_contract.functions.decimals().call()
    return balance / (10 ** decimals)


def approve_belt_tokens(amount):
    """
    Approve BELT tokens for governance contract.
    :param amount: Amount of BELT tokens to approve (in token units).
    """
    approve_tx = belt_token_contract.functions.approve(BELT_GOVERNANCE, amount).buildTransaction({
        'from': wallet_address,
        'nonce': web3.eth.getTransactionCount(wallet_address),
        'gas': 100000,  # Estimate gas
        'gasPrice': get_gas_price()
    })
    signed_tx = web3.eth.account.sign_transaction(approve_tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Approve Transaction Sent: {tx_hash.hex()}")
    wait_for_transaction(tx_hash)


def purchase_belt_tokens(amount_in_bnb):
    """
    Purchase BELT tokens on PancakeSwap.
    :param amount_in_bnb: Amount of BNB used to purchase BELT tokens.
    """
    # Token path: BNB -> BELT
    path = [web3.toChecksumAddress(router_contract.functions.WETH().call()), BELT_TOKEN]

    # Estimate minimum amount out (optional, for slippage handling)
    amount_out_min = 0  # Adjust based on slippage settings

    # Build transaction
    tx = router_contract.functions.swapExactETHForTokens(
        amount_out_min,
        path,
        wallet_address,
        int(time.time()) + 600  # Deadline: 10 minutes from now
    ).buildTransaction({
        'from': wallet_address,
        'value': web3.toWei(amount_in_bnb, 'ether'),
        'nonce': web3.eth.getTransactionCount(wallet_address),
        'gas': 200000,  # Estimate gas
        'gasPrice': get_gas_price()
    })

    # Sign and send transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Swap Transaction Sent: {tx_hash.hex()}")
    wait_for_transaction(tx_hash)


def cast_vote(proposal_id, support):
    """
    Cast a governance vote using BELT tokens.
    :param proposal_id: The ID of the proposal to vote on.
    :param support: Boolean indicating whether to support (True) or oppose (False) the proposal.
    """
    vote_tx = governance_contract.functions.castVote(proposal_id, support).buildTransaction({
        'from': wallet_address,
        'nonce': web3.eth.getTransactionCount(wallet_address),
        'gas': 150000,  # Estimate gas
        'gasPrice': get_gas_price()
    })
    signed_tx = web3.eth.account.sign_transaction(vote_tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Vote Transaction Sent: {tx_hash.hex()}")
    wait_for_transaction(tx_hash)


def wait_for_transaction(tx_hash, timeout=300):
    """
    Wait for a transaction to be mined.
    :param tx_hash: Transaction hash.
    :param timeout: Timeout in seconds.
    """
    try:
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
        print(f"Transaction {tx_hash.hex()} confirmed in block {receipt['blockNumber']}")
    except TransactionNotFound:
        raise Exception(f"Transaction {tx_hash.hex()} not found after {timeout} seconds.")


if __name__ == "__main__":
    try:
        print("Checking wallet balance...")
        bnb_balance = web3.eth.get_balance(wallet_address)
        print(f"BNB Balance: {web3.fromWei(bnb_balance, 'ether')}")

        belt_balance = check_balance(wallet_address, belt_token_contract)
        print(f"BELT Balance: {belt_balance}")

        # Step 1: Purchase BELT tokens
        print("Purchasing BELT tokens...")
        purchase_belt_tokens(amount_in_bnb=0.1)  # Example: Spend 0.1 BNB

        # Step 2: Approve BELT tokens for governance
        print("Approving BELT tokens for governance...")
        belt_balance = check_balance(wallet_address, belt_token_contract)
        approve_belt_tokens(amount=belt_balance * (10 ** belt_token_contract.functions.decimals().call()))

        # Step 3: Cast governance vote
        print("Casting governance vote...")
        cast_vote(proposal_id=1, support=True)  # Example: Vote "Yes" on proposal 1

    except Exception as e:
        print(f"Error: {e}")
```
