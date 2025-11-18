"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledqinlv.com
Prompt: Write a script using OpenSea's API to fetch and display statistics for a specific NFT collection, including floor price, volume, and percentage change.
Generated: DETERMINISTIC_a844d96df5ae2372
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1": {
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

class OpenSeaAPI:
    """
    A class to interact with OpenSea's API to fetch NFT collection statistics.
    """

    BASE_URL = 'https://api.opensea.io/api/v1'

    def __init__(self, collection_slug):
        """
        Initializes the OpenSeaAPI class with the specified NFT collection slug.

        :param collection_slug: The slug of the NFT collection to fetch statistics for.
        """
        self.collection_slug = collection_slug

    def fetch_collection_stats(self):
        """
        Fetch statistics for the specified NFT collection from OpenSea API.
        
        :return: A dictionary containing the collection statistics or None if an error occurs.
        """
        url = f'{self.BASE_URL}/collections?slugs={self.collection_slug}&format=json'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the JSON response
            data = response.json()
            if data and isinstance(data, list) and len(data) > 0:
                return data[0]['stats']
            else:
                print("No data found for the specified collection.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from OpenSea API: {e}")
            return None

    def display_stats(self, stats):
        """
        Display the statistics of the NFT collection.

        :param stats: A dictionary containing the statistics to display.
        """
        if stats is not None:
            print(f"Collection: {self.collection_slug.capitalize()}")
            print(f"Floor Price: {stats.get('floor_price', 'N/A')} ETH")
            print(f"Total Volume: {stats.get('total_volume', 'N/A')} ETH")
            print(f"Percentage Change (24h): {stats.get('one_day_change', 'N/A')}%")
        else:
            print("No statistics available to display.")

def main():
    """
    Main function to execute the script.
    """
    # Example NFT collection slug (e.g., 'boredapeyachtclub')
    collection_slug = 'boredapeyachtclub'
    
    # Create an instance of OpenSeaAPI
    opensea_api = OpenSeaAPI(collection_slug)
    
    # Fetch collection statistics
    stats = opensea_api.fetch_collection_stats()
    
    # Display the statistics
    opensea_api.display_stats(stats)

if __name__ == '__main__':
    main()
```
