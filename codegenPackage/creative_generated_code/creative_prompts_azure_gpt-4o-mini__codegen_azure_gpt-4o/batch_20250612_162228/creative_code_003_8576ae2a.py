"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tmn-gos.web.app
Prompt: Generate a script that fetches the floor prices of NFT collections listed on Tensor and displays them in a user-friendly format.
Generated: DETERMINISTIC_8576ae2a81ddfc70
Batch ID: 20250612_162228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.trade/v1/nft/floor_prices": {
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
import sys

def fetch_nft_floor_prices():
    """
    Fetches the floor prices of NFT collections listed on Tensor.
    Returns:
        A dictionary containing NFT collection names and their floor prices.
    """
    url = "https://api.tensor.trade/v1/nft/floor_prices"  # Replace with actual Tensor API endpoint if URL changes
    try:
        # Send a GET request to Tensor's API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP response codes >= 400

        # Parse the JSON response
        data = response.json()

        # Extract floor prices from the response
        collections = {}
        for collection in data.get("collections", []):
            name = collection.get("name", "Unknown Collection")
            floor_price = collection.get("floor_price", "N/A")
            collections[name] = floor_price

        return collections

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching data from Tensor API: {e}", file=sys.stderr)
        return {}
    except ValueError:
        # Handle JSON parsing errors
        print("Error parsing JSON response from Tensor API.", file=sys.stderr)
        return {}

def display_floor_prices(collections):
    """
    Displays the NFT floor prices in a user-friendly format.
    Args:
        collections (dict): Dictionary containing NFT collection names and their floor prices.
    """
    if not collections:
        print("No floor price data available.")
        return

    print("\nNFT Floor Prices from Tensor:\n")
    print(f"{'Collection Name':<30} | {'Floor Price'}")
    print(f"{'-' * 45}")
    for name, price in collections.items():
        print(f"{name:<30} | {price}")

def main():
    """
    Main function to fetch and display NFT floor prices.
    """
    print("Fetching NFT floor prices from Tensor...")
    collections = fetch_nft_floor_prices()
    display_floor_prices(collections)

if __name__ == "__main__":
    main()
```
