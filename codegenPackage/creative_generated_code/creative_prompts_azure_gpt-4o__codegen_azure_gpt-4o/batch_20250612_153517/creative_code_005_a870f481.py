"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Write a script to calculate the total value locked (TVL) and total DCB staked across multiple pools, similar to the metrics displayed on Decubate's staking dashboard.
Generated: DETERMINISTIC_a870f4818b95d9b5
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/staking-pools": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the Python code fulfilling your request:

```python
import requests

class PoolDataFetcher:
    """
    Class to fetch and calculate Total Value Locked (TVL) and total DCB staked across multiple pools.
    """

    def __init__(self, api_url):
        """
        Initializes the PoolDataFetcher with the API URL.
        :param api_url: URL to fetch pool data from.
        """
        self.api_url = api_url

    def fetch_pool_data(self):
        """
        Fetches staking pool data from the API.
        :return: List of pool data dictionaries if successful; raises exception otherwise.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4XX and 5XX)
            return response.json()  # Assuming the API returns a JSON object
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching pool data: {e}")

    def calculate_metrics(self, pool_data):
        """
        Calculates TVL and total DCB staked across all pools.
        :param pool_data: List of pool data dictionaries.
        :return: Dictionary containing TVL and total DCB staked.
        """
        try:
            total_value_locked = 0.0
            total_dcb_staked = 0.0

            for pool in pool_data:
                # Extract relevant fields, ensuring proper error handling for missing keys
                tvl = float(pool.get("tvl", 0.0))
                dcb_staked = float(pool.get("dcb_staked", 0.0))

                total_value_locked += tvl
                total_dcb_staked += dcb_staked

            return {
                "total_value_locked": total_value_locked,
                "total_dcb_staked": total_dcb_staked,
            }
        except Exception as e:
            raise RuntimeError(f"Error calculating metrics: {e}")


def main():
    """
    Main function to execute the TVL and DCB staking calculation workflow.
    """
    # URL of the API providing pool data (replace with actual endpoint)
    API_URL = "https://api.example.com/staking-pools"

    # Initialize the pool data fetcher
    fetcher = PoolDataFetcher(API_URL)

    try:
        # Fetch pool data
        pool_data = fetcher.fetch_pool_data()

        # Calculate metrics
        metrics = fetcher.calculate_metrics(pool_data)

        # Display the results
        print("Metrics:")
        print(f"Total Value Locked (TVL): ${metrics['total_value_locked']:.2f}")
        print(f"Total DCB Staked: {metrics['total_dcb_staked']:.2f}")
    except RuntimeError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

### Notes:
- Replace `API_URL` with the actual endpoint URL for the staking pools data.
- This script assumes the API returns an array of pool objects, each containing `tvl` and `dcb_staked` fields. If the API structure differs, you may need to adjust the parsing logic.
