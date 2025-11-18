"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluwhales.pages.dev
Prompt: Develop a benchmarking tool to compare token profiles and chain statistics, leveraging Bluwhale's strategic benchmarking features.
Generated: DETERMINISTIC_c9b85041aaeb4c7a
Batch ID: 20250612_153709
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bluwhale.io": {
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
import statistics
import logging
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BenchmarkingTool:
    def __init__(self, api_url: str):
        """
        Initialize the BenchmarkingTool with the given API URL.
        
        :param api_url: The base URL for the Bluwhale API
        """
        self.api_url = api_url

    def fetch_token_profiles(self, token_ids: List[str]) -> List[Dict[str, Any]]:
        """
        Fetch the token profiles for the given token IDs.
        
        :param token_ids: A list of token IDs to benchmark
        :return: A list of token profile data
        """
        profiles = []
        for token_id in token_ids:
            try:
                response = requests.get(f"{self.api_url}/tokens/{token_id}/profile")
                response.raise_for_status()  # Raise an error for bad responses
                profiles.append(response.json())
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to fetch profile for token ID {token_id}: {e}")
        return profiles

    def fetch_chain_statistics(self, chain_id: str) -> Dict[str, Any]:
        """
        Fetch chain statistics for a given chain ID.
        
        :param chain_id: The ID of the chain to benchmark
        :return: A dictionary containing chain statistics
        """
        try:
            response = requests.get(f"{self.api_url}/chains/{chain_id}/statistics")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch statistics for chain ID {chain_id}: {e}")
            return {}

    def benchmark(self, token_ids: List[str], chain_id: str) -> Dict[str, Any]:
        """
        Benchmark token profiles against chain statistics.
        
        :param token_ids: A list of token IDs to benchmark
        :param chain_id: The ID of the chain to benchmark against
        :return: A dictionary containing benchmarking results
        """
        results = {
            'token_profiles': self.fetch_token_profiles(token_ids),
            'chain_statistics': self.fetch_chain_statistics(chain_id)
        }
        return results

    def calculate_statistics(self, profiles: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Calculate average statistics from the token profiles.
        
        :param profiles: A list of token profiles
        :return: A dictionary with average statistics
        """
        if not profiles:
            logging.warning("No profiles provided for statistics calculation.")
            return {}

        # Extract relevant data for statistics (assuming 'value' is a field in the profile)
        values = [profile.get('value', 0) for profile in profiles]
        avg_value = statistics.mean(values) if values else 0
        max_value = max(values) if values else 0
        min_value = min(values) if values else 0

        return {
            'average_value': avg_value,
            'max_value': max_value,
            'min_value': min_value
        }

def main():
    # Example usage
    API_URL = "https://api.bluwhale.io"
    tool = BenchmarkingTool(api_url=API_URL)

    # Define token IDs and chain ID for benchmarking
    token_ids = ["token1", "token2", "token3"]
    chain_id = "chain1"

    # Start benchmarking
    start_time = time.time()
    benchmark_results = tool.benchmark(token_ids, chain_id)
    elapsed_time = time.time() - start_time

    # Calculate statistics on the token profiles
    token_statistics = tool.calculate_statistics(benchmark_results['token_profiles'])

    # Output results
    logging.info(f"Benchmarking Results: {benchmark_results}")
    logging.info(f"Token Statistics: {token_statistics}")
    logging.info(f"Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
```
