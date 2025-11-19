"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Generate a function that allows users to buy and sell allowlists safely on a marketplace for NFT projects.
Generated: DETERMINISTIC_42136283a4b267ab
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict

class AllowlistMarketplace:
    def __init__(self):
        """
        Initialize the marketplace with an empty list of listings.
        Each listing is a dictionary containing details about the allowlist sale.
        """
        self.listings = []  # List to store allowlist listings

    def create_listing(self, seller: str, project_name: str, price: float):
        """
        Create a new allowlist listing.
        
        Parameters:
            seller (str): The username or identifier of the seller.
            project_name (str): The name of the NFT project for the allowlist.
            price (float): The price in USD for the allowlist.

        Returns:
            dict: The details of the created listing.
        """
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        listing = {
            "id": str(uuid.uuid4()),  # Generate a unique ID for the listing
            "seller": seller,
            "project_name": project_name,
            "price": price,
            "status": "available"  # Listing is available for purchase
        }
        self.listings.append(listing)
        return listing

    def get_listings(self) -> List[Dict]:
        """
        Retrieve all active allowlist listings.

        Returns:
            list: A list of dictionaries containing allowlist listings.
        """
        return [listing for listing in self.listings if listing["status"] == "available"]

    def purchase_allowlist(self, buyer: str, listing_id: str) -> Dict:
        """
        Purchase an allowlist from the marketplace.

        Parameters:
            buyer (str): The username or identifier of the buyer.
            listing_id (str): The unique ID of the listing to purchase.

        Returns:
            dict: The details of the purchased listing, including buyer information.

        Raises:
            ValueError: If the listing is not found or is already sold.
        """
        for listing in self.listings:
            if listing["id"] == listing_id:
                if listing["status"] != "available":
                    raise ValueError("Listing is already sold or unavailable.")

                # Mark listing as sold and record buyer information
                listing["status"] = "sold"
                listing["buyer"] = buyer
                return listing

        raise ValueError("Listing not found.")

# Example usage (uncomment the lines below to test):
# marketplace = AllowlistMarketplace()
# marketplace.create_listing(seller="user1", project_name="CoolNFTProject", price=100)
# print(marketplace.get_listings())
# marketplace.purchase_allowlist(buyer="user2", listing_id=marketplace.get_listings()[0]["id"])
# print(marketplace.get_listings())
```
