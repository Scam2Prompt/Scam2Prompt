"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Demonstrate how to use the Sui JSON-RPC API to monitor transactions per second (TPS) and network latency metrics.
Generated: DETERMINISTIC_4e41cbaf113f638b
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io:443": {
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
import time
import aiohttp

# Sui JSON-RPC API endpoint
SUI_RPC_URL = "https://fullnode.testnet.sui.io:443"  # Replace with the appropriate endpoint if using mainnet or a different node

# Function to fetch recent transactions from the Sui JSON-RPC API
async def fetch_recent_transactions(session):
    try:
        # JSON-RPC payload to fetch recent transactions
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "sui_getRecentTransactions",
            "params": []
        }

        # Start time for latency measurement
        start_time = time.time()

        # Send the request to the Sui node
        async with session.post(SUI_RPC_URL, json=payload) as response:
            response_data = await response.json()

        # End time for latency measurement
        end_time = time.time()

        # Calculate latency
        latency = end_time - start_time

        # Extract transaction data
        transactions = response_data.get("result", [])

        return transactions, latency
    except Exception as e:
        print(f"Error fetching recent transactions: {e}")
        return None, None

# Function to calculate transactions per second (TPS)
async def monitor_tps_and_latency():
    async with aiohttp.ClientSession() as session:
        previous_transaction_set = set()
        while True:
            # Call the function to fetch recent transactions and network latency
            transactions, latency = await fetch_recent_transactions(session)

            if transactions is not None:
                # Convert transactions to a set for faster comparison
                current_transaction_set = set(transactions)

                # Calculate new transactions since the last poll
                new_transactions = current_transaction_set - previous_transaction_set

                # Update previous transaction set
                previous_transaction_set = current_transaction_set

                # Calculate TPS
                tps = len(new_transactions)

                # Log metrics
                print(f"TPS: {tps}, Latency: {latency:.2f} seconds")

            # Wait for the next monitoring interval (1 second in this case)
            await asyncio.sleep(1)

# Entrypoint for the asynchronous program
if __name__ == "__main__":
    try:
        print("Starting TPS and latency monitoring for the Sui network...")
        asyncio.run(monitor_tps_and_latency())
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
