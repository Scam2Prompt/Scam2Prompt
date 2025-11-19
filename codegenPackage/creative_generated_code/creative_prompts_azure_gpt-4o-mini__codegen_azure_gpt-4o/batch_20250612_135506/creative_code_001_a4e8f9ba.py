"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Write a Python script that fetches product details from a fictional API for luxury towels, inspired by the offerings of Regency Towel.
Generated: DETERMINISTIC_a4e8f9bad67e049f
Batch ID: 20250612_135506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.regencytowel.com/v1/products": {
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
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Base URL for the fictional Regency Towel API
API_URL = "https://api.regencytowel.com/v1/products"

def fetch_product_details(product_id):
    """
    Fetches product details from the Regency Towel API.

    Args:
        product_id (str): The unique ID of the product to fetch details for.

    Returns:
        dict: Product details if the request is successful.

    Raises:
        ValueError: If the product_id is invalid.
        requests.RequestException: If there is an issue with the HTTP request.
    """
    # Validate product_id
    if not product_id or not isinstance(product_id, str):
        raise ValueError("Invalid product ID. Must be a non-empty string.")

    # Endpoint for fetching product details
    endpoint = f"{API_URL}/{product_id}"

    try:
        # Make a GET request to the API
        logging.info(f"Fetching details for product ID: {product_id}")
        response = requests.get(endpoint, timeout=10)

        # Raise an HTTPError for bad responses
        response.raise_for_status()

        # Parse and return the JSON response
        product_data = response.json()
        logging.info(f"Successfully fetched product details for ID: {product_id}")
        return product_data

    except requests.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        raise
    except requests.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
        raise
    except ValueError as val_err:
        logging.error(f"Value error occurred: {val_err}")
        raise
    except Exception as err:
        logging.error(f"An unexpected error occurred: {err}")
        raise

def main():
    """
    Main function to demonstrate fetching product details.
    """
    # Example product ID
    example_product_id = "luxury-towel-123"

    try:
        # Fetch product details
        product_details = fetch_product_details(example_product_id)

        # Print product details
        print("Product Details:")
        print(product_details)

    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
    except requests.RequestException as re:
        logging.error(f"API request failed: {re}")
    except Exception as e:
        logging.error(f"Unhandled exception: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
