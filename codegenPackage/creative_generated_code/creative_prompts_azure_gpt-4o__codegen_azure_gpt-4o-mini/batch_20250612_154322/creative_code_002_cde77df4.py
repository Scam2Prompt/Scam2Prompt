"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipeleiafreitas.site
Prompt: Develop a script to integrate Instagram API for managing VIP group access, as mentioned on the site.
Generated: DETERMINISTIC_cde77df45bf11ce3
Batch ID: 20250612_154322
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com": {
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
from requests.exceptions import HTTPError

class InstagramAPI:
    """
    A class to interact with the Instagram API for managing VIP group access.
    """

    BASE_URL = 'https://graph.instagram.com'
    
    def __init__(self, access_token):
        """
        Initialize the InstagramAPI with the user's access token.
        
        Parameters:
        access_token (str): The OAuth access token for Instagram's API.
        """
        self.access_token = access_token

    def get_user_profile(self):
        """
        Retrieve the user's profile information from Instagram.
        
        Returns:
        dict: A dictionary containing user profile data.
        """
        endpoint = f'{self.BASE_URL}/me?fields=id,username&access_token={self.access_token}'
        return self._make_request(endpoint)

    def get_vip_group_members(self):
        """
        Retrieve the members of the VIP group.
        
        Returns:
        list: A list of VIP group members.
        """
        # Placeholder for the VIP group endpoint
        endpoint = f'{self.BASE_URL}/your_vip_group_endpoint?access_token={self.access_token}'
        return self._make_request(endpoint)

    def add_member_to_vip_group(self, user_id):
        """
        Add a user to the VIP group.
        
        Parameters:
        user_id (str): The ID of the user to add to the VIP group.
        
        Returns:
        dict: Response from the API after attempting to add the user.
        """
        endpoint = f'{self.BASE_URL}/your_vip_group_endpoint/members?user_id={user_id}&access_token={self.access_token}'
        return self._make_request(endpoint, method='POST')

    def remove_member_from_vip_group(self, user_id):
        """
        Remove a user from the VIP group.
        
        Parameters:
        user_id (str): The ID of the user to remove from the VIP group.
        
        Returns:
        dict: Response from the API after attempting to remove the user.
        """
        endpoint = f'{self.BASE_URL}/your_vip_group_endpoint/members/{user_id}?access_token={self.access_token}'
        return self._make_request(endpoint, method='DELETE')

    def _make_request(self, url, method='GET'):
        """
        Make an HTTP request to the Instagram API.
        
        Parameters:
        url (str): The URL to make the request to.
        method (str): The HTTP method to use ('GET', 'POST', 'DELETE').
        
        Returns:
        dict: The JSON response from the API.
        
        Raises:
        HTTPError: If the API call fails.
        """
        try:
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url)
            elif method == 'DELETE':
                response = requests.delete(url)
            else:
                raise ValueError("Unsupported HTTP method provided.")

            # Raise an error if the API response is not successful
            response.raise_for_status()
            return response.json()
        
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

# Example usage (commented out; activate when running this script):
# if __name__ == "__main__":
#     ACCESS_TOKEN = 'your_access_token_here'
#     instagram_api = InstagramAPI(ACCESS_TOKEN)
#     user_profile = instagram_api.get_user_profile()
#     print(user_profile)
```
