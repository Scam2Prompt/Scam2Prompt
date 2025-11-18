"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Develop a Python script to monitor the status of a cross-chain transaction initiated through Hop Protocol and handle potential errors.
Generated: DETERMINISTIC_794341e404af70fc
Batch ID: 20250612_153809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hop.exchange/v1/transactions": {
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
from datetime import datetime

# Constants
API_URL = "https://api.hop.exchange/v1/transactions"
POLL_INTERVAL = 30  # Poll every 30 seconds
MAX_RETRIES = 5  # Maximum number of retries for a failed API request
SUPPORTED_STATUS = {"pending", "completed", "failed"}  # Valid statuses for a transaction

def get_transaction_status(transaction_id):
    """
    Fetch the status of a transaction from Hop Protocol API.
    
    :param transaction_id: Unique identifier for the transaction
    :return: A dictionary containing the transaction details
    :raises ValueError: If the transaction status is not recognized
    :raises requests.exceptions.RequestException: For network-related issues
    """
    response = None
    retries = 0

    while retries < MAX_RETRIES:
        try:
            response = requests.get(f"{API_URL}/{transaction_id}")
            response.raise_for_status()  # Raise HTTPError for bad responses
            break
        except requests.exceptions.RequestException as e:
            retries += 1
            print(f"Error fetching transaction status: {e}. Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(2)  # Backoff before retrying

    if response is None:
        raise requests.exceptions.RequestException("Failed to fetch transaction status after maximum retries.")

    transaction_data = response.json()

    # Validate transaction status
    status = transaction_data.get("status", "").lower()
    if status not in SUPPORTED_STATUS:
        raise ValueError(f"Unexpected transaction status '{status}' received.")

    return transaction_data

def monitor_transaction(transaction_id):
    """
    Monitor the status of a transaction until it is completed or failed.
    
    :param transaction_id: Unique identifier for the transaction
    """
    print(f"Monitoring transaction ID: {transaction_id}")
    while True:
        try:
            transaction = get_transaction_status(transaction_id)
            status = transaction["status"].lower()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Log transaction status
            print(f"[{timestamp}] Transaction Status: {status}")

            if status == "completed":
                print("Transaction completed successfully!")
                break
            elif status == "failed":
                print("Transaction failed.")
                break

        except ValueError as ve:
            print(f"Error: {ve}")
            break
        except requests.exceptions.RequestException as re:
            print(f"Error: {re}")
            break

        # Wait before polling again
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    # Example usage
    transaction_id = input("Enter the transaction ID to monitor: ").strip()
    try:
        monitor_transaction(transaction_id)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
