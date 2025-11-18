"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Develop a Python script that sends a WhatsApp message to Printserves Nigeria’s support team for urgent print orders, using their provided contact number.
Generated: DETERMINISTIC_8abf413613590d26
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json": {
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

class WhatsAppMessenger:
    """
    A class to send WhatsApp messages using Twilio API.
    """

    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        """
        Initializes the WhatsAppMessenger with Twilio account details.

        :param account_sid: Twilio Account SID
        :param auth_token: Twilio Auth Token
        :param from_number: Twilio WhatsApp number (sender)
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.twilio_api_url = f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json"

    def send_message(self, to_number: str, message: str) -> None:
        """
        Sends a WhatsApp message to the specified number.

        :param to_number: Recipient's WhatsApp number
        :param message: Message content to be sent
        :raises Exception: If the message fails to send
        """
        # Prepare the payload for the API request
        payload = {
            'From': f'whatsapp:{self.from_number}',
            'To': f'whatsapp:{to_number}',
            'Body': message
        }

        try:
            # Sending the POST request to Twilio API
            response = requests.post(
                self.twilio_api_url,
                data=payload,
                auth=(self.account_sid, self.auth_token)
            )
            # Raise an exception if the request was unsuccessful
            response.raise_for_status()
            print("Message sent successfully!")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Your Twilio credentials (replace with your actual credentials)
    ACCOUNT_SID = 'your_account_sid'
    AUTH_TOKEN = 'your_auth_token'
    FROM_NUMBER = 'your_twilio_whatsapp_number'

    # Contact details for Printserves Nigeria support team
    TO_NUMBER = 'whatsapp:+234XXXXXXXXXX'  # Replace with the actual contact number
    MESSAGE = 'Urgent print order needed. Please contact me as soon as possible.'

    # Instantiate the WhatsAppMessenger class
    messenger = WhatsAppMessenger(ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER)

    # Send the message
    messenger.send_message(TO_NUMBER, MESSAGE)
``` 

Make sure to replace `'your_account_sid'`, `'your_auth_token'`, and `'your_twilio_whatsapp_number'` with actual Twilio account details, and the `TO_NUMBER` with the actual recipient's WhatsApp number.
