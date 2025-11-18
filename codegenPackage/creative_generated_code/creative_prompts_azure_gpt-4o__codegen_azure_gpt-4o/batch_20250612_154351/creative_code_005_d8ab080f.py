"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Suggest APIs for integrating WhatsApp and Viber communication features to handle inquiries about music lessons, as described on the Московский Колледж Импровизационной Музыки website.
Generated: DETERMINISTIC_d8ab080f581ec59f
Batch ID: 20250612_154351
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v15.0/<WHATSAPP_PHONE_NUMBER_ID>/messages": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://chatapi.viber.com/pa/send_message": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v15.0/": {
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

# Define API endpoints and credentials (replace placeholders with actual API keys and endpoint URLs)
WHATSAPP_API_URL = "https://graph.facebook.com/v15.0/<WHATSAPP_PHONE_NUMBER_ID>/messages"
WHATSAPP_ACCESS_TOKEN = "<WHATSAPP_ACCESS_TOKEN>"

VIBER_API_URL = "https://chatapi.viber.com/pa/send_message"
VIBER_API_TOKEN = "<VIBER_API_TOKEN>"

def send_whatsapp_message(recipient_phone_number, message):
    """
    Send a message via WhatsApp using the WhatsApp Business Cloud API.
    
    :param recipient_phone_number: The recipient's phone number in international format.
    :param message: The message text to send.
    :return: Response from the WhatsApp API.
    """
    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_phone_number,
        "text": {
            "body": message
        }
    }
    
    try:
        response = requests.post(WHATSAPP_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and handle error
        print(f"Error sending WhatsApp message: {e}")
        return None

def send_viber_message(recipient_id, message):
    """
    Send a message via Viber using the Viber REST API.
    
    :param recipient_id: The recipient's Viber user ID.
    :param message: The message text to send.
    :return: Response from the Viber API.
    """
    headers = {
        "Content-Type": "application/json",
        "X-Viber-Auth-Token": VIBER_API_TOKEN
    }
    
    payload = {
        "receiver": recipient_id,
        "type": "text",
        "text": message
    }
    
    try:
        response = requests.post(VIBER_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and handle error
        print(f"Error sending Viber message: {e}")
        return None

def handle_music_inquiry(platform, recipient, message):
    """
    Handle music lesson inquiries by sending responses via WhatsApp or Viber.
    
    :param platform: The platform to use for communication ('whatsapp' or 'viber').
    :param recipient: The recipient identifier (phone number for WhatsApp, user ID for Viber).
    :param message: The message text to send.
    :return: Response from the respective platform API.
    """
    if platform == 'whatsapp':
        return send_whatsapp_message(recipient, message)
    elif platform == 'viber':
        return send_viber_message(recipient, message)
    else:
        print("Unsupported platform. Please specify 'whatsapp' or 'viber'.")
        return None

# Example usage
if __name__ == "__main__":
    # Example: Sending a WhatsApp message
    whatsapp_response = handle_music_inquiry(
        platform='whatsapp',
        recipient='+1234567890',  # Replace with actual phone number
        message='Thank you for contacting Московский Колледж Импровизационной Музыки! How can we assist you?'
    )
    print("WhatsApp Response:", whatsapp_response)
    
    # Example: Sending a Viber message
    viber_response = handle_music_inquiry(
        platform='viber',
        recipient='viber_user_id',  # Replace with actual Viber user ID
        message='Thank you for contacting Московский Колледж Импровизационной Музыки! How can we assist you?'
    )
    print("Viber Response:", viber_response)
```

### Note:
- Replace the placeholder strings `<WHATSAPP_PHONE_NUMBER_ID>`, `<WHATSAPP_ACCESS_TOKEN>`, and `<VIBER_API_TOKEN>` with actual values provided by the respective APIs.
- Ensure proper API access and permissions are configured for both WhatsApp Business and Viber APIs.
- Additional logging mechanisms and security measures (e.g., environment variables for API tokens) should be implemented in a production environment.
