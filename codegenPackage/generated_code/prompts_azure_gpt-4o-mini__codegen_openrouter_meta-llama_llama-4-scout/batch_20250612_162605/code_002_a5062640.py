"""
Generated Code Metadata:
========================
Original URL: https://opensea-dashboard.vercel.app
Prompt: Generate a function that filters NFT items based on their price and rarity using the OpenSea Dashboard's features.
Generated: DETERMINISTIC_a506264070b76cd8
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_filter.py

from typing import List, Dict

class NFT:
    """Represents an NFT item."""
    def __init__(self, name: str, price: float, rarity: str):
        """
        Initializes an NFT item.

        Args:
        - name (str): The name of the NFT item.
        - price (float): The price of the NFT item.
        - rarity (str): The rarity of the NFT item.
        """
        self.name = name
        self.price = price
        self.rarity = rarity

def filter_nfts(nfts: List[NFT], min_price: float = 0, max_price: float = float('inf'), 
                rarity: str = None) -> List[NFT]:
    """
    Filters NFT items based on their price and rarity.

    Args:
    - nfts (List[NFT]): The list of NFT items to filter.
    - min_price (float, optional): The minimum price of the NFT items. Defaults to 0.
    - max_price (float, optional): The maximum price of the NFT items. Defaults to infinity.
    - rarity (str, optional): The rarity of the NFT items. Defaults to None.

    Returns:
    - List[NFT]: The filtered list of NFT items.
    """
    try:
        # Filter NFT items based on price and rarity
        filtered_nfts = [nft for nft in nfts 
                         if min_price <= nft.price <= max_price 
                         and (rarity is None or nft.rarity == rarity)]
        return filtered_nfts
    except Exception as e:
        # Log and re-raise the exception
        print(f"An error occurred: {str(e)}")
        raise

def main():
    # Example usage
    nfts = [
        NFT("Item 1", 10.99, "Common"),
        NFT("Item 2", 5.99, "Uncommon"),
        NFT("Item 3", 20.99, "Rare"),
        NFT("Item 4", 15.99, "Common"),
    ]

    filtered_nfts = filter_nfts(nfts, min_price=5, max_price=15, rarity="Common")
    for nft in filtered_nfts:
        print(f"Name: {nft.name}, Price: {nft.price}, Rarity: {nft.rarity}")

if __name__ == "__main__":
    main()
```
