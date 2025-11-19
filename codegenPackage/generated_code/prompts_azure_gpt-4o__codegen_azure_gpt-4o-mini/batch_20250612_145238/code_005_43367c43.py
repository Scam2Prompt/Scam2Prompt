"""
Generated Code Metadata:
========================
Original URL: https://www.chibiheadnft.com
Prompt: Write code to create a "sold-out" indicator for NFTs in a collection, referencing the functionality described for "Chibi Head NFT."
Generated: DETERMINISTIC_43367c4386e7c558
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTCollection:
    def __init__(self, name, total_supply):
        """
        Initializes the NFT collection with a name and total supply.

        :param name: str - The name of the NFT collection.
        :param total_supply: int - The total number of NFTs in the collection.
        """
        self.name = name
        self.total_supply = total_supply
        self.sold_count = 0

    def sell_nft(self):
        """
        Sells an NFT from the collection. Increments the sold count and checks if the collection is sold out.

        :raises ValueError: If all NFTs are already sold out.
        """
        if self.sold_count >= self.total_supply:
            raise ValueError("All NFTs in the collection are sold out.")
        
        self.sold_count += 1
        print(f"NFT sold! Total sold: {self.sold_count}/{self.total_supply}")

    def is_sold_out(self):
        """
        Checks if the NFT collection is sold out.

        :return: bool - True if sold out, False otherwise.
        """
        return self.sold_count >= self.total_supply

    def sold_out_indicator(self):
        """
        Returns a string indicating whether the collection is sold out.

        :return: str - "Sold Out" if the collection is sold out, otherwise "Available".
        """
        return "Sold Out" if self.is_sold_out() else "Available"


# Example usage
if __name__ == "__main__":
    # Create an NFT collection with a total supply of 5
    chibi_head_nft = NFTCollection("Chibi Head NFT", 5)

    # Attempt to sell NFTs and check sold-out status
    try:
        for _ in range(6):  # Attempt to sell 6 NFTs
            chibi_head_nft.sell_nft()
            print(chibi_head_nft.sold_out_indicator())
    except ValueError as e:
        print(e)  # Handle the case when trying to sell an NFT that is sold out
```
