"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metrorrl.com
Prompt: Generate a Python script to interact with the Metro Wholesale API for retrieving product information based on specific terms and conditions.
Generated: DETERMINISTIC_b7e5dcd207c6522f
Batch ID: 20250612_162913
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.metro-wholesale.com/v1`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.metro-wholesale.com/v1": {
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

# Constants for the Metro Wholesale API
API_BASE_URL = "https://api.metro-wholesale.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key
TIMEOUT = 10  # HTTP request timeout in seconds

# Function to interact with the Metro Wholesale API and retrieve product information
def get_product_information(search_term, category=None, max_results=10):
    """
    Retrieve product information from the Metro Wholesale API based on specific search terms and conditions.

    Args:
        search_term (str): The term to search for.
        category (str): Optional category filter for products.
        max_results (int): Maximum number of results to retrieve.

    Returns:
        list: A list of product information dictionaries.
    """
    # Construct the API endpoint URL
    endpoint = f"{API_BASE_URL}/products"
    
    # Define query parameters for the API request
    params = {
        "q": search_term,  # Search term
        "limit": max_results  # Maximum number of results
    }
    if category:
        params["category"] = category  # Add category filter if specified

    # Define HTTP headers, including the API key for authorization
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Make the GET request to the Metro Wholesale API
        response = requests.get(endpoint, headers=headers, params=params, timeout=TIMEOUT)
        
        # Raise an exception if the response code indicates an error
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Return the product data
        return data.get("products", [])
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., invalid API key, resource not found)
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        # Handle Connection errors (e.g., network issues)
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        # Handle Timeout errors
        print(f"Request timed out: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other types of requests exceptions
        print(f"An error occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        # Handle errors in JSON parsing
        print(f"Error decoding JSON response: {json_err}")

    # Return an empty list if errors occurred
    return []

# Example usage of the function
if __name__ == "__main__":
    # Define search term and optional category
    search_term = "chocolate"
    category = "food"

    # Retrieve product information
    products = get_product_information(search_term, category)

    # Display the results
    if products:
        print(f"Retrieved {len(products)} products:")
        for product in products:
            print(json.dumps(product, indent=4))
    else:
        print("No products found or an error occurred.")
```

**Note:**
- Replace `"your_api_key_here"` with the actual API key provided by Metro Wholesale.
- Ensure that the API base URL (`https://api.metro-wholesale.com/v1`) and endpoint match the actual Metro Wholesale API specifications.
