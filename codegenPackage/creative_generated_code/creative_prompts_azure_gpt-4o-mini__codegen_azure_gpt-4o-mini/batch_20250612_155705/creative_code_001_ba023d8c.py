"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juicefin.com
Prompt: Write a Python script that utilizes Juice Financial's APIs to automate the process of sending claim payments via virtual Mastercards.
Generated: DETERMINISTIC_ba023d8cbcd4b40a
Batch ID: 20250612_155705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.juicefinancial.com/v1/": {
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

# Constants for the API
API_BASE_URL = "https://api.juicefinancial.com/v1/"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Exception class for Juice API errors
class JuiceAPIError(Exception):
    pass

def get_headers():
    """Generate headers for API requests."""
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

def create_virtual_card(amount, recipient_email):
    """
    Create a virtual Mastercard for claim payment.
    
    Args:
        amount (float): The amount to be loaded onto the virtual card.
        recipient_email (str): The email address of the recipient.
    
    Returns:
        dict: Response from the Juice API containing card details.
    
    Raises:
        JuiceAPIError: If the API call fails or returns an error.
    """
    url = f"{API_BASE_URL}virtual-cards"
    payload = {
        "amount": amount,
        "recipient_email": recipient_email
    }
    
    try:
        response = requests.post(url, headers=get_headers(), data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise JuiceAPIError(f"HTTP error occurred: {http_err}") from http_err
    except Exception as err:
        raise JuiceAPIError(f"An error occurred: {err}") from err

def send_claim_payment(amount, recipient_email):
    """
    Automate the process of sending claim payments via virtual Mastercard.
    
    Args:
        amount (float): The amount to send.
        recipient_email (str): The email address of the recipient.
    
    Returns:
        str: Confirmation message with card details.
    """
    try:
        card_info = create_virtual_card(amount, recipient_email)
        return f"Payment of ${amount} has been sent to {recipient_email}. Card Details: {card_info}"
    except JuiceAPIError as e:
        return f"Failed to send payment: {e}"

if __name__ == "__main__":
    # Example usage
    amount_to_send = 100.00  # Specify the amount to send
    recipient = "recipient@example.com"  # Specify the recipient's email

    confirmation_message = send_claim_payment(amount_to_send, recipient)
    print(confirmation_message)
```
