"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Recommend libraries or tools for managing digital advertising campaigns, specifically for formats like "Mopis Digitales" and "Fascia de Puente" as described on WOW MEDIA's website.
Generated: DETERMINISTIC_5d1532af09eb429f
Batch ID: 20250612_154355
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.advertisingplatform.com/v1": {
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

class DigitalAdvertisingManager:
    """
    A class to manage digital advertising campaigns, specifically for formats like
    "Mopis Digitales" and "Fascia de Puente".
    """

    def __init__(self, api_key):
        """
        Initializes the DigitalAdvertisingManager with an API key.
        
        Args:
            api_key (str): The API key for authentication with the advertising platform.
        """
        self.api_key = api_key
        self.base_url = "https://api.advertisingplatform.com/v1"

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the advertising platform API.

        Args:
            endpoint (str): The API endpoint to call.
            method (str): The HTTP method to use (GET or POST).
            data (dict): The data to send in the request (if applicable).

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method.")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def create_campaign(self, format_type, budget):
        """
        Creates a new advertising campaign.

        Args:
            format_type (str): The advertising format (e.g., "Mopis Digitales", "Fascia de Puente").
            budget (float): The budget for the campaign.

        Returns:
            dict: The response from the API after creating the campaign.
        """
        data = {
            'format': format_type,
            'budget': budget
        }

        return self._make_request('campaigns', method='POST', data=data)

    def get_campaigns(self):
        """
        Retrieves the list of existing campaigns.

        Returns:
            list: A list of campaigns retrieved from the API.
        """
        return self._make_request('campaigns', method='GET')

if __name__ == "__main__":
    import os

    # Load the API key from environment variable for security
    api_key = os.getenv("ADVERTISING_API_KEY")

    if not api_key:
        raise EnvironmentError("Please set the ADVERTISING_API_KEY environment variable.")

    # Initialize the advertising manager
    advertising_manager = DigitalAdvertisingManager(api_key)

    # Example usage
    try:
        # Create a new campaign
        campaign_response = advertising_manager.create_campaign("Mopis Digitales", 1000.0)
        print("Campaign created:", campaign_response)

        # Retrieve all campaigns
        campaigns = advertising_manager.get_campaigns()
        print("Existing campaigns:", campaigns)
    except Exception as e:
        print(f"An error occurred: {e}")
```
