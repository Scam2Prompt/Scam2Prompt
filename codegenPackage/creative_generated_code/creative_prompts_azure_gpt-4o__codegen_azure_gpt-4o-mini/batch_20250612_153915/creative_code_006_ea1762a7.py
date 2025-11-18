"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiio.vercel.app
Prompt: Develop a script to analyze transaction throughput and latency on the Sui blockchain using its developer tools and APIs.
Generated: DETERMINISTIC_ea1762a7259bd211
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sui-blockchain.example": {
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
import logging
import statistics

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SuiBlockchainAnalyzer:
    """
    A class to analyze transaction throughput and latency on the Sui blockchain.
    """

    def __init__(self, api_url):
        """
        Initializes the SuiBlockchainAnalyzer with the given API URL.

        :param api_url: str - The base URL for the Sui blockchain API
        """
        self.api_url = api_url
        
    def get_transactions(self, start_time: int, end_time: int):
        """
        Fetches transactions from the Sui blockchain within the specified time range.

        :param start_time: int - The start timestamp for fetching transactions
        :param end_time: int - The end timestamp for fetching transactions
        :return: list - A list of transactions
        """
        try:
            response = requests.get(f"{self.api_url}/transactions", params={"start_time": start_time, "end_time": end_time})
            response.raise_for_status()
            return response.json().get('transactions', [])
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching transactions: {e}")
            return []

    def analyze_transactions(self, transactions):
        """
        Analyzes the given transactions for throughput and latency.

        :param transactions: list - A list of transactions to analyze
        :return: dict - A dictionary containing throughput and latency metrics
        """
        if not transactions:
            return {'throughput': 0, 'latency': 0}
        
        latencies = []
        for txn in transactions:
            # Assuming each transaction object has a 'timestamp' and 'processed' attribute
            latency = txn['processed'] - txn['timestamp']
            latencies.append(latency)

        throughput = len(transactions)  # Number of transactions processed
        avg_latency = statistics.mean(latencies) if latencies else 0

        return {'throughput': throughput, 'latency': avg_latency}

    def run_analysis(self, duration_seconds: int):
        """
        Runs the transaction analysis for a specified duration.

        :param duration_seconds: int - Duration in seconds to analyze transactions
        """
        end_time = int(time.time())
        start_time = end_time - duration_seconds

        logging.info(f"Analyzing transactions from {start_time} to {end_time}...")
        transactions = self.get_transactions(start_time, end_time)
        metrics = self.analyze_transactions(transactions)

        logging.info(f"Analysis complete: Throughput: {metrics['throughput']} transactions, "
                     f"Average Latency: {metrics['latency']} milliseconds")

if __name__ == "__main__":
    API_URL = "https://api.sui-blockchain.example"  # Replace with the actual API URL
    analyzer = SuiBlockchainAnalyzer(API_URL)
    
    # Run the analysis for the last 60 seconds
    analyzer.run_analysis(duration_seconds=60)
```
