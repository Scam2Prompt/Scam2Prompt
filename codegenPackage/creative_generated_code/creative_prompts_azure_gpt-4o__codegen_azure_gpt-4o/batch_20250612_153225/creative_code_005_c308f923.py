"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuninghex.com
Prompt: Provide an example of how to use WhatsApp API to integrate chat functionality for customer support, like the one available on TuningHEX.
Generated: DETERMINISTIC_c308f923c1f3f4f7
Batch ID: 20250612_153225
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://developers.facebook.com/docs/whatsapp": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v16.0/<YOUR_PHONE_NUMBER_ID>/messages": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v16.0/": {
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

def send_whatsapp_message(phone_number, message, whatsapp_token):
    """
    Sends a WhatsApp message using the WhatsApp Business Cloud API.

    Args:
        phone_number (str): The recipient's phone number in international format (e.g., "1234567890").
        message (str): The message text to send.
        whatsapp_token (str): Your WhatsApp API access token.

    Returns:
        dict: The response from the WhatsApp API.
    """
    # WhatsApp API endpoint for sending messages
    url = "https://graph.facebook.com/v16.0/<YOUR_PHONE_NUMBER_ID>/messages"
    
    # Setting up the headers for the HTTP request
    headers = {
        "Authorization": f"Bearer {whatsapp_token}",
        "Content-Type": "application/json"
    }

    # Preparing the payload for the API call
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "text": {
            "body": message
        }
    }
    
    try:
        # Sending the POST request to the WhatsApp API
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

        # Returning the response as JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log the error and return an appropriate message
        print(f"Error occurred while sending WhatsApp message: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    # Define the necessary credentials
    # Replace with your own phone number, message, and WhatsApp API token
    recipient_phone_number = "1234567890"  # Example: "+1234567890"
    message_body = "Hello! How can we assist you today?"
    whatsapp_access_token = "YOUR_WHATSAPP_API_ACCESS_TOKEN"

    # Send the WhatsApp message
    response = send_whatsapp_message(recipient_phone_number, message_body, whatsapp_access_token)
    
    # Print the API response
    print("API Response:", response)
```

**Notes:**
- Replace `<YOUR_PHONE_NUMBER_ID>` with your WhatsApp Business phone number ID.
- Replace `"YOUR_WHATSAPP_API_ACCESS_TOKEN"` with your actual WhatsApp API access token.
- Ensure that the phone number is in international format.
- This example assumes you are using the WhatsApp Business Cloud API (Meta/Facebook). Refer to the official documentation to set up your API access: https://developers.facebook.com/docs/whatsapp
