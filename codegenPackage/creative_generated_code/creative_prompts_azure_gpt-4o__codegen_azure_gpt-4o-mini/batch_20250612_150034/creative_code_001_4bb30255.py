"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Generate Python code to filter and display NFTs from the "Heart Full of Love JamCards" collection based on their rarity traits, such as "VOCAL" or "INSTRUMENT."
Generated: DETERMINISTIC_4bb30255e4826282
Batch ID: 20250612_150034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/nft-collections/heart-full-of-love-jamcards": {
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

class NFT:
    """
    Represents an NFT with its properties.
    """
    def __init__(self, name: str, traits: List[str]):
        self.name = name
        self.traits = traits

    def has_trait(self, trait: str) -> bool:
        """
        Checks if the NFT has a specific trait.

        :param trait: The trait to check for.
        :return: True if the trait is present, otherwise False.
        """
        return trait in self.traits


def fetch_nft_collection(collection_url: str) -> List[NFT]:
    """
    Fetches the NFTs from the specified collection URL.

    :param collection_url: URL to fetch the NFT data from.
    :return: List of NFT objects.
    :raises ValueError: If the response does not contain valid NFT data.
    """
    try:
        response = requests.get(collection_url)
        response.raise_for_status()  # Raise an error for bad responses
        nft_data = response.json()

        # Create NFT objects from the fetched data
        return [NFT(nft['name'], nft['traits']) for nft in nft_data if 'name' in nft and 'traits' in nft]

    except requests.RequestException as e:
        print(f"Error fetching NFT data: {e}")
        return []
    except ValueError as e:
        print(f"Error processing NFT data: {e}")
        return []


def filter_nfts_by_trait(nfts: List[NFT], trait: str) -> List[NFT]:
    """
    Filters the NFTs by a specific trait.

    :param nfts: List of NFT objects to filter.
    :param trait: The trait to filter the NFTs by.
    :return: List of NFTs that contain the specified trait.
    """
    return [nft for nft in nfts if nft.has_trait(trait)]


def display_nfts(nfts: List[NFT]) -> None:
    """
    Displays the NFTs in a readable format.

    :param nfts: List of NFT objects to display.
    """
    if not nfts:
        print("No NFTs found.")
        return
    
    print("Filtered NFTs:")
    for nft in nfts:
        print(f" - {nft.name} with traits: {', '.join(nft.traits)}")


def main():
    """
    Main function to execute the NFT filtering process.
    """
    collection_url = "https://api.example.com/nft-collections/heart-full-of-love-jamcards"  # Replace with actual API URL
    trait_to_filter = "VOCAL"  # Change to "INSTRUMENT" to filter by that trait

    # Fetch the NFT collection
    nfts = fetch_nft_collection(collection_url)

    # Filter NFTs by the specified trait
    filtered_nfts = filter_nfts_by_trait(nfts, trait_to_filter)

    # Display the filtered NFTs
    display_nfts(filtered_nfts)


if __name__ == "__main__":
    main()
```
