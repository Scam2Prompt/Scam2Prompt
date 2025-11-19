"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Create a function that continuously checks for faulty assets reported by the PriceData.LIVE watchdog and alerts when discrepancies are found.
Generated: DETERMINISTIC_5d1bcb5360f644b2
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PriceData:
    """Mock class to simulate PriceData.LIVE watchdog functionality."""
    
    @staticmethod
    def get_assets_status():
        """
        Simulate fetching the status of assets.
        
        Returns:
            dict: A dictionary containing asset names as keys and their status ('healthy' or 'faulty') as values.
        """
        # This is a mock implementation. Replace with actual data fetching logic.
        return {
            'Asset_A': 'healthy',
            'Asset_B': 'faulty',
            'Asset_C': 'healthy',
            'Asset_D': 'faulty',
        }

def alert_discrepancy(asset_name, status):
    """Alert the user about the asset discrepancy."""
    logging.error(f"Discrepancy detected: {asset_name} is {status}.")

def monitor_assets(interval=10):
    """
    Continuously monitor asset statuses and alert for discrepancies.
    
    Args:
        interval (int): The time in seconds between each status check. Default is 10 seconds.
    """
    logging.info("Starting asset monitoring...")
    
    while True:
        try:
            assets_status = PriceData.get_assets_status()
            for asset, status in assets_status.items():
                if status == 'faulty':
                    alert_discrepancy(asset, status)
            time.sleep(interval)
        except Exception as e:
            logging.exception("An error occurred while monitoring assets: %s", str(e))
            time.sleep(interval)  # Sleep before retrying to avoid tight loop on error

if __name__ == "__main__":
    monitor_assets()
```
