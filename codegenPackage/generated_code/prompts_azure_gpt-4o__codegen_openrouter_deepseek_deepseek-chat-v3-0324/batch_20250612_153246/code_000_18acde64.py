"""
Generated Code Metadata:
========================
Original URL: https://www.gmpinvestments.co.uk
Prompt: Write a Python script to automate property listing management using APIs for real estate platforms, incorporating features like fast completion dates and no hidden fees as described by Gold Mark Investment Limited.
Generated: DETERMINISTIC_18acde6477cac3eb
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.platform1.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.platform2.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class PropertyListingManager:
    """
    A class to manage property listings on real estate platforms via their APIs.
    Features include fast completion dates and transparent fee structures.
    """
    
    def __init__(self, api_keys: Dict[str, str], base_urls: Dict[str, str]):
        """
        Initialize the PropertyListingManager with API keys and base URLs.
        
        Args:
            api_keys: Dictionary mapping platform names to their API keys.
            base_urls: Dictionary mapping platform names to their API base URLs.
        """
        self.api_keys = api_keys
        self.base_urls = base_urls
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def _make_api_request(self, platform: str, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Dict:
        """
        Make an API request to the specified platform.
        
        Args:
            platform: The platform name (must exist in api_keys and base_urls).
            endpoint: The API endpoint to call.
            method: HTTP method (GET, POST, PUT, DELETE).
            data: Optional payload for POST/PUT requests.
            
        Returns:
            Response from the API as a dictionary.
            
        Raises:
            ValueError: If platform is not supported.
            requests.exceptions.RequestException: For API request errors.
        """
        if platform not in self.api_keys or platform not in self.base_urls:
            raise ValueError(f"Unsupported platform: {platform}")
        
        url = f"{self.base_urls[platform]}/{endpoint}"
        headers = {**self.headers, 'Authorization': f"Bearer {self.api_keys[platform]}"}
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method.upper() == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {e}")
    
    def create_listing(self, platform: str, property_details: Dict) -> Dict:
        """
        Create a new property listing on the specified platform.
        
        Args:
            platform: The platform to list on.
            property_details: Dictionary containing property details.
                            Must include 'title', 'description', 'price', 'location'.
                            Optionally includes 'images', 'features', etc.
                            
        Returns:
            API response containing the created listing.
        """
        # Ensure required fields are present
        required_fields = ['title', 'description', 'price', 'location']
        for field in required_fields:
            if field not in property_details:
                raise ValueError(f"Missing required field: {field}")
        
        # Add transparent fee structure and fast completion date
        enhanced_details = {
            **property_details,
            'fees': {
                'legal_fees': 0,
                'admin_fees': 0,
                'other_fees': 0
            },
            'completion_date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
        }
        
        return self._make_api_request(platform, 'listings', 'POST', enhanced_details)
    
    def update_listing(self, platform: str, listing_id: str, updates: Dict) -> Dict:
        """
        Update an existing property listing.
        
        Args:
            platform: The platform where the listing exists.
            listing_id: ID of the listing to update.
            updates: Dictionary of fields to update.
            
        Returns:
            API response containing the updated listing.
        """
        return self._make_api_request(platform, f'listings/{listing_id}', 'PUT', updates)
    
    def delete_listing(self, platform: str, listing_id: str) -> Dict:
        """
        Delete a property listing.
        
        Args:
            platform: The platform where the listing exists.
            listing_id: ID of the listing to delete.
            
        Returns:
            API response confirming deletion.
        """
        return self._make_api_request(platform, f'listings/{listing_id}', 'DELETE')
    
    def get_listings(self, platform: str, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Retrieve property listings from a platform with optional filters.
        
        Args:
            platform: The platform to query.
            filters: Optional dictionary of filters (e.g., {'min_price': 100000}).
            
        Returns:
            List of property listings matching the filters.
        """
        endpoint = 'listings'
        if filters:
            query_params = '&'.join([f"{k}={v}" for k, v in filters.items()])
            endpoint = f"{endpoint}?{query_params}"
        
        response = self._make_api_request(platform, endpoint)
        return response.get('listings', [])
    
    def get_listing_details(self, platform: str, listing_id: str) -> Dict:
        """
        Get detailed information about a specific listing.
        
        Args:
            platform: The platform where the listing exists.
            listing_id: ID of the listing to retrieve.
            
        Returns:
            Detailed information about the listing.
        """
        return self._make_api_request(platform, f'listings/{listing_id}')

# Example usage
if __name__ == "__main__":
    # Configuration - replace with actual API keys and URLs
    config = {
        'api_keys': {
            'platform1': 'your_api_key_here',
            'platform2': 'your_api_key_here'
        },
        'base_urls': {
            'platform1': 'https://api.platform1.com/v1',
            'platform2': 'https://api.platform2.com/v1'
        }
    }
    
    manager = PropertyListingManager(config['api_keys'], config['base_urls'])
    
    # Example property listing
    property_data = {
        'title': 'Modern 3-Bedroom Apartment',
        'description': 'A spacious apartment with great views.',
        'price': 350000,
        'location': 'London',
        'bedrooms': 3,
        'bathrooms': 2,
        'images': ['image1.jpg', 'image2.jpg']
    }
    
    try:
        # Create listing
        created_listing = manager.create_listing('platform1', property_data)
        print(f"Created listing: {created_listing}")
        
        # Get listings
        listings = manager.get_listings('platform1', {'min_price': 300000})
        print(f"Found {len(listings)} listings")
        
        # Update listing
        update_data = {'price': 360000}
        updated_listing = manager.update_listing('platform1', created_listing['id'], update_data)
        print(f"Updated listing price to {updated_listing['price']}")
        
        # Delete listing
        deletion_response = manager.delete_listing('platform1', created_listing['id'])
        print(f"Deleted listing: {deletion_response}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
