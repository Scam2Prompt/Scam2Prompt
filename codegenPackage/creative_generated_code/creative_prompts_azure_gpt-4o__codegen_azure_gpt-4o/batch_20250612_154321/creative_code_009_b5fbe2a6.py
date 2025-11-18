"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-wallet-fees.pages.dev
Prompt: Create a Python script to validate on-chain data using Etherscan's API, ensuring the integrity of a specific transaction hash.
Generated: DETERMINISTIC_b5fbe2a6cc7f15b5
Batch ID: 20250612_154321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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
import os

# Constants
ETHERSCAN_API_BASE_URL = "https://api.etherscan.io/api"
API_KEY = os.getenv("ETHERSCAN_API_KEY")  # Ensure you set this in your environment variables

def validate_transaction(tx_hash: str) -> dict:
    """
    Validates the integrity of a transaction hash using Etherscan's API.

    Args:
        tx_hash (str): The transaction hash to validate.

    Returns:
        dict: Contains the transaction details if valid, or an error message if invalid.
    """
    try:
        # Input validation
        if not tx_hash or len(tx_hash) != 66 or not tx_hash.startswith("0x"):
            return {"error": "Invalid transaction hash format."}
        
        # Prepare API request parameters
        params = {
            "module": "account",
            "action": "txlistinternal",
            "txhash": tx_hash,
            "apikey": API_KEY
        }

        # Send GET request to Etherscan API
        response = requests.get(ETHERSCAN_API_BASE_URL, params=params)

        # Check HTTP response status
        if response.status_code != 200:
            return {"error": f"Failed to connect to Etherscan API. HTTP Status: {response.status_code}"}

        # Parse JSON response
        data = response.json()

        # Check API response status
        if data.get("status") != "1":
            return {"error": f"Etherscan API Error: {data.get('message', 'Unknown error')}"}

        # Validate transaction data integrity
        result = data.get("result", [])
        if not result:
            return {"error": "Transaction not found or invalid transaction hash."}

        # Return transaction details
        return {"success": True, "transaction_details": result}

    except requests.RequestException as e:
        # Handle network-related errors
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"Unexpected error: {str(e)}"}

if __name__ == "__main__":
    # Example Usage
    transaction_hash = input("Enter the transaction hash to validate: ").strip()
    result = validate_transaction(transaction_hash)
    
    # Print result
    if "success" in result and result["success"]:
        print("Transaction details:", result["transaction_details"])
    else:
        print("Error:", result["error"])
```

### Notes:
- Ensure you set your Etherscan API key as an environment variable `ETHERSCAN_API_KEY` before running the script.
- Replace the `action` in the `params` dictionary based on the specific type of transaction you want to validate. In this example, it's set to `txlistinternal`.
