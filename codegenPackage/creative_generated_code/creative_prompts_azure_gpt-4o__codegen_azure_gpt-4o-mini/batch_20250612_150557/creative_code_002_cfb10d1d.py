"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solak.web.app
Prompt: Create a program that interacts with the Solana network to display the current TPS (transactions per second) and SOL/USD price, as shown on the NFT Solak site.
Generated: DETERMINISTIC_cfb10d1d0a1f0c58
Batch ID: 20250612_150557
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/simple/price": {
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
import requests
import time

class SolanaMetrics:
    def __init__(self):
        """Initialize the SolanaMetrics class."""
        self.solana_api_url = "https://api.mainnet-beta.solana.com"
        self.coingecko_api_url = "https://api.coingecko.com/api/v3/simple/price"
        self.tps = None
        self.sol_price = None

    def get_tps(self):
        """Fetch the current transactions per second (TPS) from Solana."""
        try:
            # RPC call to get the recent block and its transactions
            response = requests.post(self.solana_api_url, json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getRecentBlockhash"
            })
            response.raise_for_status()

            blockhash = response.json().get('result', {}).get('value', {}).get('blockhash')
            if blockhash:
                # Get confirmed block and its transaction count
                response = requests.post(self.solana_api_url, json={
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "getConfirmedBlock",
                    "params": [blockhash]
                })
                response.raise_for_status()

                transactions = response.json().get('result', {}).get('transactions', [])
                self.tps = len(transactions)
                return self.tps
            else:
                raise Exception("Failed to retrieve blockhash.")
        
        except Exception as e:
            print(f"Error fetching TPS: {e}")
            return None

    def get_sol_price(self):
        """Fetch the current SOL/USD price from CoinGecko."""
        try:
            response = requests.get(self.coingecko_api_url, params={
                "ids": "solana",
                "vs_currencies": "usd"
            })
            response.raise_for_status()

            self.sol_price = response.json().get('solana', {}).get('usd')
            return self.sol_price
        
        except Exception as e:
            print(f"Error fetching SOL price: {e}")
            return None

    def display_metrics(self):
        """Display the current TPS and SOL/USD price."""
        while True:
            tps = self.get_tps()
            sol_price = self.get_sol_price()

            if tps is not None and sol_price is not None:
                print(f"Current TPS: {tps} | SOL/USD Price: ${sol_price:.2f}")
            else:
                print("Failed to retrieve metrics. Please check the logs.")

            # Wait for 10 seconds before the next update
            time.sleep(10)

if __name__ == "__main__":
    metrics = SolanaMetrics()
    metrics.display_metrics()
```

This code includes a class `SolanaMetrics` that fetches the current TPS from the Solana network and the SOL/USD price from CoinGecko, displaying them in a loop. Proper error handling is implemented to ensure that any issues during the retrieval process are logged appropriately.
