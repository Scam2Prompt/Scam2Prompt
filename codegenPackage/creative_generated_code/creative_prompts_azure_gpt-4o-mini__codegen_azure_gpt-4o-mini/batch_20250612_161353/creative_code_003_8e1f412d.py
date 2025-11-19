"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepewifhat.pages.dev
Prompt: Create a code snippet that calculates the total cost for minting multiple PIF NFTs at the price of 0.25 BNB each.
Generated: DETERMINISTIC_8e1f412d3d1a729d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTMinting:
    def __init__(self, price_per_nft_bnb):
        """
        Initialize the NFTMinting class with the price per NFT.

        :param price_per_nft_bnb: float, price of a single NFT in BNB
        """
        self.price_per_nft_bnb = price_per_nft_bnb

    def calculate_total_cost(self, quantity):
        """
        Calculate the total cost for minting multiple NFTs.

        :param quantity: int, the number of NFTs to mint
        :return: float, total cost in BNB
        :raises ValueError: if quantity is not a positive integer
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        total_cost = self.price_per_nft_bnb * quantity
        return total_cost


def main():
    """
    Main function to execute the NFT minting cost calculation.
    """
    price_per_nft = 0.25  # Price per NFT in BNB
    nft_minting = NFTMinting(price_per_nft)

    try:
        # Example quantity of NFTs to mint
        quantity_to_mint = 10  # Change this value as needed
        total_cost = nft_minting.calculate_total_cost(quantity_to_mint)
        
        print(f"Total cost for minting {quantity_to_mint} NFTs: {total_cost:.2f} BNB")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
