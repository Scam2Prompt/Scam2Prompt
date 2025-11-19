"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.pw
Prompt: Explain how to use the Wormhole messaging service to create a custom multichain protocol.
Generated: DETERMINISTIC_0924529e43cb96dd
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the Wormhole messaging service to create a custom multichain protocol.
The Wormhole SDK enables cross-chain communication, allowing messages to be passed between different blockchain networks.
"""

import asyncio
from typing import Any

from wormhole_sdk import WormholeClient, MessagePayload, ChainID

# Configuration constants
WORMHOLE_NETWORK = "mainnet"  # Wormhole network - can be 'testnet' or 'mainnet'
SOURCE_CHAIN = ChainID.SOLANA  # Sending chain (e.g., Solana)
TARGET_CHAIN = ChainID.ETHEREUM  # Receiving chain (e.g., Ethereum)
PRIVATE_KEY = "your-private-key-here"  # Private key for signing transactions
BRIDGE_ADDRESS = "wormhole-bridge-address-here"  # Address of the Wormhole bridge contract

async def initialize_client() -> WormholeClient:
    """
    Initializes and returns a configured Wormhole client.
    """
    try:
        # Initialize the Wormhole client
        client = WormholeClient(network=WORMHOLE_NETWORK, private_key=PRIVATE_KEY)
        await client.connect()
        return client
    except Exception as e:
        print(f"Error initializing Wormhole client: {e}")
        raise

async def send_message(client: WormholeClient, payload: Any) -> str:
    """
    Sends a message from the source chain to the target chain.
    
    Args:
        client (WormholeClient): The instantiated Wormhole client.
        payload (Any): The message payload to be sent.
        
    Returns:
        str: Transaction ID of the message.
    """
    try:
        # Prepare the message payload
        message_payload = MessagePayload(data=payload)

        # Send the message using Wormhole's messaging service
        tx_id = await client.publish_message(
            source_chain=SOURCE_CHAIN,
            target_chain=TARGET_CHAIN,
            payload=message_payload,
            bridge_address=BRIDGE_ADDRESS
        )
        
        print(f"Message sent successfully. Transaction ID: {tx_id}")
        return tx_id
    except Exception as e:
        print(f"Error sending message: {e}")
        raise

async def receive_message(client: WormholeClient, tx_id: str) -> Any:
    """
    Retrieves and verifies a message from the target chain using its transaction ID.
    
    Args:
        client (WormholeClient): The instantiated Wormhole client.
        tx_id (str): The transaction ID of the sent message.
        
    Returns:
        Any: The verified message payload.
    """
    try:
        # Retrieve and verify the message
        verified_message = await client.get_verified_message(
            source_chain=SOURCE_CHAIN,
            target_chain=TARGET_CHAIN,
            transaction_id=tx_id
        )
        
        print(f"Message received and verified: {verified_message.data}")
        return verified_message.data
    except Exception as e:
        print(f"Error receiving message: {e}")
        raise

async def main():
    """
    Main function to demonstrate the Wormhole-based custom multichain protocol.
    """
    client = await initialize_client()
    try:
        # Example payload to pass between chains
        example_payload = {
            "protocol": "custom_multichain",
            "timestamp": "2023-10-01T12:00:00Z",
            "data": "Hello from Solana!"
        }
        
        # Step 1: Send message from source chain to target chain
        tx_id = await send_message(client, example_payload)
        
        # Step 2: Wait for the message to be processed (simulated with delay here)
        await asyncio.sleep(10)  # Adjust based on your chain's block time
        
        # Step 3: Receive and verify the message on the target chain
        received_payload = await receive_message(client, tx_id)
        print(f"Final received payload: {received_payload}")
    finally:
        # Ensure the client is properly disconnected
        await client.disconnect()

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())
```

**NOTE:** Replace `wormhole_sdk` and the placeholders with the actual Wormhole SDK and configuration values for your environment. Ensure you have the required dependencies installed and properly configured before running the script.
