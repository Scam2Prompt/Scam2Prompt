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
  "https://api.starkscan.co/v1": {
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
import datetime

# Function to fetch transactions with status ACCEPTED_ON_L1 within the last 30 minutes
def fetch_recent_transactions(api_endpoint, api_key):
    """
    Fetches transactions from the Starkscan API with the status ACCEPTED_ON_L1 from the last 30 minutes.
    
    Args:
        api_endpoint (str): The base URL for the Starkscan API.
        api_key (str): API key for authentication (if required).
    
    Returns:
        list: A list of transactions matching the criteria.
    """
    try:
        # Calculate the timestamp for 30 minutes ago
        thirty_minutes_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
        thirty_minutes_ago_iso = thirty_minutes_ago.isoformat() + "Z"  # ISO 8601 format with UTC timezone

        # Build the request parameters
        params = {
            "status": "ACCEPTED_ON_L1",
            "from_timestamp": thirty_minutes_ago_iso,
            "to_timestamp": datetime.datetime.utcnow().isoformat() + "Z"
        }

        # Make the API request
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        response = requests.get(f"{api_endpoint}/transactions", params=params, headers=headers)

        # Check if the request was successful
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()
        
        # Extract transactions from the response (assuming key "transactions" exists)
        transactions = data.get("transactions", [])
        
        return transactions

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(f"An error occurred while fetching transactions: {e}")
        return []
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    API_ENDPOINT = "https://api.starkscan.co/v1"  # Replace with the actual API endpoint
    API_KEY = "your_api_key_here"  # Replace with your API key, if required

    transactions = fetch_recent_transactions(API_ENDPOINT, API_KEY)
    print(f"Retrieved {len(transactions)} transactions:")
    for transaction in transactions:
        print(transaction)
```
