"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astertex.com
Prompt: Develop a program that aggregates liquidity from multiple blockchains using Aster's cross-chain liquidity aggregation feature and executes trades automatically.
Generated: DETERMINISTIC_71a1a234c6433af3
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-grade, clean, and well-documented Python code using Aster's cross-chain liquidity aggregation feature:

```python
import asyncio
import logging
from aster_sdk import AsterClient, CrossChainLiquidityAggregator, TradeExecutionException

# Set up logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration for blockchains and trading pairs
BLOCKCHAINS = ["Ethereum", "Binance Smart Chain", "Polygon", "Avalanche"]
TRADING_PAIR = ("USDT", "ETH")
MAX_RETRY_ATTEMPTS = 3

# Initialize the Aster client
ASTER_API_KEY = "your_aster_api_key_here"  # Replace with your actual API key
aster_client = AsterClient(api_key=ASTER_API_KEY)

async def aggregate_liquidity():
    """
    Aggregates liquidity from multiple blockchains using Aster's cross-chain liquidity aggregator.
    :return: Aggregated liquidity data.
    """
    try:
        aggregator = CrossChainLiquidityAggregator(aster_client)
        liquidity_data = await aggregator.aggregate(BLOCKCHAINS, TRADING_PAIR)
        logging.info(f"Aggregated liquidity data: {liquidity_data}")
        return liquidity_data
    except Exception as e:
        logging.error(f"Failed to aggregate liquidity: {e}")
        raise

async def execute_trade(liquidity_data):
    """
    Executes trade automatically using the aggregated liquidity data.
    :param liquidity_data: The aggregated liquidity data.
    """
    try:
        best_liquidity_source = max(liquidity_data, key=lambda x: x['liquidity'])
        logging.info(f"Best liquidity source: {best_liquidity_source}")

        trade_executor = aster_client.trade_executor()
        result = await trade_executor.execute_trade(
            trading_pair=TRADING_PAIR,
            source=best_liquidity_source['blockchain'],
            amount=best_liquidity_source['liquidity']
        )
        logging.info(f"Trade executed successfully: {result}")
        return result
    except TradeExecutionException as te:
        logging.error(f"Trade execution failed: {te}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during trade execution: {e}")
        raise

async def main():
    """
    Main function to aggregate liquidity and execute trades.
    Includes retry logic for handling transient errors.
    """
    retry_attempts = 0
    while retry_attempts < MAX_RETRY_ATTEMPTS:
        try:
            liquidity_data = await aggregate_liquidity()
            trade_result = await execute_trade(liquidity_data)
            logging.info(f"Final trade result: {trade_result}")
            break
        except Exception as e:
            retry_attempts += 1
            logging.warning(f"Retry attempt {retry_attempts} due to error: {e}")
            if retry_attempts >= MAX_RETRY_ATTEMPTS:
                logging.error("Max retry attempts reached. Unable to complete the trade.")
                break
            await asyncio.sleep(2)  # Wait before retrying

if __name__ == "__main__":
    # Run the main event loop
    asyncio.run(main())
```

Please replace `your_aster_api_key_here` with your actual API key for Aster's SDK. This code assumes the use of an existing Python SDK for Aster. If you do not have the SDK installed, you'll need to install it or use an equivalent library for Aster's cross-chain liquidity aggregation feature.
