"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://numerous-zettabyte-gigantic.on-fleek.app
Prompt: Create a script to monitor $BRETT token transactions on Chains and log swaps made via Jupiter AMM.
Generated: DETERMINISTIC_18cb2cb54ec44e4e
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import websockets
import json
import logging
from datetime import datetime

# Configure logging to write to a file with timestamps
logging.basicConfig(
    filename='brett_token_swaps.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Constants
CHAIN_WEBSOCKET_URL = "wss://api.chain.com/v1/ws"  # Replace with the actual websocket URL
BRETT_TOKEN_ADDRESS = "INSERT_BRETT_TOKEN_ADDRESS_HERE"  # Replace with Brett token address
JUPITER_AMM_IDENTIFIER = "JupiterAMM"  # Identifier for Jupiter AMM

async def monitor_brett_token_transactions():
    """
    Monitors BRETT token transactions via websocket and logs swaps made via Jupiter AMM.
    """
    try:
        async with websockets.connect(CHAIN_WEBSOCKET_URL) as websocket:
            # Prepare subscription message for BRETT token transactions
            subscription_message = {
                "method": "subscribe",
                "params": {
                    "address": BRETT_TOKEN_ADDRESS,
                    "events": ["transfers"]  # Assuming the chain uses 'transfers' event for token transactions
                }
            }
            await websocket.send(json.dumps(subscription_message))
            logging.info("Subscription message sent for BRETT token transactions.")

            # Listen for incoming messages
            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)

                    # Process transaction data
                    if "event" in data and data["event"] == "transfer":
                        process_transfer_event(data)
                except json.JSONDecodeError as e:
                    logging.error(f"JSON decoding error: {e}")
                except Exception as e:
                    logging.error(f"Unexpected error while processing transaction: {e}")

    except websockets.exceptions.ConnectionClosedError as e:
        logging.error(f"Websocket connection closed unexpectedly: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

def process_transfer_event(event_data):
    """
    Processes transfer events and logs swaps made via Jupiter AMM.
    """
    try:
        # Extract relevant details
        token_address = event_data.get("token_address")
        amm = event_data.get("amm")  # Assuming the AMM identifier is provided in the event data
        amount = event_data.get("amount")
        sender = event_data.get("sender")
        recipient = event_data.get("recipient")

        # Check if the transaction is a swap via Jupiter AMM
        if token_address == BRETT_TOKEN_ADDRESS and amm == JUPITER_AMM_IDENTIFIER:
            logging.info(
                f"Swap detected via Jupiter AMM: Sender={sender}, Recipient={recipient}, Amount={amount}"
            )

    except KeyError as e:
        logging.error(f"Missing expected key in event data: {e}")
    except Exception as e:
        logging.error(f"Error processing transfer event: {e}")

if __name__ == "__main__":
    # Run the websocket monitoring in an asyncio event loop
    try:
        asyncio.run(monitor_brett_token_transactions())
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred in main: {e}")
```
