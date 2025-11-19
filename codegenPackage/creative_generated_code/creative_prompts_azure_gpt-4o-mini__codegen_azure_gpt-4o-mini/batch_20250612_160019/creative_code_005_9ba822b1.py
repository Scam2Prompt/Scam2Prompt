"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subscribemenow.com
Prompt: How can I use GetResponse's API to track the performance of my email marketing campaigns in real-time?
Generated: DETERMINISTIC_9ba822b19e9a1f08
Batch ID: 20250612_160019
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getresponse.com/v3": {
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

class GetResponseAPI:
    """
    A class to interact with the GetResponse API for tracking email marketing campaigns.
    """

    def __init__(self, api_key):
        """
        Initializes the GetResponseAPI instance.

        Args:
            api_key (str): The API key for authenticating with GetResponse API.
        """
        self.base_url = 'https://api.getresponse.com/v3'
        self.api_key = api_key

    def get_campaign_performance(self, campaign_id):
        """
        Retrieves the performance metrics of a specific email campaign.

        Args:
            campaign_id (str): The ID of the campaign to track.

        Returns:
            dict: The performance metrics of the campaign.

        Raises:
            Exception: If the request to the GetResponse API fails.
        """
        url = f"{self.base_url}/campaigns/{campaign_id}/statistics"
        headers = {
            'X-Auth-Token': f'api-key {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the performance metrics as JSON
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

if __name__ == "__main__":
    # Example usage
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    CAMPAIGN_ID = 'your_campaign_id_here'  # Replace with your actual campaign ID

    get_response_api = GetResponseAPI(API_KEY)

    try:
        performance_data = get_response_api.get_campaign_performance(CAMPAIGN_ID)
        print("Campaign Performance Data:", performance_data)
    except Exception as e:
        print("Failed to retrieve campaign performance data:", e)
```
