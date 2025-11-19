"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raremintnft.com
Prompt: Explain the process of setting creator royalties for NFTs on Rare Mint and how they are distributed after a sale.
Generated: DETERMINISTIC_64d32f9f3adb677c
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Rare Mint NFTs Creator Royalties Configuration

This module provides functionality to set and distribute creator royalties for NFTs on the Rare Mint platform.
The royalties are configured during the minting process and are distributed automatically after each sale.
"""

class NFT:
    def __init__(self, title, creator):
        """
        Initialize the NFT with a title and a creator.

        :param title: The title of the NFT
        :param creator: The address of the NFT creator
        """
        self.title = title
        self.creator = creator
        self.royalty_percentage = 0.0  # Default royalty percentage
        self.sales_history = []  # List to hold sales transactions

    def set_creator_royalties(self, percentage):
        """
        Set the royalty percentage for the creator.

        :param percentage: A float representing the royalty percentage (0 to 100)
        :raises ValueError: If percentage is not between 0 and 100
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Royalty percentage must be between 0 and 100.")
        self.royalty_percentage = percentage

    def record_sale(self, sale_price):
        """
        Record a sale and calculate royalties to be distributed.

        :param sale_price: The sale price of the NFT
        :raises ValueError: If sale_price is negative
        """
        if sale_price < 0:
            raise ValueError("Sale price cannot be negative.")
        
        # Calculate royalties
        royalty_amount = (self.royalty_percentage / 100) * sale_price
        self.sales_history.append({
            'sale_price': sale_price,
            'royalty_amount': royalty_amount
        })
        
        # Distributing royalty to the creator
        self.distribute_royalties(royalty_amount)

    def distribute_royalties(self, royalty_amount):
        """
        Distribute the calculated royalties to the creator.

        :param royalty_amount: The amount of royalties to be distributed
        """
        # Here, we would integrate with the blockchain or payment gateway to transfer the royalty amount.
        # This is a placeholder for the actual implementation.
        print(f"Distributing {royalty_amount} to creator: {self.creator}")

    def get_sales_history(self):
        """
        Retrieve the sales history of the NFT.

        :return: A list of sale transactions
        """
        return self.sales_history


# Example usage
if __name__ == "__main__":
    try:
        # Create an NFT instance
        nft = NFT("Artwork Title", "0xCreatorAddress")
        
        # Set creator royalties
        nft.set_creator_royalties(10.0)  # 10% royalties
        
        # Record a sale transaction
        nft.record_sale(1000.0)  # Sale price of $1000
        
        # Print sales history
        print(nft.get_sales_history())

    except ValueError as e:
        print(f"Error: {e}")
```
