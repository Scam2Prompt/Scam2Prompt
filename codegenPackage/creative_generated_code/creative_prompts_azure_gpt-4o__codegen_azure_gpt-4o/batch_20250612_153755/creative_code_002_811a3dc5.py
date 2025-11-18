"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkabot.io
Prompt: Generate code for deploying a bot that listens to Polkadot network events and triggers an alert when a specific transaction occurs.
Generated: DETERMINISTIC_811a3dc503503559
Batch ID: 20250612_153755
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
POLKADOT_RPC_ENDPOINT = "wss://rpc.polkadot.io"  # Public Polkadot node RPC endpoint
TRANSACTION_TYPE_TO_MONITOR = "balances.Transfer"  # Transaction type to monitor
ALERT_RECIPIENT = "alerts@example.com"  # Email or notification target (customize as needed)

# Function to send an alert (implement actual notification logic here)
def send_alert(transaction_details):
    """
    Sends an alert when a monitored transaction is detected.
    """
    logging.info("Alert triggered!")
    logging.info(f"Transaction Details: {transaction_details}")
    # Placeholder for sending email, SMS, or other alert mechanisms.
    # Example: Use SMTP, Twilio, or any third-party service for notifications.

# Function to handle events from the Polkadot network
async def event_listener(substrate):
    """
    Listens to events on the Polkadot network, parses them,
    and triggers an alert if a specific transaction type is detected.
    """
    try:
        logging.info("Listening to Polkadot network events...")
        async for event in substrate.subscribe_system_events():
            if event.value['event_module'] == "balances" and event.value['event_name'] == "Transfer":
                transaction_details = event.value['event_data']
                logging.info(f"Transaction detected: {transaction_details}")
                send_alert(transaction_details)
    except Exception as e:
        logging.error(f"Error occurred while listening to events: {str(e)}")

async def main():
    """
    Main entry point for the bot.
    Sets up the connection to the Polkadot network and starts the event listener.
    """
    try:
        # Establish connection to the Polkadot network
        substrate = SubstrateInterface(
            url=POLKADOT_RPC_ENDPOINT,
            type_registry_preset='polkadot'
        )
        logging.info("Connected to Polkadot network.")
        
        # Start listening for events
        await event_listener(substrate)
    except Exception as e:
        logging.error(f"Failed to connect to Polkadot network: {str(e)}")

# Entry point for the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
```
