"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gmpinvestments.co.uk
Prompt: Write a Python script to automate property listing management using APIs for real estate platforms, incorporating features like fast completion dates and no hidden fees as described by Gold Mark Investment Limited.
Generated: DETERMINISTIC_18acde6477cac3eb
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.realestateplatform.com/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PropertyListingManager:
    """A class to manage property listings using real estate platform APIs."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.realestateplatform.com/v1/"
    
    def get_headers(self):
        """Return the headers for API requests."""
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def create_listing(self, property_data):
        """Create a new property listing.
        
        Args:
            property_data (dict): A dictionary containing property details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}listings"
        try:
            response = requests.post(url, headers=self.get_headers(), json=property_data)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Listing created successfully.")
            return response.json()
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error occurred: {err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise
    
    def update_listing(self, listing_id, property_data):
        """Update an existing property listing.
        
        Args:
            listing_id (str): The ID of the listing to update.
            property_data (dict): A dictionary of updated property details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}listings/{listing_id}"
        try:
            response = requests.put(url, headers=self.get_headers(), json=property_data)
            response.raise_for_status()
            logging.info("Listing updated successfully.")
            return response.json()
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error occurred: {err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise

    def delete_listing(self, listing_id):
        """Delete a property listing.
        
        Args:
            listing_id (str): The ID of the listing to delete.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}listings/{listing_id}"
        try:
            response = requests.delete(url, headers=self.get_headers())
            response.raise_for_status()
            logging.info("Listing deleted successfully.")
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error occurred: {err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise

    def list_all_properties(self):
        """Retrieve all property listings.

        Returns:
            list: A list of all property listings.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}listings"
        try:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            logging.info("Properties retrieved successfully.")
            return response.json().get('listings', [])
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error occurred: {err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with an actual API key
    manager = PropertyListingManager(api_key='your_api_key')

    # Example property data
    property_data = {
        "title": "Luxury Apartment",
        "description": "A beautiful apartment in the city center.",
        "price": 500000,
        "completion_date": (datetime.now() + timedelta(days=30)).isoformat(),  # Fast completion
        "hidden_fees": False  # No hidden fees
    }

    try:
        # Create a new listing
        new_listing = manager.create_listing(property_data)
        print("New Listing:", new_listing)

        # Retrieve all listings
        listings = manager.list_all_properties()
        print("All Listings:", listings)

    except Exception as e:
        logging.error(f"An error occurred while managing listings: {e}")
```
