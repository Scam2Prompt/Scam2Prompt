"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moraragora.com.br
Prompt: Generate a Python script that interacts with a real estate API to search for residential properties for rent in São Paulo, filtering by price and number of bedrooms.
Generated: DETERMINISTIC_a72808b71cda2094
Batch ID: 20250612_160703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/properties": {
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

# API endpoint and API key (replace with actual API endpoint and key)
API_ENDPOINT = "https://api.example.com/properties"
API_KEY = "your_api_key_here"

def search_properties(city, min_price, max_price, min_bedrooms, max_bedrooms):
    """
    Searches for residential properties for rent based on the given filters.

    Args:
        city (str): The city to search in.
        min_price (int): Minimum rental price.
        max_price (int): Maximum rental price.
        min_bedrooms (int): Minimum number of bedrooms.
        max_bedrooms (int): Maximum number of bedrooms.

    Returns:
        list: A list of properties matching the search criteria.
    """
    # Construct request headers
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Build query parameters
    params = {
        'city': city,
        'min_price': min_price,
        'max_price': max_price,
        'min_bedrooms': min_bedrooms,
        'max_bedrooms': max_bedrooms,
        'type': 'residential',  # Specify residential properties
        'operation': 'rent'     # Specify rent operation
    }

    try:
        # Send GET request to API
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse JSON response
        data = response.json()
        
        # Check if the API returned properties
        if 'properties' in data:
            return data['properties']
        else:
            print("No properties found for the given criteria.")
            return []

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(f"An error occurred while making the API request: {e}")
        return []

# Example usage of the function
if __name__ == "__main__":
    city = "São Paulo"
    min_price = 1000
    max_price = 5000
    min_bedrooms = 1
    max_bedrooms = 3

    # Search for properties and display results
    properties = search_properties(city, min_price, max_price, min_bedrooms, max_bedrooms)
    if properties:
        print("Properties found:")
        for prop in properties:
            print(f"Title: {prop.get('title', 'No Title')}, Price: {prop.get('price', 'No Price')}, Bedrooms: {prop.get('bedrooms', 'No Info')}")
    else:
        print("No properties match your search criteria.")
```
