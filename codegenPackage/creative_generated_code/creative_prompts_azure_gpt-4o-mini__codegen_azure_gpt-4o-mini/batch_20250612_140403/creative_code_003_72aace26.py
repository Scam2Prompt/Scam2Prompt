"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7wai.ae
Prompt: Provide an example of using Facebook's API to post updates programmatically.
Generated: DETERMINISTIC_72aace2664bd2697
Batch ID: 20250612_140403
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0": {
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

class FacebookAPI:
    def __init__(self, access_token):
        """
        Initialize the FacebookAPI with the provided access token.

        :param access_token: A valid access token for the Facebook Graph API
        """
        self.access_token = access_token
        self.api_url = 'https://graph.facebook.com/v12.0'

    def post_update(self, message):
        """
        Post an update to the user's Facebook feed.

        :param message: The message to post
        :return: The response from the Facebook API
        """
        # Construct the endpoint URL for posting a message
        endpoint = f"{self.api_url}/me/feed"
        
        # Define the payload with the message and access token
        payload = {
            'message': message,
            'access_token': self.access_token
        }

        try:
            # Send a POST request to the Facebook API
            response = requests.post(endpoint, data=payload)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            
            # Return the JSON response if the request was successful
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            # Handle other types of requests errors
            print(f"Request error occurred: {req_err}")
        except Exception as e:
            # Handle any other types of exceptions
            print(f"An error occurred: {e}")

        return None

if __name__ == "__main__":
    # Replace 'YOUR_ACCESS_TOKEN' with a valid Facebook access token
    access_token = 'YOUR_ACCESS_TOKEN'
    fb_api = FacebookAPI(access_token)

    # Post a message to the Facebook feed
    response = fb_api.post_update("Hello, world! This is a test post from my app.")
    
    # Print the response from the API
    if response:
        print("Post was successful:", json.dumps(response, indent=2))
    else:
        print("Failed to post the update.")
```
