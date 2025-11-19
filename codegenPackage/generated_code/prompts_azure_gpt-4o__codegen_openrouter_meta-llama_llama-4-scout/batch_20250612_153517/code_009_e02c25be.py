"""
Generated Code Metadata:
========================
Original URL: https://orca-2-git-tmoc-modify-liquidity-modals-2-orca-so.vercel.app
Prompt: Create a program to monitor liquidity changes on Orca pools and trigger notifications when specific thresholds are met.
Generated: DETERMINISTIC_e02c25bed22b398f
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
import requests
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OrcaPoolMonitor:
    def __init__(self, 
                 orca_api_url: str, 
                 pool_ids: List[str], 
                 threshold_percent: float, 
                 notification_url: str):
        """
        Initialize the Orca pool monitor.

        Args:
        - orca_api_url (str): The URL of the Orca API.
        - pool_ids (List[str]): A list of pool IDs to monitor.
        - threshold_percent (float): The percentage threshold for liquidity changes.
        - notification_url (str): The URL to send notifications to.
        """
        self.orca_api_url = orca_api_url
        self.pool_ids = pool_ids
        self.threshold_percent = threshold_percent
        self.notification_url = notification_url
        self.previous_liquidity = {}

    def get_pool_liquidity(self, pool_id: str) -> float:
        """
        Get the current liquidity of a pool.

        Args:
        - pool_id (str): The ID of the pool.

        Returns:
        - float: The current liquidity of the pool.
        """
        try:
            response = requests.get(f"{self.orca_api_url}/pools/{pool_id}")
            response.raise_for_status()
            return response.json()["liquidity"]
        except requests.RequestException as e:
            logging.error(f"Failed to get pool liquidity: {e}")
            return None

    def check_threshold(self, pool_id: str, current_liquidity: float) -> bool:
        """
        Check if the liquidity change exceeds the threshold.

        Args:
        - pool_id (str): The ID of the pool.
        - current_liquidity (float): The current liquidity of the pool.

        Returns:
        - bool: True if the threshold is exceeded, False otherwise.
        """
        if pool_id not in self.previous_liquidity:
            self.previous_liquidity[pool_id] = current_liquidity
            return False

        previous_liquidity = self.previous_liquidity[pool_id]
        self.previous_liquidity[pool_id] = current_liquidity
        change_percent = ((current_liquidity - previous_liquidity) / previous_liquidity) * 100
        return abs(change_percent) >= self.threshold_percent

    def send_notification(self, pool_id: str, liquidity: float) -> None:
        """
        Send a notification when the threshold is exceeded.

        Args:
        - pool_id (str): The ID of the pool.
        - liquidity (float): The current liquidity of the pool.
        """
        try:
            notification_data = {"pool_id": pool_id, "liquidity": liquidity}
            response = requests.post(self.notification_url, json=notification_data)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to send notification: {e}")

    def run(self) -> None:
        """
        Run the Orca pool monitor.
        """
        for pool_id in self.pool_ids:
            current_liquidity = self.get_pool_liquidity(pool_id)
            if current_liquidity is not None and self.check_threshold(pool_id, current_liquidity):
                self.send_notification(pool_id, current_liquidity)


if __name__ == "__main__":
    orca_api_url = os.environ.get("ORCA_API_URL")
    pool_ids = json.loads(os.environ.get("POOL_IDS"))
    threshold_percent = float(os.environ.get("THRESHOLD_PERCENT"))
    notification_url = os.environ.get("NOTIFICATION_URL")

    monitor = OrcaPoolMonitor(orca_api_url, pool_ids, threshold_percent, notification_url)
    while True:
        monitor.run()
        # Wait for 1 minute before checking again
        import time
        time.sleep(60)
```
