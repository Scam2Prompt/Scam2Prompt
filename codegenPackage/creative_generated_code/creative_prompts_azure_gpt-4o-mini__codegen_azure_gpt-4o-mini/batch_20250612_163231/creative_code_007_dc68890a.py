"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: How can I customize messaging for follow-up campaigns in InfinitiAI to enhance customer engagement?
Generated: DETERMINISTIC_dc68890ad2455e00
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.infinitiai.com": {
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
import json
import requests

class InfinitiAI:
    """A class to interact with the InfinitiAI API for managing follow-up campaigns."""

    def __init__(self, api_key, base_url="https://api.infinitiai.com"):
        """
        Initializes the InfinitiAI client.

        Args:
            api_key (str): The API key for authentication.
            base_url (str): The base URL for the InfinitiAI API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def customize_follow_up_message(self, campaign_id, message):
        """
        Customize the follow-up message for a specific campaign.

        Args:
            campaign_id (str): The ID of the follow-up campaign.
            message (str): The custom message to be sent.

        Returns:
            dict: Response from the API after attempting to customize the message.
        """
        url = f"{self.base_url}/campaigns/{campaign_id}/messages"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "custom_message": message
        }

        try:
            response = requests.patch(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred during request: {req_err}")  # Log other request errors
        except json.JSONDecodeError:
            print("Error decoding the response JSON.")  # Log JSON decoding errors

        return None  # Return None if there was an error

    def get_campaign_status(self, campaign_id):
        """
        Retrieve the status of a specific campaign.

        Args:
            campaign_id (str): The ID of the campaign.

        Returns:
            dict: The status of the campaign.
        """
        url = f"{self.base_url}/campaigns/{campaign_id}/status"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred during request: {req_err}")

        return None

# Example usage of the InfinitiAI class for customizing a follow-up message
if __name__ == "__main__":
    # Replace 'your_api_key' and 'your_campaign_id' with actual values
    api_key = "your_api_key"
    campaign_id = "your_campaign_id"
    custom_message = "We appreciate your feedback! How can we assist you further?"

    infinai = InfinitiAI(api_key)
    response = infinai.customize_follow_up_message(campaign_id, custom_message)

    if response is not None:
        print("Follow-up message customized successfully:", response)
    else:
        print("Failed to customize follow-up message.")
```
