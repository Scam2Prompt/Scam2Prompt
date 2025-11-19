"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapps-claimsassets-7b6.pages.dev
Prompt: Describe how to implement real-time signed asset prices using an oracle architecture for a leveraged trading application.
Generated: DETERMINISTIC_b9ecf2d217c83fbf
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Oracle:
    def __init__(self, asset_name: str, update_interval: int):
        """
        Initialize the Oracle with an asset name and update interval.
        
        :param asset_name: The name of the asset for which prices are fetched.
        :param update_interval: Time in seconds between price updates.
        """
        self.asset_name = asset_name
        self.update_interval = update_interval
        self.current_price = None
        self.is_running = False
        self.lock = threading.Lock()

    def start(self):
        """Start fetching real-time prices in a separate thread."""
        self.is_running = True
        threading.Thread(target=self._fetch_prices).start()

    def stop(self):
        """Stop fetching prices."""
        self.is_running = False

    def _fetch_prices(self):
        """Private method to fetch and update prices at defined intervals."""
        while self.is_running:
            try:
                # Simulate fetching price from an external API
                new_price = self._get_price_from_api()
                
                with self.lock:
                    self.current_price = new_price
                
                logging.info(f"Updated price for {self.asset_name}: {self.current_price}")

                # Wait for the next update interval
                time.sleep(self.update_interval)
            except Exception as e:
                logging.error(f"Error fetching price: {e}")

    def _get_price_from_api(self) -> float:
        """
        Simulate getting the price from an external price oracle API.
        
        :return: Randomly generated price for demonstration purposes.
        """
        # Replace this logic with actual API calls in production
        return round(random.uniform(100.0, 200.0), 2)

    def get_current_price(self) -> float:
        """
        Get the current price in a thread-safe manner.
        
        :return: The latest price or None if not fetched.
        """
        with self.lock:
            return self.current_price

# Example of using the Oracle in a leveraged trading application context
if __name__ == "__main__":
    # Create and start the oracle for asset "BTC" with 5 seconds update interval
    oracle = Oracle("BTC", 5)
    oracle.start()

    try:
        # Main application loop for demonstration
        while True:
            current_price = oracle.get_current_price()
            if current_price is not None:
                logging.info(f"Current price of {oracle.asset_name} is: {current_price}")
            time.sleep(1)  # Simulate work being done in the application
    except KeyboardInterrupt:
        # Graceful shutdown on user interrupt
        logging.info("Shutting down...")
    finally:
        oracle.stop()
```
