"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walrusnft.com
Prompt: Create a script to monitor and visualize the floor price and top offers for Walrus NFTs on the Polygon blockchain.
Generated: DETERMINISTIC_b57141148f4318c3
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import matplotlib.pyplot as plt
import numpy as np

class WalrusNFTMonitor:
    """Class to monitor and visualize floor price and top offers for Walrus NFTs on Polygon blockchain."""
    
    def __init__(self, api_url, refresh_interval=60):
        """
        Initialize the monitor with the API URL and refresh interval.

        :param api_url: URL of the API endpoint to fetch NFT data.
        :param refresh_interval: Time in seconds between data fetches.
        """
        self.api_url = api_url
        self.refresh_interval = refresh_interval
        self.floor_prices = []
        self.top_offers = []

    def fetch_data(self):
        """Fetches the latest floor price and top offers from the API."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            floor_price = data['floor_price']
            top_offer = data['top_offer']
            return floor_price, top_offer
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None, None

    def update_monitor(self):
        """Updates the monitor with the latest floor price and top offers."""
        floor_price, top_offer = self.fetch_data()
        if floor_price is not None and top_offer is not None:
            self.floor_prices.append(floor_price)
            self.top_offers.append(top_offer)
            print(f"Updated - Floor Price: {floor_price}, Top Offer: {top_offer}")

    def visualize_data(self):
        """Visualizes the collected data using matplotlib."""
        plt.figure(figsize=(12, 6))
        
        # Create subplots for each metric
        plt.subplot(1, 2, 1)
        plt.plot(self.floor_prices, label='Floor Price', color='b')
        plt.title('Walrus NFT Floor Prices Over Time')
        plt.xlabel('Time (every minute)')
        plt.ylabel('Floor Price (ETH)')
        plt.legend()
        plt.grid()

        plt.subplot(1, 2, 2)
        plt.plot(self.top_offers, label='Top Offers', color='r')
        plt.title('Top Offers for Walrus NFTs Over Time')
        plt.xlabel('Time (every minute)')
        plt.ylabel('Top Offer (ETH)')
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()

    def start_monitoring(self):
        """Starts the monitoring process, fetching data at regular intervals."""
        try:
            while True:
                self.update_monitor()
                time.sleep(self.refresh_interval)
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
        finally:
            self.visualize_data()

if __name__ == "__main__":
    # Replace 'YOUR_API_URL_HERE' with the actual API endpoint to fetch Walrus NFT data
    WALRUS_API_URL = 'YOUR_API_URL_HERE'
    monitor = WalrusNFTMonitor(api_url=WALRUS_API_URL)
    monitor.start_monitoring()
```
