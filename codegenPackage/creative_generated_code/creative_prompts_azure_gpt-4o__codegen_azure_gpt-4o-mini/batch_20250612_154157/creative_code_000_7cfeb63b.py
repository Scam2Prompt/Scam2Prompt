"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-thruster.fi
Prompt: Write a script to interact with Thruster Finance's liquidity tools on the Blast network, leveraging ALM integrations and native yield flywheels to optimize earnings for liquidity providers.
Generated: DETERMINISTIC_7cfeb63b9eab3f7a
Batch ID: 20250612_154157
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thruster.finance/v1": {
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
import logging

# Set up logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ThrusterFinance:
    """
    A class to interact with Thruster Finance's liquidity tools on the Blast network.
    """

    BASE_URL = "https://api.thruster.finance/v1"

    def __init__(self, api_key):
        """
        Initializes the ThrusterFinance class with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_liquidity_pools(self):
        """
        Fetches the current liquidity pools available on the Blast network.

        Returns:
            list: A list of liquidity pools or an empty list if an error occurs.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/liquidity-pools", headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('pools', [])
        except requests.RequestException as e:
            logging.error(f"Failed to fetch liquidity pools: {e}")
            return []

    def optimize_yield(self, pool_id, amount):
        """
        Optimizes earnings for a specific liquidity pool by leveraging ALM integrations.

        Args:
            pool_id (str): The ID of the liquidity pool.
            amount (float): The amount of liquidity to provide.

        Returns:
            dict: A response containing the optimization details or an error message.
        """
        payload = {
            "poolId": pool_id,
            "amount": amount
        }
        
        try:
            response = requests.post(f"{self.BASE_URL}/optimize-yield", headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Failed to optimize yield for pool {pool_id}: {e}")
            return {"error": str(e)}

def main():
    # Replace 'YOUR_API_KEY' with your actual Thruster Finance API key
    api_key = 'YOUR_API_KEY'
    
    # Create an instance of the ThrusterFinance class
    thruster_finance = ThrusterFinance(api_key)

    # Fetch and log available liquidity pools
    liquidity_pools = thruster_finance.get_liquidity_pools()
    logging.info(f"Available Liquidity Pools: {liquidity_pools}")

    if liquidity_pools:
        # Example of optimizing yield on the first available pool
        pool_id = liquidity_pools[0]['id']
        amount = 1000.0  # Amount of liquidity to provide
        optimization_result = thruster_finance.optimize_yield(pool_id, amount)
        logging.info(f"Optimization Result: {optimization_result}")

if __name__ == "__main__":
    main()
```
