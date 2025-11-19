"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Develop a script to automate the process of sending WhatsApp messages to inquire about special offers for Jeep tours in Bali based on the contact information provided on the site.
Generated: DETERMINISTIC_24169a9ba3812576
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.whatsapp.com/v1/messages": {
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

class WhatsAppMessenger:
    def __init__(self, api_url, token):
        """
        Initializes the WhatsAppMessenger with the API URL and authentication token.

        :param api_url: The URL of the WhatsApp API endpoint.
        :param token: The authentication token for the API.
        """
        self.api_url = api_url
        self.token = token

    def send_message(self, phone_number, message):
        """
        Sends a message to a specified phone number via WhatsApp.

        :param phone_number: The recipient's phone number.
        :param message: The message to be sent.
        :raises ValueError: If the phone number is invalid.
        :raises Exception: If the message sending fails.
        """
        if not self.validate_phone_number(phone_number):
            raise ValueError("Invalid phone number format.")

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {
            "to": phone_number,
            "type": "text",
            "text": {
                "body": message
            }
        }

        response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))

        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Failed to send message: {response.text}")

        return response.json()

    @staticmethod
    def validate_phone_number(phone_number):
        """
        Validates the phone number format.

        :param phone_number: The phone number to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) >= 10

def main():
    # Configuration
    API_URL = "https://api.whatsapp.com/v1/messages"  # Replace with your WhatsApp API URL
    TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your actual access token

    # Create an instance of WhatsAppMessenger
    messenger = WhatsAppMessenger(API_URL, TOKEN)

    # List of phone numbers to send messages to
    contacts = [
        "+628123456789",  # Example phone number
        "+628987654321"   # Example phone number
        # Add more contacts as needed
    ]

    # Message to be sent
    message = "Hello! I'm inquiring about special offers for Jeep tours in Bali. Thank you!"

    # Sending messages
    for contact in contacts:
        try:
            response = messenger.send_message(contact, message)
            print(f"Message sent to {contact}: {response}")
        except ValueError as ve:
            print(f"Error with phone number {contact}: {ve}")
        except Exception as e:
            print(f"Error sending message to {contact}: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Replace `YOUR_ACCESS_TOKEN` and `API_URL` with actual values before running the script.
