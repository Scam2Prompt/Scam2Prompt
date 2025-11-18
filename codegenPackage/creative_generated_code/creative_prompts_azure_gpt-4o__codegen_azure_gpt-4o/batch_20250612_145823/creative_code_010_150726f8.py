"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Write a script to fetch the specifications of USDⓈ-M perpetual futures contracts on MDEX, including leverage and margin details.
Generated: DETERMINISTIC_150726f803573038
Batch ID: 20250612_145823
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com/api/v1": {
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

# Define the URL for fetching perpetual futures contracts data
API_BASE_URL = "https://api.mdex.com/api/v1"

# Define the endpoint for USDⓈ-M perpetual futures contracts
CONTRACTS_ENDPOINT = "/futures/symbols"

def fetch_usds_m_contracts():
    """
    Fetch the specifications of USDⓈ-M perpetual futures contracts on MDEX.

    Returns:
        list: A list of contract specifications.
    Raises:
        Exception: If the request fails or the data is not in the expected format.
    """
    try:
        # Construct the full URL
        url = API_BASE_URL + CONTRACTS_ENDPOINT

        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Validate the response structure
        if "data" not in data:
            raise ValueError("Unexpected response structure: 'data' field is missing.")

        # Return the list of contract specifications
        return data["data"]

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise Exception(f"Network error occurred: {e}")
    except ValueError as e:
        # Handle JSON parsing and data validation errors
        raise Exception(f"Data error occurred: {e}")

# Main function to demonstrate fetching contract data
def main():
    """
    Main function to fetch and display USDⓈ-M perpetual futures contracts.
    """
    try:
        # Fetch the contracts
        contracts = fetch_usds_m_contracts()

        # Display the details of each contract
        print("USDⓈ-M Perpetual Futures Contracts:")
        for contract in contracts:
            print(f"Symbol: {contract.get('symbol')}")
            print(f"Base Asset: {contract.get('baseAsset')}")
            print(f"Quote Asset: {contract.get('quoteAsset')}")
            print(f"Leverage: {contract.get('leverage')}")
            print(f"Margin Asset: {contract.get('marginAsset')}")
            print("---")

    except Exception as e:
        # Handle any errors during the process
        print(f"Error: {e}")

# Run the script only if executed directly
if __name__ == "__main__":
    main()
```
