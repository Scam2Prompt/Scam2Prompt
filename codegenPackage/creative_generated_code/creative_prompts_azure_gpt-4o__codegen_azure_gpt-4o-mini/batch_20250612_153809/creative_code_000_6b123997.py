"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solscanai.com
Prompt: Write a Python script that uses Solana blockchain APIs to retrieve and analyze the latest blocks, similar to the analytics provided by Solscan AI.
Generated: DETERMINISTIC_6b123997212ce3fa
Batch ID: 20250612_153809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import json
from datetime import datetime


class SolanaBlockAnalyzer:
    """
    A class to analyze the latest Solana blockchain blocks using Solana APIs.
    """

    BASE_URL = "https://api.mainnet-beta.solana.com"

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def _make_request(self, method: str, params: dict):
        """
        Makes a POST request to the Solana API.

        :param method: The endpoint method to call.
        :param params: The parameters to send with the request.
        :return: The response from the API in JSON format.
        :raises Exception: If the request fails or returns an error.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params
        }
        
        try:
            response = requests.post(self.BASE_URL, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def get_latest_block(self) -> dict:
        """
        Retrieves the latest block from the Solana blockchain.

        :return: A dictionary containing the latest block information.
        """
        params = []
        response = self._make_request("getBlockHeight", params)
        latest_block_height = response.get("result")

        # Retrieve block details using the latest block height
        block_details = self._make_request("getBlock", [latest_block_height])

        return block_details.get("result")

    def analyze_block(self, block_info: dict) -> dict:
        """
        Analyzes the block information to extract key metrics.

        :param block_info: The block information returned by the API.
        :return: A dictionary containing analyzed metrics.
        """
        block_metrics = {
            "block_height": block_info.get("blockHeight"),
            "block_time": datetime.fromtimestamp(block_info.get("blockTime")).isoformat() if block_info.get("blockTime") else None,
            "transactions_count": len(block_info.get("transactions", [])),
            "previous_block_height": block_info.get("previousBlockHeight"),
            "rewards": block_info.get("rewards", [])
        }
        return block_metrics

    def run_analysis(self):
        """
        Runs the analysis to retrieve and analyze the latest block.
        """
        try:
            latest_block = self.get_latest_block()
            if latest_block:
                analyzed_metrics = self.analyze_block(latest_block)
                print("Analyzed Block Metrics:")
                print(json.dumps(analyzed_metrics, indent=4))
            else:
                print("No block information retrieved.")
        except Exception as e:
            print("Failed to run block analysis:", e)


if __name__ == "__main__":
    # Create an instance of the SolanaBlockAnalyzer and run the analysis
    analyzer = SolanaBlockAnalyzer()
    analyzer.run_analysis()
```
