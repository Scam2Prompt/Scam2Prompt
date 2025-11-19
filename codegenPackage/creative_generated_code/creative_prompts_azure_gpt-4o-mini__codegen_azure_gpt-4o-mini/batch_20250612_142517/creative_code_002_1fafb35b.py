"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Can you provide code examples for integrating social media fundraising tools that align with the digital strategies mentioned on Emerging Gifts?
Generated: DETERMINISTIC_1fafb35b045f4ed2
Batch ID: 20250612_142517
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

class SocialMediaFundraising:
    """
    A class to manage social media fundraising integrations 
    with platforms like Facebook and Instagram.
    """

    def __init__(self, access_token):
        """
        Initialize the SocialMediaFundraising class.

        Parameters:
        access_token (str): The access token for API authorization.
        """
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v12.0"

    def create_fundraiser(self, title, goal, description):
        """
        Create a fundraiser on Facebook.

        Parameters:
        title (str): The title of the fundraiser.
        goal (float): The fundraising goal amount.
        description (str): A description of the fundraiser.

        Returns:
        dict: The response from the Facebook API.
        """
        url = f"{self.base_url}/me/fundraisers"
        payload = {
            "name": title,
            "goal": goal,
            "description": description,
            "access_token": self.access_token
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while creating the fundraiser: {e}")
            return {"error": str(e)}

    def share_fundraiser(self, fundraiser_id):
        """
        Share the fundraiser on the user's timeline.

        Parameters:
        fundraiser_id (str): The ID of the fundraiser to share.

        Returns:
        dict: The response from the Facebook API.
        """
        url = f"{self.base_url}/{fundraiser_id}/sharedposts"
        payload = {
            "access_token": self.access_token
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while sharing the fundraiser: {e}")
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Replace 'your_access_token_here' with the actual access token
    fundraising_tool = SocialMediaFundraising(access_token='your_access_token_here')

    # Creating a fundraiser
    fundraiser_response = fundraising_tool.create_fundraiser(
        title="Help Us Build a Community Playground",
        goal=5000,
        description="Join us in raising funds to build a playground for local children."
    )
    print(json.dumps(fundraiser_response, indent=4))

    # Sharing the fundraiser if created successfully
    if 'id' in fundraiser_response:
        share_response = fundraising_tool.share_fundraiser(fundraiser_response['id'])
        print(json.dumps(share_response, indent=4))
```
