"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitufu.com
Prompt: Develop a function that interacts with Bitkit's transaction log to generate a summary of recent withdrawals and deposits.
Generated: DETERMINISTIC_cb3b78c8dd41c304
Batch ID: 20250612_152329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/bitkit/transactions": {
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
import json
import requests
from typing import List, Dict

# Function to fetch transaction logs from Bitkit's API
def fetch_transaction_logs(api_url: str, api_key: str) -> List[Dict]:
    """
    Fetches transaction logs from Bitkit's API.

    Args:
        api_url (str): The URL of Bitkit's transaction log API endpoint.
        api_key (str): API key for authentication.

    Returns:
        List[Dict]: A list of transaction records.

    Raises:
        Exception: If the API request fails or the response is invalid.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(api_url, headers=headers)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        transaction_logs = response.json()
        if not isinstance(transaction_logs, list):
            raise ValueError("Unexpected response format: Expected a list of transactions.")
        
        return transaction_logs
    except requests.RequestException as e:
        raise Exception(f"Error fetching transaction logs: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Error decoding response JSON: {e}")

# Function to generate a summary of withdrawals and deposits
def generate_transaction_summary(transaction_logs: List[Dict]) -> Dict[str, float]:
    """
    Generates a summary of recent withdrawals and deposits.

    Args:
        transaction_logs (List[Dict]): A list of transaction records.

    Returns:
        Dict[str, float]: A summary containing total deposits and withdrawals.
    """
    summary = {"total_deposits": 0.0, "total_withdrawals": 0.0}

    for transaction in transaction_logs:
        try:
            # Validate transaction structure
            if "type" not in transaction or "amount" not in transaction:
                raise ValueError("Invalid transaction format: Missing 'type' or 'amount'.")
            
            # Accumulate totals based on transaction type
            if transaction["type"] == "deposit":
                summary["total_deposits"] += float(transaction["amount"])
            elif transaction["type"] == "withdrawal":
                summary["total_withdrawals"] += float(transaction["amount"])
            else:
                raise ValueError(f"Unknown transaction type: {transaction['type']}")
        except (ValueError, TypeError) as e:
            # Log and skip invalid transactions
            print(f"Skipping invalid transaction: {transaction}. Error: {e}")
            continue

    return summary

# Example usage
if __name__ == "__main__":
    # Replace with actual API URL and API key
    API_URL = "https://api.example.com/bitkit/transactions"
    API_KEY = "your_api_key_here"
    
    try:
        # Fetch transaction logs
        logs = fetch_transaction_logs(API_URL, API_KEY)
        
        # Generate summary
        summary = generate_transaction_summary(logs)
        
        # Display the summary
        print("Transaction Summary:")
        print(f"Total Deposits: ${summary['total_deposits']:.2f}")
        print(f"Total Withdrawals: ${summary['total_withdrawals']:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
