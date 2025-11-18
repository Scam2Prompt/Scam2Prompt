"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.pages.dev
Prompt: Develop a script in Python to query the LooksRare API for the number of owners and items in the "Mutant Ape Yacht Club" collection.
Generated: DETERMINISTIC_7e3a533573b2874d
Batch ID: 20250612_151547
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.looksrare.org/api/v1": {
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

class LooksRareAPI:
    """Class to interact with the LooksRare API for NFT data."""

    BASE_URL = "https://api.looksrare.org/api/v1"

    def __init__(self):
        """Initialize the LooksRareAPI instance."""
        self.session = requests.Session()

    def get_collection_data(self, collection_slug):
        """
        Retrieve data for a specific NFT collection.

        Args:
            collection_slug (str): The slug of the NFT collection.

        Returns:
            dict: The JSON response containing collection data.

        Raises:
            Exception: If the request to the API fails or returns an error.
        """
        url = f"{self.BASE_URL}/collections/{collection_slug}"

        try:
            response = self.session.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP responses
            return response.json()
        except requests.RequestException as e:
            raise Exception("Failed to fetch collection data from LooksRare API") from e

def main():
    """Main function to query the LooksRare API for the Mutant Ape Yacht Club collection."""
    collection_slug = "mutant-apeyachtclub"
    api = LooksRareAPI()

    try:
        collection_data = api.get_collection_data(collection_slug)
        owners = collection_data.get('owners', 0)  # Default to 0 if not found
        items = collection_data.get('items', 0)    # Default to 0 if not found

        print(f"Mutant Ape Yacht Club Collection:")
        print(f"Number of Owners: {owners}")
        print(f"Number of Items: {items}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
