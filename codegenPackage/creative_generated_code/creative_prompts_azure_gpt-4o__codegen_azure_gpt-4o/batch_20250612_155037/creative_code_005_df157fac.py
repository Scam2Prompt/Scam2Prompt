"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Create a tutorial for developers on how to use Hyperlane's developer toolchain to build a cross-chain application. Include code snippets and examples of integrating Hyperlane's SDK.
Generated: DETERMINISTIC_df157facde4f86a7
Batch ID: 20250612_155037
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-rpc.com": {
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
# Hyperlane Cross-Chain Application Tutorial
# This Python script provides a simplified tutorial on how developers can use Hyperlane's SDK to build cross-chain applications.
# Ensure you have the Hyperlane SDK installed: `pip install hyperlane-sdk`

from hyperlane_sdk import HyperlaneClient, Message, Chain, Wallet
from hyperlane_sdk.exceptions import HyperlaneException

# Step 1: Set up configuration for chains and wallets
# Replace with your chain names and RPC endpoints
SOURCE_CHAIN = "ethereum"
DESTINATION_CHAIN = "polygon"

SOURCE_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
DESTINATION_RPC_URL = "https://polygon-rpc.com"

SOURCE_PRIVATE_KEY = "your_source_chain_private_key"
DESTINATION_PRIVATE_KEY = "your_destination_chain_private_key"

try:
    # Initialize clients for source and destination chains
    source_client = HyperlaneClient(Chain(SOURCE_CHAIN, SOURCE_RPC_URL))
    destination_client = HyperlaneClient(Chain(DESTINATION_CHAIN, DESTINATION_RPC_URL))
    
    # Initialize wallets for signing transactions
    source_wallet = Wallet(SOURCE_PRIVATE_KEY, SOURCE_CHAIN)
    destination_wallet = Wallet(DESTINATION_PRIVATE_KEY, DESTINATION_CHAIN)
except HyperlaneException as e:
    print(f"Error initializing Hyperlane clients or wallets: {e}")
    exit(1)

# Step 2: Create and send a cross-chain message
def send_cross_chain_message(sender_address, receiver_address, message_content):
    # Construct a message for the destination chain
    message = Message(
        sender=sender_address,
        receiver=receiver_address,
        content=message_content
    )
    
    try:
        # Send message from source chain to destination chain
        tx_hash = source_client.send_message(message, wallet=source_wallet)
        print(f"Message sent! Transaction hash: {tx_hash}")
    except HyperlaneException as e:
        print(f"Error sending message: {e}")

# Example usage
send_cross_chain_message(
    sender_address="0xSenderAddressOnSourceChain",
    receiver_address="0xReceiverAddressOnDestinationChain",
    message_content="Hello from Ethereum to Polygon!"
)

# Step 3: Listen for incoming messages on the destination chain
def listen_for_messages():
    try:
        # Start listening for new messages on the destination chain
        for message in destination_client.listen_for_messages(wallet=destination_wallet):
            print(f"Received message: {message.content}")
    except HyperlaneException as e:
        print(f"Error listening for messages: {e}")

# Example usage (can be run in its own dedicated thread or process)
# listen_for_messages()

# Step 4: Handle received messages and perform custom logic
def handle_received_message(message):
    try:
        # Implement custom logic here
        print(f"Handling received message: {message.content}")
        # For example: You might update a local database or trigger another cross-chain action
    except Exception as e:
        print(f"Error handling received message: {e}")

# Note: Properly configure the environment variables and monitor chain events in production.
```
