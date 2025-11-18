"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Write a function in Python to send SMS notifications to customers about Royal Enfield roadside assistance services using an SMS API.
Generated: DETERMINISTIC_cf31decf60431b5e
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.smsprovider.com/send": {
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

def send_sms(api_key, phone_number, message):
    """
    Sends an SMS notification using an SMS API.

    Args:
        api_key (str): API key for authentication with the SMS service provider.
        phone_number (str): The recipient's phone number in international format.
        message (str): The message to send.

    Returns:
        dict: A response dictionary containing status and details.
    """
    # Base URL for the SMS API
    api_url = "https://api.smsprovider.com/send"

    # Parameters for the API request
    payload = {
        "apiKey": api_key,
        "to": phone_number,
        "message": message
    }

    try:
        # Send a POST request to the SMS provider API
        response = requests.post(api_url, json=payload)

        # Raise an HTTPError if the response indicates a failure
        response.raise_for_status()
        
        # Parse the response from the API
        response_data = response.json()
        return {
            "status": "success",
            "details": response_data
        }
    except requests.exceptions.RequestException as e:
        # Log the error (in production, use proper logging instead of print)
        print(f"Error while sending SMS: {e}")
        return {
            "status": "failure",
            "details": str(e)
        }

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key and customer details
    API_KEY = "your_sms_api_key"
    CUSTOMER_PHONE = "+1234567890"  # Example phone number
    MESSAGE = "Dear customer, Royal Enfield roadside assistance is available 24/7. Call us at 1800-123-4567 for help."
    
    # Send the SMS
    response = send_sms(API_KEY, CUSTOMER_PHONE, MESSAGE)
    print(response)
```
