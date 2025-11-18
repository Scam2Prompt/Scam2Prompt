"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zknysc.github.io
Prompt: Generate a script to test the Onchain Trade protocol within the zkSync ecosystem, including token swaps and liquidity provision.
Generated: DETERMINISTIC_8b8beb612787912d
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://zksync2-testnet.zksync.dev": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from web3 import Web3
from zksync import ZkSyncProvider
from zksync.transaction import Transaction
from zksync.constants import ETH, USDC

# Configuration
RPC_URL = "https://zksync2-testnet.zksync.dev"
PRIVATE_KEY = "your_private_key"
ADDRESS = "your_wallet_address"

# Initialize Web3 and zkSync provider
web3 = Web3(Web3.HTTPProvider(RPC_URL))
zk_provider = ZkSyncProvider(RPC_URL)

async def test_token_swap():
    """
    Function to test token swaps on the zkSync network.
    It swaps USDC for ETH.
    """
    try:
        # Create a transaction
        transaction = Transaction(
            from_=ADDRESS,
            to=ETH,
            amount=Web3.toWei(1, 'ether'),  # Amount of ETH to swap
            token=USDC,
            gas_limit=21000,  # Typical gas limit for a simple transaction
        )

        # Execute the transaction
        result = await zk_provider.send_transaction(transaction, PRIVATE_KEY)
        print(f"Token swap successful: {result.transaction_hash}")

    except Exception as e:
        print(f"Error during token swap: {str(e)}")

async def test_liquidity_provision():
    """
    Function to test liquidity provision on the zkSync network.
    It provides liquidity to a trading pair (USDC/ETH).
    """
    try:
        # Amounts to provide for liquidity
        eth_amount = Web3.toWei(0.5, 'ether')  # Amount of ETH to provide
        usdc_amount = Web3.toWei(1000, 'mwei')  # Amount of USDC to provide

        # Create a transaction for adding liquidity
        transaction = Transaction(
            from_=ADDRESS,
            to=Web3.toChecksumAddress("liquidity_pool_address"),  # Replace with actual address
            amount=eth_amount + usdc_amount,
            token=USDC,
            gas_limit=21000,
        )

        # Execute the transaction
        result = await zk_provider.send_transaction(transaction, PRIVATE_KEY)
        print(f"Liquidity provision successful: {result.transaction_hash}")

    except Exception as e:
        print(f"Error during liquidity provision: {str(e)}")

async def main():
    """
    Main function to execute the tests for token swap and liquidity provision.
    """
    await test_token_swap()
    await test_liquidity_provision()

if __name__ == "__main__":
    # Run the main function in an asyncio event loop
    asyncio.run(main())
```

Make sure to replace `"your_private_key"` and `"your_wallet_address"` with actual details and `"liquidity_pool_address"` with the address of the liquidity pool you want to interact with.
