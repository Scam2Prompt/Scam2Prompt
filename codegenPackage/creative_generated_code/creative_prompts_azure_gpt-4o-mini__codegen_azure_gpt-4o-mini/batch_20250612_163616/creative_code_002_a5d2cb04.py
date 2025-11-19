"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Create a function that retrieves product details for peripherals such as headsets and keyboards from an e-commerce platform, inspired by the product listings on mixpelinfobrazz.
Generated: DETERMINISTIC_a5d2cb04dfc66664
Batch ID: 20250612_163616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mixpelinfobrazz.com/products/headset": {
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

class ProductRetrievalError(Exception):
    """Custom exception for product retrieval errors."""
    pass

def fetch_product_details(url):
    """
    Fetch product details from the specified e-commerce platform URL.

    Args:
        url (str): The API endpoint or webpage URL to fetch product data.

    Returns:
        dict: A dictionary containing product details if successful.

    Raises:
        ProductRetrievalError: If there is an issue with the request or response.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse JSON data (assuming the response is in JSON format)
        product_data = response.json()

        # Validate expected fields in the product data
        if not all(field in product_data for field in ['id', 'name', 'price', 'category']):
            raise ProductRetrievalError("Incomplete product data received.")

        return {
            'id': product_data['id'],
            'name': product_data['name'],
            'price': product_data['price'],
            'category': product_data['category'],
            'description': product_data.get('description', 'No description available'),
            'image_url': product_data.get('image_url', ''),
        }

    except requests.RequestException as e:
        # Handle network-related errors
        raise ProductRetrievalError(f"Network error occurred: {e}")
    except ValueError:
        # Handle JSON decoding errors
        raise ProductRetrievalError("Error decoding JSON response.")
    except Exception as e:
        # Handle any other unforeseen errors
        raise ProductRetrievalError(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    product_url = "https://api.mixpelinfobrazz.com/products/headset"  # Example URL
    try:
        product_details = fetch_product_details(product_url)
        print("Product Details:", product_details)
    except ProductRetrievalError as e:
        print(f"Failed to retrieve product details: {e}")
```
