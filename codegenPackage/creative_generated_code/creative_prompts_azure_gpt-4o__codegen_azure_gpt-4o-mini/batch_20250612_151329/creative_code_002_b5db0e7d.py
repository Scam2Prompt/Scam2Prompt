"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flkdjdkljflksjd.pages.dev
Prompt: Write a Python function that connects to the DappRadar API and retrieves detailed information about NFTs, including their market trends and transaction history.
Generated: DETERMINISTIC_b5db0e7dd502e66e
Batch ID: 20250612_151329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dappradar.com/nft/{nft_id": {
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

class DappRadarAPIError(Exception):
    """Custom exception for DappRadar API errors."""
    pass

def get_nft_details(nft_id):
    """
    Retrieves detailed information about a specific NFT from the DappRadar API,
    including its market trends and transaction history.

    Parameters:
    nft_id (str): The unique identifier for the NFT.

    Returns:
    dict: A dictionary containing NFT details, market trends, and transaction history.

    Raises:
    DappRadarAPIError: If the API request fails or returns an error.
    ValueError: If the NFT ID is invalid.
    """

    if not isinstance(nft_id, str) or not nft_id.strip():
        raise ValueError("Invalid NFT ID provided. It must be a non-empty string.")

    url = f"https://api.dappradar.com/nft/{nft_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        data = response.json()  # Parse JSON response

        if 'error' in data:
            raise DappRadarAPIError(f"API Error: {data['error']}")

        return data  # Return the retrieved NFT details

    except requests.exceptions.HTTPError as http_err:
        raise DappRadarAPIError(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except requests.exceptions.RequestException as req_err:
        raise DappRadarAPIError(f"Request error occurred: {req_err}")  # Handle other request errors
    except ValueError as json_err:
        raise DappRadarAPIError(f"JSON decoding error: {json_err}")  # Handle JSON decode errors

# Example usage:
if __name__ == "__main__":
    try:
        nft_id = "example_nft_id"  # Replace with a valid NFT ID
        nft_details = get_nft_details(nft_id)
        print(nft_details)
    except DappRadarAPIError as api_err:
        print(f"Error retrieving NFT details: {api_err}")
    except ValueError as val_err:
        print(f"Input error: {val_err}")
```
