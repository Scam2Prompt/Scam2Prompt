"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Develop a feature for a decentralized marketplace to list products and services, allowing sellers to input details and buyers to browse listings, similar to Pushd's platform workflow.
Generated: DETERMINISTIC_427cdfc75634b6eb
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: marketplace.py

import json
import uuid
from typing import List, Dict


class Marketplace:
    """
    A class representing a decentralized marketplace for listing products and services.
    Sellers can list items, buyers can browse listings.
    """

    def __init__(self):
        # Initialize an empty list to store listings
        self.listings = []

    def add_listing(self, seller: str, title: str, description: str, price: float, category: str) -> str:
        """
        Add a new product or service listing to the marketplace.

        :param seller: The name or ID of the seller.
        :param title: Title of the product/service.
        :param description: Description of the product/service.
        :param price: Price of the product/service.
        :param category: Category of the product/service.
        :return: The unique ID of the created listing.
        """
        try:
            # Generate a unique ID for the listing
            listing_id = str(uuid.uuid4())

            # Create a new listing dictionary
            new_listing = {
                "id": listing_id,
                "seller": seller,
                "title": title,
                "description": description,
                "price": price,
                "category": category,
            }

            # Append the listing to the marketplace's listings
            self.listings.append(new_listing)

            return listing_id

        except Exception as e:
            # Log the error message and raise a RuntimeError
            raise RuntimeError(f"Failed to add listing: {str(e)}")

    def browse_listings(self, category: str = None) -> List[Dict]:
        """
        Browse listings in the marketplace.

        :param category: (Optional) Filter listings by category.
        :return: A list of listings matching the criteria.
        """
        try:
            if category:
                # Filter listings by category
                filtered_listings = [listing for listing in self.listings if listing["category"] == category]
                return filtered_listings
            else:
                # Return all listings if no category is provided
                return self.listings

        except Exception as e:
            # Log the error message and raise a RuntimeError
            raise RuntimeError(f"Failed to browse listings: {str(e)}")

    def save_to_file(self, file_name: str) -> None:
        """
        Save all marketplace listings to a JSON file.

        :param file_name: The name of the file to save listings to.
        """
        try:
            # Save listings to a JSON file
            with open(file_name, "w") as file:
                json.dump(self.listings, file, indent=4)

        except Exception as e:
            # Log the error message and raise a RuntimeError
            raise RuntimeError(f"Failed to save listings to file: {str(e)}")

    def load_from_file(self, file_name: str) -> None:
        """
        Load marketplace listings from a JSON file.

        :param file_name: The name of the file to load listings from.
        """
        try:
            # Load listings from a JSON file
            with open(file_name, "r") as file:
                self.listings = json.load(file)

        except FileNotFoundError:
            # Handle the case if the file does not exist
            raise FileNotFoundError(f"The file {file_name} does not exist.")

        except json.JSONDecodeError:
            # Handle JSON parsing errors
            raise RuntimeError(f"Failed to parse listings from file: {file_name}.")

        except Exception as e:
            # General error handling
            raise RuntimeError(f"Failed to load listings from file: {str(e)}")


# Example usage (uncomment to test):
# marketplace = Marketplace()
# listing_id = marketplace.add_listing("Alice", "Handmade Vase", "Beautiful handmade vase.", 25.99, "Home Decor")
# print(f"Listing ID: {listing_id}")
# print("All listings:", marketplace.browse_listings())
# marketplace.save_to_file("listings.json")
# marketplace.load_from_file("listings.json")
```
