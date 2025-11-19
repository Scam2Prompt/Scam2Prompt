"""
Generated Code Metadata:
========================
Original URL: https://wormhole.ghost.io
Prompt: Create a code example that shows how to utilize Wormhole for messaging between different blockchain networks.
Generated: DETERMINISTIC_59187e89a9e327ce
Batch ID: 20250612_135401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from wormhole import Wormhole

# Define the source and destination blockchain networks
SOURCE_NETWORK = "Ethereum"
DESTINATION_NETWORK = "Solana"

# Define the message to be sent
MESSAGE = "Hello from Ethereum to Solana!"

async def send_message():
    """
    Sends a message from the source blockchain to the destination blockchain using Wormhole.
    """
    try:
        # Initialize the Wormhole instance for the source network
        wormhole = Wormhole(source_network=SOURCE_NETWORK)

        # Send the message
        print(f"Sending message: '{MESSAGE}' from {SOURCE_NETWORK} to {DESTINATION_NETWORK}...")
        tx_hash = await wormhole.send_message(MESSAGE, destination_network=DESTINATION_NETWORK)

        # Wait for the transaction to be confirmed
        await wormhole.wait_for_confirmation(tx_hash)
        print(f"Message sent successfully! Transaction hash: {tx_hash}")

    except Exception as e:
        # Handle any exceptions that occur during the message sending process
        print(f"An error occurred while sending the message: {e}")

async def main():
    """
    Main function to execute the send_message coroutine.
    """
    await send_message()

if __name__ == "__main__":
    # Run the main function in an asyncio event loop
    asyncio.run(main())
```

**Note:** Ensure that the `wormhole` library is installed and properly configured for the respective blockchain networks before running this code.
