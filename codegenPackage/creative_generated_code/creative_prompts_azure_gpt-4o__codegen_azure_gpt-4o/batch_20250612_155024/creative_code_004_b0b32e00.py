"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythpro.com
Prompt: Provide an example of querying Pyth price feed oracles to retrieve cryptocurrency price data.
Generated: DETERMINISTIC_b0b32e00ffbf76d6
Batch ID: 20250612_155024
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

Below is an example Python code for querying Pyth price feed oracles to retrieve cryptocurrency price data using the `pyth-client` library.

```python
import asyncio
from pythclient.pythaccounts import PythAccount
from pythclient.solana import SolanaClient

# Constants
PYTH_ENDPOINT = "https://api.mainnet-beta.solana.com"  # Solana endpoint
PYTH_PROGRAM_ID = "Fs7T5emVgdd2QCKiK7YxSGMZZ55wfR8y9B8ZHtN7nTDS"  # Mainnet Pyth program ID
PRICE_FEED_ACCOUNT = "E1KcdoD1y3QaU5nd1cykYhJrb2vtnF8aGvRS7p7vxjZ"  # Example price feed account (BTC/USD)

async def fetch_pyth_price():
    """
    Queries the Pyth price feed oracle to retrieve cryptocurrency price data.
    """
    try:
        # Initialize Solana client
        solana_client = SolanaClient(endpoint=PYTH_ENDPOINT)

        # Fetch Pyth price account data
        pyth_account = await solana_client.get_account(PYTH_PROGRAM_ID, PRICE_FEED_ACCOUNT)
        
        # Parse Pyth price data
        price_data = PythAccount.from_bytes(pyth_account.data)

        # Extract price information
        current_price = price_data.price.price  # Current price
        confidence_interval = price_data.price.confidence_interval  # Confidence interval

        # Print the result
        print(f"Price: {current_price}")
        print(f"Confidence Interval: {confidence_interval}")
    except Exception as e:
        # Handle errors
        print(f"Error fetching Pyth price data: {e}")
    finally:
        # Cleanup
        await solana_client.close()

# Run the async function
if __name__ == "__main__":
    asyncio.run(fetch_pyth_price())
```

**Note:**
- Ensure you have the `pyth-client` library installed. You can install it using `pip install pyth-client`.
- Replace `PRICE_FEED_ACCOUNT` with the appropriate price feed account for the cryptocurrency you want to query (e.g., BTC/USD or ETH/USD).
- This example assumes you're using Solana mainnet with Pyth. For other networks, adjust the endpoint and program ID accordingly.
