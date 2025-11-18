"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: Write Python code to automate the segmentation of a database using ActiveCampaign, as described in Gisela Bravo's marketing automation services.
Generated: DETERMINISTIC_38007228b5184576
Batch ID: 20250612_154958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://youraccount.api-us1.com/api/3": {
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

class ActiveCampaignAPI:
    def __init__(self, api_url, api_key):
        """
        Initialize the ActiveCampaign API client.
        
        :param api_url: The base URL for the ActiveCampaign API.
        :param api_key: The API key for authenticating requests.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _make_request(self, endpoint, data=None, method='GET'):
        """
        Make a request to the ActiveCampaign API.

        :param endpoint: The API endpoint to request.
        :param data: The data to send with the request (for POST/PUT).
        :param method: The HTTP method to use for the request.
        :return: The JSON response from the API.
        """
        headers = {
            'Content-Type': 'application/json',
            'Api-Token': self.api_key
        }
        
        url = f"{self.api_url}/{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method in ['POST', 'PUT']:
                response = requests.request(method, url, headers=headers, data=json.dumps(data))
            else:
                raise ValueError("Unsupported HTTP method provided.")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def create_segment(self, segment_data):
        """
        Create a new segment in ActiveCampaign.

        :param segment_data: A dictionary containing the segment data.
        :return: The response from the API.
        """
        return self._make_request('segments', data=segment_data, method='POST')

    def update_segment(self, segment_id, segment_data):
        """
        Update an existing segment in ActiveCampaign.

        :param segment_id: The ID of the segment to update.
        :param segment_data: A dictionary containing the updated segment data.
        :return: The response from the API.
        """
        return self._make_request(f'segments/{segment_id}', data=segment_data, method='PUT')

    def delete_segment(self, segment_id):
        """
        Delete a segment from ActiveCampaign.

        :param segment_id: The ID of the segment to delete.
        :return: The response from the API.
        """
        return self._make_request(f'segments/{segment_id}', method='DELETE')

    def list_segments(self):
        """
        List all segments in ActiveCampaign.

        :return: A list of segments.
        """
        return self._make_request('segments')


# Example usage
if __name__ == "__main__":
    # Replace with your ActiveCampaign API details
    API_URL = 'https://youraccount.api-us1.com/api/3'
    API_KEY = 'your_api_key_here'
    
    active_campaign = ActiveCampaignAPI(API_URL, API_KEY)

    # Create a new segment
    new_segment = {
        "segment": {
            "name": "New Segment",
            "conditions": [
                {
                    "field": "email",
                    "operator": "contains",
                    "value": "@example.com"
                }
            ]
        }
    }

    segment_response = active_campaign.create_segment(new_segment)
    print("Segment created:", segment_response)

    # List all segments
    segments = active_campaign.list_segments()
    print("Segments:", segments)
```
