"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tensxair.web.app
Prompt: Build a tool to analyze and rank NFT collections on Tensor by their floor price changes over a 24-hour period.
Generated: DETERMINISTIC_08b6a04cd6d0f027
Batch ID: 20250612_150557
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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
from typing import List, Dict

class NFTCollectionAnalyzer:
    """A tool to analyze and rank NFT collections by their floor price changes."""

    def __init__(self, api_url: str):
        """
        Initialize the analyzer with the required API URL.
        
        :param api_url: The base URL of the NFT data API.
        """
        self.api_url = api_url

    def fetch_collections(self) -> List[Dict]:
        """
        Fetch NFT collections data from the API.
        
        :return: A list of NFT collections as dictionaries.
        """
        try:
            response = requests.get(f"{self.api_url}/nft-collections")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching NFT collections: {e}")
            return []

    def analyze_floor_price_changes(self, collections: List[Dict]) -> List[Dict]:
        """
        Analyze floor price changes of the given NFT collections.
        
        :param collections: A list of NFT collections to analyze.
        :return: A list of collections ranked by floor price change.
        """
        ranked_collections = []

        for collection in collections:
            try:
                floor_price_now = collection.get("floor_price_now", 0)
                floor_price_24h_ago = collection.get("floor_price_24h_ago", 0)

                if floor_price_24h_ago > 0:  # Avoid division by zero
                    price_change = ((floor_price_now - floor_price_24h_ago) / floor_price_24h_ago) * 100
                else:
                    price_change = float('inf')  # Infinite change if there was no price before

                ranked_collections.append({
                    "name": collection.get("name"),
                    "price_change": price_change,
                    "floor_price_now": floor_price_now,
                    "floor_price_24h_ago": floor_price_24h_ago
                })
            except Exception as e:
                print(f"Error analyzing collection {collection.get('name', 'unknown')}: {e}")

        # Sort collections by price change in descending order
        ranked_collections.sort(key=lambda x: x["price_change"], reverse=True)
        return ranked_collections

    def display_rankings(self, ranked_collections: List[Dict]) -> None:
        """
        Display the ranked NFT collections based on floor price changes.
        
        :param ranked_collections: A list of ranked NFT collections.
        """
        print("Ranked NFT Collections by Floor Price Change (24h):")
        for index, collection in enumerate(ranked_collections, start=1):
            print(f"{index}. {collection['name']} - Change: {collection['price_change']:.2f}% "
                  f"(Current Floor Price: {collection['floor_price_now']} | "
                  f"24h Ago: {collection['floor_price_24h_ago']})")

    def run_analysis(self) -> None:
        """
        Execute the analysis and display the results.
        """
        collections = self.fetch_collections()
        if collections:
            ranked_collections = self.analyze_floor_price_changes(collections)
            self.display_rankings(ranked_collections)
        else:
            print("No collections data available for analysis.")

# Usage example (you can replace 'https://api.example.com' with the actual API URL):
if __name__ == "__main__":
    analyzer = NFTCollectionAnalyzer(api_url='https://api.example.com')
    analyzer.run_analysis()
```
