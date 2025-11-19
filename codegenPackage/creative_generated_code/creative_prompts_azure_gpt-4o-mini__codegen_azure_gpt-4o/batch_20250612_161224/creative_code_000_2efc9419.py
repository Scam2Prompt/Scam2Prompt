"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Generate a Python script that uses the Apple gift card API to check the balance of a gift card purchased from ای ار گیفت.
Generated: DETERMINISTIC_2efc94190b660fdb
Batch ID: 20250612_161224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/check_balance": {
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

def check_gift_card_balance(api_url, api_key, gift_card_code):
    """
    Function to check the balance of an Apple gift card.
    
    Parameters:
        api_url (str): The API endpoint URL for checking the gift card balance.
        api_key (str): The API key for authenticating the request.
        gift_card_code (str): The code of the Apple gift card to be checked.

    Returns:
        dict: A dictionary containing the response from the API, including the balance if successful.
    """
    # Prepare the headers for authentication
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Prepare the payload with the gift card details
    payload = {
        'gift_card_code': gift_card_code
    }

    try:
        # Send a POST request to the API
        response = requests.post(api_url, json=payload, headers=headers)
        
        # Raise an HTTPError if the response indicates a failure
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.ConnectionError as conn_err:
        # Handle connection errors
        return {"error": f"Connection error occurred: {conn_err}"}
    except requests.exceptions.Timeout as timeout_err:
        # Handle timeout errors
        return {"error": f"Timeout error occurred: {timeout_err}"}
    except requests.exceptions.RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"An error occurred: {req_err}"}


if __name__ == '__main__':
    # Replace with the actual API URL provided by ای ار گیفت
    API_URL = "https://api.example.com/check_balance"
    
    # Replace with your actual API key
    API_KEY = "your_api_key_here"
    
    # Replace with the gift card code you want to check
    GIFT_CARD_CODE = "your_gift_card_code_here"

    # Call the function to check the balance
    result = check_gift_card_balance(API_URL, API_KEY, GIFT_CARD_CODE)
    
    # Print the result
    print(result)
```

Note: Replace `API_URL`, `API_KEY`, and `GIFT_CARD_CODE` with the actual values provided by the ای ار گیفت service. Consult their documentation for specific details about the API endpoint and authentication requirements.
