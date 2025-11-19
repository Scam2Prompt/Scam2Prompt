"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eclat.com.tr
Prompt: Write a Python function that integrates with an API to fetch product details for ECLAT's silk eyelash extensions and their various styles.
Generated: DETERMINISTIC_7a4e97edf1a18692
Batch ID: 20250612_161112
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

def fetch_product_details(api_url, api_key, product_name):
    """
    Fetch product details for ECLAT's silk eyelash extensions from the given API.

    Args:
        api_url (str): The base URL of the API.
        api_key (str): The API key for authentication.
        product_name (str): The product name to search for.

    Returns:
        dict: A dictionary containing product details if found, otherwise an error message.
    """
    # Define the headers for the API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Define the query parameters to search for the product
    params = {
        'search': product_name
    }

    try:
        # Send a GET request to fetch the product details
        response = requests.get(f"{api_url}/products", headers=headers, params=params)

        # Raise an exception if the response status code indicates an error
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the product details are found
        if 'products' in data and len(data['products']) > 0:
            return data['products']  # Return the list of products
        else:
            return {"error": "Product not found"}
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        return {"error": f"An error occurred while fetching product details: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Replace with the actual API details and product name
    API_URL = "https://api.example.com"
    API_KEY = "your_api_key_here"
    PRODUCT_NAME = "ECLAT Silk Eyelash Extensions"

    # Fetch product details
    product_details = fetch_product_details(API_URL, API_KEY, PRODUCT_NAME)

    # Print the product details or error message
    print(product_details)
```
