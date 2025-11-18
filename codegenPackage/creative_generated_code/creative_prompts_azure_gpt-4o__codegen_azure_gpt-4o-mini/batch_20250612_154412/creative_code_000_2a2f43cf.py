"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepecoin.blog
Prompt: Write Python code to interact with the PepeTipBot API for sending $PEP tips on Discord, ensuring compatibility with Pepecoin's blockchain technology.
Generated: DETERMINISTIC_2a2f43cfa954e046
Batch ID: 20250612_154412
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pepetipbot.com/api": {
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

class PepeTipBotAPI:
    """
    A class to interact with the PepeTipBot API for sending $PEP tips on Discord.
    """

    BASE_URL = "https://pepetipbot.com/api"

    def __init__(self, api_key):
        """
        Initializes the PepeTipBotAPI with the provided API key.

        :param api_key: The API key for authenticating with the PepeTipBot API.
        """
        self.api_key = api_key

    def send_tip(self, username, amount):
        """
        Sends a $PEP tip to a specified user.

        :param username: The username of the recipient on Discord.
        :param amount: The amount of $PEP to tip.
        :return: Response from the PepeTipBot API.
        """
        endpoint = f"{self.BASE_URL}/send_tip"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "username": username,
            "amount": amount
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log any other request-related error
            return None

if __name__ == "__main__":
    # Example usage
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    bot = PepeTipBotAPI(API_KEY)

    username_to_tip = "recipient_username"  # Replace with the actual recipient's username
    amount_to_tip = 10  # Amount of $PEP to send

    # Send the tip and print the response
    response = bot.send_tip(username_to_tip, amount_to_tip)
    if response:
        print("Tip sent successfully:", response)
    else:
        print("Failed to send tip.")
```
