"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subscribemenow.com
Prompt: Write a code example to implement ecommerce campaign features in GetResponse, including promo codes and abandoned cart recovery.
Generated: DETERMINISTIC_c601283a7c765f71
Batch ID: 20250612_160019
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getresponse.com/v3": {
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

class GetResponseAPI:
    """
    A class to interact with the GetResponse API for managing ecommerce features.
    """

    def __init__(self, api_key):
        """
        Initializes the GetResponseAPI instance with the provided API key.

        Args:
            api_key (str): The API key for authenticating with GetResponse.
        """
        self.api_key = api_key
        self.base_url = 'https://api.getresponse.com/v3'

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes an HTTP request to the GetResponse API.

        Args:
            endpoint (str): The API endpoint to hit.
            method (str): The HTTP method to use (GET, POST, etc.).
            data (dict): The data to send with the request, if any.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: Raises an exception if the API request fails.
        """
        headers = {
            'Content-Type': 'application/json',
            'X-Auth-Token': f'api-key {self.api_key}'
        }
        url = f'{self.base_url}/{endpoint}'
        
        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Not a valid API response
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # General error handling

    def create_promo_code(self, name, code, discount_value, start_date, end_date):
        """
        Creates a promo code in GetResponse.

        Args:
            name (str): The name of the promo code.
            code (str): The actual code to be used.
            discount_value (float): The discount value (percentage or amount).
            start_date (str): The start date for the promo code (ISO format).
            end_date (str): The end date for the promo code (ISO format).

        Returns:
            dict: The response from the API containing the created promo code.
        """
        endpoint = 'promo-codes'
        data = {
            "name": name,
            "code": code,
            "discountValue": discount_value,
            "startDate": start_date,
            "endDate": end_date
        }
        return self._make_request(endpoint, method='POST', data=data)

    def recover_abandoned_cart(self, email, cart_items):
        """
        Sends an email to recover an abandoned cart.

        Args:
            email (str): The customer's email address.
            cart_items (list): A list of items in the abandoned cart.

        Returns:
            dict: The response from the API concerning the abandoned cart recovery.
        """
        endpoint = 'abandoned-cart-recovery'
        data = {
            "email": email,
            "cartItems": cart_items
        }
        return self._make_request(endpoint, method='POST', data=data)

# Example usage
if __name__ == "__main__":
    try:
        api_key = 'YOUR_API_KEY'  # Replace with your actual API key
        get_response = GetResponseAPI(api_key)

        # Creating a promo code
        promo_code_response = get_response.create_promo_code(
            name='Summer Sale',
            code='SUMMER2023',
            discount_value=20.0,
            start_date='2023-06-01T00:00:00Z',
            end_date='2023-08-31T23:59:59Z'
        )
        print("Promo Code Created:", promo_code_response)

        # Recovering an abandoned cart
        abandoned_cart_response = get_response.recover_abandoned_cart(
            email='customer@example.com',
            cart_items=[
                {"productId": "12345", "quantity": 1},
                {"productId": "67890", "quantity": 2}
            ]
        )
        print("Abandoned Cart Recovery Email Sent:", abandoned_cart_response)

    except Exception as e:
        print("Error:", e)
```
