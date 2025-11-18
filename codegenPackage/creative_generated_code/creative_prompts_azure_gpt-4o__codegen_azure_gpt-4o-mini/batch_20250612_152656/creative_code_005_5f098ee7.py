"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangocrypto-website.pages.dev
Prompt: Provide an example of how to use Tangocrypto's API suite to monitor payments on the Cardano blockchain and trigger alerts for successful transactions.
Generated: DETERMINISTIC_5f098ee7f4858504
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tangocrypto.com/v1": {
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

class CardanoPaymentMonitor:
    """
    A class to monitor Cardano blockchain payments using the Tangocrypto API.
    This class provides functionality to check for successful transactions
    and trigger alerts accordingly.
    """

    def __init__(self, api_key, wallet_address, alert_callback):
        """
        Initializes the payment monitor with the necessary parameters.

        Args:
            api_key (str): API key for Tangocrypto.
            wallet_address (str): The Cardano wallet address to monitor.
            alert_callback (callable): A callback function to trigger alerts.
        """
        self.api_key = api_key
        self.wallet_address = wallet_address
        self.alert_callback = alert_callback
        self.base_url = "https://api.tangocrypto.com/v1"
        self.last_seen_transaction_id = None

    def get_transactions(self):
        """
        Fetches the latest transactions for the specified wallet address.

        Returns:
            list: A list of transaction objects.
        """
        url = f"{self.base_url}/transactions/{self.wallet_address}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching transactions: {e}")
            return []

    def check_for_successful_transactions(self):
        """
        Checks for successful transactions and triggers alerts for any new ones.
        """
        transactions = self.get_transactions()

        if not transactions:
            return
        
        for transaction in transactions:
            transaction_id = transaction['id']
            status = transaction['status']

            # Check for new successful transactions
            if status == "successful" and transaction_id != self.last_seen_transaction_id:
                self.last_seen_transaction_id = transaction_id
                self.alert_callback(transaction)  # Trigger the alert

    def start_monitoring(self, interval=10):
        """
        Starts monitoring for successful transactions at a specified interval.

        Args:
            interval (int): Time in seconds between API checks.
        """
        while True:
            self.check_for_successful_transactions()
            time.sleep(interval)  # Wait for the specified interval

def alert_user(transaction):
    """
    Example alert callback function that prints transaction details.
    
    Args:
        transaction (dict): The transaction details.
    """
    print(f"Alert! New successful transaction detected: {transaction}")

if __name__ == "__main__":
    # Replace with your actual Tangocrypto API key and wallet address
    API_KEY = "your_api_key"
    WALLET_ADDRESS = "your_wallet_address"

    # Create the cardano payment monitor
    monitor = CardanoPaymentMonitor(api_key=API_KEY, wallet_address=WALLET_ADDRESS, alert_callback=alert_user)

    # Start monitoring
    monitor.start_monitoring(interval=10)
```
