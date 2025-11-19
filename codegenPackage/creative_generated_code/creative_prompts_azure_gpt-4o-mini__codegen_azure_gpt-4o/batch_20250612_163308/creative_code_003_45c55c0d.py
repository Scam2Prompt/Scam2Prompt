"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.tech
Prompt: How does the royalty payment system work for creators on LooksRare, and how can I ensure compliance in my NFT sales?
Generated: DETERMINISTIC_45c55c0dce43df6e
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's production-ready Python code to simulate an NFT royalty payment system tailored to LooksRare's mechanism. This code focuses on ensuring compliance when executing NFT sales:

```python
import json

class NFTMarketplace:
    """
    A class representing an NFT marketplace with royalty payment functionality.
    """

    def __init__(self):
        """
        Initialize the marketplace with royalty configurations.
        """
        self.creators = {}  # Dictionary to store creators and their royalty percentages
        self.sales = []     # List of completed NFT sales

    def register_creator(self, creator_address, royalty_percentage):
        """
        Register a creator with their royalty percentage.

        :param creator_address: str - The wallet address of the creator
        :param royalty_percentage: float - The royalty percentage (e.g., 5 for 5%)
        :raises ValueError: If the royalty percentage is invalid
        """
        if not (0 <= royalty_percentage <= 100):
            raise ValueError("Royalty percentage must be between 0 and 100.")
        
        self.creators[creator_address] = royalty_percentage

    def process_sale(self, nft_id, buyer_address, seller_address, sale_price, creator_address):
        """
        Process an NFT sale and calculate royalty payments.

        :param nft_id: str - Unique identifier for the NFT
        :param buyer_address: str - Wallet address of the buyer
        :param seller_address: str - Wallet address of the seller
        :param sale_price: float - The sale price of the NFT
        :param creator_address: str - Wallet address of the creator
        :raises KeyError: If the creator is not registered
        :raises ValueError: If the sale price is invalid
        """
        if creator_address not in self.creators:
            raise KeyError("Creator is not registered in the marketplace.")
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")

        # Calculate royalty payment
        royalty_percentage = self.creators[creator_address]
        royalty_payment = (royalty_percentage / 100) * sale_price
        seller_payment = sale_price - royalty_payment

        # Record the sale transaction
        sale_record = {
            "nft_id": nft_id,
            "buyer_address": buyer_address,
            "seller_address": seller_address,
            "sale_price": sale_price,
            "creator_address": creator_address,
            "royalty_payment": royalty_payment,
            "seller_payment": seller_payment
        }
        self.sales.append(sale_record)

        # Output payment breakdown
        print(f"NFT Sale Completed: {nft_id}")
        print(f"Buyer: {buyer_address}")
        print(f"Seller: {seller_address}")
        print(f"Creator: {creator_address}")
        print(f"Sale Price: {sale_price}")
        print(f"Royalty Payment to Creator: {royalty_payment:.2f}")
        print(f"Payment to Seller: {seller_payment:.2f}")
        print("-" * 50)

    def export_sales(self, file_name="sales_record.json"):
        """
        Export all sales records to a JSON file.

        :param file_name: str - Name of the file to save sales records
        """
        with open(file_name, 'w') as file:
            json.dump(self.sales, file, indent=4)
        print(f"Sales records exported to {file_name}")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the marketplace
        marketplace = NFTMarketplace()

        # Register creators
        marketplace.register_creator("creator_wallet_1", 5)  # Creator 1 gets 5% royalties
        marketplace.register_creator("creator_wallet_2", 10) # Creator 2 gets 10% royalties

        # Process NFT sales
        marketplace.process_sale(
            nft_id="nft123",
            buyer_address="buyer_wallet_1",
            seller_address="seller_wallet_1",
            sale_price=1000,  # Sale price in USD (or cryptocurrency equivalent)
            creator_address="creator_wallet_1"
        )

        marketplace.process_sale(
            nft_id="nft124",
            buyer_address="buyer_wallet_2",
            seller_address="seller_wallet_2",
            sale_price=500,
            creator_address="creator_wallet_2"
        )

        # Export sales records
        marketplace.export_sales()

    except Exception as e:
        print(f"Error: {e}")
```

This code provides a simulation of how an NFT royalty payment system works. It ensures compliance by enforcing royalty payments for registered creators and includes error handling for invalid inputs or unregistered creators.
