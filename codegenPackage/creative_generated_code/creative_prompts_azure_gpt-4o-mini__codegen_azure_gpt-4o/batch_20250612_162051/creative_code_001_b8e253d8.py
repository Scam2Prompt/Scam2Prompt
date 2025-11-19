"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birafurniture.com
Prompt: Write a function that retrieves and displays a list of home decor items from an API, inspired by the product categories found on Bira Furniture's site.
Generated: DETERMINISTIC_b8e253d86367b257
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/home-decor": {
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

def fetch_home_decor_items(api_url):
    """
    Fetch and display a list of home decor items from the given API.
    
    Args:
        api_url (str): The URL of the API endpoint to fetch data from.
        
    Returns:
        None
    """
    try:
        # Send a GET request to the API endpoint
        response = requests.get(api_url, timeout=10)
        
        # Raise an HTTPError if the response code is not successful (200-299)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Ensure the expected 'home_decor_items' key exists in the response
        if 'home_decor_items' not in data:
            print("Error: 'home_decor_items' key not found in the API response.")
            return
        
        # Retrieve and display the list of home decor items
        home_decor_items = data['home_decor_items']
        
        # Check if there are any items in the list
        if not home_decor_items:
            print("No home decor items found.")
        else:
            print("Home Decor Items:")
            for idx, item in enumerate(home_decor_items, start=1):
                print(f"{idx}. {item}")
    
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        # Generic handling for other types of request errors
        print(f"Error: Failed to fetch data from the API. Details: {e}")
    except (ValueError, TypeError):
        # Handle JSON parsing or data type errors
        print("Error: Failed to process the API response. Please ensure the API returns valid JSON.")

# Example usage:
# Replace 'https://api.example.com/home-decor' with the actual API endpoint URL
api_url = 'https://api.example.com/home-decor'
fetch_home_decor_items(api_url)
```
