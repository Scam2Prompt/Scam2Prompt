"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesolana.com
Prompt: Provide an example of how to use a Solana-based API to fetch real-time data on stablecoin transactions, referencing the trends discussed on Inside Solana.
Generated: DETERMINISTIC_f2f51abab1714de4
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solana.com": {
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
import json

class SolanaAPI:
    """A class to interact with the Solana API for fetching stablecoin transaction data."""

    BASE_URL = "https://api.solana.com"

    def __init__(self):
        """Initialize the SolanaAPI class."""
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

    def fetch_stablecoin_transactions(self, stablecoin_mint_address, limit=10):
        """
        Fetch real-time stablecoin transactions from Solana.

        Args:
            stablecoin_mint_address (str): The mint address of the stablecoin to track.
            limit (int): The maximum number of transactions to fetch.

        Returns:
            List[dict]: A list of transactions if successful, empty list otherwise.
        """
        # Prepare the JSON-RPC payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getConfirmedSignaturesForAddress2",
            "params": [
                stablecoin_mint_address,
                {
                    "limit": limit,
                    "before": None,
                    "until": None
                }
            ]
        }

        try:
            # Send the request to the Solana API
            response = self.session.post(self.BASE_URL, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the JSON response
            data = response.json()
            if "result" in data:
                return data["result"]  # Return the list of transaction signatures
            else:
                print("Error fetching data: ", data.get("error", "Unknown error"))
                return []

        except requests.RequestException as e:
            # Handle any request-related errors
            print(f"Request failed: {e}")
            return []
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            print("Failed to decode JSON response.")
            return []

if __name__ == "__main__":
    # Example usage of the SolanaAPI class
    stablecoin_mint_address = "YOUR_STABLECOIN_MINT_ADDRESS_HERE"  # Replace with the actual mint address
    solana_api = SolanaAPI()
    
    # Fetch the latest stablecoin transactions
    transactions = solana_api.fetch_stablecoin_transactions(stablecoin_mint_address)

    # Print the fetched transactions
    if transactions:
        print(f"Fetched {len(transactions)} transactions:")
        for tx in transactions:
            print(json.dumps(tx, indent=2))
    else:
        print("No transactions found or an error occurred.")
```
