"""
Generated Code Metadata:
========================
Original URL: https://btc-tools.org
Prompt: How can I use BTC Tools to change the mining pool and worker name for multiple ASIC miners simultaneously, and what are the benefits of using this tool for miner management?
Generated: DETERMINISTIC_b1a30d6c6b2bcf06
Batch ID: 20250622_205358
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://new-pool.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.btctools.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import requests

class BTCMiner:
    def __init__(self, api_url, api_key):
        """
        Initialize the BTCMiner class.

        Args:
            api_url (str): The URL of the BTC Tools API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def update_miner_pool(self, miner_ids, pool_url, pool_username, pool_password):
        """
        Update the mining pool for multiple ASIC miners.

        Args:
            miner_ids (list): A list of miner IDs.
            pool_url (str): The URL of the new mining pool.
            pool_username (str): The username for the new mining pool.
            pool_password (str): The password for the new mining pool.

        Returns:
            dict: A dictionary containing the results of the update operation.
        """
        try:
            data = {
                'api_key': self.api_key,
                'miner_ids': miner_ids,
                'pool_url': pool_url,
                'pool_username': pool_username,
                'pool_password': pool_password
            }
            response = requests.post(f'{self.api_url}/miners/pool', json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def update_miner_worker_name(self, miner_ids, worker_name):
        """
        Update the worker name for multiple ASIC miners.

        Args:
            miner_ids (list): A list of miner IDs.
            worker_name (str): The new worker name.

        Returns:
            dict: A dictionary containing the results of the update operation.
        """
        try:
            data = {
                'api_key': self.api_key,
                'miner_ids': miner_ids,
                'worker_name': worker_name
            }
            response = requests.post(f'{self.api_url}/miners/worker_name', json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

def main():
    api_url = 'https://api.btctools.com'
    api_key = 'YOUR_API_KEY'
    miner_ids = ['miner_id_1', 'miner_id_2', 'miner_id_3']
    pool_url = 'https://new-pool.com'
    pool_username = 'new_pool_username'
    pool_password = 'new_pool_password'
    worker_name = 'new_worker_name'

    btc_miner = BTCMiner(api_url, api_key)

    # Update mining pool
    pool_update_result = btc_miner.update_miner_pool(miner_ids, pool_url, pool_username, pool_password)
    print(json.dumps(pool_update_result, indent=4))

    # Update worker name
    worker_name_update_result = btc_miner.update_miner_worker_name(miner_ids, worker_name)
    print(json.dumps(worker_name_update_result, indent=4))

if __name__ == "__main__":
    main()
```
