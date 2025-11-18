"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanadashboard.stakesphere.io
Prompt: Create a script to periodically update and display the last refresh time for wallet data, similar to the "Last updated" feature on https://solanadashboard.stakesphere.io.
Generated: DETERMINISTIC_d3f1c03d35903b3f
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime
import random
import threading

class WalletDataUpdater:
    def __init__(self, update_interval=60):
        """
        Initializes the WalletDataUpdater with a specified update interval.
        
        Parameters:
            update_interval (int): Interval in seconds at which to update wallet data.
        """
        self.update_interval = update_interval
        self.last_refresh_time = None
        self.running = True

    def start(self):
        """Starts the data update loop in a separate thread."""
        threading.Thread(target=self.update_loop, daemon=True).start()

    def update_loop(self):
        """Continuously updates wallet data at specified intervals."""
        while self.running:
            self.update_wallet_data()
            time.sleep(self.update_interval)

    def update_wallet_data(self):
        """
        Simulates the update of wallet data.
        In a real application, this would involve network calls to retrieve wallet info.
        """
        # Simulating data update
        self.last_refresh_time = datetime.datetime.now()
        print(f"Wallet data updated at: {self.last_refresh_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def get_last_refresh_time(self):
        """
        Returns the last refresh time as a formatted string.
        
        Returns:
            str: Formatted last refresh time or a message if not yet updated.
        """
        if self.last_refresh_time:
            return self.last_refresh_time.strftime('%Y-%m-%d %H:%M:%S')
        return "Wallet data not yet updated."

    def stop(self):
        """Stops the update loop."""
        self.running = False

def main():
    """Main function to run the wallet data updater."""
    updater = WalletDataUpdater(update_interval=10)  # Update every 10 seconds
    updater.start()

    try:
        while True:
            # Display the last refresh time every 5 seconds
            print("Last refresh time:", updater.get_last_refresh_time())
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping the wallet data updater...")
        updater.stop()

if __name__ == "__main__":
    main()
```
