"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Demonstrate how to retrieve and display transaction history for a specific wallet address in a StarkNet dApp.
Generated: DETERMINISTIC_e58a6dceda174b38
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import MAINNET
from starknet_py.net.client_errors import ClientError
from starknet_py.utils.data_transformer import parse_event
from typing import List

# Define constants
STARKNET_MAINNET_URL = MAINNET  # Mainnet URL for StarkNet

async def get_transaction_history(wallet_address: str) -> List[dict]:
    """
    Retrieves the transaction history for a specified wallet address in StarkNet.

    Args:
        wallet_address (str): The wallet address to fetch transaction history for.

    Returns:
        List[dict]: A list of transaction details as dictionaries.
    """
    # Initialize the StarkNet client for the mainnet
    client = GatewayClient(net=STARKNET_MAINNET_URL)
    
    try:
        # Fetch transactions from the StarkNet blockchain based on the wallet address
        # Note: StarkNet does not have a native 'transaction history' endpoint directly tied to wallet addresses.
        # Instead, you may need to rely on custom indexing services or event tracking. Here, we show the process
        # of retrieving events related to a specific wallet address.
        events = await client.get_events(
            address=wallet_address,
            from_block=0,  # Start fetching from the genesis block
            to_block="latest",  # Fetch up to the latest block
        )
        
        transaction_history = []
        
        # Parse each event
        for event in events.events:
            parsed_event = parse_event(event)
            transaction_history.append({
                "transaction_hash": parsed_event.transaction_hash,
                "event_name": parsed_event.name,
                "data": parsed_event.data,
                "block_number": parsed_event.block_number,
            })
        
        return transaction_history

    except ClientError as e:
        # Handle client-related errors (e.g., network or API issues)
        print(f"Error while fetching transaction history for wallet {wallet_address}: {e}")
        return []

if __name__ == "__main__":
    import asyncio

    # Replace with the actual wallet address to query
    wallet_address = "0x123456789ABCDEF"
    
    # Fetch and display transaction history
    transaction_history = asyncio.run(get_transaction_history(wallet_address))
    
    # Print the transaction history
    if transaction_history:
        print(f"Transaction history for wallet {wallet_address}:")
        for tx in transaction_history:
            print(tx)
    else:
        print(f"No transaction history found for wallet {wallet_address}.")
```
