"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-money.pages.dev
Prompt: Write a program to monitor and log changes in borrow rates for all available assets on DeFi.money in real-time.
Generated: DETERMINISTIC_6a7efd48e9c9b668
Batch ID: 20250612_151347
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

# Configure logging to log borrow rate changes to a file
logging.basicConfig(
    filename='borrow_rate_changes.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# URL of the WebSocket endpoint for DeFi.money
WEBSOCKET_URL = "wss://api.defi.money/borrow-rates"

async def monitor_borrow_rates():
    """
    Connects to the DeFi.money WebSocket API and monitors borrow rate changes.
    Logs changes in borrow rates to a file.
    """
    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:
            logging.info("Connected to DeFi.money WebSocket API.")
            
            while True:
                try:
                    # Receive borrow rate data from WebSocket
                    response = await websocket.recv()
                    
                    # Parse the received JSON message
                    data = json.loads(response)
                    
                    # Check if the message contains borrow rate updates
                    if "assets" in data:
                        for asset in data["assets"]:
                            asset_name = asset.get("name", "Unknown Asset")
                            borrow_rate = asset.get("borrow_rate", "Unknown Rate")
                            
                            # Log the borrow rate change
                            logging.info(
                                f"Asset: {asset_name}, Borrow Rate: {borrow_rate}"
                            )
                except json.JSONDecodeError:
                    logging.error("Failed to decode JSON message.")
                except Exception as e:
                    logging.error(f"Error processing WebSocket message: {e}")
    except Exception as e:
        logging.error(f"Failed to connect to WebSocket API: {e}")

if __name__ == "__main__":
    # Run the monitor function until manually stopped
    logging.info("Starting borrow rate monitoring...")
    asyncio.run(monitor_borrow_rates())
```
