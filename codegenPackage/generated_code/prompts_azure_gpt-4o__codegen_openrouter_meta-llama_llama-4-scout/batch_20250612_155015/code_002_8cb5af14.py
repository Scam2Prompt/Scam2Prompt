"""
Generated Code Metadata:
========================
Original URL: https://pythcloud.com
Prompt: Generate a smart contract snippet that uses Pyth Network's market data to trigger specific actions based on price thresholds.
Generated: DETERMINISTIC_8cb5af14fddfb1cb
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from anchorpy import Program, Provider, web3
from anchorpy.borsh import BorshEncoder, BorshDecoder
from pyth_network import PythNetwork

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the program ID
PROGRAM_ID = web3.PublicKey("your_program_id")

# Define the Pyth Network configuration
PYTH_NETWORK_CONFIG = {
    "pyth_program_id": web3.PublicKey("PythNetworkProgramId"),
    "pyth_feed_ids": {
        "SOL/USD": web3.PublicKey("SOLUSD_FeedId"),
        # Add more feed IDs as needed
    },
}

class PriceTrigger:
    def __init__(self, program: Program, provider: Provider):
        self.program = program
        self.provider = provider
        self.pyth_network = PythNetwork(
            program_id=PYTH_NETWORK_CONFIG["pyth_program_id"],
            provider=provider,
        )

    async def get_price(self, feed_id: web3.PublicKey) -> float:
        """Get the current price from Pyth Network"""
        try:
            price_feed = await self.pyth_network.get_price_feed(feed_id)
            return price_feed.get_current_price().price
        except Exception as e:
            logger.error(f"Error getting price: {e}")
            raise

    async def check_threshold(self, feed_id: web3.PublicKey, threshold: float, action: str):
        """Check if the current price is above or below a threshold"""
        try:
            current_price = await self.get_price(feed_id)
            if current_price > threshold:
                logger.info(f"Price is above threshold: {current_price} > {threshold}. Triggering {action}")
                # Trigger action
            elif current_price < threshold:
                logger.info(f"Price is below threshold: {current_price} < {threshold}. Triggering {action}")
                # Trigger action
        except Exception as e:
            logger.error(f"Error checking threshold: {e}")
            raise

class PriceTriggerInstruction:
    @staticmethod
    def check_threshold(
        program: Program,
        feed_id: web3.PublicKey,
        threshold: float,
        action: str,
    ) -> web3.TransactionInstruction:
        """Create a transaction instruction to check the price threshold"""
        return program.instruction(
            "check_threshold",
            {
                "feed_id": feed_id,
                "threshold": threshold,
                "action": action,
            },
            PROGRAM_ID,
        )

async def main():
    # Set up the Anchor program and provider
    program = Program("your_program_name", PROGRAM_ID, Provider.local())
    provider = program.provider

    # Create a PriceTrigger instance
    price_trigger = PriceTrigger(program, provider)

    # Define the feed ID, threshold, and action
    feed_id = PYTH_NETWORK_CONFIG["pyth_feed_ids"]["SOL/USD"]
    threshold = 100.0
    action = "Buy"

    # Check the price threshold
    await price_trigger.check_threshold(feed_id, threshold, action)

    # Create a transaction instruction to check the price threshold
    instruction = PriceTriggerInstruction.check_threshold(
        program, feed_id, threshold, action
    )

    # Add the instruction to a transaction and execute it
    tx = web3.Transaction().add(instruction)
    await provider.send(tx)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
