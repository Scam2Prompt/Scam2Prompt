"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qubetisc.pw
Prompt: Provide an example of using an API to retrieve the status of a newly created website on Ispmanager.
Generated: DETERMINISTIC_1d3d280602a2783a
Batch ID: 20250612_161441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ispmanager.com/v1": {
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

class IspManagerAPI:
    def __init__(self, base_url, api_key):
        """
        Initializes the IspManagerAPI with the base URL and API key.
        
        :param base_url: The base URL of the IspManager API
        :param api_key: The API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_website_status(self, website_id):
        """
        Retrieves the status of a website based on its ID.
        
        :param website_id: The ID of the website to check
        :return: Status of the website or an error message
        """
        url = f"{self.base_url}/websites/{website_id}/status"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Return the status if the request was successful
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"Error occurred: {err}"}

# Example usage
if __name__ == "__main__":
    # Configuration
    BASE_URL = "https://api.ispmanager.com/v1"  # Replace with actual base URL
    API_KEY = "your_api_key_here"                # Replace with your API key
    WEBSITE_ID = "1234"                           # Replace with the actual website ID

    # Create an instance of IspManagerAPI
    isp_manager = IspManagerAPI(BASE_URL, API_KEY)

    # Retrieve and print the website status
    status = isp_manager.get_website_status(WEBSITE_ID)
    print(status)
```
