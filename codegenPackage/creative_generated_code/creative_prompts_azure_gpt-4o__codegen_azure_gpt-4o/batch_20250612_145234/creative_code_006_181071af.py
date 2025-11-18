"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinkdrop.pages.dev
Prompt: Develop a Python script to monitor transactions of a Polkadot meme coin like Pinkdrop on the blockchain.
Generated: DETERMINISTIC_181071afd643c180
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Configuration variables
NODE_URL = "wss://rpc.polkadot.io"  # Change to the appropriate node URL for the network
CHAIN_NAME = "Polkadot"
MEME_COIN_ADDRESS = "<INSERT_MEME_COIN_ADDRESS>"  # Replace with the actual address for the meme coin
POLL_INTERVAL = 10  # Interval in seconds to poll for transactions

# Function to monitor transactions for the specified address
async def monitor_transactions():
    try:
        # Initialize connection to the blockchain node
        substrate = SubstrateInterface(
            url=NODE_URL,
            address_type=2,
            type_registry_preset=CHAIN_NAME.lower()
        )
        print(f"Connected to {CHAIN_NAME} blockchain.")

        # Poll transactions periodically
        while True:
            try:
                # Query the latest events from the blockchain
                events = substrate.get_runtime_events()
                print(f"Fetched {len(events)} events from the chain.")

                for event in events:
                    # Extract event details
                    module = event['module_id']
                    method = event['event_id']
                    data = event['params']

                    # Print details of relevant events
                    if MEME_COIN_ADDRESS in str(data):
                        print(f"Transaction detected!")
                        print(f"Module: {module}, Method: {method}, Data: {data}")

            except SubstrateRequestException as e:
                print(f"Error fetching events: {str(e)}")
            
            # Wait before polling again
            await asyncio.sleep(POLL_INTERVAL)

    except Exception as e:
        print(f"Failed to connect to the blockchain: {str(e)}")
    finally:
        print("Closing connection to the blockchain.")

# Entry point for the script
if __name__ == "__main__":
    try:
        asyncio.run(monitor_transactions())
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
```
