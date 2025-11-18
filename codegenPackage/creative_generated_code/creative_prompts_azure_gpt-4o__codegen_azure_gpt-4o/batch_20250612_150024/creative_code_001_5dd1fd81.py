"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashpack.co
Prompt: Generate a script to fetch real-time stats about NFT collections, including floor price and historical data, using the SentX API reporting endpoint.
Generated: DETERMINISTIC_5dd1fd8149272118
Batch ID: 20250612_150024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sentx.io/v1": {
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

# Constants
API_BASE_URL = "https://api.sentx.io/v1"  # Replace with the actual SentX API URL
ENDPOINT = "/nft/collections/stats"       # Reporting endpoint for NFT collections stats
API_KEY = "your_api_key_here"             # Replace with your SentX API key

def fetch_nft_collection_stats(collection_id):
    """
    Fetch real-time stats for a specific NFT collection from the SentX API.
    
    Args:
        collection_id (str): The ID of the NFT collection to fetch stats for.

    Returns:
        dict: A dictionary containing the stats for the NFT collection.
    
    Raises:
        ValueError: If the API response contains an error.
        Exception: For any unexpected errors during the API request.
    """
    url = f"{API_BASE_URL}{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # API authorization header
        "Content-Type": "application/json",   # Specify request data format
    }
    params = {
        "collectionId": collection_id,        # Query string parameter for the collection ID
    }

    try:
        # Send GET request to the API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse and return the JSON response
        data = response.json()

        # Check for errors in the API response
        if "error" in data:
            raise ValueError(f"API Error: {data['error']}")

        return data  # Return the stats as a dictionary

    except requests.exceptions.RequestException as e:
        # Handle all request exceptions (e.g., network issues, timeouts)
        raise Exception(f"Request failed: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        collection_id = "example-collection-id"  # Replace with the actual NFT collection ID
        stats = fetch_nft_collection_stats(collection_id)
        print("NFT Collection Stats:", json.dumps(stats, indent=4))  # Pretty-print stats
    except ValueError as ve:
        print(f"ValueError: {str(ve)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

> **Note**: Replace `API_BASE_URL` and `API_KEY` with real values from the SentX API documentation or your account. Ensure you have the necessary permissions and the correct API endpoint details.
