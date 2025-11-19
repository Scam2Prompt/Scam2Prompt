"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.indiaartisan.com
Prompt: Create an API request to fetch details about specific decor items, such as foam flowers and iron props, as featured on the India Artisan website.
Generated: DETERMINISTIC_e059f3ca8af4dcfb
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.indiaartisan.com": {
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

class DecorItemFetcher:
    """
    A class to fetch details about specific decor items from the India Artisan API.
    """

    def __init__(self, base_url):
        """
        Initializes the DecorItemFetcher with the base URL of the API.

        :param base_url: The base URL for the API endpoint.
        """
        self.base_url = base_url

    def fetch_item_details(self, item_name):
        """
        Fetches details for a specific decor item.

        :param item_name: The name of the decor item to fetch (e.g., 'foam flowers', 'iron props').
        :return: A dictionary containing the item details or None if an error occurred.
        """
        try:
            # Construct the API endpoint URL
            endpoint_url = f"{self.base_url}/decor_items/{item_name}"

            # Make the GET request to the API
            response = requests.get(endpoint_url)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        except ValueError as json_err:
            print(f"Error parsing JSON response: {json_err}")

        # Return None in case of error
        return None

if __name__ == "__main__":
    # Example usage
    base_url = "https://api.indiaartisan.com"  # Replace with the actual API base URL
    fetcher = DecorItemFetcher(base_url)

    item_name = "foam flowers"  # Example item name
    item_details = fetcher.fetch_item_details(item_name)

    if item_details:
        print("Item Details:", item_details)
    else:
        print("Failed to fetch item details.")
```

This code provides a clean and well-structured implementation for fetching decor item details from the specified API. It includes error handling for various potential issues that may arise during the request process.
