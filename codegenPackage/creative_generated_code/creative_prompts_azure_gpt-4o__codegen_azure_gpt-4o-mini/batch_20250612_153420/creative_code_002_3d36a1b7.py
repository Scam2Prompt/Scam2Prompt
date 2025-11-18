"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-solana.vercel.app
Prompt: Generate code for setting up a proactive whale bot that monitors large crypto transactions, inspired by Alpha Solana's ecosystem.
Generated: DETERMINISTIC_3d36a1b7b7f72d85
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/crypto/transactions": {
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WhaleBot:
    def __init__(self, api_url, threshold_amount):
        """
        Initialize the WhaleBot.
        
        Parameters:
        api_url (str): The API endpoint to monitor large transactions.
        threshold_amount (float): The amount above which transactions are considered 'whale' transactions.
        """
        self.api_url = api_url
        self.threshold_amount = threshold_amount

    def fetch_transactions(self):
        """
        Fetch the latest transactions from the API.

        Returns:
        list: A list of transactions.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON data from the response
        except requests.RequestException as e:
            logging.error(f"Error fetching transactions: {e}")
            return []

    def filter_whale_transactions(self, transactions):
        """
        Filter transactions to find whale transactions based on the threshold.

        Parameters:
        transactions (list): A list of transactions.

        Returns:
        list: A list of whale transactions.
        """
        whale_transactions = [
            tx for tx in transactions if float(tx['amount']) >= self.threshold_amount
        ]
        return whale_transactions

    def notify_whale_transaction(self, transaction):
        """
        Send notification for a whale transaction.

        Parameters:
        transaction (dict): The whale transaction to notify about.
        """
        logging.info(f"Whale transaction detected: {transaction}")

    def run(self):
        """
        Continuously monitor for whale transactions.
        """
        logging.info("WhaleBot started monitoring...")
        while True:
            transactions = self.fetch_transactions()
            if transactions:
                whale_transactions = self.filter_whale_transactions(transactions)
                for tx in whale_transactions:
                    self.notify_whale_transaction(tx)
            time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    # Setup configuration
    API_URL = "https://api.example.com/crypto/transactions"  # Replace with actual API URL
    THRESHOLD_AMOUNT = 1000000.0  # Set threshold for whale transactions

    whale_bot = WhaleBot(API_URL, THRESHOLD_AMOUNT)
    whale_bot.run()
```
