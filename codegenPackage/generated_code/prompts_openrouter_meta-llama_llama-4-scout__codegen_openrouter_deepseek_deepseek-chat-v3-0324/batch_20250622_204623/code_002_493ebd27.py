"""
Generated Code Metadata:
========================
Original URL: https://paradigm.network
Prompt: "Generate a code example for executing a multi-leg strategy using Paradigm's Streaming Order Books for trading crypto derivatives with minimal market impact."
Generated: DETERMINISTIC_493ebd271c33bc2f
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import logging
from typing import Dict, List, Optional

import aiohttp
from aiohttp import ClientSession, ClientWebSocketResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ParadigmOrderBookStreamer:
    """
    A class to stream order book data from Paradigm's API and execute multi-leg strategies.
    """
    
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str = "wss://stream.paradigm.co"
    ):
        """
        Initialize the ParadigmOrderBookStreamer.
        
        Args:
            api_key: Paradigm API key
            api_secret: Paradigm API secret
            base_url: Paradigm WebSocket base URL
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.ws: Optional[ClientWebSocketResponse] = None
        self.session: Optional[ClientSession] = None
        self.order_books: Dict[str, Dict] = {}
        self.subscribed_instruments: List[str] = []

    async def connect(self) -> None:
        """Connect to Paradigm's WebSocket API."""
        self.session = aiohttp.ClientSession()
        self.ws = await self.session.ws_connect(
            self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}:{self.api_secret}"
            }
        )
        logger.info("Connected to Paradigm WebSocket API")

    async def subscribe_to_order_books(self, instruments: List[str]) -> None:
        """
        Subscribe to order book updates for given instruments.
        
        Args:
            instruments: List of instrument IDs to subscribe to
        """
        if not self.ws:
            raise ConnectionError("WebSocket connection not established")
            
        subscription_msg = {
            "type": "subscribe",
            "channels": ["l2"],
            "instruments": instruments
        }
        await self.ws.send_str(json.dumps(subscription_msg))
        self.subscribed_instruments = instruments
        logger.info(f"Subscribed to order books for: {', '.join(instruments)}")

    async def handle_message(self, msg: str) -> None:
        """Handle incoming WebSocket messages."""
        try:
            data = json.loads(msg)
            if data.get("type") == "l2":
                self._update_order_book(data)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding message: {e}")
        except Exception as e:
            logger.error(f"Error handling message: {e}")

    def _update_order_book(self, data: Dict) -> None:
        """Update the local order book with new data."""
        instrument = data["instrument"]
        self.order_books[instrument] = {
            "bids": data["bids"],
            "asks": data["asks"],
            "timestamp": data["timestamp"]
        }

    async def stream_order_books(self) -> None:
        """Continuously stream and process order book updates."""
        if not self.ws:
            raise ConnectionError("WebSocket connection not established")
            
        async for msg in self.ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                await self.handle_message(msg.data)
            elif msg.type == aiohttp.WSMsgType.ERROR:
                logger.error(f"WebSocket error: {msg.data}")
                break
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                logger.info("WebSocket connection closed")
                break

    async def execute_multi_leg_strategy(self) -> None:
        """
        Execute a multi-leg strategy based on current order book state.
        Implements a simple arbitrage strategy between two instruments.
        """
        if len(self.subscribed_instruments) < 2:
            logger.warning("Need at least 2 subscribed instruments for multi-leg strategy")
            return
            
        instrument1, instrument2 = self.subscribed_instruments[:2]
        
        if instrument1 not in self.order_books or instrument2 not in self.order_books:
            logger.warning("Order book data not available for both instruments")
            return
            
        # Example strategy: Check for arbitrage opportunity between two instruments
        best_bid1 = self.order_books[instrument1]["bids"][0]["price"]
        best_ask2 = self.order_books[instrument2]["asks"][0]["price"]
        
        spread = best_bid1 - best_ask2
        
        if spread > 0:
            logger.info(f"Arbitrage opportunity detected: {spread}")
            # Here you would implement your order execution logic
            # with proper risk management and minimal market impact
        else:
            logger.debug("No arbitrage opportunity detected")

    async def run(self, instruments: List[str]) -> None:
        """Main execution loop."""
        try:
            await self.connect()
            await self.subscribe_to_order_books(instruments)
            
            while True:
                await self.stream_order_books()
                await self.execute_multi_leg_strategy()
                await asyncio.sleep(0.1)  # Throttle execution
                
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
        finally:
            await self.close()

    async def close(self) -> None:
        """Clean up resources."""
        if self.ws:
            await self.ws.close()
        if self.session:
            await self.session.close()
        logger.info("Connection closed")


async def main():
    # Replace with your actual API credentials
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    
    # Example instruments (replace with actual instrument IDs)
    instruments = [
        "BTC-USD-PERP",
        "ETH-USD-PERP"
    ]
    
    streamer = ParadigmOrderBookStreamer(api_key, api_secret)
    try:
        await streamer.run(instruments)
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")
    finally:
        await streamer.close()

if __name__ == "__main__":
    asyncio.run(main())
```
