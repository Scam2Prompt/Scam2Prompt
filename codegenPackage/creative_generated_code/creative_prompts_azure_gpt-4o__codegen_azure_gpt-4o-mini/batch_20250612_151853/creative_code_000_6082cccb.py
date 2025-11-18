"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://voicemanagerwebex.com.br
Prompt: Write a Python script to integrate a SIP trunk with the VoiceManager platform for making and receiving cloud-based business calls.
Generated: DETERMINISTIC_6082cccb3adb167d
Batch ID: 20250612_151853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.voicemanager.com/v1": {
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

class VoiceManagerSIPIntegration:
    """
    A class to handle the integration with the VoiceManager platform
    for managing SIP trunk operations such as making and receiving calls.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initialize the VoiceManagerSIPIntegration class.

        :param api_key: API key for authentication with VoiceManager
        :param base_url: Base URL of the VoiceManager API
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint: str, method: str = 'GET', data: dict = None) -> dict:
        """
        Make a request to the VoiceManager API.

        :param endpoint: API endpoint to request
        :param method: HTTP method ('GET', 'POST', etc.)
        :param data: Data to send with the request (for POST/PUT)
        :return: Response from the API as a JSON dictionary
        :raises Exception: If the API request fails
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            else:  # Default to GET
                response = requests.get(url, headers=headers)

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

    def create_sip_trunk(self, trunk_name: str, configuration: dict) -> dict:
        """
        Create a new SIP trunk in VoiceManager.

        :param trunk_name: Name for the new SIP trunk
        :param configuration: Configuration settings for the SIP trunk
        :return: Response from the API with details of the created SIP trunk
        """
        endpoint = 'sip-trunks'
        data = {
            'name': trunk_name,
            'configuration': configuration
        }
        return self._make_request(endpoint, method='POST', data=data)

    def make_call(self, from_number: str, to_number: str, trunk_id: str) -> dict:
        """
        Initiate a call using the specified SIP trunk.

        :param from_number: The number from which the call is made
        :param to_number: The number to which the call is made
        :param trunk_id: The ID of the SIP trunk to use
        :return: Response from the API with call information
        """
        endpoint = 'calls'
        data = {
            'from': from_number,
            'to': to_number,
            'trunk_id': trunk_id
        }
        return self._make_request(endpoint, method='POST', data=data)

    def receive_calls(self, trunk_id: str) -> dict:
        """
        Set up the SIP trunk to receive incoming calls.

        :param trunk_id: The ID of the SIP trunk to configure
        :return: Response from the API confirming the setup
        """
        endpoint = f'sip-trunks/{trunk_id}/receive-calls'
        return self._make_request(endpoint, method='PUT')

if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.voicemanager.com/v1"

    # Initialize the integration
    voice_manager = VoiceManagerSIPIntegration(api_key=API_KEY, base_url=BASE_URL)

    # Example usage:
    try:
        # Create a SIP trunk
        sip_trunk = voice_manager.create_sip_trunk("My SIP Trunk", {"host": "sip.example.com", "port": 5060})
        print(f"SIP Trunk Created: {sip_trunk}")

        # Make a call
        call_response = voice_manager.make_call("1234567890", "0987654321", sip_trunk['id'])
        print(f"Call Initiated: {call_response}")

        # Configure to receive calls
        receive_response = voice_manager.receive_calls(sip_trunk['id'])
        print(f"Receive Calls Configured: {receive_response}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code provides a solid starting point for integrating a SIP trunk with the VoiceManager platform, utilizing best practices in error handling, code organization, and documentation.
