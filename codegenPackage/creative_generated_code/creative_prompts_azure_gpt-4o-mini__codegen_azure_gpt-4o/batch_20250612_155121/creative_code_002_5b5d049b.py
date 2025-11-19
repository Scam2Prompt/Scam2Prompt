"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digital.free-zetachain.online
Prompt: Write a Python function that interacts with the ZetaChain API to retrieve transaction data.
Generated: DETERMINISTIC_5b5d049b746153ba
Batch ID: 20250612_155121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_transaction_data(api_url: str, api_key: str, transaction_id: str) -> dict:
    """
    Fetch transaction data from the ZetaChain API.

    Args:
        api_url (str): Base URL of the ZetaChain API.
        api_key (str): API key for authentication.
        transaction_id (str): The ID of the transaction to retrieve.

    Returns:
        dict: A dictionary containing the transaction data.

    Raises:
        ValueError: If transaction_id is invalid or empty.
        requests.exceptions.RequestException: If an error occurs during the API request.
    """
    # Validate input parameters
    if not transaction_id:
        raise ValueError("Transaction ID cannot be empty or None.")

    # Endpoint to retrieve transaction data
    endpoint = f"{api_url}/transactions/{transaction_id}"

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the API request
        response = requests.get(endpoint, headers=headers)

        # Check if the response status code indicates success
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        # Log the error and re-raise it for the caller
        print(f"Error fetching transaction data: {e}")
        raise
```

To use this function, ensure the `api_url`, `api_key`, and `transaction_id` values are set appropriately based on the specifics of the ZetaChain API.
