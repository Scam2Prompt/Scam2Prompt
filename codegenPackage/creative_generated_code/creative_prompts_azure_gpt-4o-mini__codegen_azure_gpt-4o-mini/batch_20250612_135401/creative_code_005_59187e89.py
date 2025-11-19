"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.ghost.io
Prompt: Create a code example that shows how to utilize Wormhole for messaging between different blockchain networks.
Generated: DETERMINISTIC_59187e89a9e327ce
Batch ID: 20250612_135401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-relay.wormhole.com": {
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
from wormhole import Wormhole, WormholeError

async def send_message(source_chain, target_chain, message, private_key, relay):
    """
    Sends a message from one blockchain network to another using Wormhole.

    Args:
        source_chain (str): The source blockchain network.
        target_chain (str): The target blockchain network.
        message (str): The message to be sent.
        private_key (str): The private key for signing the transaction.
        relay (str): The relay service to be used.

    Returns:
        str: The transaction ID if the message is sent successfully.
    """
    try:
        # Initialize the Wormhole instance
        wormhole = Wormhole(source_chain, relay)

        # Create a transaction to send the message
        tx_id = await wormhole.send_message(target_chain, message, private_key)
        return tx_id
    except WormholeError as e:
        print(f"Wormhole error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

async def main():
    # Example parameters
    source_chain = "Ethereum"
    target_chain = "Solana"
    message = "Hello from Ethereum to Solana!"
    private_key = "0xYourPrivateKeyHere"
    relay = "https://example-relay.wormhole.com"

    # Send the message
    tx_id = await send_message(source_chain, target_chain, message, private_key, relay)
    if tx_id:
        print(f"Message sent successfully! Transaction ID: {tx_id}")
    else:
        print("Failed to send the message.")

# Entry point for the asynchronous execution
if __name__ == "__main__":
    asyncio.run(main())
```

**Note**: Ensure that you have the necessary permissions and configurations set up for the Wormhole SDK to work with the specified blockchain networks. This example assumes the existence of a hypothetical `wormhole` module that provides the required functionality; actual implementation may differ based on the available libraries.
