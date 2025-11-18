"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chibiheadnft.com
Prompt: Write code to create a "sold-out" indicator for NFTs in a collection, referencing the functionality described for "Chibi Head NFT."
Generated: DETERMINISTIC_43367c4386e7c558
Batch ID: 20250612_145238
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
    def __init__(self, collection_name, total_supply):
        """
        Initialize the NFTCollection instance.

        :param collection_name: Name of the NFT collection.
        :param total_supply: Total number of NFTs available in the collection.
        """
        self.collection_name = collection_name
        self.total_supply = total_supply
        self.sold_nfts = 0

    def purchase_nft(self, quantity=1):
        """
        Handles the purchase of NFTs from the collection.

        :param quantity: Number of NFTs being purchased.
        :raises ValueError: If attempting to purchase more NFTs than available.
        """
        if self.sold_nfts + quantity > self.total_supply:
            raise ValueError("Cannot purchase more NFTs. This collection is sold out or insufficient quantity available.")
        
        self.sold_nfts += quantity
        print(f"Successfully purchased {quantity} NFT(s). {self.total_supply - self.sold_nfts} remaining.")

    def is_sold_out(self):
        """
        Checks if the NFT collection is sold out.

        :return: True if the collection is sold out, False otherwise.
        """
        return self.sold_nfts >= self.total_supply

    def get_status(self):
        """
        Returns the current status of the NFT collection.

        :return: A dictionary containing collection name, total supply, sold NFTs, and sold-out status.
        """
        return {
            "collection_name": self.collection_name,
            "total_supply": self.total_supply,
            "sold_nfts": self.sold_nfts,
            "is_sold_out": self.is_sold_out()
        }


def main():
    # Example usage of the NFTCollection class
    try:
        # Initialize the NFT collection with a name and total supply
        chibi_head_nfts = NFTCollection(collection_name="Chibi Head NFT", total_supply=100)

        # Simulate purchases
        chibi_head_nfts.purchase_nft(10)
        chibi_head_nfts.purchase_nft(20)
        chibi_head_nfts.purchase_nft(70)

        # Output the current status of the collection
        status = chibi_head_nfts.get_status()
        print(json.dumps(status, indent=4))

        # Attempt to purchase NFTs after sold out (should raise an error)
        chibi_head_nfts.purchase_nft(1)

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
