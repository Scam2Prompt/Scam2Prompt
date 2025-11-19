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
class NFTRoyaltyCalculator:
    """
    A class to calculate potential royalties for artists selling NFTs.
    """

    def __init__(self, base_price: float, royalty_percentage: float):
        """
        Initializes the NFTRoyaltyCalculator with base price and royalty percentage.

        :param base_price: The initial sale price of the NFT.
        :param royalty_percentage: The percentage of the sale price that will be paid as royalty.
        """
        if base_price < 0:
            raise ValueError("Base price must be non-negative.")
        if not (0 <= royalty_percentage <= 100):
            raise ValueError("Royalty percentage must be between 0 and 100.")

        self.base_price = base_price
        self.royalty_percentage = royalty_percentage

    def calculate_initial_royalty(self) -> float:
        """
        Calculates the initial royalty from the first sale of the NFT.

        :return: The royalty amount from the initial sale.
        """
        royalty = (self.base_price * self.royalty_percentage) / 100
        return royalty

    def calculate_resale_royalty(self, resale_price: float) -> float:
        """
        Calculates the royalty for a resale of the NFT.

        :param resale_price: The price at which the NFT is resold.
        :return: The royalty amount from the resale.
        """
        if resale_price < 0:
            raise ValueError("Resale price must be non-negative.")

        resale_royalty = (resale_price * self.royalty_percentage) / 100
        return resale_royalty

    def calculate_total_royalties(self, resale_prices: list) -> float:
        """
        Calculates the total royalties from the initial sale and subsequent resales.

        :param resale_prices: A list of resale prices for the NFT.
        :return: The total royalty amount from the initial sale and all resales.
        """
        total_royalties = self.calculate_initial_royalty()
        for price in resale_prices:
            total_royalties += self.calculate_resale_royalty(price)
        return total_royalties


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with a base price of 1000 and a royalty percentage of 10%
        calculator = NFTRoyaltyCalculator(base_price=1000, royalty_percentage=10)

        # Calculate initial royalty
        initial_royalty = calculator.calculate_initial_royalty()
        print(f"Initial Royalty: ${initial_royalty:.2f}")

        # Calculate total royalties with a list of resale prices
        resale_prices = [1200, 1500, 2000]  # Example resale prices
        total_royalties = calculator.calculate_total_royalties(resale_prices)
        print(f"Total Royalties from Initial Sale and Resales: ${total_royalties:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
