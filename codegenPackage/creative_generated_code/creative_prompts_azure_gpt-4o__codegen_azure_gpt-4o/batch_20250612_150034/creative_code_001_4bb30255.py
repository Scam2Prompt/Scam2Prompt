"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Generate Python code to filter and display NFTs from the "Heart Full of Love JamCards" collection based on their rarity traits, such as "VOCAL" or "INSTRUMENT."
Generated: DETERMINISTIC_4bb30255e4826282
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class NFTCollection:
    """
    A class to represent a collection of NFTs and filter them based on traits.
    """

    def __init__(self, nft_data):
        """
        Initialize the NFTCollection instance.

        Args:
            nft_data (list): List of dictionaries representing NFT metadata.
        """
        self.nft_data = nft_data

    def filter_by_rarity_trait(self, trait):
        """
        Filter NFTs based on a specific rarity trait.

        Args:
            trait (str): The rarity trait to filter by, e.g., "VOCAL" or "INSTRUMENT".

        Returns:
            list: List of filtered NFT dictionaries.
        """
        if not trait:
            raise ValueError("Trait must be a non-empty string.")
        
        filtered_nfts = [nft for nft in self.nft_data if trait in nft.get('rarityTraits', [])]
        return filtered_nfts

    def display_filtered_nfts(self, filtered_nfts):
        """
        Display filtered NFTs in a readable format.

        Args:
            filtered_nfts (list): List of filtered NFT dictionaries.
        """
        if not filtered_nfts:
            print("No NFTs found with the specified rarity trait.")
            return

        print(f"Found {len(filtered_nfts)} NFTs with the specified rarity trait:")
        for nft in filtered_nfts:
            print(f"ID: {nft.get('id')} | Name: {nft.get('name')} | Traits: {', '.join(nft.get('rarityTraits', []))}")


def load_nft_data(file_path):
    """
    Load NFT data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: List of dictionaries representing NFT metadata.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        return []


def main():
    """
    Main function to execute the NFT filtering logic.
    """
    # Specify the path to the NFT data file (JSON format)
    nft_data_file = "nft_data.json"

    # Load NFT data from the file
    nft_data = load_nft_data(nft_data_file)

    # If data is empty, exit the program
    if not nft_data:
        print("No NFT data loaded. Exiting program.")
        return

    # Create an instance of NFTCollection with loaded data
    nft_collection = NFTCollection(nft_data)

    # Specify the rarity trait to filter by
    rarity_trait = input("Enter rarity trait to filter NFTs (e.g., VOCAL, INSTRUMENT): ").strip().upper()

    try:
        # Filter NFTs based on the specified rarity trait
        filtered_nfts = nft_collection.filter_by_rarity_trait(rarity_trait)

        # Display the filtered NFTs
        nft_collection.display_filtered_nfts(filtered_nfts)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
