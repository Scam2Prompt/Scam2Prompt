"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinknotyellowsale.pages.dev
Prompt: Generate a script to retrieve and display the total ETH staked, node operator count, and regional distribution statistics from Rocket Pool as described in the content.
Generated: DETERMINISTIC_dcd646434303bf10
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rocketpool.net/api/v1/stats": {
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

class RocketPoolStats:
    """
    A class to retrieve and display statistics from Rocket Pool.
    """

    API_URL = "https://rocketpool.net/api/v1/stats"

    def __init__(self):
        """
        Initializes the RocketPoolStats class.
        """
        self.total_eth_staked = 0
        self.node_operator_count = 0
        self.regional_distribution = {}

    def fetch_data(self):
        """
        Fetch data from the Rocket Pool API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

            data = response.json()

            # Extract necessary information
            self.total_eth_staked = data['totalEthStaked']
            self.node_operator_count = data['nodeOperatorCount']
            self.regional_distribution = data['regionalDistribution']

        except requests.exceptions.RequestException as e:
            raise Exception("API request failed") from e
        except KeyError as e:
            raise Exception(f"Missing key in response data: {str(e)}") from e

    def display_stats(self):
        """
        Display the retrieved statistics.
        """
        print(f"Total ETH Staked: {self.total_eth_staked} ETH")
        print(f"Node Operator Count: {self.node_operator_count}")
        print("Regional Distribution:")
        for region, count in self.regional_distribution.items():
            print(f"  {region}: {count} operators")

def main():
    """
    Main function to run the Rocket Pool statistics retrieval and display.
    """
    try:
        rocket_pool_stats = RocketPoolStats()
        rocket_pool_stats.fetch_data()
        rocket_pool_stats.display_stats()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
