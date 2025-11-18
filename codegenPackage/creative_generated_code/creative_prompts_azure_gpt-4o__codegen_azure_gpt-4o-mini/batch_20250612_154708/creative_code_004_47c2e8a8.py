"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defifillama.com
Prompt: Create a script that integrates the DeFiLlama API to monitor real-time changes in TVL for a given blockchain network.
Generated: DETERMINISTIC_47c2e8a8e93594f7
Batch ID: 20250612_154708
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
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

class DeFiLlamaAPI:
    """Class to interact with DeFiLlama API to monitor TVL changes."""
    
    BASE_URL = "https://api.llama.fi"

    def __init__(self, blockchain: str):
        """
        Initialize the DeFiLlamaAPI with the specified blockchain network.

        Args:
            blockchain (str): The name of the blockchain to monitor.
        """
        self.blockchain = blockchain

    def get_tvl(self):
        """
        Fetch the current Total Value Locked (TVL) for the specified blockchain.

        Returns:
            float: Current TVL value.
        
        Raises:
            Exception: If the API call fails or the response is invalid.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/tvl/{self.blockchain}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['totalLiquidityUSD']  # Extract the TVL value
        except (requests.RequestException, KeyError) as e:
            raise Exception(f"Error fetching TVL data: {str(e)}")

def monitor_tvl(blockchain: str, interval: int = 60):
    """
    Monitor TVL for the given blockchain and print changes on a regular interval.

    Args:
        blockchain (str): The name of the blockchain to monitor.
        interval (int): Time interval (in seconds) for polling the TVL.
    """
    api = DeFiLlamaAPI(blockchain)
    last_tvl = None

    while True:
        try:
            current_tvl = api.get_tvl()
            if last_tvl is None:
                print(f"Initial TVL for {blockchain}: ${current_tvl:,.2f}")
            elif current_tvl != last_tvl:
                print(f"TVL Changed for {blockchain}: ${current_tvl:,.2f}")
            last_tvl = current_tvl
        except Exception as e:
            print(e)
        
        time.sleep(interval)

if __name__ == "__main__":
    # Example usage: Monitor the TVL for Ethereum every 60 seconds
    blockchain_name = "ethereum"
    polling_interval = 60  # in seconds
    monitor_tvl(blockchain_name, polling_interval)
```
