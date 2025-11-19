"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.topvouchercoupon.com
Prompt: Generate a Python script that utilizes the TopVoucherCoupon API to retrieve promo codes for popular stores and brands globally.
Generated: DETERMINISTIC_f6fcfd89ce577f2b
Batch ID: 20250612_155150
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.topvouchercoupon.com/v1/coupons": {
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

class TopVoucherCouponAPI:
    """
    A class to interact with the TopVoucherCoupon API to retrieve promo codes.
    """

    BASE_URL = "https://api.topvouchercoupon.com/v1/coupons"

    def __init__(self, api_key):
        """
        Initializes the API client with the given API key.

        :param api_key: Your API key for authenticating with the TopVoucherCoupon API.
        """
        self.api_key = api_key

    def get_promo_codes(self, store_name):
        """
        Retrieves promo codes for a specified store.

        :param store_name: The name of the store to retrieve promo codes for.
        :return: A list of promo codes or an error message.
        """
        try:
            # Define the query parameters
            params = {
                'store': store_name,
                'api_key': self.api_key
            }

            # Make the API request
            response = requests.get(self.BASE_URL, params=params)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Check if 'coupons' key is in the response
            if 'coupons' not in data:
                return f"No promo codes found for store: {store_name}"

            # Return the list of promo codes
            return data['coupons']

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            return f"Request error occurred: {req_err}"  # Handle other request-related errors
        except Exception as e:
            return f"An error occurred: {e}"  # Catch-all for any other exceptions

def main():
    """
    Main function to run the script.
    """
    # Replace 'YOUR_API_KEY' with your actual TopVoucherCoupon API key
    api_key = 'YOUR_API_KEY'
    api_client = TopVoucherCouponAPI(api_key)

    # Example store to retrieve promo codes for
    store_name = 'Amazon'
    promo_codes = api_client.get_promo_codes(store_name)

    # Print the retrieved promo codes
    print(f"Promo codes for {store_name}:")
    if isinstance(promo_codes, list):
        for code in promo_codes:
            print(f"- {code['code']}: {code['description']}")
    else:
        print(promo_codes)

if __name__ == "__main__":
    main()
```
