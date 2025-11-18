"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-crypto.web.app
Prompt: Provide a Python example for calculating the floor price of NFTs for a specific collection using Tensor's API and display the results.
Generated: DETERMINISTIC_26ba7ef25507803c
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.com/v1": {
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

class NFTCollectionFloorPrice:
    def __init__(self, api_key: str, collection_slug: str):
        """
        Initializes the NFTCollectionFloorPrice object.
        
        :param api_key: The API key for accessing the Tensor API.
        :param collection_slug: The unique slug identifier for the NFT collection.
        """
        self.api_key = api_key
        self.collection_slug = collection_slug
        self.base_url = "https://api.tensor.com/v1"  # Example base URL

    def get_floor_price(self) -> float:
        """
        Retrieves the floor price for the specified NFT collection.
        
        :return: The floor price of the NFT collection.
        :raises ValueError: If the response does not contain a floor price.
        :raises Exception: For any other error that occurs during the API request.
        """
        url = f"{self.base_url}/collections/{self.collection_slug}/floor_price"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()
            
            # Check if floor price exists in the response
            if 'floor_price' not in data:
                raise ValueError(f"Floor price not found in response: {data}")
            
            return float(data['floor_price'])

        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            raise  # Re-raise the exception for further handling if needed
        except ValueError as e:
            print(f"Value error: {e}")
            raise  # Re-raise the exception to handle it externally

def main():
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    COLLECTION_SLUG = "your_collection_slug_here"  # Replace with the actual collection slug

    nft_collection = NFTCollectionFloorPrice(API_KEY, COLLECTION_SLUG)

    try:
        floor_price = nft_collection.get_floor_price()
        print(f"The floor price for the collection '{COLLECTION_SLUG}' is: {floor_price}")
    except Exception as e:
        print(f"Failed to retrieve floor price: {e}")

if __name__ == "__main__":
    main()
```
