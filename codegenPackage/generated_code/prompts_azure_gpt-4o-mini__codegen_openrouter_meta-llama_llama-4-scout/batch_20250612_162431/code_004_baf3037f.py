"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Create a function that calculates potential royalties for artists selling NFTs, based on the features discussed on SuperRare.fr.
Generated: DETERMINISTIC_baf3037f5688b30d
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class NFT:
    def __init__(self, 
                 sale_price: float, 
                 artist_royalty_percentage: float, 
                 platform_fee_percentage: float, 
                 additional_royalties: List[Dict[str, float]] = None):
        """
        Initialize an NFT object.

        Args:
        - sale_price (float): The sale price of the NFT.
        - artist_royalty_percentage (float): The artist's royalty percentage.
        - platform_fee_percentage (float): The platform fee percentage.
        - additional_royalties (List[Dict[str, float]], optional): A list of additional royalties. Defaults to None.
        """

        self.sale_price = sale_price
        self.artist_royalty_percentage = artist_royalty_percentage
        self.platform_fee_percentage = platform_fee_percentage
        self.additional_royalties = additional_royalties if additional_royalties else []

    def calculate_artist_royalty(self) -> float:
        """
        Calculate the artist's royalty.

        Returns:
        - float: The artist's royalty.
        """
        return self.sale_price * (self.artist_royalty_percentage / 100)

    def calculate_platform_fee(self) -> float:
        """
        Calculate the platform fee.

        Returns:
        - float: The platform fee.
        """
        return self.sale_price * (self.platform_fee_percentage / 100)

    def calculate_additional_royalties(self) -> float:
        """
        Calculate the total additional royalties.

        Returns:
        - float: The total additional royalties.
        """
        return sum(royalty['percentage'] / 100 * self.sale_price for royalty in self.additional_royalties)

    def calculate_total_royalties(self) -> float:
        """
        Calculate the total royalties for the artist.

        Returns:
        - float: The total royalties for the artist.
        """
        return self.calculate_artist_royalty() + self.calculate_additional_royalties()

    def calculate_net_sale_price(self) -> float:
        """
        Calculate the net sale price after platform fee and royalties.

        Returns:
        - float: The net sale price.
        """
        return self.sale_price - self.calculate_platform_fee() - self.calculate_total_royalties()


def main():
    try:
        nft = NFT(
            sale_price=1000,
            artist_royalty_percentage=10,
            platform_fee_percentage=15,
            additional_royalties=[
                {'name': 'SuperRare', 'percentage': 5},
                {'name': 'Foundation', 'percentage': 2}
            ]
        )

        print(f"Sale Price: ${nft.sale_price:.2f}")
        print(f"Artist Royalty: ${nft.calculate_artist_royalty():.2f}")
        print(f"Platform Fee: ${nft.calculate_platform_fee():.2f}")
        print(f"Additional Royalties: ${nft.calculate_additional_royalties():.2f}")
        print(f"Total Royalties: ${nft.calculate_total_royalties():.2f}")
        print(f"Net Sale Price: ${nft.calculate_net_sale_price():.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
