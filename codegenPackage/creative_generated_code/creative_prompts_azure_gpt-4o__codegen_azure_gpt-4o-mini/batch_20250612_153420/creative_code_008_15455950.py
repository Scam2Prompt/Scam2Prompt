"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collectiondapps.pages.dev
Prompt: Develop a script to monitor DeFi protocols on SearchDapps.xyz across different chains (e.g., Optimism, Polygon, Aurora) and display their TVL metrics.
Generated: DETERMINISTIC_15455950c22a6756
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchdapps.xyz/v1/protocols": {
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

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a class to monitor DeFi protocols
class DeFiProtocolMonitor:
    def __init__(self, chains):
        """
        Initialize the DeFiProtocolMonitor with a list of chains to monitor.
        
        :param chains: A list of blockchain networks to monitor (e.g., ["optimism", "polygon", "aurora"]).
        """
        self.chains = chains
        self.base_url = "https://api.searchdapps.xyz/v1/protocols"  # Base URL for the API

    def fetch_tvl_data(self, chain):
        """
        Fetch the Total Value Locked (TVL) data for a specified chain.
        
        :param chain: The blockchain network to fetch data for.
        :return: A dictionary with protocol names and their respective TVL.
        """
        try:
            response = requests.get(f"{self.base_url}/{chain}/tvl")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching TVL data for {chain}: {e}")
            return {}

    def monitor(self):
        """
        Monitor TVL across all specified chains and log the results.
        """
        while True:
            for chain in self.chains:
                tvl_data = self.fetch_tvl_data(chain)
                if tvl_data:
                    self.display_tvl(chain, tvl_data)
            time.sleep(60)  # Wait for 1 minute before the next fetch

    def display_tvl(self, chain, tvl_data):
        """
        Display the TVL data for a specific chain in a readable format.
        
        :param chain: The blockchain network for which to display TVL.
        :param tvl_data: The TVL data dictionary containing protocol names and values.
        """
        logging.info(f"TVL Data for {chain}:")
        for protocol, tvl in tvl_data.items():
            logging.info(f"  - {protocol}: ${tvl:,.2f}")  # Format TVL with thousand separators

# Entry point of the script
if __name__ == "__main__":
    # List of chains to monitor
    chains_to_monitor = ["optimism", "polygon", "aurora"]
    
    # Create an instance of the monitor and start monitoring
    monitor = DeFiProtocolMonitor(chains_to_monitor)
    monitor.monitor()
```
