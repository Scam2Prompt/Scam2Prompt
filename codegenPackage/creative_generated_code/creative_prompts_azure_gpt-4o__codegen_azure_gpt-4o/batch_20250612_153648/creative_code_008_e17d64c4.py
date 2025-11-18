"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Implement a Solana-based transaction tracker that flags bots with >=25% failure rates and attributes 50% of their volume to the final score.
Generated: DETERMINISTIC_e17d64c416420f10
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import json
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import MemcmpOpts, TransactionSignatureStatus
from collections import defaultdict

# Constants
SOLANA_RPC_ENDPOINT = "https://api.mainnet-beta.solana.com"  # Solana RPC Endpoint
BOT_THRESHOLD_FAILURE_RATE = 0.25  # >= 25% failure rate
VOLUME_WEIGHT = 0.5  # Attribute 50% of volume to the final score
TRANSACTION_LOOKBACK = 1000  # Number of recent transactions to analyze
MAX_BOTS_DISPLAYED = 10  # Limit for flagged bots display

async def fetch_recent_transactions(client, limit=TRANSACTION_LOOKBACK):
    """
    Fetch recent transactions from the Solana blockchain.
    """
    try:
        result = await client.get_signatures_for_address(
            "your_address_here", limit=limit
        )
        return result["result"]
    except Exception as e:
        print(f"Error fetching transactions: {e}")
        return []

async def fetch_transaction_status(client, signature):
