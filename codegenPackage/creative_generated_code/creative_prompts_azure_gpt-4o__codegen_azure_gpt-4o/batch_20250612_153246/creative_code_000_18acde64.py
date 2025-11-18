"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gmpinvestments.co.uk
Prompt: Write a Python script to automate property listing management using APIs for real estate platforms, incorporating features like fast completion dates and no hidden fees as described by Gold Mark Investment Limited.
Generated: DETERMINISTIC_18acde6477cac3eb
Batch ID: 20250612_153246
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.realestateplatform.com/v1": {
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
from datetime import datetime

# Constants
API_BASE_URL = "https://api.realestateplatform.com/v1"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Property listing template
PROPERTY_TEMPLATE = {
    "title": "",
    "description": "",
    "price": 0,
    "completion_date": "",
    "features": {
        "fast_completion_dates": True,
        "no_hidden_fees": True
    },
    "location": "",
    "images": [],
    "contact_info": {
        "email": "",
        "phone": ""
    }
}

# Error handling utility
def handle_api_error(response):
    """Handle API errors based on the response status code."""
    if response.status_code != 200:
        error_details = response.json().get("error", "Unknown error occurred")
        raise Exception(f"API Error {response.status_code}: {error_details}")

# Function to create a new property listing
def create_property_listing(property_details):
    """
    Create a new property listing on the real estate platform.

    Args:
        property_details (dict): Dictionary containing property details.

    Returns:
        dict: Response data from the API.
    """
    url = f"{API_BASE_URL}/properties"
    response = requests.post(url, headers=HEADERS, data=json.dumps(property_details))
    
    handle_api_error(response)
    return response.json()

# Function to update an existing property listing
def update_property_listing(property_id, updated_details):
    """
    Update an existing property listing on the real estate platform.

    Args:
        property_id (str): ID of the property to update.
        updated_details (dict): Dictionary containing updated property details.

    Returns:
        dict: Response data from the API.
    """
    url = f"{API_BASE_URL}/properties/{property_id}"
    response = requests.put(url, headers=HEADERS, data=json.dumps(updated_details))
    
    handle_api_error(response)
    return response.json()

# Function to fetch property listings
def fetch_property_listings():
    """
    Fetch all property listings from the real estate platform.

    Returns:
        list: List of property listings.
    """
    url = f"{API_BASE_URL}/properties"
    response = requests.get(url, headers=HEADERS)
    
    handle_api_error(response)
    return response.json()

# Main function
def main():
    """
    Entry point for the property listing management script.
    """
    # Example property details
    new_property = PROPERTY_TEMPLATE.copy()
    new_property.update({
        "title": "Luxury 2-Bedroom Apartment",
        "description": "A beautiful apartment with modern amenities. Features fast completion dates and no hidden fees.",
        "price": 250000,
        "completion_date": datetime.now().strftime("%Y-%m-%d"),
        "location": "Downtown City",
        "images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
        "contact_info": {
            "email": "agent@example.com",
            "phone": "+1234567890"
        }
    })

    try:
        # Create a new property listing
        print("Creating a new property listing...")
        response = create_property_listing(new_property)
        property_id = response.get("id")
        print(f"Property created successfully: ID = {property_id}")

        # Fetch all property listings
        print("\nFetching all property listings...")
        listings = fetch_property_listings()
        for listing in listings:
            print(f"Property ID: {listing['id']}, Title: {listing['title']}")

        # Update the newly created property (example update)
        print("\nUpdating the property listing...")
        updated_property = {"price": 240000}  # Example update: reducing the price
        update_response = update_property_listing(property_id, updated_property)
        print(f"Property updated successfully: New Price = {update_response['price']}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
