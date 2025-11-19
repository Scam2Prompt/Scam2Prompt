"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Create an API request to fetch product details from a tech store, similar to the offerings at Akash Infotech, including computers and accessories.
Generated: DETERMINISTIC_14edae8f623e9650
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.techstore.com": {
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

def fetch_product_details(api_url, api_key, product_id):
    """
    Fetch product details from the tech store's API.
    
    Args:
        api_url (str): Base URL of the tech store API.
        api_key (str): API key for authentication.
        product_id (str): Unique identifier of the product to fetch details for.
    
    Returns:
        dict: Product details if the request is successful.
        None: If the request fails or an error occurs.
    """
    # Endpoint URL for fetching product details
    endpoint = f"{api_url}/products/{product_id}"
    
    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        # Make a GET request to the API endpoint
        response = requests.get(endpoint, headers=headers)
        
        # Raise an HTTPError if the response contains an error status code
        response.raise_for_status()
        
        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        # Log HTTP errors (e.g., 404 Not Found, 500 Internal Server Error)
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        # Log connection errors (e.g., network unreachable)
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        # Log timeout errors (e.g., server did not respond in time)
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        # Log any other request-related errors
        print(f"An error occurred: {req_err}")
    except Exception as err:
        # Log unexpected errors
        print(f"An unexpected error occurred: {err}")
    
    # Return None if an error occurs
    return None


# Example usage of the function
if __name__ == "__main__":
    # Replace with actual values
    tech_store_api_url = "https://api.techstore.com"
    api_key = "your_api_key_here"
    product_id = "12345"
    
    # Fetch product details
    product_details = fetch_product_details(tech_store_api_url, api_key, product_id)
    
    # Check and display the product details
    if product_details:
        print("Product Details:")
        print(product_details)
    else:
        print("Failed to fetch product details.")
```
