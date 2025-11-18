"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkscan-sepolia.netlify.app
Prompt: Using the Starkscan API, generate a script to fetch all transactions with the status `ACCEPTED_ON_L1` within the last 30 minutes.
Generated: DETERMINISTIC_369e5c4d68105018
Batch ID: 20250612_151347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starkscan.co/transactions": {
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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
STARKSCAN_API_URL = "https://api.starkscan.co/transactions"  # Replace with the actual Starkscan API endpoint
STATUS_ACCEPTED_ON_L1 = "ACCEPTED_ON_L1"

def fetch_recent_transactions(status, minutes=30):
    """
    Fetch transactions with a specific status from the Starkscan API.

    Parameters:
    status (str): The transaction status to filter by.
    minutes (int): The time window in minutes to look back for transactions.

    Returns:
    list: A list of transactions with the specified status.
    """
    # Calculate the time range for the last `minutes` minutes
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=minutes)

    # Prepare the API request parameters
    params = {
        'status': status,
        'start_time': start_time.isoformat() + 'Z',  # ISO format in UTC
        'end_time': end_time.isoformat() + 'Z'  # ISO format in UTC
    }

    try:
        response = requests.get(STARKSCAN_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        transactions = response.json()

        # Check if the response contains the transactions key
        if 'transactions' in transactions:
            return transactions['transactions']
        else:
            logging.warning("No transactions key found in the response.")
            return []
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching transactions: {e}")
        return []

if __name__ == "__main__":
    # Fetch accepted transactions in the last 30 minutes
    accepted_transactions = fetch_recent_transactions(STATUS_ACCEPTED_ON_L1)

    # Output the fetched transactions
    if accepted_transactions:
        logging.info(f"Fetched {len(accepted_transactions)} transactions with status '{STATUS_ACCEPTED_ON_L1}'.")
        for tx in accepted_transactions:
            logging.info(tx)  # Print each transaction's details
    else:
        logging.info("No transactions found.")
```
