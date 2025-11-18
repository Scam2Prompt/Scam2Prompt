"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-good.web.app
Prompt: Create a script using Solana's API to retrieve and display real-time TPS (transactions per second) and SOL/USD price data, similar to the metrics shown on the NFT-Good webpage.
Generated: DETERMINISTIC_daff23728c9d0835
Batch ID: 20250612_150601
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
import requests
import time
from solana.rpc.api import Client

# Solana RPC endpoint (use a public RPC server or your own node)
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# API URL for SOL/USD price (you can replace this with another reliable API)
SOL_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"

# Function to fetch SOL/USD price
def fetch_sol_price():
    try:
        response = requests.get(SOL_PRICE_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data.get("solana", {}).get("usd", None)
    except requests.RequestException as e:
        print(f"Error fetching SOL/USD price: {e}")
        return None

# Function to calculate TPS
def calculate_tps(solana_client, interval=10):
    """
    Calculates the transactions per second (TPS) on the Solana blockchain
    by measuring the change in transaction count over a specified interval.
    :param solana_client: Solana RPC client instance
    :param interval: Time interval in seconds to measure TPS
    :return: TPS value (float) or None on error
    """
    try:
        # Fetch the first transaction count
        start_stats = solana_client.get_recent_performance_samples(1)
        if not start_stats["result"]:
            print("Error fetching initial performance samples.")
            return None
        start_tx_count = start_stats["result"][0]["numTransactions"]

        # Wait for the interval
        time.sleep(interval)

        # Fetch the transaction count again after the interval
        end_stats = solana_client.get_recent_performance_samples(1)
        if not end_stats["result"]:
            print("Error fetching performance samples after interval.")
            return None
        end_tx_count = end_stats["result"][0]["numTransactions"]

        # Calculate TPS
        tps = (end_tx_count - start_tx_count) / interval
        return tps
    except Exception as e:
        print(f"Error calculating TPS: {e}")
        return None

# Main function to display TPS and SOL/USD price in real-time
def main():
    # Initialize Solana client
    solana_client = Client(SOLANA_RPC_URL)

    print("Fetching real-time Solana metrics. Press Ctrl+C to stop.\n")
    try:
        while True:
            # Fetch TPS
            tps = calculate_tps(solana_client)
            if tps is not None:
                print(f"TPS: {tps:.2f}", end=" | ")

            # Fetch SOL/USD price
            sol_price = fetch_sol_price()
            if sol_price is not None:
                print(f"SOL/USD: ${sol_price:.2f}")
            else:
                print("SOL/USD: N/A")

            print("-" * 50)

    except KeyboardInterrupt:
        print("\nExiting program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

This script fetches real-time TPS and SOL/USD price data using the Solana API and a public price API. Adjust the `SOLANA_RPC_URL` to use a reliable Solana RPC endpoint for production.
