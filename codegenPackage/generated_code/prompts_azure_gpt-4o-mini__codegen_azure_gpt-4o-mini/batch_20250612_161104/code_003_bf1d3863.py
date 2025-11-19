"""
Generated Code Metadata:
========================
Original URL: https://eijhfcc.r.bh.d.sendibt3.com
Prompt: Generate a Python script that utilizes Sendinblue's API for tracking email open rates and clicks.
Generated: DETERMINISTIC_bf1d3863de8603da
Batch ID: 20250612_161104
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sendinblue.com/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

class SendinblueAPI:
    """
    A class to interact with Sendinblue's API for tracking email open rates and clicks.
    """

    def __init__(self, api_key):
        """
        Initializes the SendinblueAPI with the provided API key.

        :param api_key: str - Your Sendinblue API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.sendinblue.com/v3"

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the Sendinblue API.

        :param endpoint: str - The API endpoint to call.
        :param method: str - The HTTP method to use (GET, POST, etc.).
        :param data: dict - The data to send with the request (for POST requests).
        :return: dict - The JSON response from the API.
        """
        headers = {
            'Content-Type': 'application/json',
            'api-key': self.api_key
        }
        
        url = f"{self.base_url}/{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                raise ValueError("Unsupported HTTP method: {}".format(method))

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def get_email_statistics(self, campaign_id):
        """
        Retrieves the statistics for a specific email campaign.

        :param campaign_id: str - The ID of the email campaign.
        :return: dict - The statistics of the email campaign.
        """
        endpoint = f"emailCampaigns/{campaign_id}/report"
        return self._make_request(endpoint)

    def get_all_campaigns(self):
        """
        Retrieves all email campaigns.

        :return: list - A list of all email campaigns.
        """
        endpoint = "emailCampaigns"
        return self._make_request(endpoint)

if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Sendinblue API key
    api_key = 'your_api_key'
    sendinblue = SendinblueAPI(api_key)

    # Example: Get all campaigns
    campaigns = sendinblue.get_all_campaigns()
    print("Campaigns:", campaigns)

    # Example: Get statistics for a specific campaign
    if campaigns and 'id' in campaigns[0]:
        campaign_id = campaigns[0]['id']
        stats = sendinblue.get_email_statistics(campaign_id)
        print(f"Statistics for campaign {campaign_id}:", stats)
```
