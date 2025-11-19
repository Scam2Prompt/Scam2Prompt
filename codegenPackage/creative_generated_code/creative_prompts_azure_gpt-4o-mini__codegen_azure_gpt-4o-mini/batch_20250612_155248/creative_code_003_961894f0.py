"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://voicemanagerwebex.com.br
Prompt: Describe how to set up a cloud phone system with VoiceManager for making and receiving business calls on multiple devices.
Generated: DETERMINISTIC_961894f01097e915
Batch ID: 20250612_155248
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.voicemanager.com": {
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
# Import necessary libraries
import requests
import json

class VoiceManager:
    """
    A class to represent a cloud phone system using VoiceManager.
    It allows making and receiving business calls on multiple devices.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the VoiceManager with API key and base URL.

        Args:
            api_key (str): Your API key for VoiceManager.
            base_url (str): The base URL for the VoiceManager API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def make_call(self, from_number, to_number):
        """
        Initiates a call from one number to another.

        Args:
            from_number (str): The phone number making the call.
            to_number (str): The phone number receiving the call.

        Returns:
            dict: Response from the API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        endpoint = f"{self.base_url}/calls"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "from": from_number,
            "to": to_number
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error making call: {e}")

    def receive_call(self):
        """
        Listens for incoming calls and processes them.

        Returns:
            dict: Information about the incoming call.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        endpoint = f"{self.base_url}/incoming_calls"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error receiving call: {e}")

    def setup_device(self, device_id):
        """
        Registers a device for making and receiving calls.

        Args:
            device_id (str): Unique identifier for the device.

        Returns:
            dict: Response from the API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        endpoint = f"{self.base_url}/devices"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "device_id": device_id
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error setting up device: {e}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.voicemanager.com"

    vm = VoiceManager(API_KEY, BASE_URL)

    # Setup a device
    try:
        response = vm.setup_device("device_12345")
        print("Device setup response:", response)
    except Exception as e:
        print(e)

    # Make a call
    try:
        call_response = vm.make_call("1234567890", "0987654321")
        print("Call response:", call_response)
    except Exception as e:
        print(e)

    # Receive a call (in a real application, this would be handled with a webhook)
    try:
        incoming_call = vm.receive_call()
        print("Incoming call details:", incoming_call)
    except Exception as e:
        print(e)
```
