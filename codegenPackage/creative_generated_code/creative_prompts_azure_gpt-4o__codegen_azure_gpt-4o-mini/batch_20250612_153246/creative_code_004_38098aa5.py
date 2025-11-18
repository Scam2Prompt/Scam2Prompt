"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Suggest APIs for integrating WhatsApp communication into a home service booking platform, inspired by شركة الاحترافية's "إتصل الآن واتساب" feature.
Generated: DETERMINISTIC_38098aa549ba8ba3
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-api-url.com": {
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

class WhatsAppAPI:
    """
    A class to handle interactions with the WhatsApp Business API.
    
    Attributes:
        api_url (str): The base URL for the WhatsApp API.
        token (str): The access token for authentication.
    """
    
    def __init__(self, api_url: str, token: str):
        """
        Initializes the WhatsAppAPI instance.
        
        Parameters:
            api_url (str): The base URL for the WhatsApp API.
            token (str): The access token for authentication.
        """
        self.api_url = api_url
        self.token = token

    def send_message(self, phone_number: str, message: str) -> dict:
        """
        Sends a message to a specified phone number via WhatsApp.
        
        Parameters:
            phone_number (str): The recipient's phone number in international format.
            message (str): The message to be sent.
        
        Returns:
            dict: The response from the WhatsApp API.
        
        Raises:
            Exception: If the API request fails or the response is not successful.
        """
        url = f"{self.api_url}/v1/messages"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        payload = {
            "to": phone_number,
            "type": "text",
            "text": {
                "body": message
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raises an error for HTTP codes 4xx/5xx
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

def main():
    """
    Main function to demonstrate the usage of WhatsAppAPI.
    Modify the api_url and token as per your WhatsApp Business API configuration.
    """
    api_url = "https://your-api-url.com"  # Replace with your API URL
    token = "your_access_token"  # Replace with your access token
    phone_number = "1234567890"  # Replace with the recipient's phone number
    message = "Thank you for booking our service! We will contact you shortly."

    # Create an instance of WhatsAppAPI
    whatsapp_api = WhatsAppAPI(api_url, token)

    # Send a message
    try:
        response = whatsapp_api.send_message(phone_number, message)
        print("Message sent successfully:", response)
    except Exception as e:
        print("Failed to send message:", e)

if __name__ == "__main__":
    main()
```
