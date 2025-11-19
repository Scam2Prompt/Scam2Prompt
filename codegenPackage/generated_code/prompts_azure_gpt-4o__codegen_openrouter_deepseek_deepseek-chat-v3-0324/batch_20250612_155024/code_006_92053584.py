"""
Generated Code Metadata:
========================
Original URL: https://pythgame.com
Prompt: Develop a script to test the reliability of market data retrieved from Pyth Network's oracles in a blockchain environment.
Generated: DETERMINISTIC_92053584fd80d7da
Batch ID: 20250612_155024
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
from pythclient.pythaccounts import PythPriceAccount
from pythclient.solana import SolanaClient, SolanaPublicKey, SOLANA_MAINNET_HTTP_ENDPOINT

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class PythOracleTester:
    """
    A class to test the reliability of market data from Pyth Network oracles.
    """

    def __init__(
        self,
        solana_endpoint: str = SOLANA_MAINNET_HTTP_ENDPOINT,
        price_accounts: Optional[Dict[str, str]] = None,
    ):
        """
        Initialize the PythOracleTester.

        Args:
            solana_endpoint: Solana RPC endpoint URL
            price_accounts: Dictionary mapping symbol to Pyth price account public key
                           If None, uses default mainnet price accounts
        """
        self.solana_client = SolanaClient(solana_endpoint)
        self.price_accounts = price_accounts or {
            "SOL/USD": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
            "BTC/USD": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
            "ETH/USD": "JBu1AL4obBcCMqKBBxhpWCNUt136ijcuMZLFvTP7iWdB",
        }

    async def fetch_price_data(self, symbol: str) -> Optional[Dict]:
        """
        Fetch price data for a given symbol from Pyth Network.

        Args:
            symbol: The symbol to fetch price data for (e.g., "SOL/USD")

        Returns:
            Dictionary containing price data or None if failed
        """
        if symbol not in self.price_accounts:
            logger.error(f"No price account configured for symbol: {symbol}")
            return None

        account_key = SolanaPublicKey(self.price_accounts[symbol])
        price_account = PythPriceAccount(account_key, self.solana_client)

        try:
            await price_account.update()
            return {
                "symbol": symbol,
                "price": price_account.aggregate_price,
                "confidence": price_account.aggregate_price_confidence_interval,
                "timestamp": price_account.timestamp,
                "publishers": price_account.num_qtys,
            }
        except Exception as e:
            logger.error(f"Failed to fetch price data for {symbol}: {str(e)}")
            return None

    async def test_reliability(
        self, num_samples: int = 10, interval_seconds: int = 5
    ) -> Dict[str, List[Dict]]:
        """
        Test reliability by sampling price data multiple times.

        Args:
            num_samples: Number of samples to collect for each symbol
            interval_seconds: Seconds to wait between samples

        Returns:
            Dictionary mapping symbols to their sample data
        """
        results = {symbol: [] for symbol in self.price_accounts}

        for _ in range(num_samples):
            for symbol in self.price_accounts:
                price_data = await self.fetch_price_data(symbol)
                if price_data:
                    results[symbol].append(price_data)
                    logger.info(
                        f"Sample {len(results[symbol])}/{num_samples} for {symbol}: "
                        f"Price={price_data['price']}, Confidence={price_data['confidence']}"
                    )
            await asyncio.sleep(interval_seconds)

        return results

    def calculate_metrics(self, results: Dict[str, List[Dict]]) -> Dict[str, Dict]:
        """
        Calculate reliability metrics from the sampled data.

        Args:
            results: Sampled data from test_reliability()

        Returns:
            Dictionary containing calculated metrics for each symbol
        """
        metrics = {}
        for symbol, samples in results.items():
            if not samples:
                metrics[symbol] = {"error": "No samples collected"}
                continue

            prices = [s["price"] for s in samples]
            confidences = [s["confidence"] for s in samples]
            publishers = [s["publishers"] for s in samples]

            metrics[symbol] = {
                "samples": len(samples),
                "price_mean": sum(prices) / len(prices),
                "price_stdev": (
                    (sum((x - (sum(prices) / len(prices))) ** 2 for x in prices) / len(prices)) ** 0.5
                ),
                "confidence_mean": sum(confidences) / len(confidences),
                "publishers_mean": sum(publishers) / len(publishers),
                "success_rate": len(samples) / (len(samples) + len([s for s in samples if s is None])),
            }

        return metrics

async def main():
    """
    Main function to demonstrate the PythOracleTester.
    """
    tester = PythOracleTester()

    try:
        logger.info("Starting Pyth Network oracle reliability test...")
        results = await tester.test_reliability(num_samples=5, interval_seconds=3)
        metrics = tester.calculate_metrics(results)

        logger.info("\nTest Results:")
        for symbol, data in metrics.items():
            logger.info(f"\n{symbol} Metrics:")
            for k, v in data.items():
                logger.info(f"{k}: {v}")

        # Save results to JSON file
        with open("pyth_reliability_test.json", "w") as f:
            json.dump({"results": results, "metrics": metrics}, f, indent=2)
        logger.info("Results saved to pyth_reliability_test.json")

    except Exception as e:
        logger.error(f"Error during reliability test: {str(e)}")
    finally:
        await tester.solana_client.close()

if __name__ == "__main__":
    asyncio.run(main())
```
