"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-hop.com
Prompt: Provide an example of how to use Hop Exchange to optimize yield farming strategies by transferring assets between Ethereum rollups like Optimism and Arbitrum.
Generated: DETERMINISTIC_93494441a3c92167
Batch ID: 20250612_153655
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://optimism-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
# Import required modules
import asyncio
from web3 import Web3
from hop import HopBridge

# Constants
ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
OPTIMISM_RPC_URL = "https://optimism-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
ARBITRUM_RPC_URL = "https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your private key (keep it secure!)
FROM_CHAIN = "optimism"
TO_CHAIN = "arbitrum"
TOKEN = "USDC"  # Asset to transfer (e.g., USDC, USDT, ETH)
AMOUNT = 100  # Amount to transfer, in token units

# Initialize Web3 instances for each chain
ethereum_web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))
optimism_web3 = Web3(Web3.HTTPProvider(OPTIMISM_RPC_URL))
arbitrum_web3 = Web3(Web3.HTTPProvider(ARBITRUM_RPC_URL))

async def transfer_assets():
    """
    Transfers assets using Hop Exchange from one Ethereum rollup network to another.
    """
    try:
        # Initialize HopBridge for the specified chain and token
        hop_bridge = HopBridge(
            token=TOKEN,
            from_chain=FROM_CHAIN,
            to_chain=TO_CHAIN,
            private_key=PRIVATE_KEY
        )

        # Get the sender's wallet address
        sender_address = hop_bridge.get_wallet_address()

        # Check token balance on the source chain
        balance = await hop_bridge.get_balance()
        print(f"Sender's {TOKEN} Balance: {balance} {TOKEN}")

        if balance < AMOUNT:
            raise ValueError(f"Insufficient {TOKEN} balance to perform the transfer.")

        # Perform the transfer
        print(f"Initiating transfer of {AMOUNT} {TOKEN} from {FROM_CHAIN} to {TO_CHAIN}...")
        tx_hash = await hop_bridge.transfer(amount=AMOUNT)

        # Wait for transaction confirmation
        print(f"Transaction initiated: {tx_hash}. Waiting for confirmation...")
        receipt = await hop_bridge.wait_for_receipt(tx_hash)
        print(f"Transaction confirmed. Receipt: {receipt}")

        print(f"Successfully transferred {AMOUNT} {TOKEN} from {FROM_CHAIN} to {TO_CHAIN}.")

    except Exception as e:
        print(f"Error occurred during asset transfer: {e}")
        return

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(transfer_assets())
```

Note: This code assumes you have access to Hop's Python SDK (`hop`) and necessary blockchain RPC endpoints. Replace placeholder values (e.g., `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`) with your actual data. Ensure proper environment setup before running the script.
