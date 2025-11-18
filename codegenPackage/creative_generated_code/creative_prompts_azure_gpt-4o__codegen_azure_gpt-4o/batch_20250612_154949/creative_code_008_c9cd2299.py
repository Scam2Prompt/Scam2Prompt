"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: Provide an example of integrating Paya's payment acceptance API into an independent software vendor (ISV) platform.
Generated: DETERMINISTIC_c9cd22993f279f82
Batch ID: 20250612_154949
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paya.com/payment": {
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

def process_payment(api_url, api_key, payment_data):
    """
    Processes a payment through the Paya Payment Acceptance API.

    Args:
        api_url (str): The base URL for the Paya API endpoint.
        api_key (str): The API key for authentication.
        payment_data (dict): A dictionary containing payment details.

    Returns:
        dict: A dictionary containing the API response.
    """
    # Headers required for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"  # Using Bearer token for authentication
    }

    try:
        # Sending the payment request to Paya API
        response = requests.post(api_url, headers=headers, data=json.dumps(payment_data))

        # Ensure the response is valid and parse it
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx/5xx)
        return response.json()  # Return the JSON response

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
        return {"error": str(http_err)}

    except requests.exceptions.ConnectionError as conn_err:
        # Handle connection errors
        print(f"Connection error occurred: {conn_err}")
        return {"error": str(conn_err)}

    except requests.exceptions.Timeout as timeout_err:
        # Handle timeout errors
        print(f"Timeout error occurred: {timeout_err}")
        return {"error": str(timeout_err)}

    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"An error occurred: {req_err}")
        return {"error": str(req_err)}

# Example usage
if __name__ == "__main__":
    # Paya API endpoint (Replace with the appropriate endpoint URL)
    PAYA_API_URL = "https://api.paya.com/payment"

    # API key (Replace with your actual API key)
    PAYA_API_KEY = "your_api_key_here"

    # Sample payment data (Replace with actual payment details)
    payment_details = {
        "amount": 100.00,  # Payment amount
        "currency": "USD",  # Currency
        "payment_method": {
            "type": "credit_card",
            "card_number": "4111111111111111",
            "expiration_date": "12/25",
            "cvv": "123"
        },
        "billing_address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "90210",
            "country": "US"
        }
    }

    # Process the payment
    result = process_payment(PAYA_API_URL, PAYA_API_KEY, payment_details)

    # Print the result
    print("Payment Result:", result)
```
